from .common import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PIPELINE['PIPELINE_ENABLED'] = True

PIPELINE['YUGLIFY_BINARY'] = os.path.join(os.path.dirname(ROOT_DIR), 'node_env', 'bin', 'yuglify')
PIPELINE['LESS_BINARY'] = os.path.join(os.path.dirname(ROOT_DIR), 'node_env', 'bin', 'lessc')
