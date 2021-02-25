from typing import Any, List, Iterable
from pydoc import locate

from mkdocs_macros.plugin import MacrosPlugin
import dataclasses


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


def define_env(env: MacrosPlugin):
    """Hook function."""
    env.macro(locate, name='import')
    env.filter(print_dataclass)
