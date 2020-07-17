import pymysql

from config.sql_conf import sql_conf


def get_sql(sql):
    # 建立一个连接对象
    # host,user,password,database,port,charset='127.0.0.1','root','root','test',3306,'utf-8'
    host,user,password,database,port,charset=sql_conf()
    print(host)
    db = pymysql.connect(host=host, user=user, password=password, database=database, port=port, charset=charset)
    # 建立一个游标
    cursor = db.cursor()
    # 运行sql语句
    cursor.execute(sql)
    # 获取sql查询的值
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data


# 运行sql
data = get_sql("select traffic from skyvpn_basic_user where user = '7393118869608932'")
print(data)


"""
部分接口，参数用其他方式获取不到时，可以连接数据库去获取，比如手机验证码
"""
