# 163MV-Python-FastAPI
 API For 163MV .

### 使用 FastAPI 来搭建的一个网易云直链

- https://163.icodeq.com 的服务端（需要 `Redis` 来做数据库来支持缓存功能）

- 需要 `node.js` 环境才能运行

- 示例地址为：https://163mv.icodeq.com

- 示例文档为：https://163mv.icodeq.com/docs

### 搭建步骤

1. 安装依赖

```python
pip install -r requirements.txt
```

2. 在 `post_2_redis.py` 中填入你的 `Redis` 地址和密码

3. 运行

```python
python main.py # or python3 main.py
```

4. 本项目可运行于 `Repilt` [![Run on Replit](https://replit.com/badge/github/zkeq/163MV-Python-FastAPI)](https://replit.com/github/zkeq/163MV-Python-FastAPI)

5. 搭建好后，去部署`vercel API`即可，服务端主要起到读取缓存和请求后端的效果。

6. （为什么要分开呢？是因为我找不到 `vercel` 怎么同时部署 `Fast API` 和 `node.js` 环境..

7. Vercel 的服务端地址在这里：[zkeq/163MV-API-Vercel](https://github.com/zkeq/163MV-API-Vercel)

8. 部署好这个去部署服务端就可以了
