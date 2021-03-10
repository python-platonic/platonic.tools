import json
import operator
from typing import Iterable, Optional

import pydantic
import typecasts

from octadocs_python.get_object_name import get_object_name
from octadocs_python.get_object_path import get_object_path


class PythonObject(pydantic.BaseModel):
    """Any Python object."""

    label: str
    path: Optional[str]
    see_also: Optional[str]


class CastRow(pydantic.BaseModel):
    """Serialized typecast description."""

    source: PythonObject
    destination: PythonObject
    cast: PythonObject


def describe_python_object(obj) -> PythonObject:
    return PythonObject(
        label=get_object_name(obj),
        path=get_object_path(obj),
        see_also='',
    )


def serialize() -> Iterable[CastRow]:
    """Serialize."""
    for (source, destination), cast in typecasts.casts.items():
        yield CastRow(
            source=describe_python_object(source),
            destination=describe_python_object(destination),
            cast=describe_python_object(cast),
        )


def main() -> None:
    """Serialize typecasts.casts to YAML-LD."""
    serialized = map(
        operator.methodcaller('dict'),
        serialize(),
    )
    print(json.dumps(
        list(serialized),
        indent=4,
        ensure_ascii=False,
    ))


if __name__ == '__main__':
    main()
