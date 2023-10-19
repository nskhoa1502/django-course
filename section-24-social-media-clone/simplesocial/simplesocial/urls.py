"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.HomePage.as_view(),name='home'),
    re_path(r'^accounts/',include('accounts.urls',namespace='accounts')), # If someone has login or sign up,  it will look into views.py of accounts app
    re_path(r'^accounts/',include('django.contrib.auth.urls')), # django.contrib.auth.urls is a built in app that connect everything that Django has under the hood to make authentication work ==> We don't need to register user model in admin.py because it's inherited from auth.models.User
    re_path(r'^test/$',views.TestPage.as_view(),name='test'),
    re_path(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
]
