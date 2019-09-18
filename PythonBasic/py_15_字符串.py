str1 = "hello python"
str2 = '我的外号是"大西瓜"'
print(str2)
print(str1[4])
for char in str2:
    print(char, end="")

"""
2.字符串的常用操作
"""
hello_str = "hello hello"
# 1.统计字符串长度
print(len(str1))

# 2.统计某一子字符串出现的次数
print(hello_str.count("llo"))
print(hello_str.count("abc"))

# 3.某一个子字符串出现的位置
print(hello_str.index("o"))
# **** 注意：如果使用index方法传递的子字符串不存在，程序会报错
# print(hello_str.index("BC"))

"""
3. 字符串的常用方法
"""
# 1.判断空白字符  看到188
space_str = "      \t\n\r"
print(space_str.isspace())  # 判断字符串中是否只包含空格

