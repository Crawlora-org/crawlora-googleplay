# Google Play client usage

The `@crawlora-org/googleplay` and `crawlora-googleplay` packages call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Google Play locally; Crawlora is independent from and not endorsed by Google Play or its owners.

The package tracks the public API contract revision `sha256:12d5e7ff8b42944aabf39135226e7597a113d0dd6860efc8d43f4d8a9a960eef` bundled with release `0.1.1`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 11 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `googleplay` group and the generated `Client` alias.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| Method | Endpoint | Parameters | Description |
| --- | --- | --- | --- |
| `app` / `app` | `GET /googleplay/app` | `app_id` (query, required), `country` (query, optional), `lang` (query, optional) | Retrieve full Google Play app details |
| `categories` / `categories` | `GET /googleplay/categories` | `country` (query, optional), `lang` (query, optional) | Retrieve Google Play app categories |
| `datasafety` / `datasafety` | `GET /googleplay/datasafety` | `app_id` (query, required), `lang` (query, optional) | Retrieve Google Play data safety details |
| `developer` / `developer` | `GET /googleplay/developer/{dev_id}` | `dev_id` (path, required), `num` (query, optional), `country` (query, optional), `lang` (query, optional), `full_detail` (query, optional) | Retrieve apps by Google Play developer |
| `list` / `list` | `GET /googleplay/list` | `collection` (query, optional; values: `TOP_FREE`, `TOP_PAID`, `GROSSING`, `NEW_FREE`, `NEW_PAID`), `category` (query, optional), `device` (query, optional; values: `phone`, `tablet`, `tv`, `chromebook`, `watch`, `xr`, `car`), `age` (query, optional), `num` (query, optional), `country` (query, optional), `lang` (query, optional), `full_detail` (query, optional) | Retrieve apps from a Google Play top collection |
| `permissions` / `permissions` | `GET /googleplay/permissions` | `app_id` (query, required), `country` (query, optional), `lang` (query, optional), `short` (query, optional) | Retrieve Google Play app permissions |
| `ratings` / `ratings` | `GET /googleplay/ratings` | `app_id` (query, required), `country` (query, optional), `lang` (query, optional) | Get Google Play ratings by device |
| `reviews` / `reviews` | `GET /googleplay/reviews` | `app_id` (query, required), `sort` (query, optional; values: `helpfulness`, `newest`, `rating`), `num` (query, optional), `country` (query, optional), `lang` (query, optional), `paginate` (query, optional), `next_pagination_token` (query, optional) | Retrieve Google Play reviews |
| `search` / `search` | `GET /googleplay/search` | `term` (query, required), `num` (query, optional), `country` (query, optional), `lang` (query, optional), `full_detail` (query, optional), `price` (query, optional; values: `all`, `free`, `paid`) | Search Google Play |
| `similar` / `similar` | `GET /googleplay/similar` | `app_id` (query, required), `num` (query, optional), `country` (query, optional), `lang` (query, optional), `full_detail` (query, optional) | Retrieve similar Google Play apps |
| `suggest` / `suggest` | `GET /googleplay/suggest/{term}` | `term` (path, required), `country` (query, optional), `lang` (query, optional) | Retrieve Google Play query suggestions |

## Client forms

- JavaScript: import `GooglePlayClient` (also exported as `Client`) from `@crawlora-org/googleplay`; use `new GooglePlayClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `GooglePlayClient` (also exported as `Client`) from `crawlora_googleplay`; use `with GooglePlayClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncGooglePlayClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
