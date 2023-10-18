from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# from django.contrib.auth.decorators import login_required - ONLY FUNCTION VIEW
from blog.models import Post,Comment
from blog.forms import PostForm,CommentForm
# Create your views here.


class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    # Doing a SQL query on the model => __lte is less than or equal to => -published_date is descending order
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/' # If user is not logged in, redirect to login page
    redirect_field_name = 'blog/post_detail.html' # After creating a post, redirect to post_detail page

    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/' # If user is not logged in, redirect to login page
    redirect_field_name = 'blog/post_detail.html' # After creating a post, redirect to post_detail page

    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/' # If user is not logged in, redirect to login page
    redirect_field_name = 'blog/post_detail.html' # After creating a post, redirect to post_detail page
    model = Post
    # After deleting a post, redirect to post_list page
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/' # If user is not logged in, redirect to login page
    redirect_field_name = 'blog/post_list.html' # After creating a post, redirect to post_detail page
    model = Post

    def get_queryset(self):
        # __isnull is a Django convention for checking if something is null
        # If the published_date is null, then we know that the post is a draft
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')