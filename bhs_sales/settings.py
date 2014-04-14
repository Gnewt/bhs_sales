import os
from configurations import Configuration

class Dev(Configuration):
    # Stripe keys will be blank for pushing to GitHub
    # Fill out the test mode keys here before running
    STRIPE_PRIVATE_KEY = ""
    STRIPE_PUBLIC_KEY = ""
    
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    SECRET_KEY = 'a_v@l1i4s0$vutlyf%vvfyupz-fom1xvgsz(e(7-7u0o&tez7('
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    ALLOWED_HOSTS = []

    # Application definition

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
        'south',
        'json_field',
        'shirts',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'bhs_sales.urls'

    WSGI_APPLICATION = 'bhs_sales.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.6/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/

    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'America/Los_Angeles'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.6/howto/static-files/

    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
        os.path.join(BASE_DIR, "shirts/static"),
    )

try:
    from local_settings import *
except:
    pass