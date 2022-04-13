# coding:utf-8
import execjs
import json
import logger as lg


def get_params(video_id):
    """
    获取加密参数
    """
    with open('163.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
        params = {
            "id": video_id,
            "r": "1080",
            "csrf_token": ""
        }
        second = "010001"
        three = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        four = '0CoJUm6Qyw8W8jud'
        lg.logger_info('params: {}'.format(params))
        dit = ctx.call('jia_mi', json.dumps(params), second, three, four)
        lg.logger_info('dit: {}'.format(dit))
        return dit

