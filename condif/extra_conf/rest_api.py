REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",

}
SPECTACULAR_SETTINGS = {
    "TITLE": "Daily Book",
    "DESCRIPTION": "Yaroslav Sadovskyi",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}
# "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
# "DEFAULT_PAGINATION_CLASS": "core.pagination.Pagination",
