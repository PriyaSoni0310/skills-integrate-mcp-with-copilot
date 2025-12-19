"""Simple input validation helpers (starter).

This module provides a placeholder `sanitize_html` function using bleach.
Install `bleach` in requirements when implementing.
"""

from typing import Optional


def sanitize_html(value: Optional[str]) -> str:
    """Return a sanitized, safe HTML string. Replace with `bleach.clean` in production."""
    if not value:
        return ""
    # Placeholder: caller should install and use `bleach.clean`.
    # Example:
    # import bleach
    # return bleach.clean(value)
    return value.replace("<", "&lt;").replace(">", "&gt;")
