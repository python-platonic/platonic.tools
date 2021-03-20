---
title: Interfaces
position: -1
---

Interfaces are façades which hide intricacies and ugly parts of various backends, providing you with a clean and unified interface to rule them all. For example, if you have `Queue` implementations for AWS SQS, Apache Kafka and RabbitMQ, you may build a task queue on whichever one of them you choose - and your client code will not change too much when you switch from one to another. 

## Available interfaces

{% for page in queries.children(this=iri_by_page(page)) %}
  - [{{ page.title }}]({{ page.url }})
{% endfor %}
