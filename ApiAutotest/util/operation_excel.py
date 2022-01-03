

import xlrd

# data = xlrd.open_workbook('../ApiAutotest/dataconfig/case1.xls', 'rb')
# data = xlrd.open_workbook('F:\\GuanHuaJin\\PythonAutoTest\\Python-\\ApiAutotest\\dataconfig\\case1.xls', 'rb')
# tables = data.sheets()[0]
# print(tables.nrows)
# print(tables.cell_value(2, 4))
from xlutils.copy import copy

"""
封装操作excel函数
"""


class OperationExcel:

    # 这种写法会导致需要多次传入参数，比较麻烦，所以可以改成使用全局变量的方式
    # def __init__(self, file_name, sheet_id):
    #     self.data = self.get_data(file_name, sheet_id)

    # 使用全局变量
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            # self.file_name = 'F:\\GuanHuaJin\\PythonAutoTest\\Python-\\ApiAutotest\\dataconfig\\case1.xls'
            self.file_name = '../dataconfig/case1.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    # def get_data(selffile_name, sheet_id):  # 换成全局变量之后，这边就可以不用传参了
    #     xlrd.open_workbook(file_name)
    #     tables = data.sheets()[sheet_id]
    #     return tables

    # 获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self, row, col):
        tables = self.data
        return tables.cell_value(row, col)

    # 写入数据
    def write_value(self, row, col, value):
        '''
        写入Excel数据
        :param row:
        :param col:
        :param value:
        :return:
        '''
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)


if __name__ == '__main__':
    opers = OperationExcel()
    tables = opers.get_data().nrows
    content = opers.get_cell_value(1, 2)
    print(tables)
    print(content)
