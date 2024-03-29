"""
Django settings for videosharer project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os # Manually: Import the os module

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tx#dyodhbx44s+q&xa6z-e^*6zw6)8m5_pj2p_)e1ys8m^scjz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Manually add authentication backends to the settings.py file
AUTHENTICATION_BACKENDS = [ 
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',  
]
SITE_ID = 1 # Manually: Add the site id to the settings.py file

# Application definition

INSTALLED_APPS = [
    'videos', # Manually: Add the videos app to the list of installed apps
    'profiles',# Manually: Add the profiles app to the list of installed apps
    'crispy_forms', # Manually: Add the crispy_forms app to the list of installed apps
    'crispy_bootstrap5', # Manually: Add the crispy_bootstrap5 app to the list of installed apps
    'allauth',# Manually: Add the allauth app to the list of installed apps
    'allauth.account',# Manually: Add the allauth.account app to the list of installed apps
    'allauth.socialaccount',# Manually: Add the allauth.socialaccount app to the list of installed apps
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    "allauth.account.middleware.AccountMiddleware", # Manually: Add the allauth account middleware to the list of middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'videosharer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Manually: Add the templates directory to the list of dirs
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

WSGI_APPLICATION = 'videosharer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_ROOT = os.path.join(BASE_DIR , 'media') # Manually: Add the media root to the settings.py file
MEDIA_URL = '/media/' # Manually: Add the media url to the settings.py file

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5" # Manually: Add the crispy allowed template packs to the settings.py file
CRISPY_TEMPLATE_PACK = 'bootstrap5' # Manually: Add the crispy template pack to the settings.py file

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # Manually: Add the email backend to the settings.py file
EMAIL_HOST = 'smtp.gmail.com' # Manually: Add the email host to the settings.py file
EMAIL_PORT = 587 # Manually: Add the email port to the settings.py file
EMAIL_USE_TLS = True # Manually: Add the email use tls to the settings.py file
EMAIL_HOST_USER = 'snency16@gmail.com' # Manually: Add the email host user to the settings.py file
EMAIL_HOST_PASSWORD = 'gxqczxpftjewiyro' # Manually: Add the email host password to the settings.py file


LOGIN_REDIRECT_URL = 'index' # Manually: Add the login redirect url to the settings.py file

# Manually: additions to signup form
ACCOUNT_SIGNUP_FORM_CLASS ="profiles.forms.ProfileForm" # Manually: Add the account signup form class to the settings.py file