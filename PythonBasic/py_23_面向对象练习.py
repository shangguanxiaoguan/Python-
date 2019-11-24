"""
小明爱跑步
"""


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
