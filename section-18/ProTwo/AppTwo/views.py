from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request,'AppTwo/index.html',context={})
def help(request):
    return render(request,'AppTwo/help.html',context={})

def user(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        print('POST')

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form invalid')
    
    return render(request,'AppTwo/user.html',context={'form':form})


