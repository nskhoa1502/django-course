from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    # 5 Fields : author, title,text, create_date, published_date
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    # timezone is either UTC or GMT in settings.py
    create_date = models.DateTimeField(default = timezone.now())

    # Haven't published yet so blank=True, or haven't had a date yet so null=True
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        # Whenever we call publish, we update the published_date as the current time
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        # This will return all the comments that are approved
        # Comments are either approved or not approved, only show approved comments for filtering purposes
        return self.comments.filter(approved_comment=True)
    
    # After we create a post, we want to go back to the post_detail page
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.post.pk})
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()


    # After we create a comment, we want to go back to the post_list page
    def get_absolute_url(self):
        return reverse('post_list')

    
    def __str__(self) :
        return self.text
