import pytest
from selenium import webdriver
from time import sleep


"""
pytest常用运行参数：
   -s  打印信息
   -V  打印详细信息
   -k  运行名称中包含某个字符串的测试用例
   -q  简化输出信息
   -x  如果出现一条测试用例失败，退出测试
   pytest.main("-s", "/test_dir")   运行测试目录
   pytest.main("-s", "08_pytest常用运行参数::test_hello")   指定特定的类或方法执行
"""


"""
查看pytest版本：  pytest --version
显示可用的内置函数参数：  pytest --fixtures
获取帮助： pytest --help
"""


def test_login():
    driver = webdriver.Chrome()
    driver.get("有登录功能的URL地址")
    driver.find_element_by_link_text("登录").click()
    driver.find_element_by_xpath("//*[@name='accounts']").send_keys("zhangshan")
    # driver.find_element_by_xpath("//*[@name='accounts']").send_keys(user)
    driver.find_element_by_xpath("//*[@name='pwd']").send_keys("123456")
    # driver.find_element_by_xpath("//*[@name='pwd']").send_keys(pw)
    driver.find_element_by_xpath("//button[text()='登录']").click()
    sleep(3)

    welcome = driver.find_element_by_xpath("//*[contains(text(),'欢迎来到')]").text

    # assert 'excepted' == welcome
    assert expected == welcome


def test_hello():
    print("hello")
    assert 1 == 1


if __name__ == '__main__':
    pytest.main(["-s", "-v", "08_pytest常用运行参数.py"])
