# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import json
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = False
    PROJECT = "micro-api"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    SENTRY_DSN = os.getenv('SENTRY_DSN')
    # Setup db
    MONGO_URI = os.getenv('MONGO_URI')
    # Authentication
    AUTH_ADDRESS = os.getenv('AUTH_ADDRESS')

    CELERY_IMPORTS = ['tasks']
    ENABLE_UTC = True

    # Config celery worker

    BROKER_URL = os.getenv('BROKER_URL')
    CELERY_QUEUES = os.getenv('CELERY_QUEUES')

    CELERY_ROUTES = {
        'worker.task_hello': {'queue': 'hello-queue'}
    }
    PUBLIC_PATH = os.getenv('PUBLIC_PATH')
    REDIS_CLUSTER = json.loads(os.getenv('REDIS_CLUSTER'))

    """
        - api key video upload config
    """
    USE_THETA = os.getenv('USE_THETA')
    API_KEY = os.getenv('API_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    URL_UPLOAD_VIDEO = os.getenv('URL_UPLOAD_VIDEO')

    """
        - S3 config
    """
    S3_BUCKET = os.getenv('S3_BUCKET')
    S3_HOST = os.getenv('S3_HOST')
    S3_KEY= os.getenv('AWS_ACCESS_KEY')
    S3_SECRET = os.getenv('AWS_ACCESS_SECRET')
    
    S3_BUCKET_INTERNAL = os.getenv('S3_BUCKET_INTERNAL')
    S3_KEY_INTERNAL= os.getenv('AWS_ACCESS_KEY_INTERNAL')
    S3_SECRET_INTERNAL = os.getenv('AWS_ACCESS_SECRET_INTERNAL')

    