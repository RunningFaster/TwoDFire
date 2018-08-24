import time

def post_fixed():
    # 固定数据，无需修改
    post_dict = {}
    APP_SECRET = "d67ee437b292c992b8c34b5ea984139c"
    now_time = int(time.time())
    post_dict['timestamp'] = now_time
    post_dict['v'] = 1.0
    post_dict['appKey'] = "69966cafe1d22ebcf8c48907339d3e4d"
    post_dict['entityId'] = "00134699"
    return post_dict, APP_SECRET