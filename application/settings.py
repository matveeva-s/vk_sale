from pathlib import Path
import configparser
from os import path
import saml2
from saml2 import saml

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = path.dirname(BASE_DIR)

config_path = path.join(PROJECT_DIR, 'conf/django.conf')

config = configparser.RawConfigParser()
config.read(config_path)

SECRET_KEY = config.get('general', 'SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*', ]
CORS_ORIGIN_WHITELIST = ['http://localhost:3000']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djangosaml2',
    'users',
    'store',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'djangosaml2.middleware.SamlSessionMiddleware',
    'application.middleware.EnsureCSRFMiddleware',
]

STATIC_ROOT = config.get('general', 'STATIC_ROOT')
MEDIA_ROOT = config.get('general', 'MEDIA_ROOT')

CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False

DOMAIN = config.get('general', 'DOMAIN')

ROOT_URLCONF = 'application.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'application.wsgi.application'

AUTH_USER_MODEL = 'users.User'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'djangosaml2.backends.Saml2Backend',
)

LOGIN_URL = '/saml2/login/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SAML_BASE_URL = 'http://127.0.0.1:3001/saml2/'
LOGIN_REDIRECT_URL = 'http://127.0.0.1:3001/'

SAML_SESSION_COOKIE_NAME = 'saml_session'

SAML_CONFIG = {
    'debug': DEBUG,
    'xmlsec_binary': '/usr/local/bin/xmlsec1',
    'entityid': f'{SAML_BASE_URL}metadata/',

    'service': {
        'sp': {
            'name': 'Garage Sale VKApp',
            'endpoints': {
                'assertion_consumer_service': [
                    (f'{SAML_BASE_URL}acs/', saml2.BINDING_HTTP_POST),
                ],
                'single_sign_on_service': [
                    ('{}/ls/post'.format(SAML_BASE_URL), saml2.BINDING_HTTP_POST),
                    ('{}/ls/redirect'.format(SAML_BASE_URL), saml2.BINDING_HTTP_REDIRECT),
                ]
            },
            'name_id_format': [saml.NAMEID_FORMAT_EMAILADDRESS],
            'authn_requests_signed': True,
            'want_assertions_signed': True,
            'allow_unsolicited': True,
        },
    },
    'attribute_map_dir': path.join(BASE_DIR, 'saml2/attribute_maps'),
    'metadata': {
        'local': [path.join(BASE_DIR, 'saml2/metadata/authcorp_metadata_prod.xml')],
    },
    'key_file': path.join(BASE_DIR, 'saml2/certificates/private.key'),
    'cert_file': path.join(BASE_DIR, 'saml2/certificates/public.cert'),

    'encryption_keypairs': [{
        'key_file': path.join(BASE_DIR, 'saml2/certificates/private.key'),
        'cert_file': path.join(BASE_DIR, 'saml2/certificates/public.cert'),
    }],
    'valid_for': 365 * 24,
    'accepted_time_diff': 300,
}

SAML_USE_NAME_ID_AS_USERNAME = True
SAML_DJANGO_USER_MAIN_ATTRIBUTE = 'username'
SAML_DJANGO_USER_MAIN_ATTRIBUTE_LOOKUP = '__iexact'
SAML_CREATE_UNKNOWN_USER = True

SAML_ATTRIBUTE_MAPPING = {
    'email': ('email', ),
    'first_name': ('first_name', ),
    'last_name': ('last_name', ),
    'is_staff': ('is_staff', ),
    'is_superuser':  ('is_superuser', ),
}
