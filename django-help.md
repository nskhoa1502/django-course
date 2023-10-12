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
