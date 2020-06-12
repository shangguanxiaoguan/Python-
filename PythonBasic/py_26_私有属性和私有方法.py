"""
1.定义方式：
  在定义属性和方法时，在属性名和方法名前增加两个下划线，定义的就是私有属性和方法

"""
class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        """
        【知识点】：
         在对象的内部，是可以访问对象的私有属性的
        """
        print("%s 的年龄是 %d" %(self.name, self.__age))

lisi = Women("李四")
# 私有属性，在外界不能够被直接访问
# print(lisi.__age)

# 私有方法，同样在外界不能够被直接访问
# lisi.__secret()

"""
伪私有属性和私有方法(科普)
1.在Python中，并没有真正意义的私有
2.使用  _类名__名称  的方式，依然可以访问私有属性和私有方法

"""

print(lisi._Women__age)
lisi._Women__secret()

