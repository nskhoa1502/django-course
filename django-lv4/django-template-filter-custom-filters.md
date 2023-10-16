- We can use python methods inside html template
- We can also create custom filter

```python
# inside app's folder create a templatetags folder -> create __init__.py and <custom_filter>.py

from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    this cuts out all values of "arg" from the string!

    """
    return value.replace(arg, '')


# register.filter('cut', cut)

```

- Use it inside template

```html
<!DOCTYPE html>
{% extends "basic_app/base.html" %}
<!--  -->
{% block body_block %}
<h1>Welcome to index</h1>
<!-- <h1>This is index.html page showing</h1> -->
<!-- Custom filter -->
<h1>{{text | cut:'hello' |upper}}</h1>
<h1>{{number|add:'99'}}</h1>
<!--  -->
<!--  -->
{% endblock %}
```
