from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')


def form_name_view(request):
    form = forms.FormName()
    # for field in form:
        # print('field:', field)
        # print('label_tag', field.label_tag)
        # print('help_text', field.help_text)
        # print('errors', field.errors)
        # print('is_hidden', field.is_hidden)
        # print('name', field.name)
        # print('value', field.value)
        # print('field.data', field.data)
        # print('field id for label', field.id_for_label)
    
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid(): # This is where the validation happens
            # Do something code
            print('Validation success!') 

            # Accessing the data from the form
            print('Name:', form.cleaned_data['name'] ) 
            print('Email:', form.cleaned_data['email'])
            print('Text:', form.cleaned_data['text'])
    return render(request,'basicapp/form_page.html',{'form':form})