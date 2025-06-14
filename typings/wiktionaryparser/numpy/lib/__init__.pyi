"""
This type stub file was generated by pyright.
"""

from pathlib import Path
from typing import Any, IO, TypeAlias
from _typeshed import OpenBinaryMode, OpenTextMode

_Mode: TypeAlias = OpenBinaryMode | OpenTextMode
class DataSource:
    def __init__(self, /, destpath: Path | str | None = ...) -> None:
        ...
    
    def __del__(self, /) -> None:
        ...
    
    def abspath(self, /, path: str) -> str:
        ...
    
    def exists(self, /, path: str) -> bool:
        ...
    
    def open(self, /, path: str, mode: _Mode = ..., encoding: str | None = ..., newline: str | None = ...) -> IO[Any]:
        ...
    


class Repository(DataSource):
    def __init__(self, /, baseurl: str, destpath: str | None = ...) -> None:
        ...
    
    def listdir(self, /) -> list[str]:
        ...
    


def open(path: str, mode: _Mode = ..., destpath: str | None = ..., encoding: str | None = ..., newline: str | None = ...) -> IO[Any]:
    ...

