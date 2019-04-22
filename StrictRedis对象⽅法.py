from redis import *


class Redis_conn(object):
    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.db = db

    def conn(self):
        self.rs = StrictRedis(host=self.host,
                                    port=self.port,
                                    db=self.db,
                                    decode_responses=True
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
    redis = Redis_conn('192.168.100.100', 6379, 2)
    redis.conn()
    print(redis.host,redis.port,redis.db)
    redis.rs_set()
    redis.rs_get()
    redis.rs_modify()
    redis.rs_get()
