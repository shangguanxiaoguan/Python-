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

# 2.判断字符串中是否只包含数字

# 1>都不能判断小数
# num_str = "1.1"
# 2>unicode 字符串
# num_str = "\u00b2"
# 3> 中文数字
num_str = "一千零一"
print(num_str)
print(num_str.isdecimal())  # 开发时常用这个
print(num_str.isdigit())
print(num_str.isnumeric())

# 3.字符串的查找和替换

hello_str = "hello world"
# 判断是否以指定字符串开始
print(hello_str.startswith("Hello"))  # 大小写有区别
# 判断是否以执行字符串结束
print(hello_str.endswith("world"))
# 查找指定字符串
# index同样可以查找指定字符串在大字符串中的索引
print(hello_str.find("llo"))
# 与index不同的是：
# index 如果指定的字符串不存在：会报错
# find 如果指定的字符串不存在，会返回-1
print(hello_str.find("abc"))

# 替换字符串
# replace方法执行完成后，会返回一个新的字符串
# 注意：不会修改原有字符串的内容
print(hello_str.replace("world", "python"))
print(hello_str)

# 4.文本对齐方法
poem = ["\t\n很纠结年份佳都科技kg并不能",
       "就黄金国际和回家回家打防结合"]

for poem_str in poem:

    # 先使用strip方法去除字符串中的空白字符
    # 再使用center方法居中显示文本
    print("|%s|" % poem_str.strip().center(15, " "))
    # print("|%s|" % poem_str.ljust(15, " "))
    # print("|%s|" % poem_str.rjust(15, " "))


# 5.去除空白字符


# 6.拆分和拼接字符串
# 空字符串 \t \r \n
poem_str2 = "剑歌江湖\t的可观花开的\t时候的解放军\n的赶快改\t\n黑胡椒"
print(poem_str2)
# 拆分字符串
poem_list = poem_str2.split()
print(poem_list)
# 合并字符串
poem_str3 = " ".join(poem_list)
print(poem_str3)


# 7.字符串切片

num_str = "0123456789"
# 截取从2 - 5位置的字符串
print(num_str[2:6])
# 截取从2 - 末尾的字符串
print(num_str[2:])
# 截取从开始 - 5位置的字符串
print(num_str[0:6])
print(num_str[:6])
# 截取完整的字符串
print(num_str[0:])
print(num_str[:])
# 从开始位置，每隔一个字符串截取字符串
print(num_str[::1])
print(num_str[::2])
# 从索引 1 开始，每隔一个取一个
print(num_str[1::2])
# 截取从 2 - 末尾 - 1 的字符串
print(num_str[2:-2])
print(num_str[2:-1])
# 截取字符串末尾两个字符
print(num_str[-2:])
# 字符串的逆序（面试题）
print(num_str[0::-1])
print(num_str[-1::-1])  # 相当于从右往左切片
print(num_str[::-1])
