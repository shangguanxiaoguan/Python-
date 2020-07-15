import json

import requests

data = {
    'username': 'test',
    'password': '123456'
}
res = requests.post(url='http://127.0.0.1:8000/logingforpost', data=data)
# print(res.json())
# print(res)
response = res.text
print(response)


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
    return json.loads(res)
# json.loads(param)函数是将字典型的文本字符串转换成json串，其参数param必须要是一个字典型的字符串
# json.dumps(param)函数是将json数据对象转换为文本字符串的函数，其参数param必须要是json对象
#

sendPost(url, data)



