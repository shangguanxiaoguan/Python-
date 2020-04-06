"""
1.继承的概念：子类拥有父类的所有方法和属性
2.继承的语法：
   class 类名(父类名)：
      pass
3.子类继承自父类，可以直接享受父类中已经封装好的方法，不需要再次开发
  子类中应该根据职责，封装子类持有的属性和方法

4.专业术语：
  Dog类是Animal类的子类，Animal类是DOg类的父类，Dog类从Animal类继承
  Dog类是Animal类的派生类，Animal类是Dog类的基类，Dog类从Animal类派生

5.继承的传递性
  子类拥有父类以及父类的父类中封装的所有属性和方法

"""


class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

# Dog类继承自Animal类
class Dog(Animal):
    # def eat(self):
    #     print("吃")
    #
    # def drink(self):
    #     print("喝")
    #
    # def run(self):
    #     print("跑")
    #
    # def sleep(self):
    #     print("睡")

    def bark(self):
        print("叫")


# XiaoTianQuan类继承自Dog类
class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")


# 创建对象
# wangcai = Animal()
wangcai = Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()

# 第33节  继承的传递性
xtq = XiaoTianQuan()
xtq.fly()
xtq.bark()
xtq.sleep()
