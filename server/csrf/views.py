from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
@ensure_csrf_cookie
def get_csrf(request):
    return JsonResponse({'csrfToken': request.COOKIES.get('csrftoken')})
