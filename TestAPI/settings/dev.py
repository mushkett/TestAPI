from .base import *
# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'django-insecure-n30x%2$3^9=e01@a4&r1l8k!mep5ds!$esm+r&!&$tcq4fuojd'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd9fcfr59k686g8',
        'USER': 'ipywmgxrnkdeja',
        'PASSWORD': '951c63e0b1d89444cd828ce6aaf269a5bca9d57552c0960cfaeec624b5de40bd',
        'HOST': 'ec2-63-35-156-160.eu-west-1.compute.amazonaws.com',
        'POST': '',
        'TEST': {
            'MIRROR': 'default',
        },
    },

}
