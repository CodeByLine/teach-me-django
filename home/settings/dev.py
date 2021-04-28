'''Use this for development'''

from .base import *

ALLOWED_HOSTS += ['127.0.0.1']
DEBUG = True

WSGI_APPLICATION = 'home.wsgi.dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CORS_ORIGIN_WHITELIST = (
    u'https://localhost:8888',
    u'https://127.0.0.1:8000',
    u'http://127.0.0.1:8080',
    u'http://localhost:8000',
    u'http://localhost',
    u'http://127.0.0.1:3000',
    u'http://192.168.7.23:3000',
)