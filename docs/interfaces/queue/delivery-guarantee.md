---
title: Delivery Guarantees
---

Different Queue backends may provide different delivery guarantees.

| Code | Name          | Definition |
| ---  | ---           | ---        |
| ⩽1   | At most Once  | Messages will not be duplicated, but may be lost.
| =1   | Exactly Once  | Messages will be neither lost nor duplicated. You will receive every distinct message exactly once.
| ⩾1   | At Least Once | Messages will not be lost, but can be duplicated.

[This StackOverflow question](https://stackoverflow.com/q/44204973) has a few good answers explaining these concepts.
