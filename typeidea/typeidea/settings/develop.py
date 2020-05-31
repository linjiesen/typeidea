from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Typeidea',
        'USER': 'root',
        'PASSWORD': 'kid1412',
        'HOST': '127.0.0.1',
    }
}
