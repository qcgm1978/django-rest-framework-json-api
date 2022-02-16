import os

SITE_ID = 1
MEDIA_ROOT = os.path.normcase(os.path.dirname(os.path.abspath(__file__)))
MEDIA_URL = "/media/"
USE_TZ = False
DATABASE_ENGINE = "sqlite3"
ALLOWED_HOSTS = []
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "drf_example",
    }
}
# django-debug-toolbar
# First, ensure that 'django.contrib.staticfiles' is in your INSTALLED_APPS setting, and configured properly:
# Add "debug_toolbar" to your INSTALLED_APPS setting:
INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.auth",
    "rest_framework_json_api",
    "rest_framework",
    "polymorphic",
    "example",
    "debug_toolbar",
    "django_filters",
    "tests",
    "corsheaders",
]
STATIC_URL = "/static/"
# Second, ensure that your TEMPLATES setting contains a DjangoTemplates backend whose APP_DIRS options is set to True:
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # insert your TEMPLATE_DIRS here
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
ROOT_URLCONF = "example.urls"
SECRET_KEY = "abc123"
PASSWORD_HASHERS = ("django.contrib.auth.hashers.UnsaltedMD5PasswordHasher",)
# The Debug Toolbar will only display when DEBUG = True in your project’s settings (see Show Toolbar Callback) and your IP address must also match an entry in your project’s INTERNAL_IPS setting (see 6. Configure Internal IPs). It will also only display if the MIME type of the response is either text/html or application/xhtml+xml and contains a closing </body> tag.
DEBUG = True
# The Debug Toolbar is shown only if your IP address is listed in Django’s INTERNAL_IPS setting. This means that for local development, you must add "127.0.0.1" to INTERNAL_IPS. You’ll need to create this setting if it doesn’t already exist in your settings module:
INTERNAL_IPS = ("127.0.0.1",)
# The Debug Toolbar is mostly implemented in a middleware. Add it to your MIDDLEWARE setting:
MIDDLEWARE = (
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
)
# MIDDLEWARE_CLASSES = (
# )
JSON_API_FORMAT_FIELD_NAMES = "camelize"
JSON_API_FORMAT_TYPES = "camelize"
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    "PAGE_SIZE": 5,
    "EXCEPTION_HANDLER": "rest_framework_json_api.exceptions.exception_handler",
    "DEFAULT_PAGINATION_CLASS": "rest_framework_json_api.pagination.JsonApiPageNumberPagination",
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework_json_api.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ),
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework_json_api.renderers.JSONRenderer",
        # If you're performance testing, you will want to use the browseable API
        # without forms, as the forms can generate their own queries.
        # If performance testing, enable:
        # 'example.utils.BrowsableAPIRendererWithoutForms',
        # Otherwise, to play around with the browseable API, enable:
        "rest_framework_json_api.renderers.BrowsableAPIRenderer",
    ),
    "DEFAULT_METADATA_CLASS": "rest_framework_json_api.metadata.JSONAPIMetadata",
    "DEFAULT_SCHEMA_CLASS": "rest_framework_json_api.schemas.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": (
        "rest_framework_json_api.filters.OrderingFilter",
        "rest_framework_json_api.django_filters.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
    ),
    "SEARCH_PARAM": "filter[search]",
    "TEST_REQUEST_RENDERER_CLASSES": ("rest_framework_json_api.renderers.JSONRenderer",),
    "TEST_REQUEST_DEFAULT_FORMAT": "vnd.api+json",
}
CORS_ORIGIN_ALLOW_ALL = True
