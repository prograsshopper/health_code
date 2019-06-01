import pymysql
from .common import *


# sentry 를 이용한 에러 체크
# Todo 개발 종료시 꼭 False로 변환
DEBUG = False

# add a app
INSTALLED_APPS += ['storages']

# allowed hosts
ALLOWED_HOSTS = ['*']

pymysql.install_as_MySQLdb()

# database
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.mysql'),
        'HOST': os.environ['DB_HOST'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'NAME': os.environ['DB_NAME'],
        'PORT': os.environ.get('DB_PORT', 3306),
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

# Cors heaers
CORS_ORIGIN_WHITELIST = (
    '*',
)

# django-storages 앱 의존성 추가
# 기본 static/media 저장소를 django-storages로 변경
STATICFILES_STORAGE = 'health_code.storages.StaticS3Boto3Storage'
DEFAULT_FILE_STORAGE = 'health_code.storages.MediaS3Boto3Storage'

# S3 파일 관리에 필요한 최소 설정
# 소스코드에 설정정보를 남기지마세요. 환경변수를 통한 설정 추천

# 필수 지정
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', 'ap-northeast-2')
