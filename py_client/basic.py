import requests

endpoint = "http://127.0.0.1:8000/api/"

res = requests.get(endpoint, params={"param1": "param1value"}, json={"json1": "json1value"})
print(res)
print(res.json())