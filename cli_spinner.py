"""Spinners and progress bars that degrade gracefully when not a TTY."""

from __future__ import annotations

__all__ = ["cliSpinner"]


def cliSpinner(value):
    """Spinners and progress bars that degrade gracefully when not a TTY."""
    if value is None:
        raise ValueError("value must not be None")
    return value
