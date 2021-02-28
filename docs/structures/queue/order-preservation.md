---
title: Order Preservation
---

- If the backend guarantees order, the messages are received in the precise order in which they were sent. For example, if message `M1` was sent before `M2`, you will not receive `M2` first and then `M1`.
- If the backend does not guarantee order, you very well may receive `M2` before `M1`.

If backend is a multi-tenant distributed system, order preservation may require extra effort and cause performance penalty. That is why, say, SQS provides this property as an optional feature for extra pay.
