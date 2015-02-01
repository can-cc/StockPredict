"""
Django settings for stockPredict project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
import djcelery
djcelery.setup_loader()
BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a1#rxu-n=hp8qy*1&q&(plwo$i-!+qy1&euy($+rvp)*+5$qz^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'middleware',
    'kombu.transport.django',
    'corsheaders',
    'rest_framework',
    'predictCenter',
    'userSys',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.crossdomainxhr.XsSharing',
)
REST_FRAMEWORK = {
    'PAGINATE_BY': 50
}

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'stockPredict.urls'

WSGI_APPLICATION = 'stockPredict.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'StockPredict',
        'USER': 'root',
        'PASSWORD': 'tyanmysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '../' 'front/template/'),
)

STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../', 'static/')
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../', 'media/')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'requestFile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'log/RequestDebug.log',
        },
        'PredictFile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': 'log/PredictInfo.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'PredictFile'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['requestFile'],
            'propagate': True,
            'level': 'INFO',
        },
    }
}



CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}



SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

from celery.schedules import crontab
CELERY_TIMEZONE = 'UTC'
CELERYBEAT_SCHEDULE = {
    'add-every-monday-morning': {
        'task': 'predictCenter.tasks.judge',
        'schedule': crontab(hour=5, minute=10),
        'args': ('NYSE'),
    },
}