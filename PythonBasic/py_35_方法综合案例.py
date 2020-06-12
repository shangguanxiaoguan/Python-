class Game():
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("游戏帮助信息。。。")

    @classmethod
    def show_top_score(cls):
        print("历史最高分 %d" % cls.top_score)

    def start_game(self):
        print("%s 开始进入游戏" % self.player_name)


# 1. 查看游戏的帮助信息
Game.show_help()

# 2. 查看历史最高分
Game.show_top_score()

# 3. 创建游戏对象
game = Game("吕布")
game.start_game()

"""
【案例小结】
1. 方法内部需要访问实例属性  ——定义实例方法
   实例方法内部可以使用类名.访问类属性
   既需要访问实例属性，又需要访问类属性时，也定义为实例方法。
2. 方法内部只需要访问类属性 ——定义为类方法
3. 方法内部不需要访问实例属性和类属性 ——静态方法


"""