from django.shortcuts import render,get_object_or_404,redirect 
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required # for function based views
from django.utils import timezone
from blog.models import Post,Comment
from blog.forms import PostForm,CommentForm
# Create your views here.


class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    # Doing a SQL query on the model => __lte is less than or equal to => -published_date is descending order
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

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
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
    

# ===============================

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish() # Call the publish method in the Post model
    return redirect('post_detail',pk=pk) # Redirect to the post_detail page of the post that was published based on the primary key


@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST) # Get the form data

        if form.is_valid():
            comment = form.save(commit=False) # commit=False means don't save to database, just get the form data and save it in memory
            comment.post = post # Assign the comment to the post, because post is a foreign key in the Comment model
            comment.save() # Save to database
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm() # If the request is not a POST request, then just create a blank form
    
    return render(request,'blog/comment_form.html',{'form':form}) # Pass the form to the template

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve() # Call the approve method in the Comment model
    return redirect('post_detail',pk=comment.post.pk) # Redirect to the post_detail page of the post that the comment belongs to based on the primary key

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk # Get the primary key of the post that the comment belongs to
    comment.delete() # Delete the comment
    return redirect('post_detail',pk=post_pk) # Redirect to the post_detail page of the post that the comment belongs to based on the primary key

@login_required
def comment_edit(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk # Get the primary key of the post that the comment belongs to

    if request.method == 'POST':
        form = CommentForm(request.POST,instance=comment) # We pass in the instance of the comment so that the form knows which comment to update
        if form.is_valid():
            comment = form.save()
            return redirect('post_detail',pk=post_pk)
    else:
        form = CommentForm(instance=comment) # We pass in the instance of the comment so that the form knows which comment to update
    return render(request,'blog/comment_form.html',{'form':form})

