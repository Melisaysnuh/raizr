"""
This type stub file was generated by pyright.
"""

from ctypes import Structure, Union, c_char, c_long, c_short, c_ulong
from ctypes.wintypes import BOOL, DWORD, LPVOID, WCHAR, WORD
from typing import TYPE_CHECKING

STD_INPUT_HANDLE = ...
STD_OUTPUT_HANDLE = ...
STD_ERROR_HANDLE = ...
class COORD(Structure):
    """
    Struct in wincon.h
    http://msdn.microsoft.com/en-us/library/windows/desktop/ms682119(v=vs.85).aspx
    """
    if TYPE_CHECKING:
        X: int
        Y: int
        ...
    _fields_ = ...
    def __repr__(self) -> str:
        ...
    


class UNICODE_OR_ASCII(Union):
    if TYPE_CHECKING:
        AsciiChar: bytes
        UnicodeChar: str
        ...
    _fields_ = ...


class KEY_EVENT_RECORD(Structure):
    """
    http://msdn.microsoft.com/en-us/library/windows/desktop/ms684166(v=vs.85).aspx
    """
    if TYPE_CHECKING:
        KeyDown: int
        RepeatCount: int
        VirtualKeyCode: int
        VirtualScanCode: int
        uChar: UNICODE_OR_ASCII
        ControlKeyState: int
        ...
    _fields_ = ...


class MOUSE_EVENT_RECORD(Structure):
    """
    http://msdn.microsoft.com/en-us/library/windows/desktop/ms684239(v=vs.85).aspx
    """
    if TYPE_CHECKING:
        MousePosition: COORD
        ButtonState: int
        ControlKeyState: int
        EventFlags: int
        ...
    _fields_ = ...


class WINDOW_BUFFER_SIZE_RECORD(Structure):
    """
    http://msdn.microsoft.com/en-us/library/windows/desktop/ms687093(v=vs.85).aspx
    """
    if TYPE_CHECKING:
        Size: COORD
        ...
    _fields_ = ...


class MENU_EVENT_RECORD(Structure):
    """
    http://msdn.microsoft.com/en-us/library/windows/desktop/ms684213(v=vs.85).aspx
    """
    if TYPE_CHECKING:
        CommandId: int
        ...
    _fields_ = ...


class FOCUS_EVENT_RECORD(Structure):
    """
    http://msdn.microsoft.com/en-us/library/windows/desktop/ms683149(v=vs.85).aspx
    """
    if TYPE_CHECKING:
        SetFocus: int
        ...
    _fields_ = ...


class EVENT_RECORD(Union):
    if TYPE_CHECKING:
        KeyEvent: KEY_EVENT_RECORD
        MouseEvent: MOUSE_EVENT_RECORD
        WindowBufferSizeEvent: WINDOW_BUFFER_SIZE_RECORD
        MenuEvent: MENU_EVENT_RECORD
        FocusEvent: FOCUS_EVENT_RECORD
        ...
    _fields_ = ...


class INPUT_RECORD(Structure):
    """
    http://msdn.microsoft.com/en-us/library/windows/desktop/ms683499(v=vs.85).aspx
    """
    if TYPE_CHECKING:
        EventType: int
        Event: EVENT_RECORD
        ...
    _fields_ = ...


EventTypes = ...
class SMALL_RECT(Structure):
    """struct in wincon.h."""
    if TYPE_CHECKING:
        Left: int
        Top: int
        Right: int
        Bottom: int
        ...
    _fields_ = ...


class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    """struct in wincon.h."""
    if TYPE_CHECKING:
        dwSize: COORD
        dwCursorPosition: COORD
        wAttributes: int
        srWindow: SMALL_RECT
        dwMaximumWindowSize: COORD
        ...
    _fields_ = ...
    def __repr__(self) -> str:
        ...
    


class SECURITY_ATTRIBUTES(Structure):
    """
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa379560(v=vs.85).aspx
    """
    if TYPE_CHECKING:
        nLength: int
        lpSecurityDescriptor: int
        bInheritHandle: int
        ...
    _fields_ = ...


