# day1/views.py
from django.shortcuts import render

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # You can process or save the data here
        return render(request, "day1/success.html", {"name": name})  # Must return a response
    else:
        return render(request, "day1/contact.html")  

     

