import os
import json

from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Env for dev / deploy
def get_env(setting, envs):
    try:
        return envs[setting]
    except KeyError:
        error_msg = "You SHOULD set {} environ".format(setting)
        raise ImproperlyConfigured(error_msg)

DEV_ENVS = os.path.join(BASE_DIR, "envs_dev.json")
DEPLOY_ENVS = os.path.join(BASE_DIR, "envs.json")

if os.path.exists(DEV_ENVS):  # Develop Env
    env_file = open(DEV_ENVS)
elif os.path.exists(DEPLOY_ENVS):  # Deploy Env
    env_file = open(DEPLOY_ENVS)
else:
    env_file = None

if env_file is None:  # System environ
    try:
        FACEBOOK_KEY = os.environ['FACEBOOK_KEY']
        FACEBOOK_SECRET = os.environ['FACEBOOK_SECRET']
        GOOGLE_KEY = os.environ['GOOGLE_KEY']
        GOOGLE_SECRET = os.environ['GOOGLE_SECRET']
        GMAIL_ID = os.environ['GMAIL_ID']
        GMAIL_PW = os.environ['GMAIL_PW']
    except KeyError as error_msg:
        raise ImproperlyConfigured(error_msg)
else: # JSON env
    envs = json.loads(env_file.read())
    FACEBOOK_KEY = get_env('FACEBOOK_KEY', envs)
    FACEBOOK_SECRET = get_env('FACEBOOK_SECRET', envs)
    GOOGLE_KEY = get_env('GOOGLE_KEY', envs)
    GOOGLE_SECRET = get_env('GOOGLE_SECRET', envs)
    GMAIL_ID = get_env('GMAIL_ID', envs)
    GMAIL_PW = get_env('GMAIL_PW', envs)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+0%vy1r=h&ygm!f=cwe7^#86o92nc2^0acj@nn-w5fu-ls77)6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # pip
    'debug_toolbar',
    'bootstrap3',
    'rest_framework',
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',

    # Django Apps
    'events.apps.EventsConfig',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # pip
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'DGSUMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'), # Use Root Templates Folder
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Social Login with DjangoRestFramework
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'DGSUMS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# Social Login
AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2', # Google
    'social_core.backends.facebook.FacebookOAuth2', # Facebook
    'rest_framework_social_oauth2.backends.DjangoOAuth2', # Django Defalut User + REST
    'django.contrib.auth.backends.ModelBackend', # Django Base User
]

# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# Social Login : KEY/SECRET

# SocialLogin: Facebook
SOCIAL_AUTH_FACEBOOK_KEY = FACEBOOK_KEY
SOCIAL_AUTH_FACEBOOK_SECRET = FACEBOOK_SECRET
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id, name, email'
}

# SocialLogin: Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = GOOGLE_KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = GOOGLE_SECRET
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']

# Social Login : Redirect
SOCIAL_AUTH_URL_NAMESPACE = 'social'

LOGIN_REDIRECT_URL='/'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static_deploy/')

# Media/Upload files
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# DJDT
INTERNAL_IPS = [
    '127.0.0.1',
]

# Django REST Framework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10,

}

# DRF Social AUTH
# DRFSO2_URL_NAMESPACE = 'social'
