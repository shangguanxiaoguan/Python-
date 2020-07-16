import unittest
import pytest

from requeststest.get import RunMain


class TestMethod:

    def setUp(self):
        self.run = RunMain()
        print("==============")

    def test_01(self):
        url = 'http://54.241.21.249:8089/skyvpn/v2/invite/getUrl'
        data = {
            "userId": "7393118869613203",
            "deviceId": "And.3cfdbb3b0287b0fed79432dcd50b9de7.fvpn",
            "types": 3,
            "token": "d60862e5cb47119b260f20ccafb03e75",
            "timestamp": 1590382152623,
            "sign": "86BDF442174FFD02F38C88E81CA83D8C"
        }
        # run = RunMain()
        res = self.run.run_main(url, 'POST', data)
        print("test_01------>" + res)
        assert res['result'] == 0

    def test_02(self):
        url = 'http://54.241.21.249:8089/skyvpn/v2/invite/getUrl'
        data = {
            "userId": "7393118869612558",
            "deviceId": "And.7b71b6ca37a1cd40c3a5a9e3596661f5.fvpn",
            "types": 3,
            "token": "2a02bf1a5fb1895cd1bd21d471e81b37",
            "timestamp": 1590382152623,
            "sign": "86BDF442174FFD02F38C88E81CA83D8C"
        }
        # run = RunMain()
        res = self.run.run_main(url, 'POST', data)
        print("test_02---->" + res)

