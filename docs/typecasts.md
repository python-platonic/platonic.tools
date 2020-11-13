# Typecasts

## What is this?

Every `platonic` data structure converts the application-specific data types (`int`, `bool`, `class Robot`) into backend-specific data types (JSON strings, byte sequences) — and vice versa.

Writing the conversion code in each and every data structure would be boilerplate, hard to maintain and customize.

`typecasts` is a central repository where all such type conversions are managed. Once and only once you have to define that:

```python
from typecasts import casts

casts[int, str] = str
```

Now, every `typecasts`-aware structure will know how to convert `int` to `str`:

```pycon
from typecasts import casts

>>> casts[int, str](5)
# '5'
```

## Installation

```bash
pip install typecasts
```

(However, `typecasts` will be installed as dependency for `platonic`.)

## Decorator syntax

If the conversion function is hard to reflect as a lambda function, you can write it as a decorator.

```python
from typecasts import casts
import pydantic

@casts.register(pydantic.BaseModel, str)
def pydantic_to_json_string(instance: pydantic.BaseModel) -> str:
    """Convert Pydantic model instance to JSON string."""
    return instance.json()
```

## Conversion by inheritance

If the `casts[ParentClass, str]` conversion is defined, it will be reused for `casts[ChildClass, str]` if `ChildClass` is a subclass of `ParentClass`.

## Custom typecasts repositories

`typecasts.casts` is the default repository of typecasts, but you can always create your own like this:

```python
from typecasts import Typecasts

your_casts = Typecasts()
```
