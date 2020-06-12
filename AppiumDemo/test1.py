import time

from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': '3584d0d8',
    'platformVersion': '5.1.1',
    'appPackage': 'free.vpn.unblock.proxy.vpnforce',
    'appActivity': 'com.force.vpn.app.ui.activity.VpnForceSplashActivity',
    'unicodeKeyboard': True,   # 使用Unicode编码方式发送字符串
    'resetKeyboard': True      #  隐藏键盘
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 等待页面加载完成
time.sleep(5)
driver.find_element_by_id("free.vpn.unblock.proxy.vpnforce:id/connect_view").click()
time.sleep(5)
driver.find_element_by_id("free.vpn.unblock.proxy.vpnforce:id/iv_support_view").click()
time.sleep(2)
driver.find_element_by_id("free.vpn.unblock.proxy.vpnforce:id/et_content").click()
time.sleep(2)
# driver.find_element_by_id("free.vpn.unblock.proxy.vpnforce:id/et_content").send_keys(u"zha")
driver.find_element_by_id("free.vpn.unblock.proxy.vpnforce:id/et_content").send_keys(u"连接很好")

# driver.scroll( "free.vpn.unblock.proxy.vpnforce:id/rb_network", "free.vpn.unblock.proxy.vpnforce:id/tv_submit")

"""
appium 元素定位：
1. id定位——> resource-id 【有些clickable值为false时，不可点击，执行点击无反应】
2. name定位——> text属性
3. class属性——> class属性【一般一个页面上的class属性不唯一，元素不唯一会报错】
4. accessibility_id——> content-desc属性
5.

"""




