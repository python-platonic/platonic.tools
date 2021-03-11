---
title: Send a message
---

```python
from platonic.sqs.queue import SQSSender

numbers_out = SQSSender[int](
    url='{{ sqs_queue_url }}',
)

numbers_out.send(15)
numbers_out.send_many([1, 1, 2, 3, 5, 8, 13])
```


::: platonic.sqs.queue.SQSSender
    :members: send
