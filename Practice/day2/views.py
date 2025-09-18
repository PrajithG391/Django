from django.shortcuts import render,redirect
from .forms import ContactForm

# Create your views here.

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            print("contact subbission:",name,email,message)

            return redirect('contact:success')
        else:
            form = ContactForm()
        return render(request,"day2/contact.html")

def success_view(request):
    return render(request,"day2/success.html")
