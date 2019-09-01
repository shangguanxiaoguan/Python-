"""
1.定义函数——封装独立的功能
2.调用函数——享受封装的成果
3.函数的作用：代码重用
4.def是英文define的缩写
5.函数名称应该能够表达函数封装代码的功能
6.函数名称的命名应该符合标识符的命名规则

**** 定义函数的上方要与其他代码保留两行空格
"""


def multiple_table():
    print("=======输出九九乘法表=========")
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print("%d * %d = %d" % (j, i, j * i), end="  ")
            j += 1
        print("")
        i += 1

# *** 注意：定义好函数之后，只表示封装了一段代码
# 如果不主动调用函数，函数是不会执行的


name = "小明"
# say_hello()   # 函数调用不能在函数定义的上方，，因为在调用函数的时候，必须让Python知道已经定义了函数


def say_hello():
    """增加函数注释。光标放在函数调用处，按Ctrl + Q可以看到函数注释"""
    print("hello 1")
    print("hello 2")
    print("hello 3")


print(name)

say_hello()

print(name)


"""
函数的参数：
1. 形参和实参
   形参：定义函数时，小括号中的参数，是用来接收参数用的，在函数内部作为变量使用
   实参：调用函数时，小括号中的参数，是用来把数据传递到函数内部用的
2. 函数的返回值
   使用return关键字   
   **** 注意：return 下方的代码不会被执行到
3. 函数的嵌套调用：
"""


# def sum_2_num():
def sum_2_num(num1, num2):
    """对两个数字的求和"""
    # num1 = 10
    # num2 = 23
    result = num1 + num2
    print("%d + %d = %d" % (num1, num2, result))


sum_2_num(23, 45)


def sum_return(num1, num2):
    """函数的返回值"""

    return num1 + num2
    # **** 注意：return 下方的代码不会被执行到


result1 = sum_return(32, 23)
print(result1)

# 函数嵌套的演练


def print_line(char, times):
    """打印单行分割线

    :param char: 分割线使用的分割字符
    :param times: 分割线重复的次数
    """
    print(char * times)


def print_lines(char, times):
    """函数嵌套的练习：打印多行分割线

    :param char: 分割线使用的分割字符
    :param times: 分割线重复的次数
    """
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1


print_lines("-", 30)
