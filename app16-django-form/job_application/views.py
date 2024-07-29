from django.shortcuts import render
from .forms import ApplicationForm
# we need to use this . before forms because 
# the root directory is app16-django-forms,
# but the file forms.py is in the job_application dir
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"] 
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]
        
            # form.cleaned_data is a dict whose keys come from
            # html, see the name of the inputs
            
            Form.objects.create(first_name=first_name, last_name=last_name, 
                                email=email, date=date, occupation=occupation)
            
            message_body = f"A new job application is submitted. Thank you, {first_name}"
            email_message = EmailMessage("Form submission confirmation", message_body, to=[email])
            # email_message.send()
            print(message_body)
            
            messages.success(request, "Form submitted succesfully :)")
    return render(request, "index.html")