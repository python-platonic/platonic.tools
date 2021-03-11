---
title: Acknowledge
position: 99
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

incoming_numbers.acknowledge(cmd)
```

::: platonic.sqs.queue.SQSReceiver
    :members: acknowledge acknowledge_many
