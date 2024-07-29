from django import forms
# All this is for the application form
# it will help us get the data that the user
# wrote in the application form 
# - together with index() func. from views.py


class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)