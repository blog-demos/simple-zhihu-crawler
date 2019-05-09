# -*- coding=UTF-8 -*-
# 模拟登录

import requests

url = "https://www.zhihu.com/api/v3/oauth/sign_in"

headers = {
    'cookie': '_xsrf=JbPQZktCinqDvoAim94sk0lbZNPn4rXo;'
              '_zap=fe1f3746-6bd4-4338-a297-6d3bea1c1809;'
              'd_c0="AGCo7wVXZw-PTt4tOs52fyQaX-JxRILw_ys=|1557413063";'
              'tst=r;'
              'q_c1=32ab22c7518f4090ae5fbd44c7bf14f6|1557413233000|1557413233000;'
              '__gads=ID=a4fc5fca25f0825f:T=1557413234:S=ALNI_MbfNtVCcOdUsRG4OQiH1npma1ZVHQ;'
              'tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330;'
              'capsion_ticket="2|1:0|10:1557416453|14:capsion_ticket|44:ZThjN2JlNzIyOTEyNGVjNWI3OGQ1NDIxM'
              'TQwNzAyOTE=|fca7a091fd0510e6a557b4e90ac0fe5d098348fc63928d9590a24e738997a7ae"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/70.0.3538.102 Safari/537.36'
}

hmackey = 'd1b964811afb40118a12068ff74a12f4'

formdata = ''

r = requests.post(url=url, headers=headers)
print(r.text)
