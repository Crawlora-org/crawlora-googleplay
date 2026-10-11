"""Typed Google Play client for the Crawlora hosted API."""

from .platform import GooglePlayClient, AsyncGooglePlayClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = GooglePlayClient
AsyncClient = AsyncGooglePlayClient
__version__ = '0.1.1'
DISPLAY_NAME = 'Google Play'
PLATFORM = 'googleplay'
CONTRACT_REVISION = 'sha256:12d5e7ff8b42944aabf39135226e7597a113d0dd6860efc8d43f4d8a9a960eef'

__all__ = [
    "GooglePlayClient", "AsyncGooglePlayClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
