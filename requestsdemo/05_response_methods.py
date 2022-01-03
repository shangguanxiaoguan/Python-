
import requests

url = "http://www.baidu.com"
r = requests.get(url)
print(r.encoding)
r.encoding = "utf-8"
print(r.text)

print(r.headers)

"""
相应方法：
response.status_code  获取响应状态码
response.url          获取请求url地址
response.encoding     1。查看默认请求编码格式   2。设置响应编码格式
response.headers      获取服务器响应信息头
response.cookies      获取响应cookies信息
response.text         以文本形式解析响应内容
response.content      以字节码形式解析响应内容  【图片和视频时使用】
response.json()       以json字符串形式解析响应内容
   
"""

"""
cookies
    1⃣️来源：由服务器生成
    2⃣️作用：区分同一请求客户端
    3⃣️获取：响应对象.cookies["键名"]
    4⃣️设置：
        设置：cookies = {"获取出的cookies键名":"获取出的值"}
        应用：request.请求方法(url, cookies=cookies)
"""

"""
session
  为什么使用session？
     session可以自动保存服务器产生的cookies信息，并且自动在下一条请求时附加
     
  什么是session？
      一次会话（从客户端和服务器创建请求连接开始，客户端和服务器断开连接结束）
      
  session获取及应用
    获取：
      导包 import requests
      获取session对象  session = requests.session()
    
    应用：
      通过session对象.方法
    
    示例：
      session.get()
      session.post()
      session.delete()
      session.put()
    无论通过session对象调用哪个方法，返回结果都是response对象
"""