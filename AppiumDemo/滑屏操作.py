import time

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

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

# ����֮ǰ�ȵȴ�����������
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("FAQS")')
WebDriverWait(driver, 30).until(EC.visibility_of_element_located(loc))

"""
���²�������Android��IOSϵͳ���ɷ�װ������������
"""

# ��ȡ��Ļ�ĸ߶ȺͿ�� height��width
size = driver.get_window_size()

# ��ʼλ��
start_x = size["width"] * 0.9
start_y = size["height"] * 0.5

# ��ֹλ��
end_x = size["width"] * 0.1
end_y = size["height"] * 0.5   # ��Ϊ�û�����ϰ�߶����м䣬����ȡ0.5

"""
���һ�����Y�᲻����X�������ƶ�
"""

# ��������
driver.swipe(start_x, start_y, end_x, end_y)
time.sleep(2)   # ��������
driver.swipe(start_x, start_y, end_x, end_y)


# �������һ�
driver.swipe(end_x, end_y, start_x, start_y)

"""
���»�����X�᲻����Y�������ƶ�
"""

# ���ϻ������������ϻ�
driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5, size["height"] * 0.1)

# ���»������������ϻ�
driver.swipe(size["width"] * 0.5, size["height"] * 0.1, size["width"] * 0.5, size["height"] * 0.9)
