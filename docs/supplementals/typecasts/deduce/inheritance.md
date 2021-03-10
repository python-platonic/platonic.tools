---
title: By Inheritance
---

If the `casts[ParentClass, str]` conversion is defined, it will be reused for `casts[ChildClass, str]` if `ChildClass` is a subclass of `ParentClass`. That is justified by Liskov Substitution Principle (LSP).

A demonstration of this is provided at [@register decorator page](/supplementals/typecasts/create/register/).
