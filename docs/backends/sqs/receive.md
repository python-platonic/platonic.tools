---
title: Receive a message
---

```python
from platonic.sqs.queue import SQSReceiver
from platonic.timeout import ConstantTimeout
from datetime import timedelta

incoming_numbers = SQSReceiver[int](
    url='{{ sqs_queue_url }}',
    # Thus we prevent the receiver from blocking forever if queue is empty
    timeout=ConstantTimeout(period=timedelta(minutes=3)),
)

# If the queue is empty, this call with block until there is a message.
cmd = incoming_numbers.receive()
assert cmd.value == 15
# Do complicated stuff with the value
print(cmd.value * 1234 + 5767)
```

!!! warning
    The message will **appear again** in the queue after visibility timeout expires, and you will receive it again, if you do not [acknowledge the message](/backends/sqs/acknowledge/) after successful processing.

::: platonic.sqs.queue.SQSReceiver
    :members: receive
