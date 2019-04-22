from redis import *


class Redis_conn(object):
    #__init__()方法接收python和redis交互中host、port和第几个db
    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.db = db

    def conn(self):
        self.rs = StrictRedis(host=self.host,
                              port=self.port,
                              db=self.db,           # 对于redis返回的每个中文字会显示成为3个字节表示为16进制例如b'\xe5\x93\x88'
                              decode_responses=True #  这里需要设置decode解码               
                              )
        return self.rs

    def rs_set(self):
        try:
            result = self.rs.set('name','redis')
            print(result)
        except Exception as e:
            print(e)

    def rs_get(self):
        try:
            result = self.rs.get('name')
            print(result)
        except Exception as e:
            print(e)

    def rs_modify(self):
        try:
            result = self.rs.set('name','哈哈')
            print(result)
        except Exception as e:
            print(e)

    def rs_delete(self):
        try:
            result = self.rs.delete('name','redis')
            print(result)
        except Exception as e:
            print(e)

    def __del__(self):
        print('执行完毕')


if __name__ == '__main__':
    redis = Redis_conn('192.168.100.100', 6379, 2) #指定连接的redis服务器地址：host端口默认6379，指定数据库第2个（默认是0）
    redis.conn()
    print(redis.host,redis.port,redis.db)
    redis.rs_set()
    redis.rs_get()
    redis.rs_modify()
    redis.rs_get()
