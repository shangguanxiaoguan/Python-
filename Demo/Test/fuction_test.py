import math
import uuid

"""
UUID是128位的全局唯一标识符，通常由32字节的字符串表示。它可以保证时间和空间的唯一性，也称为GUID，
全称为：UUID —— Universally Unique IDentifier，Python 中叫 UUID。
它通过MAC地址、时间戳、命名空间、随机数、伪随机数来保证生成ID的唯一性。
UUID主要有五个算法，也就是五种方法来实现。
"""
u = uuid.uuid1()
device_tmp = str(u).replace('-', '')
print(u)
print(device_tmp)


"""
python3.5的math模块新增一个isclose函数用来判断两个浮点数的值是否接近或相等，这是由于浮点数的计算总是存在一定的误差。

"""
print(math.isclose(1.25, 1.25))
print(math.isclose(2.1, 2.2, rel_tol=0.00001))
print(math.isclose(2.1, 2.2, abs_tol=0.2))
