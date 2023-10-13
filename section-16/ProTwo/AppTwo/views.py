from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'AppTwo/index.html',context={})
def help(request):
    return render(request,'AppTwo/help.html',context={})

