# Crawlora Google Play JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `11`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| googleplay | `googleplay.app` | `googleplay-app` | `GET /googleplay/app` | `app_id` (query string required)<br>`country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `GoogleplayAppResponse` |  |
| googleplay | `googleplay.categories` | `googleplay-categories` | `GET /googleplay/categories` | `country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `GoogleplayCategoriesResponse` |  |
| googleplay | `googleplay.datasafety` | `googleplay-datasafety` | `GET /googleplay/datasafety` | `app_id` (query string required)<br>`lang` (query string) | `ApiKeyAuth` | `GoogleplayDatasafetyResponse` |  |
| googleplay | `googleplay.developer` | `googleplay-developer` | `GET /googleplay/developer/{dev_id}` | `dev_id` (path string required)<br>`num` (query number)<br>`country` (query string)<br>`lang` (query string)<br>`full_detail` (query boolean) | `ApiKeyAuth` | `GoogleplayDeveloperResponse` |  |
| googleplay | `googleplay.list` | `googleplay-list` | `GET /googleplay/list` | `collection` (query "TOP_FREE" \| "TOP_PAID" \| "GROSSING" \| "NEW_FREE" \| "NEW_PAID")<br>`category` (query string)<br>`device` (query "phone" \| "tablet" \| "tv" \| "chromebook" \| "watch" \| "xr" \| "car")<br>`age` (query string)<br>`num` (query number)<br>`country` (query string)<br>`lang` (query string)<br>`full_detail` (query boolean) | `ApiKeyAuth` | `GoogleplayListResponse` |  |
| googleplay | `googleplay.permissions` | `googleplay-permissions` | `GET /googleplay/permissions` | `app_id` (query string required)<br>`country` (query string)<br>`lang` (query string)<br>`short` (query boolean) | `ApiKeyAuth` | `GoogleplayPermissionsResponse` |  |
| googleplay | `googleplay.ratings` | `googleplay-ratings` | `GET /googleplay/ratings` | `app_id` (query string required)<br>`country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `GoogleplayRatingsResponse` |  |
| googleplay | `googleplay.reviews` | `googleplay-reviews` | `GET /googleplay/reviews` | `app_id` (query string required)<br>`sort` (query "helpfulness" \| "newest" \| "rating")<br>`num` (query number)<br>`country` (query string)<br>`lang` (query string)<br>`paginate` (query boolean)<br>`next_pagination_token` (query string) | `ApiKeyAuth` | `GoogleplayReviewsResponse` |  |
| googleplay | `googleplay.search` | `googleplay-search` | `GET /googleplay/search` | `term` (query string required)<br>`num` (query number)<br>`country` (query string)<br>`lang` (query string)<br>`full_detail` (query boolean)<br>`price` (query "all" \| "free" \| "paid") | `ApiKeyAuth` | `GoogleplaySearchResponse` |  |
| googleplay | `googleplay.similar` | `googleplay-similar` | `GET /googleplay/similar` | `app_id` (query string required)<br>`num` (query number)<br>`country` (query string)<br>`lang` (query string)<br>`full_detail` (query boolean) | `ApiKeyAuth` | `GoogleplaySimilarResponse` |  |
| googleplay | `googleplay.suggest` | `googleplay-suggest` | `GET /googleplay/suggest/{term}` | `term` (path string required)<br>`country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `GoogleplaySuggestResponse` |  |
