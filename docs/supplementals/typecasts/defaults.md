---
title: Defaults
---

Here are the typecasts available in the default repository, available as

```python
from typecasts import casts
```

{% macro python_object(iri) %}
  {% set obj = queries.python_object(iri=iri)|first %}
  {% if obj.link %}
    <a href="{{ obj.link }}"><code>{{ obj.label }}</code></a>
  {% else %}
    <code>{{ obj.label }}</code>
  {% endif %}
{% endmacro %}

<table>
  <thead>
    <tr>
      <th>Source</th>
      <th>Destination</th>
      <th>Cast</th>
    </tr>
  </thead>
  <tbody>
    {% for row in queries.typecasts.list() %}
    <tr>
      <td>{{ python_object(row.source) }}</td>
      <td>{{ python_object(row.destination) }}</td>
      <td>{{ python_object(row.cast) }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

## Notes

- `pydantic` typecasts are only enabled if [pydantic](https://github.com/samuelcolvin/pydantic/) library is installed.
