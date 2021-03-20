---
$id: Queue
title: Queue
$type: Interface
---

We use queues to communicate between applications, typically over a network. Queues provide certain guarantees to mitigate inevitable network glitches and code bugs.

- One or more processes, **Sender(s)**, are dispatching messages to a Queue. One or more processes, **Receiver(s)**, are listening to the queue and processing every message.
- **Receiver** ought to acknowledge every successfully processed message within a specific time period, called **Visibility Timeout**.
- If **Receiver** fails to do so, the message is sent to that or another **Receiver** again, to make sure it is processed.

<iframe style="border:none" width="800" height="450" src="https://whimsical.com/embed/9FrduJ8TXTaKaQH33Sjiya"></iframe>

## Use Cases

- An API handler submits tasks to convert video files which are served by multiple workers.
- A periodic job submits orders to generate heavy PDF reports, which are served by multiple serverless functions.
