from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world, i am Prajith G, nice meeting you")
    return render(request, 'index.html' )

def about(request):
    return HttpResponse("its my about page")

def contact(request):
    return HttpResponse("hay, its my contact section")