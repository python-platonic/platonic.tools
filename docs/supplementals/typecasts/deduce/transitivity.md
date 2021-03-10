---
title: By Transitivity
---

!!! warning
    This one is not implemented yet. Is in plans though.

If conversions `casts[A, B]` and `casts[B, C]` are defined, they will be applied to a value sequentially to deduce a `casts[A, C]` conversion.


```python
import typecasts

c = typecasts.Typecasts()

c[int, str] = str
c[str, bytes] = str.encode

assert c[int, bytes](5) == b'5'
```
