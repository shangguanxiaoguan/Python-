"""
1.程序的三大流程：
  顺序
  分支
  循环

2.while循环的基本使用

**** 注意：while语句以及缩进部分是一个完整的代码块

3.赋值运算符
c=a+b
c+=a : c=c+a
c-=a
c*=a
c/=a
c//=a : c=c//a
c%=a
c**=a


"""

# 练习1.计算0-100之间所有数字的累计求和结果

# 0.定义最终结果的变量
result = 0
# 1.定义一个整数变量记录循环的次数
i = 0
# 2.开始循环
while i <= 100:
    print(i)
    # 每一次循环都让result和i 相加
    result += i
    # 处理计数器
    i += 1
print("0-100之间的数字求和结果 = %d" % result)


# 练习2.计算0-100之间所有偶数的累计求和结果
j = 0
sum = 0
while j <= 100:

    # 判断变量 i 中的数值，是否是一个偶数
    # 偶数 j % 2 == 0
    # 奇数 j % 2 != 0
    if j % 2 == 0:
        print(j)
        sum += j
    j += 1
print("0-100之间所有偶数的求和结果 = %d" % sum)


"""
4. break 和 continue 是专门在循环中使用的关键字
break ：某一条件满足时，退出循环，不再执行后续重复的代码 
continue ：某一条件满足时，不执行后续重复的代码

"""

i = 0
while i < 10:
    if i == 3:
        break
    print(i)
    i += 1
print("over")

z = 0
while z < 10:

    if z == 3:
        # **** 注意：在循环中，如果使用continue关键字
        # 在使用关键字之前，需要确认循环的计数是否修改，
        # 否则可能会导致死循环
        z += 1
        continue
    print(z)
    z += 1

print("over")


"""
5. 循环嵌套

1）在默认情况下，print函数输出内容之后，会自动在内容末尾增加换行
   如果不希望末尾增加换行，可以在print函数输出内容的后面增加 ,end=""
   其中 "" 中间可以指定print函数输出内容之后，继续希望显示的内容
   print("*",end="")
"""
# 练习1.使用循环嵌套打印小星星
# 方法一：不使用嵌套
print("=========不使用循环嵌套输出小星星==========")
row = 1
while row <= 5:
    print("*" * row)
    row += 1
# 方法二：使用嵌套
print("=========使用循环嵌套输出小星星=============")
row = 1
while row <= 5:

    col = 1
    while col <= row:
        print("*", end="")
        col += 1

    # print("第 %d 行" % row)
    # ！！！这行代码很重要，在一行星星输出完成之后，添加换行
    print("")
    row += 1

# 练习2.输出九九乘法表
print("=======输出九九乘法表=========")
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d * %d = %d" % (j, i, j * i), end="  ")
        j += 1
    print("")
    i += 1


