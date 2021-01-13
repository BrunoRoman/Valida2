from celery.decorators import task
from celery.utils.log import get_task_logger

from internet.valida.classes import *

import requests

logger = get_task_logger(__name__)


@task(name="connect_device_task")
def connect_device_task(ambiente,equipamentos):
    requests.post(f'http://127.0.0.1:8000/{ambiente}/',data=equipamentos,auth=('admin','admin'))