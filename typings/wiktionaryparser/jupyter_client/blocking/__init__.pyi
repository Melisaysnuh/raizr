"""
This type stub file was generated by pyright.
"""

import typing as t
from traitlets import Type
from ..channels import HBChannel, ZMQSocketChannel
from ..client import KernelClient, reqrep
from ..utils import run_sync

"""Implements a fully blocking kernel client.

Useful for test suites and blocking terminal interfaces.
"""
def wrapped(meth: t.Callable, channel: str) -> t.Callable:
    """Wrap a method on a channel and handle replies."""
    ...

class BlockingKernelClient(KernelClient):
    """A KernelClient with blocking APIs

    ``get_[channel]_msg()`` methods wait for and return messages on channels,
    raising :exc:`queue.Empty` if no message arrives within ``timeout`` seconds.
    """
    get_shell_msg = ...
    get_iopub_msg = ...
    get_stdin_msg = ...
    get_control_msg = ...
    wait_for_ready = ...
    shell_channel_class = ...
    iopub_channel_class = ...
    stdin_channel_class = ...
    hb_channel_class = ...
    control_channel_class = ...
    _recv_reply = ...
    execute = ...
    history = ...
    complete = ...
    inspect = ...
    kernel_info = ...
    comm_info = ...
    is_alive = ...
    execute_interactive = ...
    shutdown = ...


