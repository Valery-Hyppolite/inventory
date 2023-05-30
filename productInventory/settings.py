
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-_8$viqnjbn-im%cb%5owiwc3%&iwv1=izg=w$90azww*d2vmn^'
DEBUG = True

# SECRET_KEY = os.environ.get("SECRET_KEY")
# DEBUG = str(os.environ.get("DEBUG"))

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products.apps.ProductsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    #additonal application
    'whitenoise.middleware.WhiteNoiseMiddleware',
    #---------------------------------------
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'productInventory.urls'

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

WSGI_APPLICATION = 'productInventory.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get("DB_HOST"),
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD")
    }
}

# POSTGRESS_DB = os.environ.get("POSTGRESS_DB")
# POSTGRESS_PASSWRD = os.environ.get("POSTGRESS_PASSWRD")
# POSTGRESS_USER = os.environ.get("POSTGRESS_USER")
# POSTGRESS_HOST = os.environ.get("POSTGRESS_HOST")
# POSTGRESS_PORT = os.environ.get("POSTGRESS_PORT")

# DB_IS_AVAILABLE = all([
#     POSTGRESS_DB,
#     POSTGRESS_PASSWRD,
#     POSTGRESS_USER,
#     POSTGRESS_HOST,
#     POSTGRESS_PORT
# ])

# POSTGRESS_READY = str(os.environ.get("POSTGRESS_READY")) == "1"

# if DB_IS_AVAILABLE and POSTGRESS_READY:
#     DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': POSTGRESS_DB,
#         "USER": POSTGRESS_USER,
#         "PASSWORD": POSTGRESS_PASSWRD,
#         "HOST": POSTGRESS_HOST,
#         "PORT": POSTGRESS_PORT
#     }
# }

print(DATABASES)

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/imgs/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/imgs') # tell django where to upload imgs upload by uers

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
