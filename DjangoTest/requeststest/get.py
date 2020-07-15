import json

import requests


"""
 ʹ�����װ�ӿڲ��Խű�
"""


class RunMain:
    def __init__(self, url, method, data=None):
        self.res = self.run_main(url, method, data)

    def send_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        # return json.dumps(res)
        # �Է��ص����ݽ��и�ʽ����indent��������룻sort_keys������
        return json.dumps(res, indent=2, sort_keys=True)

    def send_post(self,url, data):
        res = requests.post(url=url, data=data).json()
        # return json.dumps(res)
        # �Է��ص����ݽ��и�ʽ����indent��������룻sort_keys������
        return json.dumps(res, indent=2, sort_keys=True)

    def run_main(self, url, data, method):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        if method == 'POST':
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/logingforpost'
    data = {
        'username': 'test',
        'password': '123456'
    }
    run = RunMain()
    print(run.run_main(url, data, 'GET'))

