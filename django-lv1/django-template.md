- Check file-path = pathlib in project's settings.py

```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR/'templates
print(BASE_DIR/'templates') # Concatenate subdir
print(Path(__file__).name) # File name

$ python settings.py
C:\Users\Admin\Desktop\New folder (2)\django-course\section-16\first_project\subdir
settings.py

```

- Inside TEMPLATES config in settings.py

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR], # add template dir
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```

- Create templates folder => inside views.py of app's folder => define which html file inside template folder we'll render according to the urls

- Serve static files (image or css or js files)
  1. Setup:

```python
# inside settings.py in project's folder
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR/'templates'
STATIC_DIR=BASE_DIR/'static'

STATIC_URL = 'static/' # We can access static files via url : {{base_url}}/static/...
STATICFILES_DIRS=[
    STATIC_DIR,
]

```

2. After setup, create a static folder, inside static folder, create subfolders like css or js or images file
3. Inject those static files into html file

```html
<!DOCTYPE html>
<!-- VERY IMPORTANT -->
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Cat image</title>
    <!-- Inject css file -->
    <link rel="stylesheet" href="{% static 'css/mystyle.css' %}" />
  </head>
  <body>
    <h1>This is a picture of a cat</h1>
    <!-- Inject image file -->
    <img src='{% static "images/cat1.jpg" %}' alt="cat picture" width="300px" />
  </body>
</html>
```

- How to use if, for loop in template

```python
# views.py

def index(request):
  # Access the AccessRecord object
    webpages_list = AccessRecord.objects.order_by('date')
    # create a dict with the AccessRecord data
    date_dict = {'access_records':webpages_list}
    return render(request,'first_app/index.html',context=date_dict)
```

```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Django level 2</title>
    <link rel="stylesheet" href='{% static "css/mystyle.css" %}' />
  </head>
  <body>
    <h1>Hi welcome to Django Level two!</h1>
    <h2>Here are your access record:</h2>

    <div class="djangtwo">
      {% if access_records %}
      <table>
        <thead>
          <th>Site Name</th>
          <th>Date Accessed</th>
        </thead>
        {% for acc in access_records %}
        <tr>
          <td>{{ acc.name}}</td>
          <td>{{ acc.date}}</td>
        </tr>
        {% endfor %}
      </table>

      {% else %}
      <p>NO ACCESS RECORDS FOUND</p>
      {% endif %}
    </div>
  </body>
</html>
```
