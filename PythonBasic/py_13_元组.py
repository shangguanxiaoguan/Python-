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
