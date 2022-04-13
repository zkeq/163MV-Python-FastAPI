# coding:utf-8
import redis
import logger as lg

r = redis.Redis(
    host='xxxxxxxxxxxxxxxxxxx.upstash.io',
    port=XXXXX,
    password='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', ssl=True)


def post_mv_2_redis(_video_id, _video_url):
    lg.logger_info('正在将获取到的视频地址放入 Redis 中: ....')
    result = r.set(_video_id, _video_url, ex=6000)
    lg.logger_info('正在将获取到的视频地址放入 Redis 中: %s' % result)
    return_url = r.get(_video_id)
    return return_url
