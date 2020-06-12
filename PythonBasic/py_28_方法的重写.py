"""
方法的重写：
1.应用场景：
  当父类的方法实现不能满足子类需求时，可以对方法进行重写（override）

2.重写父类方法有两种情况：
  a.覆盖父类的方法：
    相当于在子类中定义了一个和父类同名的方法并且实现
    【***】重写之后，在运行时，只会调用子类中重写的方法，而不再会调用父类封装的方法

  b.对父类方法进行扩展
    1.在子类中重写父类的方法
    2.在需要的位置使用super().父类方法 来调用父类方法的执行
    3.代码其他的位置针对子类的需求，编写子类特有的代码实现

3.关于super
  a.super是一个特殊的类
  b.super()就是使用super类创建出来的对象
  c.最常使用的场景就是在重写父类方法时，调用在父类中封装的方法实现

"""


class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

# Dog类继承自Animal类
class Dog(Animal):
    # def eat(self):
    #     print("吃")
    #
    # def drink(self):
    #     print("喝")
    #
    # def run(self):
    #     print("跑")
    #
    # def sleep(self):
    #     print("睡")

    def bark(self):
        print("叫")


# XiaoTianQuan类继承自Dog类
class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")


    # 覆盖父类的方法：子类重写父类方法，运行时，只调用子类重写的方法
    def bark(self):
        # 1.针对子类特有的需求，编写代码
        print("狗神一样的叫")

        # 2.使用 super(). 调用原本在父类中封装的方法
        # super().bark()

        # 父类名.方法(self)
        # 【知道就行，使用这种方式容易发生递归调用，导致出现死循环】
        Dog.bark(self)

        # 3.增加子类其他的代码
        print("$%#%$@%%")


    # def eat(self):
    #     # 重写父类的方法
    #     print("吃天食")



xtq = XiaoTianQuan()
xtq.fly()

xtq.bark()
xtq.eat()



class A:
    def work(self):
        print('A.work被调用')

class B(A):
    '''B类继承A类'''
    def work(self):
        print('B.work被调用')

    def super_work(self):
        '''调用B类自己的work方法'''
        self.work()  # B.work被调用，调用自身类的方法，和调用属性一样
        super(B, self).work()  # A.work被调用， 借助super调用父类被覆盖的方法
        # super().work()  # A.work被调用  这种必须在方法内使用 ，可以省略（自身类）参数

b = B()
b.super_work()