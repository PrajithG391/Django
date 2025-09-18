class SimpleLoggingMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("Middleware initialized!")

    def __call__(self,request):
        print(f"Request url:{request.path}")

        response = self.get_response(request)

        print(f"Response status:{response.status_code}")

        return response
    
class RequestLoggerMiddleware:
    def  __init__(self,get_response):
        self.get_response = get_response
        print("RequestLoggerMiddleware initialized!")

    def __call__(self,request):
        print(f"[Before View]URL:{request.path},Method: {request.method}")

        response = self.get_response(request)

        print(f"[After View] status Code:{response.status_code}")

        return response  