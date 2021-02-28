from pydoc import locate

from mkdocs_macros.plugin import MacrosPlugin

from main.print_class import PrintClass
from main.print_dataclass import print_dataclass


def define_env(env: MacrosPlugin):
    """Hook function."""
    env.macro(locate, name='import')
    env.filter(print_dataclass)
    env.filter(PrintClass, name='print_class')
