# FILE: /blog_project/project/settings.py

"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR.parent / 'data' / 'web' # /data/web/static | /data/web/media


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'change-me') # /blog_project/dotenv_files/.env

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = bool(int(os.getenv('DEBUG', 0))) # /blog_project/dotenv_files/.env


ALLOWED_HOSTS = [h.strip() for h in os.getenv('ALLOWED_HOSTS', '').split(',') if h.strip()] # /blog_project/dotenv_files/.env


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # IMPORT⬇: /blog_project/djangoapp/blog/apps.py
    'blog',
    # IMPORT⬇: /blog_project/djangoapp/site_setup/apps.py
    'site_setup',

    'django_summernote',
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

ROOT_URLCONF = 'project.urls'

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

                # LOCALE: /blog_project/djangoapp/site_setup/context_processors.py
                # COMMENT: Call the function.
                'site_setup.context_processors.context_processor_example',

                # #LOCALE: /blog_project/djangoapp/site_setup/context_processors.py
                'site_setup.context_processors.site_setup',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = { # /blog_project/dotenv_files/.env
        'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'change-me'), ##
        'NAME': os.getenv('POSTGRES_DB', 'change-me'),
        'USER': os.getenv('POSTGRES_USER', 'change-me'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'change-me'),
        'HOST': os.getenv('POSTGRES_HOST', 'change-me'),
        'PORT': os.getenv('POSTGRES_PORT', 'change-me'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us' # 'pt-br'

TIME_ZONE = 'America/Sao_Paulo' # 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/' # 'static/'
STATIC_ROOT = DATA_DIR / 'static' # /data/web/static
MEDIA_URL = '/media/'
MEDIA_ROOT = DATA_DIR / 'media' # /data/web/media
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') # Teste summernote.


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# django_summernote
SUMMERNOTE_CONFIG = { #1:
    'summernote': {
        # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        'toolbar': [
            ['style', ['style', ]],
            ['font', ['bold', 'italic', 'clear']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph', 'hr', ]],
            ['table', ['table']],
            ['insert', ['link', 'picture']],
            ['view', ['fullscreen', 'codeview', 'undo', 'redo']],
        ],
        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': 'true',
            'lineWrapping': 'true',
            'theme': 'dracula',
        },
    },
    'css': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/6.65.7/theme/dracula.min.css',
    ),
    'attachment_filesize_limit': 30 * 1024 * 1024,
    'attachment_model': 'blog.PostAttachment',
}


# ------------------------------------------------------------------
#1: Este dicionário configura as opções específicas para o editor de texto Summernote, utilizado para criar e editar conteúdo rico no Django. Ele está relacionado ao pacote django-summernote, permitindo customizações como a configuração da toolbar, habilitação de temas para o editor, e definições sobre o comportamento do editor.