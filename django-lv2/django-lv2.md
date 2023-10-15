- Django comes equipped with SQLite, but can also connect to other SQL engine (MySQL or PostgreSQL)

==> By adjusting the ENGINE param used for DATABASES in settings.py

- CREATE MODELS: use class structure in models.py

  - This class is a subclass of Django's built-in class : django.db.models.Model
  - Each attribute of the class is a field (or column with constraints in SQL)

- Model in Django:
  - Each column = a field, each field has type field (CharField, URLField, etc.) and constraints (max_length, min_length, not null,etc)

```python
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique = True)

class Webpage(models.Model):
    # on_delete options: https://docs.djangoproject.com/en/4.2/ref/models/fields/#module-django.db.models.fields.related
    category = models.ForeignKey(Topic,on_delete=models.<options>) # set Foreign Key
    name = models.CharField(max_length = 264)
    url = models.URLField()

    def __str___(self)
        return self.name
```

- After setup model, migrate the database

```bash
# Migrate the database
python manage.py migrate

# Register the changes to the app
python manage.py makemigrations <app_name>

# migrate the database one more time
python manage.py migrate
```

- Need to register the models to the admin.py file to use them in the Admin interface

```python
from django.contrib import admin
from app.models import Model1,Model2
admin.site.register(Model1)
admin.site.register(Model2)

```

- After register, we can interact with the database using django admin interface, we'll need to crate a 'superuser'

```bash
python manage.py createsuperuser

# Provide name, email, password
```

- Populate the database with fake data using "Faker" library and a script

- Register to admin.py

```python
from django.contrib import admin
from first_app.models import AccessRecord,Topic,Webpage

# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

```

- Create superuser

```python
python manage.py createsuperuser #username , email, password - confirm password
```

- Create fake data

```python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen=Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get topic for the entry
        top = add_topic()

        # create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # Create a fake access record for that webpage
        acc_rec= AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print('Populating script!')
    populate(20)
    print("populating complete!")
```
