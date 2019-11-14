import requests
import pymongo

class SafetySearch:
	def __init__(self):
		self.url = "https://openapi.naver.com/v1/search/adult.json"
		self.safty_msg = "해당 검색어는 Safety Search 에 의해 사용하실수 없습니다."

		# NAVER API Authentication
		self.headers = {
			"X-Naver-Client-Id": "",
			"X-Naver-Client-Secret": ""
		}
	def adult_filter(self, search: str):
		data = {
			"query": search
		}
		client = pymongo.MongoClient('mongodb://localhost', 27017)
		db = client['adult_filter']
		collection = db['database']
		mo = db.database.find_one({"filter_string": search})
		try:
			if mo != None:
				check = mo['filter_string']
				if check == search:
					print("DB 조회\n"+self.safty_msg)
					return
				else:
					print("DB 조회\n"+"System Error")
					return
			else:
				mx = db.database.find_one({"green": search})
				if mx == None:
					resp = requests.get(self.url, params=data, headers=self.headers).json()
					if resp['adult'] == '1':
						print("API 사용\n"+self.safty_msg)
						query = [
							{
								"filter_string": search
							}
						]
						collection.insert_many(query)
						return
					elif resp['adult'] == '0':
						print("API 사용\n정상")
						query2 = [
							{
								"green": search
							}
						]
						collection.insert_many(query2)
						return search
					else:
						print("API 사용\nSystem Error")
				else:
					print("DB 조회 \n 정상")
					return search
		except Exception as ex:
			pass



_inst = SafetySearch()
_inst.adult_filter(search="청소년")
