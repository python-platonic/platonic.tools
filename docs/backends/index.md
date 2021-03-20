---
title: Backends
---

Backends are software systems and tools that we interface with using Platonic.

## Available Backends

{% for page in queries.children(this=iri_by_page(page)) %}
  - [{{ page.title }}]({{ page.url }})
{% endfor %}
