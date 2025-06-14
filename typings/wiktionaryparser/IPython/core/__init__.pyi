"""
This type stub file was generated by pyright.
"""

import warnings
from IPython.core.getipython import get_ipython

"""A payload based version of page."""
def page(strng, start=..., screen_lines=..., pager_cmd=...): # -> None:
    """Print a string, piping through a pager.

    This version ignores the screen_lines and pager_cmd arguments and uses
    IPython's payload system instead.

    Parameters
    ----------
    strng : str or mime-dict
        Text to page, or a mime-type keyed dict of already formatted data.
    start : int
        Starting line at which to place the display.
    """
    ...

