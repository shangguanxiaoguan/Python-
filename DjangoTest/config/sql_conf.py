def server_ip():
    '''
    dev_ip：开发环境ip
    sit_ip：测试环境ip
    :return:
    '''
    dev_ip ='http://127.0.0.1:8000'  # 开发环境ip

    sit_ip = 'http://106.12.126.197:8000'  # 测试环境ip

    return sit_ip

def sql_conf():
    '''

    :return: 返回数据库连接信息
    '''

    host = '127.0.0.1'
    user = 'root'
    password = 'root'
    database = 'test'
    port = 3306
    charset = 'utf8'   # 【注意】是utf8不是utf-8，否则会报错：AttributeError: 'NoneType' object has no attribute 'encoding'


    return host, user, password, database, port, charset
