from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    # blank=True means that the field is not required
    portfolio_site = models.URLField(blank=True)
    # upload_to='profile_pics' is the directory where the image will be uploaded to
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User
        return self.user.username
