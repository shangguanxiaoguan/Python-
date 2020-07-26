from ApiAutotest.util.operation_excel import OperationExcel
from ApiAutotest.util.operation_json import OperationJson
from data import data_config

"""
��װ��ȡ�ӿ�����
"""

class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()

    # ȥ��ȡexcel�������������ǵ�case����
    def get_case_lines(self):
        return  self.opera_excel.get_lines()

    # ��ȡ�Ƿ�ִ��
    def get_is_run(self, row):
        flag = None
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # �Ƿ�Я��header
    def is_header(self, row):
        col = data_config.get_header_value()
        if col != None:
            col = int(data_config.get_header_value())
        header = self.opera_excel.get_cell_value(row, col)
        if header == 'yes':
            return data_config.get_header_value()
        else:
            return None

    # ��ȡ����ʽ
    def get_request_method(self, row):
        col = int(data_config.get_request_way())
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    # ��ȡurl
    def get_url(self, row):
        col = int(data_config.get_url())
        url = self.opera_excel.get_cell_value(row, col)
        return url

    # ��ȡ��������
    def get_request_data(self, row):
        col = int(data_config.get_data())
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            data = None
        return data

    # ͨ����ȡ�ؼ����õ�data����
    def get_data_from_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    # ��ȡԤ�ڽ��
    def get_expect_data(self, row):
        col = int(data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect
