## Django

- create Django project

```bash

django-admin startproject <project-name>

django-admin startproject first_project
```

- Folder structure

  - '**init**.py' : Blank python script that let python know that this directory is treated as a package
  - settings.py : Store all project settings
  - urls.py : Python script that will store all the URL patterns for the project ==> Different pages of your web application
  - wsgi.py : Python script that acts as the Web Server gateway Interface => Help us deploy the web app to production
  - manage.py : Python script that will be associated with many commands when we build the web app (will use a lot)

- Use manage.py ==> localhost:8000 by default or http://127.0.0.1:8000/

```bash
python manage.py runserver
```

- migration : allow to move databases from one design to another => like sequelize or prisma db push or migrate

  - npx sequelize-cli db:migrate

- A Django project is a collection of applications and configs that make up the full web application
- A Django application is created to perform A PARTICULAR FUNCTIONALITY for the entire web application (registration app, polling app, comment app,etc.)
  ==> One Django project can have many Django apps (Plug-able Django application)

  ```bash
  python manage.py startapp <app-name>

  python manage.py startapp first_app
  ```

- Folder structure of an Django app:
  - init.py : Let python know that this directory can be treated as package
  - admin.py : We can register models for Django will then use them with Django's admin interface
  - apps.py : application specific configs
  - tests.py : store testing functions
  - models.py : store application's data models ==> define relationship between the data
  - views.py : handle REQUESTS and return RESPONSE
  - Migration Folder: store database specific information related to the models
    ==> Follow model views template application
