from pathlib import Path
import dj_database_url
import cloudinary
import cloudinary_storage
import os



SECRET_KEY = 'django-insecure-5^*pa^928$jc$lfrhf8zibxc4-#qy!3c_bz*h=_0x9a^1b5^g=' 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!

LOGIN_URL = 'login'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.gitpod.io']
CSRF_TRUSTED_ORIGINS = ['https://*.gitpod.io']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cleaning_agency',
    'users',
    "crispy_forms",
    "crispy_bootstrap5",
    'bookings',
    'about',
    'contact',  # Replace 'your_app_name' with the name of your Django app
]
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5" # or 'bootstrap5' if you're using Bootstrap 5
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cleaning_agency.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required for the admin sidebar
                'django.contrib.auth.context_processors.auth',  # Required for using the admin
                'django.contrib.messages.context_processors.messages',  # Required for admin messages
                'django.template.context_processors.media',  # If you use media files in templates
            ],
        },
    },
]


WSGI_APPLICATION = 'cleaning_agency.wsgi.application'

# Database configuration
DATABASE_URL = 'postgres://ffribynssvujbr:ee9c3123182d36a0c7d548a1703558ebe6f672dccfafe2f15f8af16d1c0a5254@ec2-34-232-92-61.compute-1.amazonaws.com:5432/ddp6r0fflu4nj8'
DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600, engine='django.db.backends.postgresql')
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images) configuration
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Cloudinary configurations
cloudinary.config(
  cloud_name = 'createnova',
  api_key = '732142741797832',
  api_secret = 'a_PIRjoEdLwHcDk5npdrRioP5sE'
)

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'

ANYMAIL = {
    "MAILJET_API_KEY": "0ef641b51ea63176b36792f30a1c13e0",
    "MAILJET_SECRET_KEY": "8b6a67b8e18eecd4b54df51a1a7a7a1f",
    "MAILJET_SEND_DEFAULTS": {
        "esp_extra": {
            # Add any Mailjet-specific send settings here
        },
    },
}

EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
DEFAULT_FROM_EMAIL = "help.angleseycleaners@gmail.com"



# Heroku settings
import django_heroku
django_heroku.settings(locals())