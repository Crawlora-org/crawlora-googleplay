# Crawlora Google Play Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `11`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| googleplay | `googleplay.app` | `googleplay-app` | `GET /googleplay/app` | `app_id` (query String required)<br>`country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `GoogleplayAppResponse` |  |
| googleplay | `googleplay.categories` | `googleplay-categories` | `GET /googleplay/categories` | `country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `GoogleplayCategoriesResponse` |  |
| googleplay | `googleplay.datasafety` | `googleplay-datasafety` | `GET /googleplay/datasafety` | `app_id` (query String required)<br>`lang` (query String) | `ApiKeyAuth` | `GoogleplayDatasafetyResponse` |  |
| googleplay | `googleplay.developer` | `googleplay-developer` | `GET /googleplay/developer/{dev_id}` | `dev_id` (path String required)<br>`num` (query i64)<br>`country` (query String)<br>`lang` (query String)<br>`full_detail` (query bool) | `ApiKeyAuth` | `GoogleplayDeveloperResponse` |  |
| googleplay | `googleplay.list` | `googleplay-list` | `GET /googleplay/list` | `collection` (query String enum{TOP_FREE, TOP_PAID, GROSSING, NEW_FREE, NEW_PAID})<br>`category` (query String)<br>`device` (query String enum{phone, tablet, tv, chromebook, watch, xr, car})<br>`age` (query String)<br>`num` (query i64)<br>`country` (query String)<br>`lang` (query String)<br>`full_detail` (query bool) | `ApiKeyAuth` | `GoogleplayListResponse` |  |
| googleplay | `googleplay.permissions` | `googleplay-permissions` | `GET /googleplay/permissions` | `app_id` (query String required)<br>`country` (query String)<br>`lang` (query String)<br>`short` (query bool) | `ApiKeyAuth` | `GoogleplayPermissionsResponse` |  |
| googleplay | `googleplay.ratings` | `googleplay-ratings` | `GET /googleplay/ratings` | `app_id` (query String required)<br>`country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `GoogleplayRatingsResponse` |  |
| googleplay | `googleplay.reviews` | `googleplay-reviews` | `GET /googleplay/reviews` | `app_id` (query String required)<br>`sort` (query String enum{helpfulness, newest, rating})<br>`num` (query i64)<br>`country` (query String)<br>`lang` (query String)<br>`paginate` (query bool)<br>`next_pagination_token` (query String) | `ApiKeyAuth` | `GoogleplayReviewsResponse` |  |
| googleplay | `googleplay.search` | `googleplay-search` | `GET /googleplay/search` | `term` (query String required)<br>`num` (query i64)<br>`country` (query String)<br>`lang` (query String)<br>`full_detail` (query bool)<br>`price` (query String enum{all, free, paid}) | `ApiKeyAuth` | `GoogleplaySearchResponse` |  |
| googleplay | `googleplay.similar` | `googleplay-similar` | `GET /googleplay/similar` | `app_id` (query String required)<br>`num` (query i64)<br>`country` (query String)<br>`lang` (query String)<br>`full_detail` (query bool) | `ApiKeyAuth` | `GoogleplaySimilarResponse` |  |
| googleplay | `googleplay.suggest` | `googleplay-suggest` | `GET /googleplay/suggest/{term}` | `term` (path String required)<br>`country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `GoogleplaySuggestResponse` |  |
