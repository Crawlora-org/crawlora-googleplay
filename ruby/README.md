# Crawlora Google Play API client for Ruby (`crawlora-googleplay`)

This Ruby gem calls Crawlora's hosted Google Play API at `https://api.crawlora.net/api/v1`. It exposes 11 endpoints covering app search, details, reviews, ratings, permissions, data safety, charts, similar apps, and developers; it does not call or scrape Google Play directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-googleplay"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/googleplay"

client = Crawlora::Googleplay::Client.new
result = client.request("googleplay-search", JSON.parse("{\"term\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 11 API operations.

```ruby
client = Crawlora::Googleplay::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Google Play API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-googleplay/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-googleplay) for account setup, the API operation reference, and release history.
