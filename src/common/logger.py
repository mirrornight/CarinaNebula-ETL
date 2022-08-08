import logging
import os
from celery._state import get_current_task

from src.conf.internal_config import LOG_DIR


class Formatter(logging.Formatter):
    """Formatter for tasks, adding the task name and id."""

    def format(self, record):
        task = get_current_task()
        if task and task.request:
            record.__dict__.update(task_id='%s ' % task.request.id,
                                   task_name='%s ' % task.name)
        else:
            record.__dict__.setdefault('task_name', '')
            record.__dict__.setdefault('task_id', '')
        return logging.Formatter.format(self, record)


root_logger = logging.getLogger()  # 返回logging.root
root_logger.setLevel(logging.DEBUG)

# 将日志输出到文件
fh = logging.FileHandler(os.path.join(LOG_DIR, 'celery_worker.log'))  # 这里注意不要使用TimedRotatingFileHandler，celery的每个进程都会切分，导致日志丢失
formatter = Formatter('[%(task_name)s%(task_id)s%(process)s %(thread)s %(asctime)s %(pathname)s:%(lineno)s] %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
root_logger.addHandler(fh)

# 将日志输出到控制台
sh = logging.StreamHandler()
formatter = Formatter('[%(task_name)s%(task_id)s%(process)s %(thread)s %(asctime)s %(pathname)s:%(lineno)s] %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
sh.setFormatter(formatter)
sh.setLevel(logging.INFO)
root_logger.addHandler(sh)