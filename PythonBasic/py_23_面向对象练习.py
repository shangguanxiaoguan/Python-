"""
面向对象的三大特性：
 1.封装：根据职责将属性和方法封装到一个抽象的类中
 2.继承：实现代码的重用，相同的代码不需要重复的编写。
         子类拥有父类的所有方法和属性
         针对子类特有的需求，编写特定的代码
 3.多态：不同的子类对象调用相同的父类方法，产生不同的执行结果
         可以增加代码的灵活度
         以继承和重写父类方法为前提
         是调用方法的技巧，不会影响到类的内部设计
"""

# 小明爱跑步

class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫 %s，我的体重是%.2f 公斤" % (self.name, self.weight)

    def run(self):
        # pass
        print("%s 爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        # pass
        print("%s 是吃货，越吃越胖" % self.name)
        self.weight += 1


xiaoming = Person("小明", 75)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

xiaomei = Person("小美", 45)
xiaomei.run()
xiaomei.eat()
print(xiaomei)   