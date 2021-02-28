from dataclasses import dataclass
from typing import Iterable, List


class Markdown:
    """Base class for every Markdown object."""

    def __add__(self, other: 'Markdown') -> 'Fragment':
        """Concatenate this Markdown object with another."""
        return Fragment(children=[self, other])


@dataclass
class Fragment(Markdown):
    """A concatenation of several Markdown objects."""

    children: List[Markdown]

    def __str__(self):
        """Render the whole tree."""
        return '\n'.join(map(str, self.children))


@dataclass
class List(Markdown):
    """Render a Markdown list."""

    items: Iterable[str]
    marker: str = '-'

    def __str__(self):
        """Render as string."""
        return '\n'.join(
            f'{self.marker} {list_item}'
            for list_item in self.items
        )


@dataclass
class Header(Markdown):
    """Render a Markdown header."""

    text: str
    level: int = 2

    def __str__(self):
        """Render the header."""
        prefix = '#' * self.level
        return f'{prefix} {self.text}'


@dataclass
class InlineCode(Markdown):
    """String of code inline."""

    text: str

    def __str__(self):
        """Render."""
        return f'`{self.text}`'


@dataclass
class Quote(Markdown):
    """Block quote."""

    text: str

    def __str__(self):
        """Render."""
        lines = self.text.split('\n')
        return ''.join(
            f'> {line}\n'
            for line in lines
        )


@dataclass
class Paragraph(Markdown):
    """Text paragraph."""

    text: str

    def __str__(self):
        return f'{self.text}\n'
