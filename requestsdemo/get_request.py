import requests

url = "http://www.baidu.com"

# params = {"id": 1002, "kw": "python"}
params = {"id": "1002,1003"}
response = requests.get(url, params=params)

print("url:", response.url)
print("status_code:", response.status_code)
print("text:", response.text)

