import requests

"""
post、get基类的封装
"""


class RunMethod:
    def post_main(self, url, data, header=None):
        res = None
        if header is not None:
            res = requests.post(url=url, data=data, headers=header).json()
        else:
            res = requests.post(url=url, data=data).json()
        return res

    def get_main(self, url, data, header):
        res = None
        if header is not None:
            res = requests.get(url=url, data=data, headers=header).json()
        else:
            res = requests.get(url=url, data=data).json()
            print('-------' + str(res))
        return res

    def run_main(self, method, url, data, header=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, header)
            print('post请求结果：' + str(res))
        else:
            print('====url====data====header' + url + str(data))
            res = self.get_main(url, data, header)
            print('get请求结果：' + str(res))
        return res

