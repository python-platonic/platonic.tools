---
title: typecasts
---

```shell
pip install typecasts
```

Typecasts provides a centralized repository of type conversions. Given two types - source type and destination type - it knows how to convert a value of the first into a value of the latter.

## Example

```python
from typecasts import casts
from pydantic import BaseModel

class Robot(BaseModel):
    """Robot."""

    name: str

robot = Robot(name='Chuzz')

assert casts[Robot, str](robot) == '{"name": "Chuzz"}'
```

## Why?

Every `platonic` data structure converts the application-specific data types (`int`, `bool`, `class Robot`) into backend-specific data types (usually JSON strings or byte sequences) — and vice versa.

Writing the conversion code in each and every data structure would be boilerplate, hard to maintain and customize.
