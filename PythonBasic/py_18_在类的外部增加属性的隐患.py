class Cat:
    def eat(self):
        print(" %s爱吃鱼" % self.name)

    def drink(self):
        print(" %s爱喝水" % self.name)


"""
设置简单属性，给对象增加属性，不推荐使用该方法
"""
sheep_cat = Cat()
# 如果把增加的属性放在方法调用的后面，程序就会报错
# sheep_cat.name = "贪睡猫"
sheep_cat.eat()
sheep_cat.drink()
sheep_cat.name = "贪睡猫"