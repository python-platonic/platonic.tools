---
title: Queue
---

- One or more processes, **Sender(s)**, are dispatching messages to a Queue. One or more processes, **Receiver(s)**, are listening to the queue and processing every message.
- **Receiver** ought to acknowledge every successfully processed message within a specific time period, called **Visibility Timeout**.
- If **Receiver** fails to do so, the message is sent to that or another **Receiver** again, to make sure it is processed.

<iframe style="border:none" width="800" height="450" src="https://whimsical.com/embed/9FrduJ8TXTaKaQH33Sjiya"></iframe>

## Use Cases

- An API handler submits tasks to convert video files which are served by multiple workers.
- A periodic job submits orders to generate heavy PDF reports, which are served by multiple serverless functions.

## Backends

<table>
    <thead>
        <tr>
            <th rowspan="2"></th>
            <th rowspan="2" style="vertical-align: middle">Simple</th>
            <th colspan="2" align="center">
                <a href="/backends/sqs/">SQS</a>
            </th>
        </tr>
        <tr>
            <th>Standard</th>
            <th>FIFO</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>
                <a href="#delivery-guarantees">Delivery Guarantees</a>
            </th>
            <td>=1</td>
            <td>⩾1</td>
            <td>=1</td>
        </tr>
        <tr>
            <th>
                <a href="#order-preservation">Order Preserved</a>
            </th>
            <td>✔</td>
            <td>❌</td>
            <td>✔</td>
        </tr>
        <tr>
            <th colspan="4" align="center">Communicate</th>
        </tr>
        <tr>
            <th>Between Threads</th>
            <td>✔</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <th>Between Processes</th>
            <td>❌</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <th>Between Machines</th>
            <td>❌</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
    </tbody>
</table>
