- Django Form

```python
# in app's folder, create forms.py
from django import forms
from django.core import validators

# Custom validator
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

    # Clean all data
    def clean(self):
        all_clean_data = super().clean() # This will return all the clean data in a dictionary
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError('Make sure emails match!')




# in views.py in app's folder
from django.shortcuts import render
from . import forms
# Create your views here.

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
```

- In templates:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- insert bootstrap -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
      crossorigin="anonymous"
    />
    <title>Forms</title>
  </head>
  <body>
    <!-- 1st option -->
    <h1>Fill out the form!</h1>
    <div class="container">
      <form method="post">
        {{form.as_p}} {% csrf_token %}
        <input type="submit" value="Submit" class="btn btn-primary" />
      </form>
    </div>

    <!-- 2nd option -->
    <h1>Fill out the form!</h1>
    <div class="container">
      <form method="post">
        <!-- Exclude the botcatcher field which is hidden -->
        {% for field in form %}
        <div class="form-group">
          <label for="{{ field.id_for_label }}" class="form-label">
            {{ field.label_tag }}
          </label>
          {{ field }}
        </div>
        {% endfor %} {% csrf_token %}

        <input type="submit" value="Submit" class="btn btn-primary" />
      </form>
    </div>
  </body>
</html>
```
