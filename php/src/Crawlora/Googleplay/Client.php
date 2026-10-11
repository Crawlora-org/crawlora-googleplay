<?php

declare(strict_types=1);

namespace Crawlora\Googleplay;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'googleplay';
    public const VERSION = '0.1.1';
    public const OPERATION_COUNT = 11;
    public const OPERATION_IDS = ["googleplay-app", "googleplay-categories", "googleplay-datasafety", "googleplay-developer", "googleplay-list", "googleplay-permissions", "googleplay-ratings", "googleplay-reviews", "googleplay-search", "googleplay-similar", "googleplay-suggest"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"googleplay-app": {"bodyParam": null, "bodyRequired": false, "id": "googleplay-app", "method": "GET", "params": [{"description": "Google Play package name", "in": "query", "name": "app_id", "required": true, "type": "string", "x-example": "com.openai.chatgpt"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Two-letter language code", "in": "query", "name": "lang", "type": "string", "x-example": "en"}], "path": "/googleplay/app", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "app_id", "required": true, "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "googleplay-categories": {"bodyParam": null, "bodyRequired": false, "id": "googleplay-categories", "method": "GET", "params": [{"description": "Two-letter country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Two-letter language code", "in": "query", "name": "lang", "type": "string", "x-example": "en"}], "path": "/googleplay/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "googleplay-datasafety": {"bodyParam": null, "bodyRequired": false, "id": "googleplay-datasafety", "method": "GET", "params": [{"description": "Google Play app id", "in": "query", "name": "app_id", "required": true, "type": "string", "x-example": "com.openai.chatgpt"}, {"description": "Two-letter language code", "in": "query", "name": "lang", "type": "string", "x-example": "en"}], "path": "/googleplay/datasafety", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "app_id", "required": true, "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "googleplay-developer": {"bodyParam": null, "bodyRequired": false, "id": "googleplay-developer", "method": "GET", "params": [{"description": "Developer id or name", "in": "path", "name": "dev_id", "required": true, "type": "string", "x-example": "OpenAI"}, {"description": "Number of apps", "in": "query", "name": "num", "type": "integer", "x-example": 60}, {"description": "Two-letter country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Two-letter language code", "in": "query", "name": "lang", "type": "string", "x-example": "en"}, {"default": false, "description": "Resolve each app to full detail", "in": "query", "name": "full_detail", "type": "boolean"}], "path": "/googleplay/developer/{dev_id}", "pathParams": ["dev_id"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "num", "type": "integer"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}, {"in": "query", "name": "full_detail", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "googleplay-list": {"bodyParam": null, "bodyRequired": false, "id": "googleplay-list", "method": "GET", "params": [{"description": "Collection: TOP_FREE, TOP_PAID, GROSSING, NEW_FREE, NEW_PAID", "enum": ["TOP_FREE", "TOP_PAID", "GROSSING", "NEW_FREE", "NEW_PAID"], "in": "query", "name": "collection", "type": "string", "x-example": "TOP_FREE"}, {"description": "Category id", "in": "query", "name": "category", "type": "string", "x-example": "TOOLS"}, {"description": "Google Play device tab: phone, tablet, tv, chromebook, watch, xr, car", "enum": ["phone", "tablet", "tv", "chromebook", "watch", "xr", "car"], "in": "query", "name": "device", "type": "string", "x-example": "tablet"}, {"description": "Family age range", "in": "query", "name": "age", "type": "string", "x-example": "AGE_RANGE1"}, {"description": "Number of apps", "in": "query", "name": "num", "type": "integer", "x-example": 50}, {"description": "Two-letter country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Two-letter language code", "in": "query", "name": "lang", "type": "string", "x-example": "en"}, {"default": false, "description": "Resolve each app to full detail", "in": "query", "name": "full_detail", "type": "boolean"}], "path": "/googleplay/list", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["TOP_FREE", "TOP_PAID", "GROSSING", "NEW_FREE", "NEW_PAID"], "in": "query", "name": "collection", "type": "string"}, {"in": "query", "name": "category", "type": "string"}, {"enum": ["phone", "tablet", "tv", "chromebook", "watch", "xr", "car"], "in": "query", "name": "device", "type": "string"}, {"in": "query", "name": "age", "type": "string"}, {"in": "query", "name": "num", "type": "integer"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}, {"in": "query", "name": "full_detail", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "googleplay-permissions": {"bodyParam": null, "bodyRequired": false, "id": "googleplay-permissions", "method": "GET", "params": [{"description": "Google Play app id", "in": "query", "name": "app_id", "required": true, "type": "string", "x-example": "com.openai.chatgpt"}, {"description": "Two-letter country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Two-letter language code", "in": "query", "name": "lang", "type": "string", "x-example": "en"}, {"default": false, "description": "Return only permission names", "in": "query", "name": "short", "type": "boolean"}], "path": "/googleplay/permissions", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "app_id", "required": true, "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}, {"in": "query", "name": "short", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "googleplay-ratings": {"bodyParam": null, "bodyRequired": false, "id": "googleplay-ratings", "method": "GET", "params": [{"description": "Google Play package name", "in": "query", "name": "app_id", "required": true, "type": "string", "x-example": "com.openai.chatgpt"}, {"description": "Two-letter storefront country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Two-letter language code", "in": "query", "name": "lang", "type": "string", "x-example": "en"}], "path": "/googleplay/ratings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "app_id", "required": true, "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "googleplay-reviews": {"bodyParam": null, "bodyRequired": false, "id": "googleplay-reviews", "method": "GET", "params": [{"description": "Google Play app id", "in": "query", "name": "app_id", "required": true, "type": "string", "x-example": "com.openai.chatgpt"}, {"description": "Sort: helpfulness, newest, rating", "enum": ["helpfulness", "newest", "rating"], "in": "query", "name": "sort", "type": "string", "x-example": "newest"}, {"description": "Number of reviews", "in": "query", "name": "num", "type": "integer", "x-example": 100}, {"description": "Two-letter country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Two-letter language code", "in": "query", "name": "lang", "type": "string", "x-example": "en"}, {"default": false, "description": "Only fetch the requested page", "in": "query", "name": "paginate", "type": "boolean"}, {"description": "Token from a previous response", "in": "query", "name": "next_pagination_token", "type": "string"}], "path": "/googleplay/reviews", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "app_id", "required": true, "type": "string"}, {"enum": ["helpfulness", "newest", "rating"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "num", "type": "integer"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}, {"in": "query", "name": "paginate", "type": "boolean"}, {"in": "query", "name": "next_pagination_token", "type": "string"}], "security": ["ApiKeyAuth"]}, "googleplay-search": {"bodyParam": null, "bodyRequired": false, "id": "googleplay-search", "method": "GET", "params": [{"description": "Search term", "in": "query", "name": "term", "required": true, "type": "string", "x-example": "chatgpt"}, {"description": "Number of apps", "in": "query", "name": "num", "type": "integer", "x-example": 20}, {"description": "Two-letter country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Two-letter language code", "in": "query", "name": "lang", "type": "string", "x-example": "en"}, {"default": false, "description": "Resolve each app to full detail", "in": "query", "name": "full_detail", "type": "boolean"}, {"description": "Price filter: all, free, paid", "enum": ["all", "free", "paid"], "in": "query", "name": "price", "type": "string", "x-example": "all"}], "path": "/googleplay/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "term", "required": true, "type": "string"}, {"in": "query", "name": "num", "type": "integer"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}, {"in": "query", "name": "full_detail", "type": "boolean"}, {"enum": ["all", "free", "paid"], "in": "query", "name": "price", "type": "string"}], "security": ["ApiKeyAuth"]}, "googleplay-similar": {"bodyParam": null, "bodyRequired": false, "id": "googleplay-similar", "method": "GET", "params": [{"description": "Google Play app id", "in": "query", "name": "app_id", "required": true, "type": "string", "x-example": "com.openai.chatgpt"}, {"description": "Number of apps", "in": "query", "name": "num", "type": "integer", "x-example": 24}, {"description": "Two-letter country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Two-letter language code", "in": "query", "name": "lang", "type": "string", "x-example": "en"}, {"default": false, "description": "Resolve each app to full detail", "in": "query", "name": "full_detail", "type": "boolean"}], "path": "/googleplay/similar", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "app_id", "required": true, "type": "string"}, {"in": "query", "name": "num", "type": "integer"}, {"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}, {"in": "query", "name": "full_detail", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "googleplay-suggest": {"bodyParam": null, "bodyRequired": false, "id": "googleplay-suggest", "method": "GET", "params": [{"description": "Search term prefix", "in": "path", "name": "term", "required": true, "type": "string", "x-example": "chatg"}, {"description": "Two-letter country code", "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Two-letter language code", "in": "query", "name": "lang", "type": "string", "x-example": "en"}], "path": "/googleplay/suggest/{term}", "pathParams": ["term"], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country", "type": "string"}, {"in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-googleplay-php/0.1.1',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function app(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("googleplay-app", $params, $responseType);
    }
    public function categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("googleplay-categories", $params, $responseType);
    }
    public function datasafety(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("googleplay-datasafety", $params, $responseType);
    }
    public function developer(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("googleplay-developer", $params, $responseType);
    }
    public function list(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("googleplay-list", $params, $responseType);
    }
    public function permissions(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("googleplay-permissions", $params, $responseType);
    }
    public function ratings(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("googleplay-ratings", $params, $responseType);
    }
    public function reviews(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("googleplay-reviews", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("googleplay-search", $params, $responseType);
    }
    public function similar(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("googleplay-similar", $params, $responseType);
    }
    public function suggest(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("googleplay-suggest", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
