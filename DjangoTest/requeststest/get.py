import json

import requests


"""
 使用类封装接口测试脚本
"""


class RunMain:
    def __init__(self, url, method, data=None):
        self.res = self.run_main(url, method, data)

    def send_get(self, url, data):
        res = requests.get(url=url, data=data)
        # res = requests.get(url=url, data=data, cookies=cookies)

        return res
        # res = requests.get(url=url, data=data).json()
        # return json.dumps(res)
        # 对返回的数据进行格式化，indent：间隔距离；sort_keys：排序
        # return json.dumps(res, indent=2, sort_keys=True)

    def send_post(self,url, data):
        res = requests.post(url=url, data=data).json()
        # return json.dumps(res)
        # 对返回的数据进行格式化，indent：间隔距离；sort_keys：排序
        return json.dumps(res, indent=2, sort_keys=True)

    def run_main(self, url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        if method == 'POST':
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':
    # url = 'http://127.0.0.1:8000/logingforpost'
    #
    url = 'http://54.241.21.249:8089/skyvpn/v2/invite/getUrl'
    data = {
        "userId": "7393118869613203",
        "deviceId": "And.3cfdbb3b0287b0fed79432dcd50b9de7.fvpn",
        "types": 3,
        "token": "d60862e5cb47119b260f20ccafb03e75",
        "timestamp": 1590382152623,
        "sign": "86BDF442174FFD02F38C88E81CA83D8C"
    }
    # data = {'userId': 7393118869613203, 'deviceId': "And.3cfdbb3b0287b0fed79432dcd50b9de7.fvpn",
    #            'types': 3, 'token': "d60862e5cb47119b260f20ccafb03e75", 'timestamp': 1590382152623,
    #            'sign': "86BDF442174FFD02F38C88E81CA83D8C"}
    # url = 'http://54.241.21.249:8089/skyvpn/v2/invite/getUrl'
    # rsp = requests.post(url, data=payload)

    # 请求方式的传入要确认好，不然会报400
    run = RunMain(url, 'POST', data)
    res = run.run_main(url, 'POST', data)
    # res.text.encode('utf-8').decode('unicode_escape')  # 先把返回结果转换成utf-8，再去解码成中文的编码
    print(json.loads(res))

