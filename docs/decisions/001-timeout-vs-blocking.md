---
title: Timeout vs Blocking operations
---

## Context

While using `platonic-sqs` in real development practice, I found out that it lacks a number of important features which a working developer often needs. These are:

- `SQSReceiver.iterate_with_timeout(timeout=...)` to continue reading messages from the queue until, while waiting for the next message, timeout strikes;
- `SQSReceiver[:...]` to iterate over the given number of messages and avoid fetching messages you will never need;
- `SQSReceiver.acknowledge_many(...)` to delete multiple messages from the queue;
- `with SQSReceiver.receive_batch() as batch` to work with as a context manager which will automatically acknowledge the processed messages.

While adding new operations to the class, we have to avoid overly cluttering it. The interface of the class should stay concise and minimalistic.

How do we organize the interface of the platonic `Queue` class and its derivatives to solve this issue?

## Decision

Every operation which entails reading from the queue supports two variants: timeout operation and blocking operation. Examples:

|     | Blocking | Timeout |
| --- | --- | --- |
| One | `receive()` | `receive_with_timeout()` | 
| Many | `__iter__()` | `iterate_with_timeout()` | 

But in fact, the blocking operations can be represented as timeout operations with `timeout=INFINITY`. To reduce the number of operations, I suggest that we create a new class-level parameter named `timeout` which by default will have a value of positive infinity, but will support `timedelta()` values too.

## Consequences

This will mean we will easily iterate over a queue using the iterator protocol - this is both idiomatic and will support timeouts.

I believe that, in most cases, when having created a queue, people will only do one or two `.receive()` or `__iter__()` operations on it. Thus, if we are to provide timeout as the queue class parameter, we are likely not going to make their code more complicated.
