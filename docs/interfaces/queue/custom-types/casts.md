---
title: Via typecasts
position: 2
---

We will continue to use the `Spell` class described in the previous chapter.

The default internal type for SQS has `str` as its internal type. That means `SQSSender[Spell]` must know how to convert `Spell` to `str`, and `SQSReceiver[Spell]` must know how to convert `str` back to `Spell`. 

```python
import operator
from typecasts import casts
from platonic.sqs.queue import SQSSender


class Spell:
    """Magical spell."""

    def __init__(self, text: str) -> None:
        """Initialize."""
        self.text = text


casts[Spell, str] = operator.attrgetter('text')
casts[str, Spell] = Spell

SQSSender[Spell](
    url=...,
).send(Spell('bazinga!'))
```

Very simple, as you can see. Once you have declared the necessary `casts`, all Platonic data structures will know how to use your custom classes. 

Of course, in many cases you don't even need to do that because built-in classes or Pydantic models you're using are supported by `typecasts` by default.

