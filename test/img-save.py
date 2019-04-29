import requests

r = requests.get(url='https://github.com/favicon.ico')
print(r.text)
print(r.content)

with open('H:/favicon.ico', 'wb') as f:
    f.write(r.content)
