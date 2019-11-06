
import time;
# 获取当前的时间戳
ticks = time.time()
print("当前时间戳为：%s" % ticks)

# 从返回浮点数的时间戳方式向时间元祖转换
localtime = time.localtime(time.time())
print("本地时间为：" , localtime)

# 获取格式化时间
localtime = time.asctime(time.localtime(time.time()))
print("当前格式化时间为：",localtime)

print("localtime:",time.localtime())
# 格式化成2019-11-05 14:54:56形式
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# 格式化成Tue Nov 05 15:12:49 2019形式
print(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))
# 将格式字符串转换为时间戳
str_time = "2019-11-05 15:12:49"
print(time.mktime(time.strptime(str_time,"%Y-%m-%d %H:%M:%S")))

# %y 两位数的年份表示
# %Y 四位数的年份表示
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）

# 获取某月日历
import calendar
cal = calendar.month(2020,12)
print("输出2020年12月份的日历：")
print(cal)


"""
File对象的属性
"""

fo = open("foo.txt","w")
print("文件名：", fo.name)
print("是否已关闭：", fo.closed)
print("访问模式：", fo.mode)
# print("末尾是否强制加空格：", fo.softspace)

#  write方法&&close方法
fo.write("Python basic sleep")
fo.close()

# read方法
fo = open("foo.txt","r")
str = fo.read(5)
print("读取的字符串是：", str)
fo.close()

