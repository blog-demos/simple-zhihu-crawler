# -*- coding=UTF-8 -*-

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/70.0.3538.102 Safari/537.36'
}

URL = 'https://www.zhihu.com'

r = requests.get(url=URL, headers=headers)
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
