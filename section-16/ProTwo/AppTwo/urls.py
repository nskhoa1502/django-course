from django.urls import path,re_path, include
from AppTwo import views

urlpatterns = [
    re_path(r'^$',views.help,name='help'),
]
