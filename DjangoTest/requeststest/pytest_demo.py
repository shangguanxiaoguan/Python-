import pytest
import requests

"""
1、在终端运行用例：
    进入用例所在根目录，输入pytest **.py
2、在终端显示测试代码中print的内容
   pytest -s
3、在终端显示更详细的执行信息，包括每个测试类、测试函数的名字
   pytest -s -v 或者  pytest -sv 
4、产生测试报告的命令
   4.1 生成html报告
        pytest --html=report.html --self-contained-html **.py
   4.2 生成allure报告
       4.2.1 生成allure结果目录
            'alluredir','../report/reportallure'
       4.2.2 生成allure报告
            1.安装一个allure工具
            2.解压安装包
            3.配置allure工具的环境变量
            4.进入report报告的目录
            5.运行命令：allure generate ../reportallure/ -o ./reporthtml/ --clean
5、在终端根据标签来执行用例
   pytest -m 标签名

6、pytest需要动态关联时，可以将需要用到的变量定义为一个全局变量
 比如，第一个pytest中请求到的cookies，在第二个pytest中需要用到，就将需要用到的cookies定义为全局变量
 global cookies
 cookies = res.json()['cookies'] 
   
"""


def setup_module():
    print("\n *** 初始化-模块  可以执行用例的公共初始化***")


def teardown_module():
    print("\n *** 清除-模块 ***")


class Test_Demo:

    @classmethod
    def setup_class(cls):
        print("\n===== 初始化 == 类===")

    @classmethod
    def teardown_class(cls):
        print("\n===== 清除 == 类===")

    def setup_module(self):
        print("\n ------ 初始化-方法  ------")

    def teardown_module(self):
        print("\n ------ 清除-方法 ------")

    @pytest.mark.smoke
    def test_C001001(self):
        print('\n用例C001001')
        global cookies   # 定义全局变量
        cookies = 'test'
        assert 1 == 1

    @pytest.mark.smoke
    def test_C001002(self):
        # url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-07-17&leftTicketDTO.from_station=FZS&leftTicketDTO.to_station=HGH&purpose_codes=ADULT'

        # requests.get(url=url, cookies=cookies)  # 用到全局变量
        print('\n用例C001002')

        assert 2 == 2

    @pytest.mark.smoke
    def test_C001003(self):
        print('\n用例C001003')
        assert 3 == 2

    class Test_错误密码2:
        @pytest.mark.smoke
        @pytest.mark.webtest
        def test_C001021(self):
            print('\n用例C001021')
            assert 1 == 1

        def test_C001022(self):
            print('\n用例C001022')
            assert 2 == 2



