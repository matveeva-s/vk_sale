from django.middleware.csrf import get_token


class EnsureCSRFMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if 'csrftoken' not in request.COOKIES and response.status_code == 200:
            response['csrftoken'] = get_token(request)
        
        return response
