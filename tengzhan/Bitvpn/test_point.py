import json
import random
import time

import requests


def traversal_list(alist, i):
    while True:
        length = len(alist)
        i = i % length
        yield alist[i]
        i += 1


uid_list = ['500576669346975744', '492951197834432512', '492887577595367425', '492239891242307584', '492234935399501825',
            '490834570275868672', '490469032974503937', '489279503018119168', '489270025627521025',
            '489264321860620288', '487919840582324225', '487910068407652352', '487886924208820225', '487883258164826112',
            '487882946196688897', '487880701946253312', '487875751312773121', '487875205537353728', '487874558058450945',
            '487873612389699584', '487831705554931713']

add_point_url = ''

exchange_point_url = ''


i = 0
f = traversal_list(uid_list, i)
while True:
    uid = next(f)
    print(str(uid))
    # amount = int(random.uniform(100, 1000))
    amount = int(random.uniform(99, 101))
    orderId = str(int(time.time() * 1000))
    # source_list = [2, 5, 3, 9]
    source_list = [3]
    source = random.choice(source_list)
    payload = {
        'uid': uid,
        'orderId': orderId,
        'amount': amount,
        'source': source,
        'extInfo': ''
    }
    data = json.dumps(payload)
    result = requests.post(add_point_url, data=data)
    # print("积分增加结果：" + result.text)
    print("用户：" + uid + " 在" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "通过source = " + str(
        source) + "，增加了" + str(amount) + "积分")

    # productId_list = [113, 114, 115, 116, 117]
    productId_list = [115]
    productId = random.choice(productId_list)
    key = str(int(time.time() * 1000))
    payload = {
        'uid': uid,
        'key': key,
        'productId': productId,
        'address': 'dingtone'
    }

    result = requests.get(exchange_point_url, params=payload)
    print("用户：" + uid + " 在" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "兑换了" + str(
        productId) + "的商品")
    time.sleep(2)
    i += 1



#
# for i in uid_list:
#     uid = i
#     print(uid)
#     amount = int(random.uniform(100, 1000))
#     orderId = str(int(time.time() * 1000))
#     source_list = [2, 5, 3, 9]
#     source = random.choice(source_list)
#     payload = {
#         'uid': uid,
#         'orderId': orderId,
#         'amount': amount,
#         'source': source,
#         'extInfo': ''
#     }
#     data = json.dumps(payload)
#     result = requests.post(add_point_url, data=data)
#     # print("积分增加结果：" + result.text)
#     print("用户：" + uid + " 在" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "通过source = " + str(source) + "，增加了" + str(amount) + "积分")
#     productId_list = [113, 114, 115, 116, 117]
#     productId = random.choice(productId_list)
#     key = str(int(time.time() * 1000))
#     payload = {
#         'uid': uid,
#         'key': key,
#         'productId': productId,
#         'address': 'dingtone'
#     }
#
#     result = requests.get(exchange_point_url, params=payload)
#     print("用户：" + uid + " 在" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "兑换了" + str(productId) + "的商品")
#     # print('3-Hours积分兑换结果：' + result.text)
#     time.sleep(5)

