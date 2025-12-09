from .settings import *

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'luanf$default',
            'USER': 'luanf',
            'PASSWORD': 'crjmvi2f',
            'HOST': 'luanf.mysql.pythonanywhere-services.com',
            'PORT': '3306',
            'OPTIONS': {
                'charset': 'utf8mb4',
            },
        }
    }

DEBUG = False
