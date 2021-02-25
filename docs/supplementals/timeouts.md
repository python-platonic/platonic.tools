---
title: platonic.timeout
---

These classes are included in the main `platonic` library.

## Code

::: platonic.timeout.ConstantTimeout
    :docstring:
    :members:

::: platonic.timeout.InfiniteTimeout
    :docstring:
    :members:

## Usage example

```python
import time
from platonic.timeout import ConstantTimeout
from datetime import timedelta

timeout = ConstantTimeout(period=timedelta(minutes=5))

with timeout.timer() as timer:
    time.sleep(30)
    print(int(round(timer.remaining_seconds)))

# >>> 270
```

*(This script should be runnable as-is.)*


