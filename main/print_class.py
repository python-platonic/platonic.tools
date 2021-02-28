import abc
import dataclasses
import inspect
import textwrap
from main.cached_property import cached_property
from typing import Optional, List

from main import md


def class_name(python_class: type) -> str:
    """Return class name."""
    return python_class.__name__


@dataclasses.dataclass()
class ClassMember:
    """Member."""

    name: str
    method: callable
    header_level: int = 3

    @property
    def docstring(self) -> str:
        """Method docstring."""
        return textwrap.dedent(self.method.__doc__)

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

    @cached_property
    def header(self):
        """Construct the header."""
        return f'{self.name}{self.signature}'

    def __iter__(self):
        """Construct Markdown description of the member."""
        yield md.Header(self.header, level=self.header_level)
        yield md.Quote(self.docstring)

    def __str__(self):
        return str(md.Fragment(list(self)))


@dataclasses.dataclass(repr=False)
class PrintClass:
    """Print class."""

    cls: type
    header_level: int = 2

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

    @cached_property
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
            ClassMember(
                name=name,
                method=method,
                header_level=self.header_level + 1,
            )
            for name, method in members
        ]

    @property
    def superclasses(self) -> Optional[md.List]:
        """List of superclasses."""
        bases = self.cls.__bases__

        if bases:
            return md.List(map(class_name, bases))

    @cached_property
    def modifier(self) -> Optional[md.InlineCode]:
        """Class modifier."""
        if issubclass(self.cls, abc.ABC):
            return md.InlineCode('abstract')

        return None

    def __iter__(self):
        """Construct Markdown fragment for class documentation."""
        header = f'class {self.name}'
        if self.modifier is not None:
            header = f'{self.modifier} {header}'

        yield md.Header(header, level=self.header_level)

        if self.docstring:
            yield md.Quote(self.docstring)

        yield from self.members

    def __str__(self):
        """Render as string."""
        return str(md.Fragment(list(self)))
