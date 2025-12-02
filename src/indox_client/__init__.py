"""
Public package interface for indox-client.
"""

from .client import IndoxClient
from .docs import DocsClient
from .media import MediaClient
from .exceptions import IndoxClientError, IndoxHTTPError
from .version import __version__

__all__ = [
    "IndoxClient",
    "DocsClient",
    "MediaClient",
    "IndoxClientError",
    "IndoxHTTPError",
    "__version__",
]
