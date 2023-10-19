from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm # This is the form we created in forms.py 
    success_url = reverse_lazy('login') # This is the url we want to redirect to after successful signup , if only reverse is used, it will try to redirect to login before the url is loaded
    template_name = 'accounts/signup.html'

