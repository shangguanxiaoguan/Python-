import json

import requests

response = requests.get('http://httpbin.org/get')
print(response.text)

response = requests.post('http://httpbin.org/post')
print(response.text)

# 从客户端向服务器传送的数据取代指定的文档的内容
response = requests.put('http://httpbin.org/put')
print("put:" + response.text)

# 只请求页面页面的首部
response = requests.head('http://httpbin.org/get')
print("head:" + response.text)

# 请求服务器删除指定的页面
print("delete:" + requests.delete('http://httpbin.org/get').text)

print("options:" + requests.options('http://httpbin.org/get').text)

# 带参数的get请求
response = requests.get('http://httpbin.org/get?name=kim&age=22')
print("带参数的get请求：" + response.text)

data = {
    'name': 'kim',
    'age': 22
}
url = 'http://httpbin.org/get'

response = requests.get(url, data=data)
print(response.text)
# 部分返回结果：
# "args": {},

"""
【get请求时，使用data是不行的，需要使用params】

"""""
response = requests.get(url, params=data)
print('带参数的get请求二：' + response.text)
# "args": {
#     "age": "22",
#     "name": "kim"
#   },


"""
解析json
"""
print(type(response.text))   # <class 'str'>
print(response.json())
print(json.loads(response.text))
print(type(response.json()))  # <class 'dict'>

"""
获取二进制数据
"""
response = requests.get('https://github.com/favicon.ico')
print(type(response.text), type(response.content))
print(response.text, "GBK")
print(response.content)  # 获取二进制数据

"""
添加headers
"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
url = 'https://www.zhihu.com/explore'
response = requests.get(url, headers=headers)
# print(response.json())
print(response.text)

"""
基本post请求
"""

data = {
    'name': 'kim',
    'age': 110
}
response = requests.post('http://httpbin.org/post', data=data)
print("基本post请求：" + response.text)

"""
 响应
"""
response = requests.get('http://www.baidu.com')
print(response.status_code)
print(response.headers)
print(response.cookies)
print(response.history)
print(response.url)


"""
文件上传
"""
files = {'file': open('cookie.txt', 'rb')}
response = requests.post('http://httpbin.org/post', files=files)
response = requests.get('http://httpbin.org/post')
print("文件上传：" + response.text)

"""
会话
"""
