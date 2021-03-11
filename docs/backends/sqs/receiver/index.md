---
title: SQSReceiver
---

{% set receiver_path = 'platonic.sqs.queue.SQSReceiver' %}
{% set receiver = import(receiver_path) %}

### {{ receiver_path }}

> {{ receiver.__doc__ }}

{{ receiver | print_dataclass }}
