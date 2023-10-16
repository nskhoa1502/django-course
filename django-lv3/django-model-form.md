- Situation: We want to save to the model the info that user input in (reply a comment)
  ==> We can accept form input and pass it to a model
  ==> Instead of inheriting forms.Forms , we use forms.ModelForm instead
  ==> forms.ModelForm allows us to **create a form from a pre-existing model**
  ==> We add an inline class called Meta, the Meta class provides information connecting the model to the form

```python
# models.py

from django.db import models

# Create your models here.

class User(models.Model):
first_name=models.CharField(max_length=264)
last_name=models.CharField(max_length=264)
email=models.CharField(max_length=264,unique=True)

    def __str__(self):
        return f'Full_name: {self.first_name} + {self.last_name}\nEmail: {self.email}'

# forms.py ==> Create a form based on the User model

from django import forms
from AppTwo.models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        # Choose one in 3 options:
        # fields = '__all__'
        # exclude = ['first_name','email']
        # include = ('first_name','last_name')
```
