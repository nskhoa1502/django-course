from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name needs to start with z')

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()

    verify_email = forms.EmailField(label='Enter your email again:')
    # This is a text area
    text = forms.CharField(widget=forms.Textarea)
    # This is a hidden field that will be used to catch bots, so the bot script will look for all the input field in the form, and it will fill out all the input -> So we can use validation to check if the hidden field is filled out or not, if it is filled out, then it is a bot
    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)]) 

    def clean(self):
        all_clean_data = super().clean() # This will return all the clean data in a dictionary
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError('Make sure emails match!')

   
