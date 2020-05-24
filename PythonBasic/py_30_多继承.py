class A:
    def test(self):
        print("test 方法")


class B:
    def demo(self):
        print("demo 方法")


class C(A, B):
    """
    多继承可以让子类对象同时具有多个父类的属性和方法
    """
    pass


# 创建子类对象
# c = C()
# c.test()
# c.demo()

"""
Python中的MRO方法 ——方法搜索顺序
  内置属性
  主要用于在多继承时判断方法、属性的调用路径
"""

class A:
    def test(self):
        print("A-- test 方法")

    def demo(self):
        print("A-- demo方法")


class B:
    def demo(self):
        print("B-- demo 方法")

    def test(self):
        print("B-- test方法")


class C(A, B):
    """
    多继承可以让子类对象同时具有多个父类的属性和方法
    """
    def mroTest(self):
        print("C-- mroTest")


# 创建子类对象
c = C()
c.test()
c.demo()
print(C.__mro__)

"""
3.新式类和经典类
  新式类：以Object为基类的类
  经典类：不以Object为基类的类
  可以使用dir函数查看
  python3.x中提供的都是新式类
"""


class A(object):
    pass

a = A()
print(dir(a))