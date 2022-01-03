# 1.导包 unittest requests
import unittest
import requests


# 2.新建测试类 ---》unittest.TestCase
class TPShopLogin(unittest.TestCase):
    """ 注意： 测试类必须继承 unittest.TestCase"""
    # 3. setup
    def setUp(self):
        """
        作用：test开头的方法执行之前，首先会执行
        :return:
        """
        # 获取session对象
        self.session = requests.session()
        # 登录URL
        self.url_login = ""
        # 验证码URL
        self.verify_code = ""

    # 4。teardown
    def tearDown(self):
        """
        作用：test开头的方法执行之后，会被执行
        :return:
        """
        # 关闭session
        self.session.close()

    # 5. 登录成功
    def test_login_success(self):
        # 请求验证码
        self.session.get(self.verify_code)

        # 请求登录
        data = {}
        res = self.session.post(url=self.url_login, data=data)

        # 断言
        self.assertEqual("登录成功", res.json()['msg'])

    # 6. 登录失败--账号不存在
    def test_username_not_exist(self):
        pass

    # 7。登录失败--密码错误
    def test_password_error(self):
        pass


if __name__ == '__main__':
    unittest.main()
