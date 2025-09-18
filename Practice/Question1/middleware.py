import time
from django.conf import settings

# class TimerMiddleware:
#     def __init__(self,get_response):
#         self.get_response = get_response

#     def __call__(self,request):
#         start_time = time.time()

#         response = self.get_response(request)

#         duration = time.time() - start_time
#         if getattr(settings, "DEBUG", False):
#             print(f"[Timer] Request to {request.path} took {duration : .3f} seconds")

#         return response

class UserAgentMiddleware:

    def __init__ (self,get_response):
        self.get_response = get_response 

    def __call__ (self, request):
        user_agent = request.META.get("HTTP_USER_AGENT","Unknown Browser")

        print(f"[UserAgent] Request to {request.path} from: {user_agent}")

        response = self.get_response(request)

        return response
    