from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
import misaka
from django.contrib.auth import get_user_model
User = get_user_model() # This is a way to get the current user model that is active in this project

from django import template
register = template.Library() # This is a way to register custom template tags

class Group(models.model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToManyField(User,through='GroupMember') # This is a way to create a many to many relationship between the Group model and the User model
    
    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description) # This is a way to convert the description to html
        super().save(*args,**kwargs)  # super is used to call the save method of the parent class, in this case, the parent class is models.model

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ['name'] # This is to make sure that the groups are ordered by name
    
class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE) 
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    class Meta:
        unique_together = ('group','user') # This is to make sure that a user can only be a member of a group once