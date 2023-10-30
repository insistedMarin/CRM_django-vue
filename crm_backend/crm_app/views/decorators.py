from functools import wraps
from django.http import HttpResponse


def add_cors_headers(view_func):
    @wraps(view_func)
    def _decorated(*args, **kwargs):
        response = view_func(*args, **kwargs)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
        return response

    return _decorated
