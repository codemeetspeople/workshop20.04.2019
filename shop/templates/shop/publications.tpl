{% extends 'core/base.tpl' %}
{% import 'shop/macro.tpl' as macros %}

{% block title %}Главная{% endblock %}
{% block content %}
<div class="row">
    <div class="col-lg-12">
        <br /><br />
        {{ macros.publications_list(title, publications) }}
    </div>
</div>
{% endblock %}