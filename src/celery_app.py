from celery import Celery
from src.common.logger import *

app = Celery()
app.config_from_object("src.celery_config")