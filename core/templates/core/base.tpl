<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="{{ STATIC_URL }}bootstrap.min.css">
    <link href="{{ STATIC_URL }}sticky.css" rel="stylesheet">
    <title>{% block title %}Main page{% endblock %}</title>
  </head>
  <body>
    {% include 'core/navbar.tpl'%}

    <div class="container-fluid">
      {% block content %}{% endblock %}
    </div>

    {% include 'core/footer.tpl' %}
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="{{ STATIC_URL }}bootstrap.min.js"></script>
  </body>
</html>