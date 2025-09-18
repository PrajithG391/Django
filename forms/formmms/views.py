from django.shortcuts import render
from .forms import feedbackForm


# Create your views here.

def feedback_view(request):
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            print(f"Message from {name} ({email}):{message}")

            return render(request,'account/thanks.html',{'name': name})
        else:
            form = feedbackForm()

        return render(request,'accounts/feedback.html',{'form':form})
    