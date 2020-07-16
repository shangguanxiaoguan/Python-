import pytest

"""
1、在终端运行用例：
    进入用例所在根目录，输入pytest **.py
2、在终端显示测试代码中print的内容
   pytest -s
3、在终端显示更详细的执行信息，包括每个测试类、测试函数的名字
   pytest -s -v 或者  pytest -sv 
4、产生测试报告的命令
   pytest --html=report.html --self-contained-html **.py
5、在终端根据标签来执行用例
   pytest -m 标签名
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
        assert 1 == 1

    @pytest.mark.smoke
    def test_C001002(self):
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



