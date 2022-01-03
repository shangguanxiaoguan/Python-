"""
url = ""
data = {}
res = requests.post(url=url, data=data,headers=headers)
res = requests.post(url=url, json=data,headers=headers)
print(res.json())

请求参数中 data与json的区别：

data : 字典对象
json ： json字符串

在python中，字典对象和json字符串长得一样，但是后台格式化有区别

将字典对象转为json字符串：
1。 导入json
2。 json.dumps(字典对象)


响应数据中，json()与text的区别：
json(): 返回类型为字典，可以通过键名来获取相应的值
text： 返回类型为 字符串，不能通过键名来获取相应的值


"""