## class {{ this.name }}{{ this.type_args }}

```python
{{ this.object_path }}
```

> {{ this.docstring }}

{% for member in this.members %}
### {% if member.type %}**{{ member.type }}**{% endif %} `{{ member.name }}{{ member.printable_signature }}`

> {{ member.docstring }}
{% endfor %}
