from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

# Create your views here.

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'basic_app/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse('You are logged in, nice!')


def register(request):
    # Boolean to check if registration was successful
    registered = False

    # Check if the request is a POST request
    if request.method == 'POST':
        # Grab the data from the forms
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check if the forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database
            user = user_form.save()
            # Hash the password with the set_password method
            user.set_password(user.password)  # Hash the password
            user.save()

            # Don't commit to the database yet (commit=False)
            profile = profile_form.save(commit=False)
            # Set up the OneToOne relationship between the UserForm and UserProfileInfoForm
            profile.user = user

            # Check if a profile picture was uploaded

            if 'profile_pic' in request.FILES:  # Check if a file was uploaded
                # If a file was uploaded, then grab it from the POST request
                profile.profile_pic = request.FILES['profile_pic']

            # Save the profile to the database
            profile.save()

            # Registration was successful
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        # Not a POST request, so render the forms as blank
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    # Check if the request is a POST request
    if request.method == 'POST':
        # Grab the username from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username and password are valid
        user = authenticate(username=username, password=password)

        if user:
            # Check if the user is active
            if user.is_active:
                # Log the user in
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                # Account is not active
                return HttpResponse('Account not active')
        else:
            print('Someone tried to login and failed')
            print(r'Username: {username} and password {password}')
            return HttpResponse('Invalid login details supplied')

    else:
        # Not a POST request, so render the login form
        return render(request, 'basic_app/login.html')
