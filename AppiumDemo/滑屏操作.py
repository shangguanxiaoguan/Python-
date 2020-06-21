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
    'unicodeKeyboard': True,   # 使用Unicode编码方式发送字符串
    'resetKeyboard': True,      # 隐藏键盘
    'onReset': True   # APP缓存不重置   这种方式可以跳过启动页
}


# 连接appium服务器
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 滑屏之前先等待界面加载完成
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("FAQS")')
WebDriverWait(driver, 30).until(EC.visibility_of_element_located(loc))

"""
以下操作不分Android和IOS系统，可封装起来后续调用
"""

# 获取屏幕的高度和宽度 height、width
size = driver.get_window_size()

# 起始位置
start_x = size["width"] * 0.9
start_y = size["height"] * 0.5

# 终止位置
end_x = size["width"] * 0.1
end_y = size["height"] * 0.5   # 因为用户操作习惯都在中间，所以取0.5

"""
左右滑动：Y轴不动，X轴左右移动
"""

# 从右向左滑
driver.swipe(start_x, start_y, end_x, end_y)
time.sleep(2)   # 连续滑动
driver.swipe(start_x, start_y, end_x, end_y)


# 从左向右滑
driver.swipe(end_x, end_y, start_x, start_y)

"""
上下滑动：X轴不动，Y轴上下移动
"""

# 向上滑动，从下往上滑
driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5, size["height"] * 0.1)

# 向下滑动，从上往上滑
driver.swipe(size["width"] * 0.5, size["height"] * 0.1, size["width"] * 0.5, size["height"] * 0.9)
