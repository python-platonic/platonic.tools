---
title: typecasts
---

{{ query('
  SELECT * WHERE {
    GRAPH <local:supplementals/typecasts/defaults.yaml> {
      ?s ?p ?o .
    }
  }')
}}

This is a repository of type conversions. `typecasts` knows how to convert value of one type into a value of another.

```python
from typecasts import casts

casts[int, str](5)
# '5'

casts[bytes, str](b'boo')
# 'boo'

import pydantic
class Robot(pydantic.BaseModel):
    """Robot."""
    name: str

casts[Robot, str](Robot(name='Jazz'))
# {"name": "Jazz"}
```

## Why?

Every `platonic` data structure converts the application-specific data types (`int`, `bool`, `class Robot`) into backend-specific data types (JSON strings, byte sequences) — and vice versa.

Writing the conversion code in each and every data structure would be boilerplate, hard to maintain and customize.

## Installation

```bash
pip install typecasts
```

(However, `typecasts` will be installed as dependency for `platonic`.)

## Create your own typecast

### As a λ

```python
casts[int, bool] = lambda v: v != 0
```

`casts` is just a `dict`, so you can plainly add your own conversion (and overwrite conversions configured before) using simple `dict` syntax.

### As a decorator

If the conversion function is hard to reflect as a lambda function, you can write it as a decorator.

```python
from typecasts import casts
import pydantic

@casts.register(pydantic.BaseModel, str)
def pydantic_to_json_string(instance: pydantic.BaseModel) -> str:
    """Convert Pydantic model instance to JSON string."""
    return instance.json()
```

## Heuristics

You do not need to explicitly define every possible type conversion. Some of them can be implicitly deduced.

### By inheritance

If the `casts[ParentClass, str]` conversion is defined, it will be reused for `casts[ChildClass, str]` if `ChildClass` is a subclass of `ParentClass`. That is justified by Liskov Substitution Principle (LSP).

### By transitivity

!!! warning
    This one is not implemented yet. I think it makes the `casts` repository into a *category*.

If conversions `casts[A, B]` and `casts[B, C]` are defined, they will be applied sequentially to deduce a `casts[A, C]` conversion.

## Parametric conversion

Best explained on an example:

```python
@casts.register(str, SubclassOf[pydantic.BaseModel])
def json_string_to_pydantic(
    serialized_value: str,
    destination_type: Type[PydanticModel],
) -> PydanticModel:
    """Convert a JSON representation of a Pydantic model into model instance."""
    return pydantic.parse_raw_as(destination_type, serialized_value)
```

If the destination type is specified as `SubclassOf[SomeType]`, the conversion function gets the requested destination type as second parameter. Using `partial`, it will be converted into a one-argument conversion function and that will be available as, say, `casts[str, Robot]` for you to use.

## Custom typecasts repositories

`typecasts.casts` is the default repository of typecasts, but you can always create your own like this:

```python
from typecasts import Typecasts

your_casts = Typecasts()
```
