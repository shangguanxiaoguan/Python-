import json

import requests

# data = {
#     'username': 'Test',
#     'password': '123456'
# }
url = 'http://54.241.21.249:8089/skyvpn/v2/invite/getUrl?' \
      'userId=7393118869613203&deviceId=And.3cfdbb3b0287b0fed79432dcd50b9de7.fvpn&types=3&' \
      'token=d60862e5cb47119b260f20ccafb03e75&timestamp=1590382152623&sign=86BDF442174FFD02F38C88E81CA83D8C'
cookies = {
      'sessionId': 'd60862sdde5cb47119b260f20ccafb03e75'
}
# res = requests.get(url='http://127.0.0.1:8000/logingforpost', data=data)
res = requests.post(url=url, cookies=cookies)
# print(res.json())
# print(res)
response = res.text
print(response)

#
# """
# 重构post请求
# """
#
#
# url='http://127.0.0.1:8000/logingforpost'
# data = {
#     'username': 'Test',
#     'password': '123456'
# }
#
#
# def sendPost(url, data):
#     res = requests.post(url=url, data=data)
#     return json.loads(res)
# # json.loads(param)函数是将字典型的文本字符串转换成json串，其参数param必须要是一个字典型的字符串
# # json.dumps(param)函数是将json数据对象转换为文本字符串的函数，其参数param必须要是json对象
# #

# sendPost(url, data)



