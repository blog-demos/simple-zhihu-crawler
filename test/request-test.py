# -*- coding=UTF-8 -*-

import requests

URL = 'https://www.zhihu.com'

r = requests.get(url=URL)
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
