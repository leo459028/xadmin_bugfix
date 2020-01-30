"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 2.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# Application definition

SITE_APPS = [
    'users',
    'base',
    'index',
    'login',
    'service',
    'errorpage',
]

EXTERNAL_APPS = [
    'xadmin',
    'reversion',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = SITE_APPS + EXTERNAL_APPS + DJANGO_APPS

AUTH_USER_MODEL = 'users.UserProfile'

SESSION_SAVE_EVERY_REQUEST = True

SESSION_COOKIE_AGE = 86400

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'base.views.get_site_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'demo.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'users.views.UserMinimumLengthValidator',
    },
    {
        'NAME': 'users.views.UserCommonPasswordValidator',
    },
    {
        'NAME': 'users.views.UserNumericPasswordValidator',
    },
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# debug模式下要配置，不然找不到路径
# 先在这个路径下查找static文件，找不到再去apps下的static目录查找
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 这个路径只在执行python manage.py collectstatic时才用到，debug模式下没用
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'www', 'static')

STATIC_URL = '/static/'

MEDIA_ROOT = '/media'
MEDIA_URL = '/media/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'toolbar_Custom': [
            [
                'Blockquote',
                'CodeSnippet'
            ],
        ],
        'height': '500px',
        'width': 'auto',
        'image_previewText': '请选择图片',
    },
}

CKEDITOR_UPLOAD_PATH = 'uploads/ckeditor/'