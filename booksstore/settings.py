import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# =======================
# SECURITY / DEBUG
# =======================
SECRET_KEY = "django-insecure-f*k@=53bc5!shef1-6w+m$-g)kspbaljz%8k4(j7iuc-u2_dyd"

# Para rodar local: export PA_DEBUG=true
DEBUG = os.environ.get("PA_DEBUG", "false").lower() == "true"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "luanf.pythonanywhere.com",
]


# =======================
# APPS
# =======================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "order",
    "product",

    "rest_framework",
    "rest_framework.authtoken",
]

# Debug Toolbar só quando DEBUG=True
if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")


# =======================
# MIDDLEWARE
# =======================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # Whitenoise deve vir logo após security
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")


ROOT_URLCONF = "booksstore.urls"


# =======================
# TEMPLATES
# =======================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "booksstore", "templates")],
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


WSGI_APPLICATION = "booksstore.wsgi.application"


# =======================
# DATABASE
# =======================
if os.environ.get("GITHUB_ACTIONS") == "true":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "test_db.sqlite3",
        }
    }

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "luanf$default",
            "USER": "luanf",
            "PASSWORD": "crjmvi2f",
            "HOST": "luanf.mysql.pythonanywhere-services.com",
            "PORT": "3306",
            "OPTIONS": {"charset": "utf8mb4"},
        }
    }


# =======================
# PASSWORD VALIDATION
# =======================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# =======================
# INTERNATIONALIZATION
# =======================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# =======================
# STATIC FILES
# =======================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# =======================
# REST FRAMEWORK
# =======================
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}


# Debug Toolbar local
INTERNAL_IPS = ["127.0.0.1"]
