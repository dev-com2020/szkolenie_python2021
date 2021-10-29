import requests

url = 'https://www.comarch.pl/szkolenia/'
headers = {'content-Length': '108', 'Content-Type':'application/json'}
body = """{
    "value": 100,
    "description": "Python"
    }"""

req = requests.post(url,headers=headers,data=body)

print(req.status_code)
print(req.headers)
print(req.text)