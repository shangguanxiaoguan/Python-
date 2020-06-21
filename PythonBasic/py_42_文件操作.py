# 1. 打开文件
# 如果文件存在，返回文件操作对象
# 如果文件不存在，会抛出异常
# 默认以只读方式打开文件
# file = open("Readme.txt")

# 2. 读取文件内容
# 可以一次性读入并返回文件的所有内容
# text = file.read()
# print(text)

# 3. 关闭文件
# 【注意】如果忘记关闭文件，会造成系统资源消耗，而且会影响到后续对文件的访问
# file.close()


"""
打开文件的方式
"""
# 1. 打开文件
# file = open("Readme.txt", "w")  # 以只写的方式打开文件，文件存在会被覆盖，文件不存在，会创建新文件
# file = open("Readme.txt", "a")  # 以追加的方式打开文件，文件不存在，则创建新文件写入
#
# # 2. 写入文件
# file.write("过往即是过往，回不去了。怎么可以这样子")
#
#
# # 3. 关闭
# file.close()

"""
读取大文件：readline() 一次只读取一行内容
"""
# file = open("Readme.txt")
#
# while True:
#     text = file.readline()
#     # print(text, end="")
#     if not text:
#         break
#     print(text, end="")
#
# file.close()


"""
文件复制
"""
# 1.打开文件
file_read = open("Readme.txt")
file_write = open("Readme[复件]", "w")

# 2. 读写文件
# 小文件复制
# text = file_read.read()
# file_write.write(text)

# 大文件复制
while True:
    text = file_read.readline()

    if not text:
        break

    file_write.write(text)

# 3. 关闭文件
file_read.close()
file_write.close()

"""
os模块的作用：
创建、重命名、删除、改变路径、查看目录内容....
os.rename(源文件名, 目标文件名)
os.remove(文件名)

listdir  目录列表
mkdir    创建目录
rmdir    删除目录
getcwd   获取当前目录
chdir    修改工作目录
path.isdir 判断是否是文件

"""
