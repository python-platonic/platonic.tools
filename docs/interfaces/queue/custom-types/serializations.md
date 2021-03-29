---
title: Custom serializations
position: 5
---

## Problem

By default, when sending Pydantic models over the wire, `platonic-sqs` serializes them into JSON using built-in means of Pydantic library. What if you want to change that? For example, you need to do Base64 encoding of the JSON data.

## Solution: custom `internal_type`

```python
import base64
import pydantic
from typing import NewType
from typecasts import casts
from platonic.sqs.queue import SQSSender

Base64JSONString = NewType('Base64JSONString', str)

casts[pydantic.BaseModel, Base64JSONString] = lambda instance: base64.b64decode(
    instance.json().encode('ascii'),
)
...


class Spell(pydantic.BaseModel):
    """Magic spell."""
    
    text: str


SQSSender[Spell](
    internal_type=Base64JSONString,
    url=...,
).send(Spell(text='Ahalai-mahalai'))
```

## Pro

- By declaring explicit types, you improve the readability of your program, making it obvious to the reader that specifically Base64 encoded JSON (not just an arbitrary string) is what your application is sending over the wire.
- mypy and IDEs recognize that type, provide hints, point at errors.
- The conversion, once defined, is reusable.

## Contra

- I do not know of any. Do you?
