import pytest
import requests
import mock


class TestMethod():
    @pytest.mark.mock
    def test_12306(self):
        url = 'https://apitest.hexiaoxiang.com/course/portal/api/v1/union/app/user/lesson/list?platform=0'
        headers = {
            'Authorization': 'c1eb27d366e9a55b440cce4f62e878c00e4a0be5e0804dbb11601a5ab3bb554c'
        }
        data = {
            "userId": "7393118869613203",
            "deviceId": "And.3cfdbb3b0287b0fed79432dcd50b9de7.fvpn",
            "types": 3,
            "token": "d60862e5cb47119b260f20ccafb03e75",
            "timestamp": 1590382152623,
            "sign": "86BDF442174FFD02F38C88E81CA83D8C"
        }
        mock_data = mock.Mock(return_value=data)
        test_12306 = mock_data
        res = requests.get(url=url, headers=headers)

        print(res.text)

# test_12306()

