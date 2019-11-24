class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")
        # 在初始化方法内部定义属性，调用时会有提示
        # self.name = "Tom"
        self.name = new_name

    def eat(self):
        print("%s爱吃鱼" % self.name)


# 创建类对象时，会自动调用初始化方法__init__
tom = Cat("Tom")
print(tom.name)
tom.eat()

lazy_cat = Cat("大懒猫")
lazy_cat.eat()
