# -*- coding=UTF-8 -*-

""" 方法一
from urllib import request
from http import cookiejar

# 声明一个CookieJar对象实例来保存cookie
cookie = cookiejar.CookieJar()
# 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
handler = request.HTTPCookieProcessor(cookie)
# 通过CookieHandler创建opener
opener = request.build_opener(handler)
# 此处的open方法打开网页
response = opener.open('https://www.zhihu.com')
# 打印cookie信息
for item in cookie:
    # print('Name = %s' % item.name)
    # print('Value = %s' % item.value)
    print('%s : %s' % (item.name, item.value))
"""


''' 方法二
import http.cookiejar
import urllib.request

cookies = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookies)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.zhihu.com')
for item in cookies:
    print(item.name + ' : ' + item.value)
'''


''' 方法三 '''
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/70.0.3538.102 Safari/537.36'
}

r = requests.get(url='https://www.zhihu.com')  # 加了headers反而拿不到cookies
# print(r.cookies)
for key, value in r.cookies.items():
    print(key + ' : ' + value)

