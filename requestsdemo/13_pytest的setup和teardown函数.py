"""
类外面的函数执行顺序：
    第一批次：setup_module/teardown_module：在当前文件中，在所有测试用例执行之前与之后执行
    第二批次：setup_function/teardown_function：在每个测试函数之前与之后执行
    第三批次：setup/teardown：在每个测试函数之前与之后执行，同样适用于类方法
    PS：方法的定义顺序调整了，也还是按既定规则执行

"""

"""
类里面的函数执行顺序：
    第一批次：setup_class/teardown_class：在当前测试类的开始与结束执行，使用@classmethod标记
    第二批次：setup_method/teardown_method：在每个测试方法开始与结束时执行
    第三批次：setup/teardown：在每个测试方法开始与结束时执行，同样适用于测试函数（在类外面的方法）
    PS：方法的定义顺序调整了，也还是按既定规则执行
"""