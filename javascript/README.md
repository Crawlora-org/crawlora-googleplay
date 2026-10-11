# @crawlora-org/googleplay — Google Play API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Google Play API.
It exposes 11 API endpoints for app search, details, reviews, ratings, permissions, data safety, charts, similar apps, and developers through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-javascript-homepage). It does not run a browser or scrape Google Play locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Google Play or its owners.

## Install

```sh
npm install @crawlora-org/googleplay
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { GooglePlayClient } from "@crawlora-org/googleplay";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new GooglePlayClient({ apiKey });
const result1 = await client.search({ term: "podcast player" });
console.log(result1);
const result2 = await client.app({ app_id: "com.spotify.music" });
console.log(result2);
```

The client also exports `Client` as an alias for `GooglePlayClient`. Operation
methods are available directly in camelCase and through the `googleplay`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-googleplay/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-googleplay/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Google Play API endpoints

This package exposes each route below as a direct method and through the `googleplay` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-googleplay/blob/main/docs/usage.md) for complete input details.

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

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
