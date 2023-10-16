- Generate reusable piece of code in template

```html
<!-- Base.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
      crossorigin="anonymous"
    />
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="navbar-brand" href="{% url 'index' %}">BRAND</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'admin:index' %}">Admin</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'basic_app:other' %}">Other</a>
          </li>
        </ul>
      </div>
    </nav>

    <div class="container">
      <!-- Everything inside this block will be the content -->
      {% block body_block %}
      <!-- Anything outside of this will be inherited if you extend! -->
      {% endblock %}
    </div>
  </body>
</html>
```

```html
<!-- index.html -->
<!DOCTYPE html>
{% extends "basic_app/base.html" %}
<!--  -->
{% block body_block %}
<h1>Welcome to index</h1>
<h1>This is index.html page showing</h1>
{% endblock %}
```
