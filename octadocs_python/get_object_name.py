import functools
import types

import typing
from typeclasses import typeclass

ObjectType = typing.TypeVar('ObjectType')


@typeclass(ObjectType)
def get_object_name(obj: ObjectType) -> str:
    """Get a name of a Python object."""
    return getattr(obj, '__name__', '')


@get_object_name.instance(types.FunctionType)
def _get_object_name_from_function(obj: types.FunctionType) -> str:
    return '{}.{}'.format(
        obj.__module__,
        obj.__name__,
    )


@get_object_name.instance(functools.partial)
def _get_object_name_from_functools_partial(obj: functools.partial) -> str:
    func = get_object_name(obj.func)

    args = f', '.join(map(str, obj.args))
    kwargs = f', '.join(
        '='.join(map(str, pair))
        for pair in obj.keywords.items()
    )

    arguments = ', '.join(filter(bool, [args, kwargs]))
    return f'functools.partial({func}, {arguments})'
