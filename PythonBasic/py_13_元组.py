"""
1. 元组（Tuple）和列表[list]的区别：
  1）元组用()定义，列表用[]定义
  2）元组一旦定义完成，元组的元素不能修改

2. 元组变量的定义
"""
info_tuple = ("zhangsan", 18, 1.85)
print(info_tuple[1])

# 创建空元组
empty_tuple = ()
print(type(empty_tuple))

# 定义单元素的元组
# 如果括号内不加逗号，解释器会只解析括号内部的内容
single_tuple1 = (5)
print(type(single_tuple1))  # <class 'int'>

single_tuple2 = (5,)
print(type(single_tuple2))  # <class 'tuple'>


"""
3. 元组变量的常用操作：count()、index()
"""
info_tuple2 = ("zhangsan", 18, 1.85, "zhangsan")

# 1. 取值和取索引
print(info_tuple2[0])

print(info_tuple2.index("zhangsan"))

# 2. 统计一个数据在元组中出现的次数
print(info_tuple2.count("zhangsan"))
# 统计元组中包含的元素个数
print(len(info_tuple2))

"""
4. 元组的应用场景
   a.函数的参数和返回值，一个函数可以接收任意多个参数，或者一次返回多个数据
   b.格式字符串，格式字符串后面的()本质上就是一个元组
   c.让列表不可以被修改，以保护数据安全
"""

# b.格式字符串，格式化字符串后面的()本质上就是一个元组
# print("%s 年龄是 %d 身高是 %.2f" % ("小明", 17, 1.98))
info_tuple3 = ("小飞", 15, 1.38)
print("%s 年龄是 %d 身高是 %.2f" % info_tuple3)
info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple3
print(info_str)

# 元组和列表之间的转换
# 使用 list 函数可以把元组转换成列表
num_tuple = (2,3,5,1)
print(type(num_tuple))
num_list = list(num_tuple)
print(type(num_list))
# 使用 tuple 函数可以把列表转换成元组

