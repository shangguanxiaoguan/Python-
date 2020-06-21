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
    'resetKeyboard': True      #  隐藏键盘
}
# 连接appium服务器
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 等待页面加载完成，【没有明确元素时可用这个等待，比如启动界面】
# time.sleep(5)

# 等待元素出现  【有明确元素时，使用这种方式等待】
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(MobileBy.ID, 'free.vpn.unblock.proxy.vpnforce:id/connect_view'))

driver.find_element_by_id("free.vpn.unblock.proxy.vpnforce:id/connect_view").click()
time.sleep(5)
driver.find_element_by_id("free.vpn.unblock.proxy.vpnforce:id/iv_support_view").click()
time.sleep(2)
driver.find_element_by_id("free.vpn.unblock.proxy.vpnforce:id/et_content").click()
time.sleep(2)

# 往文本框中输入内容
# driver.find_element_by_id("free.vpn.unblock.proxy.vpnforce:id/et_content").send_keys(u"zha")
driver.find_element_by_id("free.vpn.unblock.proxy.vpnforce:id/et_content").send_keys(u"连接很好")

# driver.scroll( "free.vpn.unblock.proxy.vpnforce:id/rb_network", "free.vpn.unblock.proxy.vpnforce:id/tv_submit")

driver.find_element_by_class_name()


# 对应content-desc属性
driver.find_element_by_accessibility_id()

# 前面的属性查找都不可行时，可以使用这种方法，这种方法效率快些，可用多个属性
driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                           '"free.vpn.unblock.proxy.vpnforce:id/et_content").text("help us")')


"""
appium 元素定位：
1. id定位——> resource-id 【有些clickable值为false时，不可点击，执行点击无反应】
2. name定位——> text属性
3. class属性——> class属性【一般一个页面上的class属性不唯一，元素不唯一会报错】
4. accessibility_id——> content-desc属性
5.xpath定位（少用，效率不高）

"""




