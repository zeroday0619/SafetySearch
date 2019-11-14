What is SafetySearch ?
====
![pythonVersion](https://img.shields.io/badge/python-v3.7-blue) ![License](https://img.shields.io/badge/License-MIT-blue)

**Adult search term determination program**

SafetySearch is a project that implements adult search word filtering module \
using NAVER's adult search word judging API and MongoDB.

## Prerequisites
 - Python 3.7 +
 - pymongo
 - mongoDB
 
## Usage

**1. Install prerequisites**
``` sh
$ pip install pymongo
```

**2. Install mongoDB**
- Windows \
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/

- Ubuntu \
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

- Debian \
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-debian/

- ETC \
https://docs.mongodb.com/manual/tutorial/

**3. Code Example**
```python
from SafetySearch import safesearch

resp = safesearch.adult_filter(search="***")
print(resp)
```

## Author
 - Euiseo Cha (차의서) | zeroday0619 : \
    [Github](https://github.com/zeroday0619) \
    [Facebook](https://www.facebook.com/EuiseoCha) \
    [Tistory | 티스토리 블로그](https://blog.zeroday0619.kr/)
## LICENSE
Copyright 2019 Euiseo Cha (차의서) | zeroday0619 \
[MIT License](https://github.com/zeroday0619/SafetySearch/blob/master/LICENSE)