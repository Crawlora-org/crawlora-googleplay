"""Typed Google Play client for the Crawlora hosted API."""

from .platform import GooglePlayClient, AsyncGooglePlayClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = GooglePlayClient
AsyncClient = AsyncGooglePlayClient
__version__ = '0.1.2'
DISPLAY_NAME = 'Google Play'
PLATFORM = 'googleplay'
CONTRACT_REVISION = 'sha256:49b4b5e73d6e29cb250c945e2beb79d7022e97fbf223413435ee1a3a2e1e1ade'

__all__ = [
    "GooglePlayClient", "AsyncGooglePlayClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
