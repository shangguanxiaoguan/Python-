"""
1. 列表 ===>数组
**** 注意列表的索引越界

2. 列表的常用操作
"""

name_list = ["zhangsan", "lisi", "wangwu"]
# 1.取值和取索引
print(name_list[2])

# 知道数据的内容，想确定数据在列表的位置
# 如果传递的数据不再列表中，程序会报错
print(name_list.index("lisi"))

# 2.修改
# 列表指定的索引超出范围，程序会报错
name_list[2] = "李斯"

# 3.增加
# append方法可以向 列表的末尾追加 数据
name_list.append("王小五")
# insert方法可以在 列表的指定索引位置插入 数据
name_list.insert(1, "哈哈哈")
# extend 方法可以 把其他列表中的完整内容，追加 到当前列表的末尾
temp_list = ["孙悟空", "猪八戒", "沙师弟"]
name_list.extend(temp_list)


print(name_list)

# 3.删除
# remove 方法可以从列表中删除指定的数据
name_list.remove("lisi")
# pop 方法默认可以把列表中最后一个元素删除
name_list.pop()
# pop 方法可以指定要删除元素的索引
name_list.pop(2)
# clear 方法可以清空列表
# name_list.clear()


# (知道)使用 del 关键字（delete）删除列表元素
del name_list[1]
# print(name_list[1])

# del 关键字本质上是用来将一个变量从内存中删除的
name = "小明"

del name
# **** 注意：如果使用 del 关键字将变量从内存中删除
#            后续的代码就不能再使用这个变量了

# print(name)   # NameError: name 'name' is not defined

print(name_list)


"""
3. 列表统计及删除方法扩展
"""


name_list2 = ["张三", "李四", "王五", "赵六", "张三"]
# len 函数可以统计列表中元素的总数
list_len = len(name_list2)
print("列表中包含 %d 个元素" % list_len)

# count 方法可以统计列表中某一个数据出现的次数
count = name_list2.count("张三")
print("张三出现了 %d 次" % count)


# 从列表中删除第一次出现的数据，如果数据不存在，程序会报错
name_list2.remove("张三")
print(name_list2)


"""
4. 列表的排序和反转
"""


name_list3 = ["zhangsan", "lisi", "wangwu", "wangxiaoer", "yangsq"]
num_list = [6, 4, 8, 5, 1, 10]

# 升序
# name_list3.sort()
# num_list.sort()

# 降序
# name_list3.sort(reverse=True)
# num_list.sort(reverse=True)

# 逆序（反转）
name_list3.reverse()
num_list.reverse()

print(name_list3)
print(num_list)


"""
5. 关键字、函数和方法
"""

# 1.关键字后面不需要使用括号


"""
6.迭代遍历
  1）顺序的从列表中依次获取数据
  2）for循环与while循环的区别：for循环不用在外部定义计数器，也不用在里面让计数器加 1
"""
name_list4 = ["张三", "李四", "王五", "赵六", "张三"]
# 使用迭代遍历列表
for my_name in name_list4:
    print("我的名字叫 %s" % my_name)


"""
7. 列表的应用场景
  在 Python 的列表中是可以存储不同类型的数据的
   但是在开发中，更多的应用场景是：
   1）列表存储相同类型的数据
   2）通过迭代遍历，在循环体内部，针对列表中的每一项元素，执行相同的操作
"""
# 在 Python 的列表中是可以存储不同类型的数据的
list_type = ["zhangsan", 3, 2.9]
print(list_type)
