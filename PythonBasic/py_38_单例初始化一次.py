class MusicPlayer:
    # 记录第一个被创建对象的引用
    instance = None

    # 标记执行初始化的动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
      # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2.调用父类方法，为第一个创建的对象分配空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        # 1. 判断是否执行过初始化
        if MusicPlayer.init_flag:
            return

        # 2. 如果没有执行过初始化，则执行
        print("初始化函数")

        # 3.标记已执行过初始化
        MusicPlayer.init_flag = True

player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)