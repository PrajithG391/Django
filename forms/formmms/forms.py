from django import forms

class feedbackForm(forms.Form):
    name = forms.CharField(max_length=100, required=True,label = "Your Name")
    email = forms.EmailField(required=True,label="Email Address")
    message = forms.CharField(widget=forms.Textarea, label="Message")
    