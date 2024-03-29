"""
Django settings for pc project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-n=tcx0_e_)0s0$k-20$#=m9+)t9afcmt7rtoi^g64a$59u4ak="

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "home",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "pc.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "pc.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = "/var/www/Contact-Website/static"

MEDIA_URL = "/media/"
MEDIA_ROOT = "/var/www/Contact-Website/media"
# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": None,
    },
}

THUMBNAIL_ALIASES = {
    "": {
        "avatar": {"size": (200, 200), "crop": True},
    },
}

CRISPY_TEMPLATE_PACK = "bootstrap4"
CSRF_TRUSTED_ORIGINS = ["https://fableey.com"]


# # Set your email backend. Here's an example using the console backend for testing.
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# Set the email host and port for SMTP.
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587

# Set the default 'from' address for emails.
DEFAULT_FROM_EMAIL = "ap1solutions0201@gmail.com"

# Additional settings for sending emails using SMTP.
EMAIL_USE_TLS = True  # Use TLS if required, set to False if using SSL
EMAIL_USE_SSL = False  # Use SSL if required, set to True if using SSL

# If your SMTP server requires authentication, provide the username and password.
EMAIL_HOST_USER = "ap1solutions0201@gmail.com"
EMAIL_HOST_PASSWORD = "gwkv pdeo leod teti"
