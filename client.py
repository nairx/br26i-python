import requests

url = "http://localhost:8081"

res = requests.get(url).json()

print(res)

