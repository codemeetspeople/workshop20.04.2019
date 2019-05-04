{% macro publications_list(name, publications) -%}
    <div class="list-group">
        {% set url_name = 'shop:' + name %}
        {% for publication in publications %}
            <a href="{{ url(url_name, publication.id) }}" class="list-group-item list-group-item-action">{{ publication.title }}</a>
        {% endfor %}
    </div>
{%- endmacro %}