"""
1. 单例设计模式的应用场景
    音乐播放对象
    回收站对象
    打印机对象
2. 单例设计模式概念
  目的：让类创建的对象，在系统中只有唯一的一个实例
        每一次执行 类名() 返回的对象，内存地址都是相同的
3. __new__方法
  __new__是一个由 object 基类提供的内置的静态方法，主要作用有两个：
  1）. 在内存中为对象分配空间
  2）. 返回对象的引用
  python解释器获得对象的引用后，将引用作为第一个参数，传递给__init__方法
4. 重写__new__ 方法一定要 return super().__new__(cls)
   否则python解释器得不到分配了空间的对象引用，就不会调用对象的初始化方法


"""


class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        # 创建对象时，会自动调用new方法
        print("创建对象，分配空间")
        # 为对象分配空间
        instance = super().__new__(cls)
        # 返回对象的引用 【如果不返回，python解释器就不会往下执行了】
        return instance

    def __init__(self):
        print("播放器初始化")


player = MusicPlayer()
print(player)