import requests

url = 'https://www.ctrip.com/'

"""
requests 访问HTTPS需要证书：
解决方案：
1.发送请求时候忽略证书，
2.增加证书路径
"""

# 忽略证书
# res = requests.get(url=url, verify=False)   # verify参数默认为true，false为忽略证书
# print(res.text)

# 添加证书路径
# res = requests.get(url=url, verify='证书的路径')   # verify参数默认为true，false为忽略证书
res = requests.get(url=url, verify='证书的路径')   # verify参数默认为true，false为忽略证书
print(res.text)
