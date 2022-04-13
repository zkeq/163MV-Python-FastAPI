# coding:utf-8
import requests
from encode_params import get_params
from post_2_redis import post_mv_2_redis
import logger as lg

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}


def get_data(encText, encSecKey):
    url = 'https://music.163.com/weapi/song/enhance/play/mv/url?csrf_token='
    _data = {
        'params': encText,
        'encSecKey': encSecKey
    }
    response = requests.post(url, headers=headers, data=_data)
    lg.logger_success(response.text)
    return response.json()


def run(video_id):
    _dict = get_params(video_id)
    lg.logger_success("所获取到的加密参数为：%s" % _dict)
    lg.logger_info('-' * 100)
    encText = _dict['encText']
    encSecKey = _dict['encSecKey']
    _data = get_data(encText, encSecKey)
    return _data


def get_video_link(video_id):
    data = run(video_id)
    lg.logger_success("获取到的完整数据为: %s" % data)
    lg.logger_info('-' * 100)
    video_url = data['data']['url']
    video_url = video_url.replace('http://', 'https://')
    video_name = '163_mv_liunx_' + str(video_id)
    post_mv_2_redis(video_name, video_url)
    lg.logger_success("正在获取 ID: {0} 所对应链接: {1}".format(video_id, video_url))
    lg.logger_info('-' * 100)
    video_dict = {video_name: video_url}
    return video_dict
