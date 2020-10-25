# SQS: Queue

* Data structure: [Queue](structures/queue.md)
* Backend: [SQS](sqs/)

> **TODO:** Make this somewhat human readable and more generic

## Send a message

```pycon
>>> from platonic.sqs.queue import SQSOutputQueue


>>> class ControlQueue(SQSOutputQueue[int]):
...     """Send encoded commands to a Martian rover via SQS."""

>>> output = ControlQueue(url=...)
>>> output.send(15)
>>> output.send_many([1, 1, 2, 3, 5, 8, 13])
```

## Receive and acknowledge a message

```pycon
>>> from platonic.sqs.queue import SQSInputQueue

>>> class RoverQueue(SQSInputQueue[int]):
...     """Receive the commands from Earth."""

>>> input = RoverQueue(url=...)

# If the queue is empty, this call with block until there is a message.
>>> cmd = input.receive()
>>> cmd.value
15

# And now this must be acknowledged.
>>> input.acknowledge(cmd)

# This call will raise MessageReceiveTimeout exception if nothing appears at
# the queue during the specified time frame.
>>> cmd = input.receive_with_timeout(timeout=5)
>>> cmd.value
1
>>> input.acknowledge(cmd)

# Or, you can do differently:
>>> for message in input:
...     with input.acknowledgement(message):
...         print(message.value)
1
2
...
```
