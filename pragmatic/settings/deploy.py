from .base import *

# secret에서 KEY를 불러오도록 하는 함수
# secret_name을 받아서 해당 이름을 가진 secret을 읽어오라는 함수
def read_secret(secret_name):
    file = open('/run/secrets/'+secret_name)# open()을 이용해 파일을 읽을 수 있따
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret('Django_Secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django_1',
        'PASSWORD': read_secret('MySQL_PASSWORD'),
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}