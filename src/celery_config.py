from celery.schedules import crontab

from src.conf.internal_config import REDIS_URL, processor_conf_dict, TZ

# 消息中间件 Broker
broker_url = "redis://" + REDIS_URL + "/1"   # 使用redis存储任务队列
# Backend 用于存储任务的执行结果，以供查询。
result_backend = "redis://" + REDIS_URL + "/2"  # 使用redis存储结果


task_serializer = 'json'
result_serializer = 'json'
# 指定任务接受的序列化类型.
accept_content = ['json']
timezone = TZ  # 时区设置
worker_hijack_root_logger = False  # celery默认开启自己的日志，可关闭自定义日志，不关闭自定义日志输出为空
celeryd_max_tasks_per_child = 1  # Maximum number of tasks a pool worker process can execute before it’s replaced with a new one. Default is no limit.
result_expires = 60 * 60 * 24  # 存储结果过期时间（默认1天）


# 导入任务所在文件 todo: 自动导入任务文件
imports = [
    "src.app_scripts.etl_task",
]


# 需要执行任务的配置
beat_schedule = {
    "etl_task_example": {
        "task": "src.app_scripts.etl_task.etl_task_example",
        "schedule": crontab(**processor_conf_dict['etl_task_example']['schedule']),
        "kwargs": processor_conf_dict['etl_task_example']['kwargs']
    },
}

