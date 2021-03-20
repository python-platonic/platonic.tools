---
title: SQSSender
---

{% set sender_path = 'platonic.sqs.queue.SQSSender' %}
{% set sender = import(sender_path) %}

### {{ sender_path }}

> {{ sender.__doc__ }}

{{ sender | print_dataclass }}
