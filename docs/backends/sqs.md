# SQS/Queue

| Data structure              | Backend                            |
| ---                         | ---                                |
| [Queue](/structures/queue/) | [SQS](https://aws.amazon.com/sqs/) |

## Installation

```bash
pip install platonic-sqs
```

## What is SQS?

Amazon Simple Queue Service is the default choice to communicate data between services on AWS.

### Flavors

SQS comes in two flavors: [Standard](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html) and [FIFO](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html).

|          | Standard       | FIFO         |
| ---      | ---            | ---          |
| [Delivery](/structures/queue/#delivery-guarantees) | ⩾1             | =1 |
| [Order preserved](/structures/queue/#order-preservation) | ❌ | ✔ |
| Pricing    | Lower 🙂   | Higher 🙁 |


### Visibility timeout

Defines how much time the receiver has to process the message and acknowledge it. If the receiver fails to acknowledge the message before timeout expires, the message becomes available for processing again.

## Creating a queue

Before using an SQS queue, you have to create it. `platonic` is not responsible for creating queues. Please use one of:

- [AWS Console](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.html)
- [Hashicorp Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/sqs_queue)
- AWS CLI, AWS CloudFormation, AWS CDK, ...

Whatever solution you choose, `platonic-sqs` will require **the unique identifier — the URL — of your queue**.

## Sending a message

```python
from platonic.sqs.queue import SQSSender


class NumbersOut(SQSSender[int]):
    """Sending out a stream of random numbers."""
    url = 'https://sqs.us-west-2.amazonaws.com/123456789012/queue-name'


numbers_out = NumbersOut()

numbers_out.send(15)
numbers_out.send_many([1, 1, 2, 3, 5, 8, 13])
```

## Receive and acknowledge a message

```python
from platonic.sqs.queue import SQSInputQueue

class RoverQueue(SQSInputQueue[int]):
    """Receive the commands from Earth."""

input = RoverQueue(url=...)

# If the queue is empty, this call with block until there is a message.
cmd = input.receive()
assert cmd.value == 15

# And now this must be acknowledged.
input.acknowledge(cmd)

# This call will raise MessageReceiveTimeout exception if nothing appears at
# the queue during the specified time frame.
cmd = input.receive_with_timeout(timeout=5)
assert cmd.value == 1
input.acknowledge(cmd)

# Or, you can do differently:
for message in input:
    with input.acknowledgement(message):
        print(message.value)
# 1
# 2
# ...
```
