import dataclasses
import inspect
import itertools
import textwrap
from pathlib import Path
from pydoc import locate
from typing import List, Iterable, Optional

import jinja2
import typing_inspect
from generic_args import generic_type_args
from mkdocs_macros.plugin import MacrosPlugin


def markdown_table_as_list(
    headers: List[str],
    rows: Iterable[Iterable[str]],
) -> str:
    """Create a Markdown table."""
    yield ' | '.join(headers)
    yield ' | '.join(' --- ' for _ in headers)

    for row in rows:
        yield ' | '.join(row)


def print_dataclass(cls) -> str:
    """Print dataclass as table."""
    return '\n'.join(markdown_table_as_list(
        headers=['Name', 'Type', 'Default', 'Description'],
        rows=[
            map(str, (
                field.name,
                field.type.__name__,
                field.default,
                field.metadata.get('__doc__', ''),
            ))
            for field in dataclasses.fields(cls)
        ]
    ))


@dataclasses.dataclass()
class ClassMember:
    """Member."""

    name: str
    method: callable

    @property
    def docstring(self) -> str:
        """Method docstring."""
        return self.method.__doc__

    @property
    def signature(self) -> inspect.Signature:
        """Method signature."""
        return inspect.signature(self.method)

    @property
    def printable_signature(self) -> str:
        """Pretty signature."""
        signature = self.signature
        return_annotation = signature.return_annotation

        signature = signature.replace(
            # return_annotation=inspect.Signature.empty,
        )

        return str(signature).replace(
            '->', '→',
        )

    @property
    def category(self) -> Optional[str]:
        """Member category."""
        if inspect.isabstract(self.method):
            return 'abstract'

        return None


@dataclasses.dataclass(init=False, repr=False)
class PrintClass:
    """Print class."""

    cls: type

    def __init__(self, cls: type) -> None:
        """Initialize the class."""
        self.cls = cls

    @property
    def object_path(self) -> str:
        """
        Full path to the object.

        Source: https://stackoverflow.com/a/55080445/1245471
        """
        return '.'.join((
            self.cls.__module__,
            self.cls.__qualname__,
        ))

    @property
    def name(self):
        return self.cls.__name__

    @property
    def docstring(self) -> str:
        """Docstring of the class."""
        return self.cls.__doc__

    @property
    def members(self) -> List[ClassMember]:
        """Return the class members."""
        members = inspect.getmembers(
            self.cls,
            predicate=lambda method: (
                inspect.ismethod(method) or
                inspect.isfunction(method)
            ),
        )

        members = [
            (name, method)
            for name, method in members
            if (
                not name.startswith('__')
                or name == '__init__'
            )
        ]

        return [
            ClassMember(name=name, method=method)
            for name, method in members
        ]

    def __str__(self):
        """Representation."""
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(Path(__file__).parent / 'templates'),
        )
        template = env.get_template('class.md')
        return template.render(this=self)

    @property
    def type_args(self):
        return list(generic_type_args(self.cls))

    # -------------------------------------------------------------------------

    def print_member(self, method_name, method) -> str:
        """Print the method."""
        signature = str(inspect.signature(method)).replace('->', '→')

        return textwrap.dedent(
            f'''
            ### `{method_name}{signature}`
            > {method.__doc__}
            '''
        )

    def print_members(self) -> str:
        """Print members of the class."""
        pairs = ...

        pairs = [
            (name, method)
            for name, method in pairs
            if (
                not name.startswith('__')
                or name == '__init__'
            )
        ]

        return '\n'.join(
            itertools.starmap(
                self.print_member,
                pairs,
            )
        )


def define_env(env: MacrosPlugin):
    """Hook function."""
    env.macro(locate, name='import')
    env.filter(print_dataclass)
    env.filter(PrintClass, name='print_class')
