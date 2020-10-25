# Queue

FIFO Acknowledgement queue with:

* output (where you write things) 
* and input (where you read things from).

## Acknowledgement

Normally, acknowledgement queue is used to communicate tasks from one service to another. When the downstream service receives a message and processes it successfully, it must acknowledge the message, meaning deletion from the queue.

## Output Queue

::: platonic.queue.OutputQueue
    :docstring:
    :members: send send_many

## Input Queue

::: platonic.queue.InputQueue
    :docstring:
    :members: receive receive_with_timeout acknowledge acknowledgement

## Implementations

* [SQS](/sqs/)
