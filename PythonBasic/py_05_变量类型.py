"""
个人信息：
姓名：小明
年龄：18岁
性别：是男生
身高：178cm
体重：65kg
"""

# 在Python中，定义变量时是不需要指定变量的类型的
# 在运行的时候，Python解释器，会根据赋值语句等号右侧的数据
# 自动推断出变量中保存数据的准确类型

# str : 字符串
name = "小明"
# int : 整数类型
age = 18
# bool : 布尔类型
gender = True
# float : 浮点数
height = 1.75

weight = 75.0

print(name)

"""
数据类型可以分为数字型和非数字型。
数字型：
 整型（int）
 浮点型（float）
 布尔型（bool）
    真 True 非 0 数 ——非零即真
    假 False 0
 复数型（complex）
    主要用于科学计算，例如：平面场问题、波动问题、电感电容等问题
非数字型：
  字符串
  列表
  元组
  字典

"""

# 可以使用type()函数查看变量类型
type(name)

# 提示：在Python2.x中，整数根据保存数值的长度还分为：
# int(整数)
# long(长整数)
# 在Python3中，整数只有int类型没有long类型


"""
不同类型变量之间的计算：
1）数字型变量之间可以直接计算，
   如果变量时bool型，在计算时，
      True对应的数字是1
      False对应的数字是0
      
2）字符串变量之间使用 + 拼接字符串 

3）字符串变量可以和整数使用 * 重复拼接相同的字符串

4）数字型变量和字符串之间不能进行其他计算

"""
first_name = "三"
last_name = "张"
print(last_name + first_name)
print(first_name * 10)
print((last_name + first_name) * 10)


"""
变量的输入
"""
# input函数实现键盘输入
# 语法： 字符串变量 = input("提示信息： ")
# 用户输入的任何内容，Python都认为是一个字符串

password = input("请输入银行卡密码：")

# 类型转换函数
# int(x):将x转换为一个整数
# float(x):将x转换为一个小数


"""
买苹果增加版演练：
"""
# 1.输入苹果的单价
price_str = input("请输入苹果的单价：")

# 2.输入苹果的重量
weight_str = input("请输入购买苹果的重量：")

# 3.计算支付的总金额
# 注意：两个字符串变量之间是不能直接用乘法的
# money = price_str * weight_str
# 1>将价格转换成小数
price_fl = float(price_str)
# 2>将重量转换成小数
weight_fl = float(weight_str)
# 3>两小数相乘
money = price_fl * weight_fl
# 4.输出计算后的金额
print(money)







