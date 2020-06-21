from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
    'platformName': 'Android',
    'deviceName': '3584d0d8',
    'platformVersion': '5.1.1',
    'appPackage': 'free.vpn.unblock.proxy.vpnforce',
    'appActivity': 'com.force.vpn.app.ui.activity.VpnForceSplashActivity',
    'unicodeKeyboard': True,   # ʹ��Unicode���뷽ʽ�����ַ���
    'resetKeyboard': True,      # ���ؼ���
    'onReset': True   # APP���治����   ���ַ�ʽ������������ҳ
}


# ����appium������
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

"""
�Ź�������������ư��� ���ʰ�119�ڿ�ʼ
"""
# �ҵ������Ź�����Ǹ�Ԫ�أ����¼��Ԫ�أ����Ǹ�������
ele = driver.find_element_by_id("")
# ��ȡ�����Ź����Ԫ�صĴ�С
size = ele.size
# ���ֵĲ��� �ߺͿ�һ��
step = size["width"]/6    # �Ÿ��㽫������ƽ���ֳ���6��
# Ԫ�ص�������� �������Ͻ�
ori = ele.location
point1 = (ori["x"] + step, ori["y"] + step)  # �Ź����е�һ����
point2 = (point1[0] + step * 2, point1[1])  # �Ź����еڶ����㣺�����point1��X��������2*step
point3 = (point2[0] + step * 2, point2[1])  # �Ź����е������㣺�����point2��X��������2*step
point4 = (point3[0] - step * 2, point3[1] + step * 2)  # �Ź����е�����㣺�����point3��X�������2*step��Y��������2*step
point5 = (point4[0], point4[1] + step * 2)    # �Ź����еڰ˸��㣺�����point4��X�᲻�䣬Y��������2*step

TouchAction(driver).press(x=point1[0], y=point1[1]).wait(200).\
    move_to(x=point2[0], y=point2[1]).\
    move_to(x=point3[0], y=point3[1]).\
    move_to(x=point4[0], y=point4[1]).\
    move_to(x=point4[0], y=point4[1]).\
    release().\
    perform()


# 120��Appium���ò�������������

