"""
【异常捕获的完整语法：】
try:
    # 尝试执行的代码
except 错误类型1：
    # 针对错误类型1，对应的代码处理
except (错误类型3，错误类型4):
    pass
except Exception as result:
    print(result)
else:
    # 没有异常才会执行的代码
finally:
    # 无论是否有异常，都会执行的代码


"""


try:
    num = int(input("请输入一个整数："))
    print(num)
except:
    print("请输入正确的整数")

"""
捕获未知错误
"""
try:
    num = int(input("请输入一个整数："))
    result = 8 / num
    print(result)

# 根据错误类型捕获异常
except ValueError:
    print("请输入正确的整数。")

# 捕获未知错误
except Exception as result:
    print("未知错误 %s" % result)


"""
【异常的传递性】
 1. 当函数/方法执行出现异常，会将异常传递给函数/方法的调用方
 2. 利用异常的传递性，可以在主程序捕获异常，可以保证代码的整洁
"""

"""
【抛出raise异常】
"""