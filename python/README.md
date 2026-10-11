# crawlora-googleplay — Google Play API client for Python

Python client for Crawlora's hosted Google Play API. It exposes 11 API endpoints covering app search, details, reviews, ratings, permissions, data safety, charts, similar apps, and developers. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-python-homepage); the package does not run a browser or scrape
Google Play locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
Google Play or its owners.

## Install

```sh
python -m pip install crawlora-googleplay
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_googleplay import GooglePlayClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with GooglePlayClient(api_key=api_key) as client:
    result_1 = client.search(term='podcast player')
    print(result_1)
    result_2 = client.app(app_id='com.spotify.music')
    print(result_2)
```

The package also exports `Client` as an alias for `GooglePlayClient`. Operation
methods are available directly in snake_case and through the `googleplay`
group. The async package client is `AsyncGooglePlayClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-googleplay/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-googleplay/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_googleplay import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.search(term='podcast player')
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-googleplay/blob/main/examples/python.py) for a complete usage example.

## Supported Google Play API endpoints

This package exposes every route below through direct snake_case methods and the `googleplay` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-googleplay/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/googleplay/app` | `googleplay-app` | Retrieve full Google Play app details |
| `GET` | `/googleplay/categories` | `googleplay-categories` | Retrieve Google Play app categories |
| `GET` | `/googleplay/datasafety` | `googleplay-datasafety` | Retrieve Google Play data safety details |
| `GET` | `/googleplay/developer/{dev_id}` | `googleplay-developer` | Retrieve apps by Google Play developer |
| `GET` | `/googleplay/list` | `googleplay-list` | Retrieve apps from a Google Play top collection |
| `GET` | `/googleplay/permissions` | `googleplay-permissions` | Retrieve Google Play app permissions |
| `GET` | `/googleplay/ratings` | `googleplay-ratings` | Get Google Play ratings by device |
| `GET` | `/googleplay/reviews` | `googleplay-reviews` | Retrieve Google Play reviews |
| `GET` | `/googleplay/search` | `googleplay-search` | Search Google Play |
| `GET` | `/googleplay/similar` | `googleplay-similar` | Retrieve similar Google Play apps |
| `GET` | `/googleplay/suggest/{term}` | `googleplay-suggest` | Retrieve Google Play query suggestions |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
