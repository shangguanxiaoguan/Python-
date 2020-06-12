"""
练习重点：
1.封装是面向对象编程的一大特点
2.面向对象编程的第一步——将属性和方法封装到一个抽象的类中
3.外界使用类创建对象，然后让对象调用方法
4.对象方法的细节都被封装在类的内部

一个对象的属性可以是另外一个类创建的对象

"""

class Gun:
    def __init__(self, model):
        # 1.枪的型号
        self.model = model
        # 2.子弹的数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 1.判断子弹的数量
        if self.bullet_count <= 0:
            print("[%s]没有子弹了" % self.model)
            return
        # 2.发射子弹
        self.bullet_count -= 1
        # 3.提示发射信息
        print("[%s]发射成功，剩余[%d]发子弹" % (self.model, self.bullet_count))
        # self.bullet_count = self.bullet_count

class Soldier:
    def __init__(self, name):
        self.name = name
        # 新兵没有枪
        # 【知识点】：
        # 在定义属性时，如果不知道设置什么初始值，可以设置为None
        # None关键字表示什么都没有
        # 表示一个空对象，没有方法和属性，是一个特殊的常量
        # 可以将None赋值给任何一个变量
        # 新兵没有枪，不知道给该属性赋予什么初始值，就设置为None
        self.gun = None

    def fire(self):
        # 1.检查士兵是否有枪

        """
        【知识点】：
        1.身份运算符：
          用于比较两个对象的内存地址是否一致——是否是对同一个对象的引用
        2.针对None比较时，使用is判断
          is : 判断两个标识符是不是引用同一个对象
          is not : 判断两个标识符是不是引用不同对象
        3.is 和 == 区别：
          is ：用于判断两个变量引用对象是否为同一个
          == ：用于判断引用变量的值是否相等

        """

        # if self.gun == None:
        if self.gun is None:
            print("[%s]没有枪支" % self.name)
            return
        # 2.给枪装子弹
        self.gun.add_bullet(30)

        # 3.扣动扳机，发射子弹
        self.gun.shoot()

# 1.创建枪对象
ak47 = Gun("AK47")
# ak47.add_bullet(10)
# ak47.shoot()

# 2.创建士兵对象
zhangsan = Soldier("张三")
zhangsan.gun = ak47
zhangsan.fire()
print(zhangsan)