"""
面向对象的三大特性：
 1.封装：根据职责将属性和方法封装到一个抽象的类中
 2.继承：实现代码的重用，相同的代码不需要重复的编写。
         子类拥有父类的所有方法和属性
 3.多态：不同的对象调用相同的方法，产生不同的执行结果，增加代码的灵活度
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