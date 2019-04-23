from redis import *


class Redis_conn(object):
    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.db = db

    def conn(self):
        self.rs = StrictRedis(host=self.host,
                              port=self.port,
                              db=self.db,           # 使用解码这样中文就不出现这样的
                              decode_responses=True  # b'\xe8\xb0\xa2\xe9\x80\x8
                              )
        return self.rs

    # hash用于存储对象key，对象key结构为field(属性)和value(属性值)
    # hset key field value
    def rs_add(self):
        try:
            # hmset接收两个参数一个是对象key名，后面的mapping也就是接收类似于字典或者
            # js对象格式的大括号加键值对{field1:value1,field2:value2...}
            result = self.rs.hmset('hash_data', {'name':'peter','age':20})
            print(result)
        except Exception as e:
            print(e)

    def rs_get(self):
        try：
            result = self.rs.mget('')
            #   hkeys获取hash的对象所有属性(field)
            #   192.168.100.100:6379[2]> help HKEYS  通过redis-cli连接redis数据库help命令查看HKEYSS命令
            #   HKEYS key
            #   summary: Get all the fields in a hash   获取hash的key对象中所有的field
            #   since: 2.0.0
            #   group: hash
            result = self.rs.hkeys('hash_data')
            print(result)
            #   192.168.100.100:6379[2]> help HVALS 通过redis-cli连接redis数据库help命令查看HVALS命令
            #   HVALS key
            #   summary: Get all the values in a hash   获取hash的key对象中所有的value值
            #   since: 2.0.0
            #   group: hash

            result = self.rs.hvals('hash_data')
            print(result)
        except Exception as e:
            print(e)

    def rs_modify(self):
        try:
            result = self.rs.hset('hash_data', 'name', '谢逊')
            print(result)
        except Exception as e:
            print(e)

    def rs_delete(self):
        try:
            result = self.rs.hdel('hash_data', 'name')
            print(result)
        except Exception as e:
            print(e)

    def __del__(self):
        print('执行完毕')


if __name__ == '__main__':
    redis = Redis_conn('192.168.100.100', 6379, 2)
    redis.conn()
    print(redis.host,redis.port,redis.db)
    redis.rs_add()
    redis.rs_get()
    redis.rs_modify()
    redis.rs_get()
#test
