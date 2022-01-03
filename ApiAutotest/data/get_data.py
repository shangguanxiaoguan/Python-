from ApiAutotest.data import data_config
from ApiAutotest.util import operation_json
from ApiAutotest.util.operation_excel import OperationExcel
from ApiAutotest.util.operation_json import OperationJson


class GetData:
    def __init__(self):
        self.operation_excel = OperationExcel()

    # ��ȡExcel�������������ǵ�case����
    def get_case_lines(self):
        return self.operation_excel.get_lines()

    # ��ȡcase�Ƿ�����
    def get_is_run(self, row):
        flag = None
        col = data_config.get_run()
        run_model = self.operation_excel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # �Ƿ�Я��header
    def is_header(self, row):
        col = data_config.get_header()
        header = self.operation_excel.get_cell_value(row, col)
        if header == 'yes':
            # return header
            return data_config.get_header_value()
        else:
            return None

    # ��ȡ����ʽ
    def get_request_method(self, row):
        col = data_config.get_run_way()
        request_method = self.operation_excel.get_cell_value(row, col)
        return request_method

    # ��ȡurl
    def get_url(self, row):
        col = data_config.get_url()
        url = self.operation_excel.get_cell_value(row, col)
        return url

    # ��ȡ��������
    def get_request_data(self, row):
        col = data_config.get_data()
        data = self.operation_excel.get_cell_value(row, col)
        if data == '':
            return None
        else:
            return data

    # ͨ����ȡ�ؼ����õ�data����
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        opera_json.get_data(self.get_request_data(row))

    # ��ȡԤ�ڽ��
    def get_expect_data(self, row):
        col = data_config.get_expect()
        expect_data = self.operation_excel.get_cell_value(row, col)
        if expect_data == '':
            return None
        return expect_data

    def write_result(self, row, value):
        col = data_config.get_result()
        self.operation_excel.write_value(row, col, value)
