---
title: generic-args
---

```shell
pip install generic-args
```

[This little library](https://github.com/python-platonic/generic-args) lets you to determine values of type args for generic classes.

```python
from typing import List
from generic_args import generic_type_args

generic_type_args(List[int])
# (<type 'int'>, )
```
