# Queue

`platonic` views queues as a method of communication between threads, processes, services, and systems with each other. Queue is a one-way communication medium: one system is sending messages, and the other is receiving them.

Messages are usually encapsulating units of work, tasks to run, pieces of data to process.

## Properties

Every queue is represented by two Python objects: `Sender` and `Receiver`. Obviously, you can use the first to send messages to queue and the latter to retrieve them.

* Order of messages is generally not guaranteed to be preserved;
* The same message should be delivered at least once (if the backend is feeling well),
* And (depending on the backend) the message may be delivered more than once.

## Sender

Only supports two operations:

::: platonic.queue.OutputQueue
    :members: send send_many

If you only have to send one message, naturally use `send()`. If you need to send multiple messages, `send_many()`, which accepts an iterable, may offer benefits in terms of performance and/or price, because it leverages low-level batch APIs the backend provides.

## Receiver

::: platonic.queue.InputQueue
    :docstring:
    :members: receive receive_with_timeout __iter__

`receive()` is a blocking call. If the queue is empty at the moment, it will block until a message arrives and thus keep your program wait for it.

`receive_with_timeout()` will either return a message from queue or, if it is empty, wait for specified number of seconds. If nothing is there - you will get an exception raised.

And finally, you can just iterate over the `Receiver` object and get all messages one by one.

### Acknowledgement

Sometimes, the receiver can receive the message but fail to successfully process it due to whatever reason you can imagine: bug in code, failed database instance, server restart, network glitch. That is why we require the receiver to **acknowledge** every message it has successfully processed, using one of the following methods. 

::: platonic.queue.InputQueue
    :docstring:
    :members: acknowledge acknowledgement
    
If message is not acknowledged, it will later reappear in the queue for the same (or another) receiver to process it again. That is how queues improve stability of our systems.

## Implementations

* [SQS](/sqs/queue/)
