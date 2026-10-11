# Google Play clients for Crawlora

Official Crawlora client packages for the hosted Google Play API. Access 11 API endpoints covering app search, details, reviews, ratings, permissions, data safety, charts, similar apps, and developers from JavaScript/TypeScript, Python, Go, Ruby, Java, and PHP. These clients call Crawlora's hosted API; they do not scrape Google Play locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Google Play or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/googleplay`](javascript/README.md)
- Python: [`crawlora-googleplay`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-googleplay`](go.mod)
- Ruby: [`crawlora-googleplay`](ruby/README.md)
- Java: [`net.crawlora:crawlora-googleplay:0.1.1`](java/README.md)
- PHP: [`crawlora/googleplay`](php/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The six language clients provide access to all 11 selected public Google Play API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
