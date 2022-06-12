from functools import wraps
from django.core.exceptions import PermissionDenied


def require_ajax(view):
    @wraps(view)
    def wrapped_view(request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return view(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    return wrapped_view
