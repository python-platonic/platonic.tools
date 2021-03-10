---
title: As a λ
---

`casts` is just a `dict`, so you can plainly add your own conversion (and overwrite conversions configured before) using simple `dict` syntax.

```python
from typecasts import casts

casts[int, bool] = lambda v: v != 0

assert casts[int, bool](5) is True
```
