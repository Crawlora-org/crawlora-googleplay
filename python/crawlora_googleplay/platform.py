"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class GooglePlayClient(CrawloraClient):
    """Synchronous Google Play API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-googleplay-python/0.1.1')
        super().__init__(*args, **kwargs)

    def app(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('googleplay-app', params, response_type=response_type, timeout=timeout, headers=headers)

    def categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('googleplay-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def datasafety(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('googleplay-datasafety', params, response_type=response_type, timeout=timeout, headers=headers)

    def developer(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('googleplay-developer', params, response_type=response_type, timeout=timeout, headers=headers)

    def list(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('googleplay-list', params, response_type=response_type, timeout=timeout, headers=headers)

    def permissions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('googleplay-permissions', params, response_type=response_type, timeout=timeout, headers=headers)

    def ratings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('googleplay-ratings', params, response_type=response_type, timeout=timeout, headers=headers)

    def reviews(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('googleplay-reviews', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('googleplay-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def similar(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('googleplay-similar', params, response_type=response_type, timeout=timeout, headers=headers)

    def suggest(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('googleplay-suggest', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncGooglePlayClient(AsyncCrawloraClient):
    """Asynchronous Google Play API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-googleplay-python/0.1.1')
        super().__init__(*args, **kwargs)

    async def app(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('googleplay-app', params, response_type=response_type, timeout=timeout, headers=headers)

    async def categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('googleplay-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def datasafety(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('googleplay-datasafety', params, response_type=response_type, timeout=timeout, headers=headers)

    async def developer(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('googleplay-developer', params, response_type=response_type, timeout=timeout, headers=headers)

    async def list(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('googleplay-list', params, response_type=response_type, timeout=timeout, headers=headers)

    async def permissions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('googleplay-permissions', params, response_type=response_type, timeout=timeout, headers=headers)

    async def ratings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('googleplay-ratings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def reviews(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('googleplay-reviews', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('googleplay-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def similar(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('googleplay-similar', params, response_type=response_type, timeout=timeout, headers=headers)

    async def suggest(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('googleplay-suggest', params, response_type=response_type, timeout=timeout, headers=headers)
