# Google Play API endpoint reference and client usage

This reference lists all 11 public Google Play API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/googleplay`, `crawlora-googleplay`, and `crawlora-googleplay` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Google Play locally; Crawlora is independent from and not endorsed by Google Play or its owners.

The package tracks the public API contract revision `sha256:49b4b5e73d6e29cb250c945e2beb79d7022e97fbf223413435ee1a3a2e1e1ade` bundled with release `0.1.2`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `googleplay`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `app` | `app` | `googleplay.app` | `GET /googleplay/app` | `app_id` (query, required), `country` (query, optional), `lang` (query, optional) | Retrieve full Google Play app details |
| `categories` | `categories` | `googleplay.categories` | `GET /googleplay/categories` | `country` (query, optional), `lang` (query, optional) | Retrieve Google Play app categories |
| `datasafety` | `datasafety` | `googleplay.datasafety` | `GET /googleplay/datasafety` | `app_id` (query, required), `lang` (query, optional) | Retrieve Google Play data safety details |
| `developer` | `developer` | `googleplay.developer` | `GET /googleplay/developer/{dev_id}` | `dev_id` (path, required), `num` (query, optional), `country` (query, optional), `lang` (query, optional), `full_detail` (query, optional) | Retrieve apps by Google Play developer |
| `list` | `list` | `googleplay.list` | `GET /googleplay/list` | `collection` (query, optional; values: `TOP_FREE`, `TOP_PAID`, `GROSSING`, `NEW_FREE`, `NEW_PAID`), `category` (query, optional), `device` (query, optional; values: `phone`, `tablet`, `tv`, `chromebook`, `watch`, `xr`, `car`), `age` (query, optional), `num` (query, optional), `country` (query, optional), `lang` (query, optional), `full_detail` (query, optional) | Retrieve apps from a Google Play top collection |
| `permissions` | `permissions` | `googleplay.permissions` | `GET /googleplay/permissions` | `app_id` (query, required), `country` (query, optional), `lang` (query, optional), `short` (query, optional) | Retrieve Google Play app permissions |
| `ratings` | `ratings` | `googleplay.ratings` | `GET /googleplay/ratings` | `app_id` (query, required), `country` (query, optional), `lang` (query, optional) | Get Google Play ratings by device |
| `reviews` | `reviews` | `googleplay.reviews` | `GET /googleplay/reviews` | `app_id` (query, required), `sort` (query, optional; values: `helpfulness`, `newest`, `rating`), `num` (query, optional), `country` (query, optional), `lang` (query, optional), `paginate` (query, optional), `next_pagination_token` (query, optional) | Retrieve Google Play reviews |
| `search` | `search` | `googleplay.search` | `GET /googleplay/search` | `term` (query, required), `num` (query, optional), `country` (query, optional), `lang` (query, optional), `full_detail` (query, optional), `price` (query, optional; values: `all`, `free`, `paid`) | Search Google Play |
| `similar` | `similar` | `googleplay.similar` | `GET /googleplay/similar` | `app_id` (query, required), `num` (query, optional), `country` (query, optional), `lang` (query, optional), `full_detail` (query, optional) | Retrieve similar Google Play apps |
| `suggest` | `suggest` | `googleplay.suggest` | `GET /googleplay/suggest/{term}` | `term` (path, required), `country` (query, optional), `lang` (query, optional) | Retrieve Google Play query suggestions |

## Client forms

- JavaScript: import `GooglePlayClient` (also exported as `Client`) from `@crawlora-org/googleplay`; use `new GooglePlayClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `GooglePlayClient` (also exported as `Client`) from `crawlora_googleplay`; use `with GooglePlayClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncGooglePlayClient`, used with `async with` and `await`.
- Rust: add `crawlora-googleplay` with Cargo; import `Client` and the generated operation parameter struct, then call `client.googleplay.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-googleplay/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
