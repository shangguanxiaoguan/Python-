class Cat:
    def __init__(self):
        print("这是一个初始化方法")
        # 在初始化方法内部定义属性，调用时会有提示
        self.name = "Tom"

    def eat(self):
        print("%s爱吃鱼" % self.name)


# 创建类对象时，会自动调用初始化方法__init__
tom = Cat()
print(tom.name)
tom.eat()
