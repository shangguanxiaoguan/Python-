import time

import requests

from selenium import webdriver

from case.byhypytest.webui import login_and_check


class Test_Login:

    def test_login_failed_UI_0001(self):
        # print("\n *** UI_0001 ****")
        # driver = webdriver.Chrome()
        # driver.implicitly_wait(10)
        # driver.get('http://127.0.0.1/mgr/sign.html')
        # driver.find_element_by_id('password').send_keys('88888888')
        # driver.find_element_by_css_selector("button[type='submit']").click()
        # time.sleep(2)
        # alert_text = driver.switch_to_alert().text
        # print(alert_text)

        # alert_text = login_and_check('', '88888888')
        alert_text = login_and_check(None, '88888888')

        assert alert_text == '请输入用户名'

    def test_login_failed_UI_0001(self):
        # print("\n *** UI_0001 ****")
        # driver = webdriver.Chrome()
        # driver.implicitly_wait(10)
        # driver.get('http://127.0.0.1/mgr/sign.html')
        # driver.find_element_by_id('username').send_keys('byhy')
        # # driver.find_element_by_id('password').send_keys('88888888')
        # driver.find_element_by_css_selector("button[type='submit']").click()
        # time.sleep(2)
        # alert_text = driver.switch_to_alert().text
        # print(alert_text)

        alert_text = login_and_check('hyby', None)

        assert alert_text == '请输入密码'
