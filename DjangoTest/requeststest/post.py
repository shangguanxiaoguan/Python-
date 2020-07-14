import requests

data = {
    'username': 'test',
    'password': '123456'
}
res = requests.post(url='http://127.0.0.1:8000/logingforpost', data=data)
# print(res.json())
print(res)


"""
重构post请求
"""


url='http://127.0.0.1:8000/logingforpost'
data = {
    'username': 'test',
    'password': '123456'
}


def sendPost(url, data):
    res = requests.post(url=url, data=data)
    return res.json()


print(sendPost(url, data))



