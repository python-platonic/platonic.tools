import dataclasses
from typing import List, Iterable


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
