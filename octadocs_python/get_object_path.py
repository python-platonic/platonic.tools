"""
Get the full definition path to an object.

Based on: https://stackoverflow.com/q/2020014/1245471
"""

import functools
import inspect
import types
from typing import TypeVar, Optional, _GenericAlias, get_origin

import typing_inspect
from typeclasses import typeclass

ObjectType = TypeVar('ObjectType')


@typeclass(ObjectType)
def get_object_path(obj: ObjectType) -> str:
    """Get a name of a Python object."""
    object_class = getattr(obj, '__class__', None)

    qualified_name = getattr(obj, '__qualname__', None)
    if not qualified_name:
        qualified_name = getattr(object_class, '__qualname__', None)

    module_path = getattr(obj, '__module__', None)
    if not module_path:
        module_path = getattr(object_class, '__module__', None)

    return '.'.join((
        module_path,
        qualified_name,
    ))


@get_object_path.instance(types.FunctionType)
def _get_object_path_function(obj: types.FunctionType) -> Optional[str]:
    if typing_inspect.is_new_type(obj):
        return None

    return '.'.join((
        obj.__module__,
        obj.__qualname__,
    ))


@get_object_path.instance(functools.partial)
def _get_object_path_functools_partial(obj: functools.partial) -> str:
    return get_object_path(obj.func)


@get_object_path.instance(_GenericAlias)
def _get_object_name_generic_alias(obj: _GenericAlias) -> Optional[str]:
    return get_object_path(get_origin(obj))
