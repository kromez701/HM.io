import os
from pathlib import Path
from dotenv import dotenv_values
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent
CREDENTIALS = dotenv_values(BASE_DIR / 'hooks_app/.env')

# WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r$rtz-t^^i#q#21049me&2^1!!n8p-(w4iwfnvdh%ygz9z6+#n'

# WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'account.apps.AccountConfig',
  'hooks.apps.HooksConfig',
  'merger.apps.MergerConfig',
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

ROOT_URLCONF = 'hooks_app.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS':
      {
        'context_processors':
          [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
          ],
      },
  },
]

WSGI_APPLICATION = 'hooks_app.wsgi.application'

DATABASES = {
  'default':
    {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
  {
    'NAME':
      'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
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

LANGUAGE_CODE = 'en-us'
USE_I18N = True
TIME_ZONE = 'UTC'
USE_TZ = True

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'account.User'

AUTHENTICATION_BACKENDS = [
  'django.contrib.auth.backends.ModelBackend',
  'account.authentication.EmailAuthBackend',
]

LOGIN_REDIRECT_URL = 'hooks:upload'
LOGIN_URL = 'account:login'
LOGOUT_URL = 'account:logout'

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'media', 'uploads')
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'media', 'output')
if not os.path.exists(UPLOAD_FOLDER):
  os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(OUTPUT_FOLDER):
  os.makedirs(OUTPUT_FOLDER)

DATA_UPLOAD_MAX_MEMORY_SIZE = 2 * 1024 * 1024 * 1024
FILE_UPLOAD_MAX_MEMORY_SIZE = 1 * 1024 * 1024 * 1024
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DOMAIN = 'http://91.108.112.100:6816'
# DOMAIN = 'http://localhost:8000'

STRIPE_REDIRECT_DOMAIN = 'http://0.0.0.0:8000'
STRIPE_PRICE_ID_PRO = CREDENTIALS['STRIPE_PRICE_ID_PRO']
STRIPE_PRICE_ID_EXCLUSIVE = CREDENTIALS['STRIPE_PRICE_ID_EXCLUSIVE']
STRIPE_SEC_KEY = CREDENTIALS['STRIPE_SEC_KEY']
STRIPE_ENDPOINT_SECRET = CREDENTIALS['STRIPE_ENDPOINT_SECRET']

MESSAGE_TAGS = {
  messages.DEBUG: 'debug',
  messages.INFO: 'info',
  messages.SUCCESS: 'success',
  messages.WARNING: 'warning',
  messages.ERROR: 'error',
}

EMAIL_HOST_USER = 'support@hooksmaster.io'
EMAIL_HOST_PASSWORD = 'ddhdnjgykygwwgqv'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.office365.com'
EMAIL_PORT = 587
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True
