---
title: Send many messages
---

```python
from platonic.sqs.queue import SQSSender

odd_numbers = SQSSender[int](
    url='{{ sqs_queue_url }}',
)

odd_numbers.send_many(
    range(start=1, stop=100, step=2),
)
```

::: platonic.sqs.queue.SQSSender
    :members: send_many
