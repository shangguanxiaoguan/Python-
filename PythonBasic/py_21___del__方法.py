class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 去了" % self.name)

 
# tom 是个全局变量
tom = Cat("Tom")
# print(tom.name)
del tom
print("-" * 50)

"""
生命周期：
1.一个对象从调用 类名() 创建，生命周期开始
2.一个对象的 __del__方法一旦被调用，生命周期结束
3.在对象的生命周期内，可以访问对象属性，或者让对象调用方法

"""
