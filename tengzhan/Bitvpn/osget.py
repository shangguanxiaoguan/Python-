import os

"""
所有环境变量设置后都要重启
"""

url = 'dn1_skyvpn_service_url'
test = 'dn1_db_user'

value = os.getenv(url)

testos = os.getenv(test)

print(testos)

print("ajgdkjg", value)

