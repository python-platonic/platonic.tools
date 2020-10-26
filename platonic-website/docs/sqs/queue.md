# SQS: Queue

* Data structure: [Queue](/structures/queue/)
* Backend: [SQS](/sqs/)

Amazon Simple Queue Service is the default choice to communicate data between services on AWS. It comes in two flavors: Standard and FIFO.

|          | Standard       | FIFO         |
| ---      | ---            | ---          |
| Delivery | At Least Once  | Exactly Once |
| Order    | Not guaranteed | Guaranteed   |
| Price    | Lower :)       | Higher :(    |

**Visibility timeout** is an important parameter of an SQS queue: it defines how much time the receiver has to process the message and acknowledge it. If the receiver fails to acknowledge the message before timeout expires, the message becomes available for processing again, and thus can be processed multiple times. 

## Pricing

!!! todo
    Interactivity:
    
    * idyll-lang.org
    * tangle.js
    * Wolfram widgets
    * https://github.com/explorableexplanations/explorableexplanations.github.io/blob/master/-data/explorables.csv
    * ...?

## Creating a queue

!!! note
    `platonic-sqs` is not responsible for creating the queue for you.

!!! todo
    At least some help or links are necessary.

You can create queues manually in AWS console, but an automated solution like Terraform, AWS CDK, or AWS Cloudformation is recommended.

Whatever solution you choose, `platonic-sqs` will require the unique identifier — the URL — of your queue.

## Sending a message

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
