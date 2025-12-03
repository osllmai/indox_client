"""
Public package interface for indox-client.
"""

from .client import IndoxClient, DEFAULT_DOCS_BASE_URL, DEFAULT_MEDIA_BASE_URL
from .docs import DocsClient
from .media import MediaClient
from .exceptions import IndoxClientError, IndoxHTTPError
from .version import __version__

__all__ = [
    "IndoxClient",
    "DEFAULT_DOCS_BASE_URL",
    "DEFAULT_MEDIA_BASE_URL",
    "DocsClient",
    "MediaClient",
    "IndoxClientError",
    "IndoxHTTPError",
    "__version__",
]
