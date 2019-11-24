class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


tom = Cat()
tom.eat()
tom.drink()

# 输出这个变量引用的对象是由哪一个类创建的对象，以及在内存中的地址
print(tom)


addr = id(tom)
# %d 可以以 10 进制输出数字
print("%d" % addr)
# %x 可以以16进制输出数字
print("%x" % addr)

# 新建一个猫对象
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

lazy_cat2 = lazy_cat
print(lazy_cat2)

"""
设置简单属性，给对象增加属性，不推荐使用该方法
"""
sheep_cat = Cat()
sheep_cat.name = "贪睡猫"
sheep_cat.eat()
sheep_cat.drink()


