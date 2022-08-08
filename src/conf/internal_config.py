import os
import logging

try:
    from src.conf.external_config import global_conf, component_conf
    # redis
    celery_conf = component_conf.get('celery_conf', {})
    REDIS_URL = celery_conf.get('redis_url', 'redis:6379')
    processor_conf_dict = celery_conf.get('processor_conf_dict', {})
except ImportError as e:
    logging.error(e)


TZ = "Asia/Shanghai"


TEST = True
# path
DATA_BASE_PATH = "/data" if not TEST else '../../../data/upload'
# dir
LOG_DIR = os.path.join(DATA_BASE_PATH, 'log')
UPLOAD_DIR = os.path.join(DATA_BASE_PATH, "upload")
OUTPUT_DIR = os.path.join(DATA_BASE_PATH, "output")
INIT_DATA_DIR = os.path.join(DATA_BASE_PATH, 'init_data')