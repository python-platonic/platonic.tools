---
title: Custom typecasts repositories
---

`typecasts.casts` is the default repository of typecasts, but you can always create your own like this:

```python
from typecasts import Typecasts

your_casts = Typecasts()

your_casts[str, int] = ...
```
