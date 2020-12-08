import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'dc=wn$q$whc7i4sim-!*=$aawo%3*%-zau29+j&)g4s(pe4b@t'
DEBUG = False
ALLOWED_HOSTS = ['localhost']
#ALLOWED_HOSTS = ['godod4.pythonanywhere.com']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "SystemNotification",
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
ROOT_URLCONF = 'Notification.urls'

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
            ],
        },
    },
]
WSGI_APPLICATION = 'Notification.wsgi.application'
#WSGI_APPLICATION = 'mysite111.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'

#STATIC_URL = '/static/'
#MEDIA_ROOT = '/home/godod4/dj_project/media'
#MEDIA_URL = '/media/'
#STATIC_ROOT = '/home/godod4/dj_project/static'



MEDIA_ROOT = r'C:\Users\prog2.HLEB\Desktop\Нужное\p\ProjectVs\SystemNotification/media'
MEDIA_URL = '/media/'
STATIC_ROOT = r'C:\Users\prog2.HLEB\Desktop\Нужное\p\ProjectVs\SystemNotification/static'
STATIC_URL = '/static/'

