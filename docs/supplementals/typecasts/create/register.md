---
title: With @register decorator
---

If the conversion function is hard to reflect as a lambda function, you can write it as a decorator.

```python
from typecasts import casts
import pydantic

@casts.register(pydantic.BaseModel, str)
def pydantic_to_json_string(instance: pydantic.BaseModel) -> str:
    """Convert Pydantic model instance to JSON string."""
    return instance.json()


class Robot(pydantic.BaseModel):
    """Robot."""
    
    name: str

robot = Robot(name='Jimbo')

assert casts[Robot, str](robot) == '{"name": "Jimbo"}'
```
