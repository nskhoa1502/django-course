from django.urls import path,re_path, include
from AppTwo import views

urlpatterns = [
    path('',views.index,name='index'),
    re_path(r'^user/',views.user,name='user'),
    re_path(r'^help/',views.help,name='help'),
]
