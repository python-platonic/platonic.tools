---
title: Timeout vs Blocking operations
---

## Context

### Iterate with timeout

While using `platonic-sqs` in real development practice, I found out that it lacks an important feature: a function named `SQSReceiver.iterate_with_timeout(timeout=...)` to continue reading messages from the queue until, while waiting for the next message, a timeout occurs.

This function we often had to implement ourselves, creating the boilerplate that I specifically tried to avoid by starting the whole `platonic` project. 

### Short vs Long polling

In current implementation, `receive()` and `__iter__()` are using the [ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) API call without `WaitTimeSeconds` parameter, which means they rely upon [short polling instead of long polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html).

Short polling means we only query a subset of SQS servers to optimize by performance. Since we repeat the call in cycle, we are likely to pay for a handful of empty receive events.

### Timeout length

Right now, we support providing `timeout` as `timedelta()` instance. We convert it to seconds count and then provide as `WaitTimeSeconds` parameter to the aforementioned `ReceiveMessage` call. But in fact, the max value of that parameter is `20`:

```
Value 50 for parameter WaitTimeSeconds is invalid. Reason: must be <= 0 and >= 20 if provided.
```

which is not properly handled in the library code.

### Interface structure

While adding new operations to the class, we have to avoid overly cluttering it. The interface of the class should stay concise and minimalistic. How do we organize the interface of the platonic `Queue` class and its derivatives to solve this issue?

## Decision

Every operation which entails reading from the queue supports two variants: timeout operation and blocking operation. Examples:

|     | Blocking | Timeout |
| --- | --- | --- |
| One | `receive()` | `receive_with_timeout()` | 
| Many | `__iter__()` | `iterate_with_timeout()` | 

But in fact, the blocking operations can be represented as timeout operations with `timeout=INFINITY`. To encapsulate timeout behavior, we are going to create a new `Timeout` class with a number of subclasses.

### Usage of Timeout class

```python
timeout = ConstantTimeout(timeout=timedelta(minutes=5))

with timeout.timer() as as timer:
    while timer.remaining_seconds > 0:
        ...  # do something
```

## Consequences

We will easily iterate over a queue using the iterator protocol - this is both idiomatic and will support timeouts.

I believe that, in most cases, when having created a queue, people will only care about blocking operations or about operations that timeout, not both at the same queue object.
