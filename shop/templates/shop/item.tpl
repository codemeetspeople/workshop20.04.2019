{% extends 'core/base.tpl' %}

{% block title %}Главная{% endblock %}
{% block content %}
<br />
<h1>{{ item.title }}</h1>
<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Характеристика</th>
      <th scope="col">Значение</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Описание</th>
      <td>{{ item.description }}</td>
    </tr>
    <tr>
      <th scope="row">Цена</th>
      <td>{{ item.price }}</td>
    </tr>
  </tbody>
</table>
{% endblock %}