import os

"""
Django settings for practice project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*%*k0^*)ru$250r@u7*fzy-8+4-zd*zj__xz#(ols5hu+x1&c%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# →本番環境ではfalseにする。エラーが出た際に、色々表示されていしまう

ALLOWED_HOSTS = ["52.194.68.1","127.0.0.1"]
# →外部サーバでゆるすもの

STATIC_ROOT = '/home/ubuntu/mysite/static'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    # →管理サイト

    'django.contrib.auth',

    # →認証システム
    'django.contrib.contenttypes',


    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "dashboard",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'practice.middleware.auth.authMiddleware',
]

# →リクエストを受け取ってレスポンスを返す間に実施する処理のこと

ROOT_URLCONF = 'practice.urls'
# →作成されたurlsを基本しめす。

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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
# →DIRSテンプレートの保存場所について　
        # 'DIRS': [os.path.join(BASE_DIR, "templates")],　templateの場所を指定する。


WSGI_APPLICATION = 'practice.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "dbmaster",
        'USER': "dbmasteruser",
        'PASSWORD': "Ny>vWz,(Sg,JSLX1=oF.|:>gRTz_mF24",
        'HOST': "ls-ecaecf9be3a421694c9409c54be022cce3db1be8.cuj2dsctfctf.ap-northeast-1.rds.amazonaws.com",
        'PORT': "3306",
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4'
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
    
USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'text'

