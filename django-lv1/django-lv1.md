- Add new app to django's project:

```python
# settings.py in project folder

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'first_project' # app name
]

==> python manage.py runserver # Check if the app has been registered (success if no error)
```

- HTTP Response:

```python
# Inside views.py in application folder
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')


```

- URL PATH:

```python
# Basic - in urls.py in project folder

from django.urls import path, re_path
from <app_name> import views

urlpatterns = [
    re_path(r'^$', views.index,name='index'), # ^$ == ''
    path('admin/', admin.site.urls),
]

```

- include() function allow us to look for match with regex and link back to our app's own urls.py file => Each application will have its own urls.py. Have to manually add in the urls.py

```python
# In urls.py in project's folder
from django.contrib import admin
from django.urls import path, re_path,include
from first_app import views

urlpatterns = [
    # localhost:8000
    re_path(r'^$', views.index,name='index'), # ^$ == ''
    # localhost:8000/my-new-extension/ ==> Will look into urls.py file in first_app folder
    re_path(r'^my-new-extension/',include('first_app.urls')),
    path('admin/', admin.site.urls),
]


# urls.py in app's folder

from django.urls import path, re_path
from first_app import views

urlpatterns=[
    # localhost:8000/my-new-extension
    re_path(r'^$',views.index,name='index'),
]
```

- Template : similar to template engine in Nodejs, can generate HTML page and use **_template tags_** to inject dynamic content
