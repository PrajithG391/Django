from django.conf import settings

class LogRequestMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        if getattr(settings,"DEBUG",False):
            print(f"[Request] {request.method} {request.path}")
        response = self.get_response(request)
        return response