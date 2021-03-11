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

## Code

{% set receiver_path = 'platonic.sqs.queue.SQSReceiver' %}
{% set receiver = import(receiver_path) %}

### {{ receiver_path }}

> {{ receiver.__doc__ }}

{{ receiver | print_dataclass }}

---

{% set sender_path = 'platonic.sqs.queue.SQSSender' %}
{% set sender = import(sender_path) %}

### {{ sender_path }}

> {{ sender.__doc__ }}

{{ sender | print_dataclass }}
