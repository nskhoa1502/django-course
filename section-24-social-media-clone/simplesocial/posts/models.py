from django.db import models
from django.urls import reverse
from django.conf import settings

import misaka
from groups.models import Group

# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE) # This is a way to create a many to many relationship between the Post model and the User model
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False) # This is to make sure that the message is not editable
    group = models.ForeignKey(Group,related_name='posts',null=True,blank=True,on_delete=models.CASCADE) 

    def __str__(self):
        return self.message
    
    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message) # This is a way to convert the message to html
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk}) # This is to make sure that the user is redirected to the post detail page after creating a post
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','message'] # This is to make sure that a user can only post a message once
