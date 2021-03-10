import functools
import types

import typing

import typing_inspect
from typeclasses import typeclass

ObjectType = typing.TypeVar('ObjectType')


@typeclass(ObjectType)
def get_object_name(obj: ObjectType) -> str:
    """Get a name of a Python object."""
    return getattr(obj, '__name__', '')


@get_object_name.instance(types.FunctionType)
def _get_object_name_from_function(obj: types.FunctionType) -> str:
    if typing_inspect.is_new_type(obj):
        # NewType is a function with __supertype__ attribute assigned to it.
        supertype = get_object_name(obj.__supertype__)
        return f'NewType {obj.__name__}({supertype})'

    # We only print the module in which function is. We do not print the whole
    # module path.
    module_name = obj.__module__.split('.')[-1]

    return '{}.{}'.format(
        module_name,
        obj.__qualname__,
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
