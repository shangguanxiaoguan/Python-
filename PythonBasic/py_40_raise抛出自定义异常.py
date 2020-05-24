"""
自定义异常类需要继承异常的基类——Exception
"""


class ShortInputException(Exception):
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast

    def main(self):
        try:
            s = input("请输入至少% d个字符串：" % self.atleast)
            # if len(s) < self.atleast:
            if len(s) < self.atleast:
                raise ShortInputException(len(s), self.atleast)
                # raise ShortInputException("长度不对")
        except ShortInputException as result:
            print("ShortInputException：输入的长度是 %d，长度至少应该是 %d" % (result.length, result.atleast))
        else:
            print("没有异常发生")


define_exception = ShortInputException(2, 3)
define_exception.main()
