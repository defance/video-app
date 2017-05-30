"""
Django settings for insurance_test project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import twitter_bootstrap

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&h5mjja1y47bo%%68b)f_zdu3+q-o^2!pbs1yy2ez=7*32!ao7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pipeline',
    'jquery',
    'twitter_bootstrap',
    'crispy_forms',

    # actual apps
    'videos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'insurance_test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'insurance_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = './collected_static/'

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

bootstrap_less = os.path.join(os.path.dirname(twitter_bootstrap.__file__),
                              'static', 'less')

PIPELINE = {
    'PIPELINE_ENABLED': False,
    'COMPILERS': (
        'pipeline.compilers.less.LessCompiler',
    ),
    'YUGLIFY_BINARY': os.path.join(os.path.dirname(BASE_DIR),
                                   'node_env', 'bin', 'yuglify'),

    'LESS_BINARY': os.path.join(os.path.dirname(BASE_DIR),
                                'node_env', 'bin', 'lessc'),
    'LESS_ARGUMENTS': u'--include-path={}'.format(
        os.pathsep.join([bootstrap_less, ])
    ),
    'STYLESHEETS': {
        'bootstrap': {
            'source_filenames': (
                'twitter_bootstrap/less/bootstrap.less',
            ),
            'output_filename': 'css/bootstrap.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
    },
    'JAVASCRIPT': {
        'app': {
            'source_filenames': (
                'videos/app.js',
            ),
            'output_filename': 'js/app.min.js',
        },
        'jquery': {
            'source_filenames': (
                'js/jquery.js',
            ),
            'output_filename': 'js/jquery.min.js',
        },
    }
}

PIPELINE_JS = {
    'bootstrap': {
        'source_filenames': (
          'twitter_bootstrap/js/transition.js',
          'twitter_bootstrap/js/modal.js',
          'twitter_bootstrap/js/dropdown.js',
          'twitter_bootstrap/js/scrollspy.js',
          'twitter_bootstrap/js/tab.js',
          'twitter_bootstrap/js/tooltip.js',
          'twitter_bootstrap/js/popover.js',
          'twitter_bootstrap/js/alert.js',
          'twitter_bootstrap/js/button.js',
          'twitter_bootstrap/js/collapse.js',
          'twitter_bootstrap/js/carousel.js',
          'twitter_bootstrap/js/affix.js',
        ),
        'output_filename': 'js/bootstrap.js',
    },
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'
