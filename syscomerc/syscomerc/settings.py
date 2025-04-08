"""
Django settings for syscomerc project.

Generated by 'django-admin startproject' using Django 5.2.
"""

from pathlib import Path
import os

# =====================
# CONFIGURAÇÕES BÁSICAS
# =====================
BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança
SECRET_KEY = 'django-insecure-x%r!vqvp0_7!_la-&^+olqsu8z_7)4f*0p)k$_w0$w_y^8cro$'
DEBUG = True
ALLOWED_HOSTS = []

# =============
# APLICAÇÕES
# =============
INSTALLED_APPS = [
    # Apps Django padrão
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Apps do projeto
    'cliente',
    'usuario',
]

# =============
# MIDDLEWARE
# =============
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =============
# URLs
# =============
ROOT_URLCONF = 'syscomerc.urls'
WSGI_APPLICATION = 'syscomerc.wsgi.application'

# =============
# TEMPLATES
# =============
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'syscomerc/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# =============
# BANCO DE DADOS
# =============
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# =============
# VALIDAÇÃO DE SENHAS
# =============
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

# =============
# INTERNACIONALIZAÇÃO
# =============
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ===================
# ARQUIVOS ESTÁTICOS
# ===================
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Para produção

# Configurações de mídia (se necessário)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ===================
# OUTRAS CONFIGURAÇÕES
# ===================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'