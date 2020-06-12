class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍" % self.name)


class XiaoTianDog(Dog):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 飞上天去玩耍" % self.name)


class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 一起愉快的玩耍" % (self.name, dog.name))

        """
        game 方法是在Dog父类中定义的
        在程序执行时，传入不同的狗对象实参，就会产生不同的执行效果
        """
        dog.game()



wangcai = Dog("旺财")
xiaotianquan = XiaoTianDog("哮天犬")

xiaoming = Person("小明")
xiaoming.game_with_dog(xiaotianquan)
