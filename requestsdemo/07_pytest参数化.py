import pytest
from selenium import webdriver
from time import sleep

"""
学习地址：https://www.bilibili.com/video/BV1pU4y1J7Eq?p=84&spm_id_from=pageDriver
"""


"""
pytest参数化
   当一组测试用例有固定的测试数据时，就可以通过参数化的方式简化测试用例的编写
   通过pytest.mark.parametrize()方法设置参数：
     参数名："user,pw,expected"用来定义参数的名称
     参数值：通过数组定义参数值时，每一个元组都是一条测试用例的测试数据
     ids参数：默认None，用来重新定义测试用例名称
"""
@pytest.mark.parametrize(
    "user,pw,expect",
    ["zhangsan", "123456", "zhangsan,欢迎来到"],
    ["lisi", "123456", "lisi,欢迎来到"]
)

def test_login(user,pw,expected):
    driver = webdriver.Chrome()
    driver.get("有登录功能的URL地址")
    driver.find_element_by_link_text("登录").click()
    # driver.find_element_by_xpath("//*[@name='accounts']").send_keys("zhangshan")
    driver.find_element_by_xpath("//*[@name='accounts']").send_keys(user)
    # driver.find_element_by_xpath("//*[@name='pwd']").send_keys("123456")
    driver.find_element_by_xpath("//*[@name='pwd']").send_keys(pw)
    driver.find_element_by_xpath("//button[text()='登录']").click()
    sleep(3)

    welcome = driver.find_element_by_xpath("//*[contains(text(),'欢迎来到')]").text

    # assert 'excepted' == welcome
    assert expected == welcome
