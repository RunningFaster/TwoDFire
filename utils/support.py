import time

def post_fixed():
    # 固定数据，无需修改
    post_dict = {}
    APP_SECRET = "xx"
    now_time = int(time.time())
    post_dict['timestamp'] = now_time
    post_dict['v'] = 1.0
    post_dict['appKey'] = "yy"
    post_dict['entityId'] = "zz"
    return post_dict, APP_SECRET