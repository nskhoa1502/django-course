- Setup urls.py

```python
# project's urls.py
from django.contrib import admin
from django.urls import path, re_path, include
from basic_app import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),  # /
    path('admin/', admin.site.urls),  # /admin/
    re_path(r'^basic_app/', include('basic_app.urls')),  # /basic_app/
]


# app's urls.py
from django.urls import path, re_path
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    re_path(r'^other/$', views.other, name='other'),  # /other/
    re_path(r'^relative/$', views.relative, name='relative'),  # /relative/
]


```

- Setup anchor tag in html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>Welcome to relative url</h1>
    <!-- basic_app must match the app_name in urls.py in basic_app folder  -->
    <a href="{% url 'basic_app:other' %}">THE OTHER PAGE</a>
    <a href="{% url 'admin:index' %}">ADMIN PAGE</a>
    <a href="{% url 'index' %}">link to index</a>
  </body>
</html>
```
