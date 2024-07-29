from django.shortcuts import render
from .forms import ApplicationForm
# we need to use this . before forms because 
# the root directory is app16-django-forms,
# but the file forms.py is in the job_application dir


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
    return render(request, "index.html")