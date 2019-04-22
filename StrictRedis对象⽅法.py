#自定义一个类通过__enter__()和__exit__()方法
# 结合 with语句完成连接和断开数据库的操作
import pymysql

class MysqlConn(object):


    def __init__(self, host, port, user, password, database, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset

    def __enter__(self):
        print('开始执行__enter__()方法')
        self.conn = pymysql.connect(host = self.host,
                                    port = self.port,
                                    user = self.user,
                                    password = self.password,
                                    database = self.database,
                                    charset = self.charset
        )
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('开始执行__exit()__方法')
        self.conn.close()


if __name__ == '__main__':
    with MysqlConn('192.168.100.100', 3306, 'root', 'mysql', 'stock_db', 'utf8') as conn:
        cursor = conn.cursor()
        sql = 'select * from info;'
        cursor.execute(sql)
        for row in cursor.fetchall():
            print(row)
        cursor.close()