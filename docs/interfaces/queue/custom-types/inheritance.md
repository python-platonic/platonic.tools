---
title: Via inheritance
position: 1
---

## As example

```python
{% include "_generated/custom-types/test_inheritance.py" %}
```

## Pro

- Easy to implement
- mypy compatible

## Contra

- PyCharm is unhappy:
  > Signature of method 'SpellSender.serialize_value()' does not match signature of base method in class 'Sender' 
- Subclassing is required
- Type conversion is tightly coupled with the data structure you're using it with, and cannot be reused

!!! warning
    That is why this method is DISCOURAGED. Use it at your own risk. Click **Next** to see an alternative.

