import redis, json

# 信息失效策略还未设置
redis_conn = redis.ConnectionPool(host="127.0.0.1",port="6379", db=1)
my_redis = redis.Redis(connection_pool=redis_conn)

# 获取信息，先查询redis
def getAllMenu(menu_db,session_key):
    try:
        menu_msg = my_redis.hget(menu_db, session_key)
        if menu_msg:
            menu_msg = json.loads(menu_msg)
            return menu_msg
    except Exception as e:
        return None