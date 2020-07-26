"""
主流程封装
"""
from ApiAutotest.base.run_method import RunMethod
from data.get_data import GetData
# 解决ImportError: No module named base.runmethod
import sys
sys.path.append("F:\\GuanHuaJin\\PythonAutoTest\\Python-\\ApiAutotest")

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()

    def go_on_run(self):
        rows_count = self.data.get_case_lines()
        # excel中第一行数据要去掉
        for i in range(1, rows_count):
            url = self.data.get_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_from_json(i)
            header = self.data.is_header(i)
            if is_run:
                res = self.run_method.run_main(method, url, data, header)
            return res


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()


