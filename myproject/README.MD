# 项目说明

```text

1 用户登陆认证
2 返回数据加密（base64、aes加密）
3 使用redis缓存 

```

```shell
# 启动 Celery worker
celery -A myproject.celery_app worker --loglevel=info

# 启动redis

```
