# coding:utf-8
import uvicorn
from fastapi import FastAPI
import logger as lg
import get_data as gd

app = FastAPI()


@app.get("/", summary="163 MV Permanent API")
def main(vid: int = None):
    """
    网易云 `MV` 直链 API
    
    参数:

      **vid**: int, 必须, MV ID

    返回:

     **json**: 直链

    特性

      - 本 API 仅支持 `GET` 请求

      - 可以指定 `vid` 参数, 获取对应 MV 的直链

      - 自动刷新 Redis 缓存

      - 本 API 为 `https://163.icodeq.com` 308 跳转的 `数据接口`

      - 可以通过定时命令定时访问本 API, 来实现自动刷新 Redis 缓存

      - Redis 缓存有效期为 1.6 小时

      - 所以推荐每 1.5 小时访问一次本 API, 刷新 Redis 缓存
    """
    lg.logger_info('-' * 20 + '开始记录日志' + '-' * 20)
    if not isinstance(vid, int):
        lg.logger_error('params must be a int')
        return {'message': 'Fast API'}
    params_data = gd.get_video_link(vid)
    return params_data


if __name__ == "__main__":
    uvicorn.run("index:app", host="0.0.0.0", port=8080, log_level="info")
