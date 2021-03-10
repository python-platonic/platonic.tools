---
title: With parameters
---

## Problem

Suppose you'd want to add a cast from `str` (presumably JSON encoded) to a Pydantic model. With plain model described in the previous chapters, that would require you to write quite a lot of boilerplate, like this:


```python
import functools
from typecasts import casts
import pydantic


class Robot(pydantic.BaseModel):
    """Robot."""
    
    name: str


class Dinosaur(pydantic.BaseModel):
    """Rrrrrrroarrrr."""
    
    species: str
    

casts[str, Robot] = functools.partial(pydantic.parse_raw_as, Robot)
casts[str, Dinosaur] = functools.partial(pydantic.parse_raw_as, Dinosaur)
...   # and so on, for each of your Pydantic models.
```

## Solution

Works like this:

```python
from typing import Type

import pydantic

from typecasts import casts
from typecasts.types import SubclassOf


@casts.register(str, SubclassOf[pydantic.BaseModel])
def json_string_to_pydantic(
    serialized_value: str,
    destination_type: Type[pydantic.BaseModel],
) -> pydantic.BaseModel:
    """Convert a JSON representation of a Pydantic model into model instance."""
    return pydantic.parse_raw_as(destination_type, serialized_value)

```

## In a nutshell

If the **destination type** of your typecast is a `SubclassOf[Something]`, then:

- this cast will be applicable when destination type is any subclass of `Something` including itself;
- the cast function will be provided with two arguments: the value to convert plus the destination type requested by the casts user.
