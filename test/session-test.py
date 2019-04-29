import requests

s = requests.Session()
s.get('')
r = s.get('')
print(r.text)
