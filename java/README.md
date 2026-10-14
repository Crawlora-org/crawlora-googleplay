# Crawlora Google Play API client for Java

The official Java client for Crawlora's hosted Google Play API. It exposes 11 endpoints covering app search, details, reviews, ratings, permissions, data safety, charts, similar apps, and developers. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-googleplay</artifactId>
  <version>0.1.2</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-java-console) to get an API key.

```java
import net.crawlora.googleplay.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.search(Map.ofEntries(Map.entry("term", "podcast player")));
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported Google Play API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-googleplay/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-googleplay)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=googleplay-java-api-docs)
