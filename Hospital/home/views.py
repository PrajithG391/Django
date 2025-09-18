from django.shortcuts import render,HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm
# Create your views here.

def index(request):
    person={
        "name":"prajith",
        "age":18,
        "place":"palakkad",


    }

    numbers = { 
        'num1': [1,2,3,4,5,6,7,8,9,10],
    }
    return render(request,"home/index.html", numbers)

def about(request):
    return render(request,"home/about.html")

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home/confirmation.html')
        
    form = BookingForm()
    dict_form = {
        'form' : form
    }
    return render(request,"home/booking.html", dict_form)

def contact(request):
    return render(request,"home/contact.html")

def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request,"home/doctors.html",  dict_docs)

def department(request):
    dict_dept={
        'dept': Departments.objects.all()

    }
    return render(request,"home/department.html", dict_dept)
