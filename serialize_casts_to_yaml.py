import json
import operator
from typing import Iterable, Optional

import pydantic
import typecasts
import yaml

from octadocs_python.get_object_name import get_object_name
from octadocs_python.get_object_path import get_object_path

import strictyaml


class PythonObject(pydantic.BaseModel):
    """Any Python object."""

    label: str
    path: Optional[str] = None
    see_also: Optional[str] = pydantic.Field(None, alias='seeAlso')


class CastRow(pydantic.BaseModel):
    """Serialized typecast description."""

    source: PythonObject
    destination: PythonObject
    cast: PythonObject


def describe_python_object(obj) -> PythonObject:
    return PythonObject(
        label=get_object_name(obj),
        path=get_object_path(obj),
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
        operator.methodcaller('dict', by_alias=True, exclude_defaults=True),
        serialize(),
    )

    document = {
        '$context': {
            'casts': '$included',
            'meta': '$included',

            'seeAlso': 'rdfs:seeAlso',
            'label': 'rdfs:label',

            'cast': {
                '$type': 'PythonObject',
            },
            'source': {
                '$type': 'PythonObject',
            },
            'destination': {
                '$type': 'PythonObject',
            },
        },
        '$id': 'python://typecasts.casts',
        'casts': list(serialized),
    }

    # print(document['casts'][9])
    print(strictyaml.as_document(document).as_yaml())
    # print(yaml.dump(document))
    # print(json.dumps(document))


if __name__ == '__main__':
    main()
