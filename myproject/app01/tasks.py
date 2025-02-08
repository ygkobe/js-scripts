# tasks.py
from celery import shared_task
import time


@shared_task
def add(x, y):
    time.sleep(10)  # 模拟一个耗时任务
    return x + y
