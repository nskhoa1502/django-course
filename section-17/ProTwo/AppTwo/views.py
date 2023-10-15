from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.

def index(request):
    return render(request,'AppTwo/index.html',context={})
def help(request):
    return render(request,'AppTwo/help.html',context={})

def user(request):
    user_list = User.objects.all()
    user_dict = {'users':user_list}
    return render(request,'AppTwo/user.html',context=user_dict)

