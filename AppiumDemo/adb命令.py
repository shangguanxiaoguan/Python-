"""
adb devices
adb logcat 打印log信息
adb pull <手机路径><本机路径>从手机中拉取信息放到本地电脑上
adb push <本机路径><手机路径>
adb shell（root过的手机）
adb shell dumpsys activity | find "mFocusedActivity"
adb kill-server 停止adb服务
adb start-server
adb shell pm list packages 列出所有包名
-f 列出所有apk路径及包名
-s 列出系统apk路径及包名
-3 列出用户apk路径及包名

"""