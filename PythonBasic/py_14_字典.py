"""
1. 字典的定义：
   字典同样可以用来存储多个数据
   通常用来存储描述一个物体的相关信息

2.字典和列表的区别：
  a. 列表是 有序 的对象集合
     字典是 无序 的对象集合
  b. 字典用 {} 定义
  c. 字典使用键值对存储数据，键和值之间使用 : 分隔，键值对之间使用,分隔
    键必须是唯一的。键只能使用字符串、数字或元组

"""

xiaoming = {"name": "小明",
            "age": 15,
            "gender": True}
print(xiaoming)

"""
3. 字典的增删改查

"""
# 1.取值
# *** 注意：如果指定的key不存在，程序会报错
print(xiaoming["age"])

# 2.增加/修改

# 如果key不存在，会新增键值对
xiaoming["weight"] = 65.5

# 如果key存在，会修改已经存在的键值对
xiaoming["name"] = "大明"

# 3.删除
# xiaoming.pop("gender")

print(xiaoming)


"""
4. 字典的统计、合并、清空操作
"""
# 1.统计键值对数量
print(len(xiaoming))

# 2.合并字典
# **** 注意：如果合并的键值对已经存在，则被合并的键值对会被覆盖
temp_dict = {"height": 1.85,
             "age": 25}
xiaoming.update(temp_dict)

# 3.清空字典
# xiaoming.clear();

print(xiaoming)


"""
5. 字典的循环遍历

"""
# 变量k是每一次循环中，获取到的键值对的key
for k in xiaoming:
    print("%s - %s" % (k, xiaoming[k]))

"""
6. 字典和列表组合的应用场景：
   a. 使用多个键值对，存储描述一个物体的相关信息
   b. 将多个字典放在一个列表中，再进行遍历，在循环体内部针对每一个字典进行相同的处理
   
"""
card_list = [
    {"name": "张三",
     "qq": "12345",
     "phone": "123"},
    {"name": "李四",
     "qq": "54321",
     "phone": "10000"}
]
for card_info in card_list:
    print(card_info)

"""

"""

