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
    'unicodeKeyboard': True,   # 使用Unicode编码方式发送字符串
    'resetKeyboard': True,      # 隐藏键盘
    'onReset': True   # APP缓存不重置   这种方式可以跳过启动页
}


# 连接appium服务器
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

"""
九宫格手势密码绘制案例 柠檬班119节开始
"""
# 找到包裹九宫格的那个元素（以下简称元素），是个正方形
ele = driver.find_element_by_id("")
# 获取包裹九宫格的元素的大小
size = ele.size
# 均分的步长 高和宽一样
step = size["width"]/6    # 九个点将正方形平均分成了6份
# 元素的起点坐标 ——左上角
ori = ele.location
point1 = (ori["x"] + step, ori["y"] + step)  # 九宫格中第一个点
point2 = (point1[0] + step * 2, point1[1])  # 九宫格中第二个点：相对于point1，X轴增加了2*step
point3 = (point2[0] + step * 2, point2[1])  # 九宫格中第三个点：相对于point2，X轴增加了2*step
point4 = (point3[0] - step * 2, point3[1] + step * 2)  # 九宫格中第五个点：相对于point3，X轴减少了2*step，Y轴增加了2*step
point5 = (point4[0], point4[1] + step * 2)    # 九宫格中第八个点：相对于point4，X轴不变，Y轴增加了2*step

TouchAction(driver).press(x=point1[0], y=point1[1]).wait(200).\
    move_to(x=point2[0], y=point2[1]).\
    move_to(x=point3[0], y=point3[1]).\
    move_to(x=point4[0], y=point4[1]).\
    move_to(x=point4[0], y=point4[1]).\
    release().\
    perform()


# 120节Appium常用操作（二）看完

