"""
Python 内置函数：

len(item) 计算容器中元素个数
del(item) 删除变量   或 del item
max(item) 返回容器中元素最大值   如果是字典，只针对key比较
min(item) 返回容器中元素最小值  如果是字典，只针对key比较


切片：
支持的数据类型：字符串、列表、元组
不支持的数据类型：字典  无序集合，使用键值对保存数据

运算符:
+
*
成员运算符：
in
not in


完整的for循环语法：
for 变量 in 集合
    循环体代码
else:
   没有通过 break 退出循环，循环结束后，会执行的代码
"""
for num in [1, 2, 3, 4, 5]:
    print(num)
    if num == 3:
        break
else:
    # 如果循环体内部使用break退出了循环
    # else下方的代码就不会被执行
    print("会执行吗？")
print("循环结束")

# 应用场景：
# 在迭代遍历嵌套的数据类型时，例如一个列表包含了多个字典
# 需求：要判断某一个字典中是否存在指定的值
# 如果存在，提示并且退出循环
# 如果不存在，在循环整体结束后，希望得到一个统一的提示
students = [
    {"name": "old wu",
     "age": 20,
     "height": 1.8,
     "weight": 75},
    {"name": "old liu",
     "age": 24,
     "height": 1.7,
     "weight": 65}
]
find_name = "old wu"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)
        break
else:
    print("抱歉，没有找到 %s" % find_name)
print("循环结束")
