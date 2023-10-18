from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author','title','text') # Fields that we want to edit

        # We want to add some styling to our form
        # We want to add a class to each of the fields
        # We want to add a placeholder to each of the fields
        # We want to add a class to the text area
        # We want to add a class to the text area's text
        widgets = {
            # textinputclass is our own class - we can use this to style our text
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            # medium-editor-textarea is a class that we can use connect to medium-editor
            # editable allows us to edit the text
            # postcontent is our own class - we can use this to style our text
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}) 
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }