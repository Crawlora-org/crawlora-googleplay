from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelGoogleplaySuggestResponseDoc = TypedDict('ModelGoogleplaySuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelGoogleplaySuggestion]],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplaySuggestion = TypedDict('ModelGoogleplaySuggestion', {
    'term': NotRequired[str],
}, total=False)

ModelGoogleplaySimilarResultsResponseDoc = TypedDict('ModelGoogleplaySimilarResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[Any]],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplaySearchResultsResponseDoc = TypedDict('ModelGoogleplaySearchResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[Any]],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplayReviewsResponseDoc = TypedDict('ModelGoogleplayReviewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGoogleplayReviewsResult],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplayReviewsResult = TypedDict('ModelGoogleplayReviewsResult', {
    'data': NotRequired[list[ModelGoogleplayReview]],
    'next_pagination_token': NotRequired[str],
}, total=False)

ModelGoogleplayReview = TypedDict('ModelGoogleplayReview', {
    'criterias': NotRequired[list[ModelGoogleplayReviewCriteria]],
    'date': NotRequired[str],
    'id': NotRequired[str],
    'reply_date': NotRequired[str],
    'reply_text': NotRequired[str],
    'score': NotRequired[int],
    'score_text': NotRequired[str],
    'text': NotRequired[str],
    'thumbs_up': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'user_image': NotRequired[str],
    'user_name': NotRequired[str],
    'version': NotRequired[str],
}, total=False)

ModelGoogleplayReviewCriteria = TypedDict('ModelGoogleplayReviewCriteria', {
    'criteria': NotRequired[str],
    'rating': NotRequired[int],
}, total=False)

ModelGoogleplayRatingsResponseDoc = TypedDict('ModelGoogleplayRatingsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelGoogleplayDeviceRating]],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplayDeviceRating = TypedDict('ModelGoogleplayDeviceRating', {
    'device': NotRequired[str],
    'histogram': NotRequired[dict[str, Any]],
    'ratings': NotRequired[int],
    'reviews': NotRequired[int],
    'score': NotRequired[float],
    'score_text': NotRequired[str],
}, total=False)

ModelGoogleplayPermissionsResultsResponseDoc = TypedDict('ModelGoogleplayPermissionsResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[Any]],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplayListResultsResponseDoc = TypedDict('ModelGoogleplayListResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[Any]],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplayDeveloperResultsResponseDoc = TypedDict('ModelGoogleplayDeveloperResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[Any]],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplayDataSafetyResponseDoc = TypedDict('ModelGoogleplayDataSafetyResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGoogleplayDataSafetyResult],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplayDataSafetyResult = TypedDict('ModelGoogleplayDataSafetyResult', {
    'collected_data': NotRequired[list[ModelGoogleplayDataSafetyEntry]],
    'privacy_policy_url': NotRequired[str],
    'security_practices': NotRequired[list[ModelGoogleplaySecurityPractice]],
    'shared_data': NotRequired[list[ModelGoogleplayDataSafetyEntry]],
}, total=False)

ModelGoogleplayDataSafetyEntry = TypedDict('ModelGoogleplayDataSafetyEntry', {
    'data': NotRequired[str],
    'optional': NotRequired[bool],
    'purpose': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelGoogleplaySecurityPractice = TypedDict('ModelGoogleplaySecurityPractice', {
    'description': NotRequired[str],
    'practice': NotRequired[str],
}, total=False)

ModelGoogleplayCategoriesResponseDoc = TypedDict('ModelGoogleplayCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[str]],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplayAppDetailsResponse = TypedDict('ModelGoogleplayAppDetailsResponse', {
    'code': NotRequired[int],
    'data': NotRequired[ModelGoogleplayApp],
    'msg': NotRequired[str],
}, total=False)

ModelGoogleplayApp = TypedDict('ModelGoogleplayApp', {
    'ad_supported': NotRequired[bool],
    'android_max_version': NotRequired[str],
    'android_version': NotRequired[str],
    'android_version_text': NotRequired[str],
    'app_id': NotRequired[str],
    'available': NotRequired[bool],
    'categories': NotRequired[list[ModelGoogleplayCategory]],
    'comments': NotRequired[list[str]],
    'content_rating': NotRequired[str],
    'content_rating_description': NotRequired[str],
    'currency': NotRequired[str],
    'description': NotRequired[str],
    'description_html': NotRequired[str],
    'developer': NotRequired[str],
    'developer_address': NotRequired[str],
    'developer_email': NotRequired[str],
    'developer_id': NotRequired[str],
    'developer_internal_id': NotRequired[str],
    'developer_legal_address': NotRequired[str],
    'developer_legal_email': NotRequired[str],
    'developer_legal_name': NotRequired[str],
    'developer_legal_phone_number': NotRequired[str],
    'developer_website': NotRequired[str],
    'discount_end_date': NotRequired[str],
    'early_access_enabled': NotRequired[bool],
    'features': NotRequired[list[ModelGoogleplayFeature]],
    'free': NotRequired[bool],
    'genre': NotRequired[str],
    'genre_id': NotRequired[str],
    'header_image': NotRequired[str],
    'histogram': NotRequired[dict[str, Any]],
    'iap_range': NotRequired[str],
    'icon': NotRequired[str],
    'installs': NotRequired[str],
    'is_available_in_play_pass': NotRequired[bool],
    'max_installs': NotRequired[int],
    'min_installs': NotRequired[int],
    'more_by_developer': NotRequired[list[ModelGoogleplayListApp]],
    'offers_iap': NotRequired[bool],
    'original_price': NotRequired[float],
    'platforms': NotRequired[list[str]],
    'preregister': NotRequired[bool],
    'preview_video': NotRequired[str],
    'price': NotRequired[float],
    'price_text': NotRequired[str],
    'privacy_policy': NotRequired[str],
    'ratings': NotRequired[int],
    'recent_changes': NotRequired[str],
    'released': NotRequired[str],
    'reviews': NotRequired[int],
    'score': NotRequired[float],
    'score_text': NotRequired[str],
    'screenshots': NotRequired[list[str]],
    'similar_apps': NotRequired[list[ModelGoogleplayListApp]],
    'summary': NotRequired[str],
    'title': NotRequired[str],
    'updated': NotRequired[int],
    'url': NotRequired[str],
    'version': NotRequired[str],
    'video': NotRequired[str],
    'video_image': NotRequired[str],
}, total=False)

ModelGoogleplayListApp = TypedDict('ModelGoogleplayListApp', {
    'app_id': NotRequired[str],
    'currency': NotRequired[str],
    'developer': NotRequired[str],
    'developer_id': NotRequired[str],
    'free': NotRequired[bool],
    'icon': NotRequired[str],
    'price': NotRequired[float],
    'price_text': NotRequired[str],
    'score': NotRequired[float],
    'score_text': NotRequired[str],
    'summary': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelGoogleplayFeature = TypedDict('ModelGoogleplayFeature', {
    'description': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelGoogleplayCategory = TypedDict('ModelGoogleplayCategory', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

GoogleplayAppResponse = ModelGoogleplayAppDetailsResponse
GoogleplayAppParams = TypedDict('GoogleplayAppParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'app_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplayCategoriesResponse = ModelGoogleplayCategoriesResponseDoc
GoogleplayCategoriesParams = TypedDict('GoogleplayCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplayDatasafetyResponse = ModelGoogleplayDataSafetyResponseDoc
GoogleplayDatasafetyParams = TypedDict('GoogleplayDatasafetyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'app_id': Required[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplayDeveloperResponse = ModelGoogleplayDeveloperResultsResponseDoc
GoogleplayDeveloperParams = TypedDict('GoogleplayDeveloperParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'dev_id': Required[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
}, total=False)

GoogleplayListResponse = ModelGoogleplayListResultsResponseDoc
GoogleplayListParams = TypedDict('GoogleplayListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'collection': NotRequired[Literal['TOP_FREE', 'TOP_PAID', 'GROSSING', 'NEW_FREE', 'NEW_PAID']],
    'category': NotRequired[str],
    'device': NotRequired[Literal['phone', 'tablet', 'tv', 'chromebook', 'watch', 'xr', 'car']],
    'age': NotRequired[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
}, total=False)

GoogleplayPermissionsResponse = ModelGoogleplayPermissionsResultsResponseDoc
GoogleplayPermissionsParams = TypedDict('GoogleplayPermissionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'app_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'short': NotRequired[bool],
}, total=False)

GoogleplayRatingsResponse = ModelGoogleplayRatingsResponseDoc
GoogleplayRatingsParams = TypedDict('GoogleplayRatingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'app_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplayReviewsResponse = ModelGoogleplayReviewsResponseDoc
GoogleplayReviewsParams = TypedDict('GoogleplayReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'app_id': Required[str],
    'sort': NotRequired[Literal['helpfulness', 'newest', 'rating']],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'paginate': NotRequired[bool],
    'next_pagination_token': NotRequired[str],
}, total=False)

GoogleplaySearchResponse = ModelGoogleplaySearchResultsResponseDoc
GoogleplaySearchParams = TypedDict('GoogleplaySearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'term': Required[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
    'price': NotRequired[Literal['all', 'free', 'paid']],
}, total=False)

GoogleplaySimilarResponse = ModelGoogleplaySimilarResultsResponseDoc
GoogleplaySimilarParams = TypedDict('GoogleplaySimilarParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'app_id': Required[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
}, total=False)

GoogleplaySuggestResponse = ModelGoogleplaySuggestResponseDoc
GoogleplaySuggestParams = TypedDict('GoogleplaySuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'term': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

class GoogleplayGroup:
    @overload
    def app(self, **params: Unpack[GoogleplayAppStreamParams]) -> BinaryIO: ...
    @overload
    def app(self, **params: Unpack[GoogleplayAppTextResponseParams]) -> str: ...
    @overload
    def app(self, **params: Unpack[GoogleplayAppDefaultParams]) -> GoogleplayAppResponse: ...
    @overload
    def categories(self, **params: Unpack[GoogleplayCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[GoogleplayCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[GoogleplayCategoriesDefaultParams]) -> GoogleplayCategoriesResponse: ...
    @overload
    def datasafety(self, **params: Unpack[GoogleplayDatasafetyStreamParams]) -> BinaryIO: ...
    @overload
    def datasafety(self, **params: Unpack[GoogleplayDatasafetyTextResponseParams]) -> str: ...
    @overload
    def datasafety(self, **params: Unpack[GoogleplayDatasafetyDefaultParams]) -> GoogleplayDatasafetyResponse: ...
    @overload
    def developer(self, **params: Unpack[GoogleplayDeveloperStreamParams]) -> BinaryIO: ...
    @overload
    def developer(self, **params: Unpack[GoogleplayDeveloperTextResponseParams]) -> str: ...
    @overload
    def developer(self, **params: Unpack[GoogleplayDeveloperDefaultParams]) -> GoogleplayDeveloperResponse: ...
    @overload
    def list(self, **params: Unpack[GoogleplayListStreamParams]) -> BinaryIO: ...
    @overload
    def list(self, **params: Unpack[GoogleplayListTextResponseParams]) -> str: ...
    @overload
    def list(self, **params: Unpack[GoogleplayListDefaultParams]) -> GoogleplayListResponse: ...
    @overload
    def permissions(self, **params: Unpack[GoogleplayPermissionsStreamParams]) -> BinaryIO: ...
    @overload
    def permissions(self, **params: Unpack[GoogleplayPermissionsTextResponseParams]) -> str: ...
    @overload
    def permissions(self, **params: Unpack[GoogleplayPermissionsDefaultParams]) -> GoogleplayPermissionsResponse: ...
    @overload
    def ratings(self, **params: Unpack[GoogleplayRatingsStreamParams]) -> BinaryIO: ...
    @overload
    def ratings(self, **params: Unpack[GoogleplayRatingsTextResponseParams]) -> str: ...
    @overload
    def ratings(self, **params: Unpack[GoogleplayRatingsDefaultParams]) -> GoogleplayRatingsResponse: ...
    @overload
    def reviews(self, **params: Unpack[GoogleplayReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def reviews(self, **params: Unpack[GoogleplayReviewsTextResponseParams]) -> str: ...
    @overload
    def reviews(self, **params: Unpack[GoogleplayReviewsDefaultParams]) -> GoogleplayReviewsResponse: ...
    @overload
    def search(self, **params: Unpack[GoogleplaySearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[GoogleplaySearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[GoogleplaySearchDefaultParams]) -> GoogleplaySearchResponse: ...
    @overload
    def similar(self, **params: Unpack[GoogleplaySimilarStreamParams]) -> BinaryIO: ...
    @overload
    def similar(self, **params: Unpack[GoogleplaySimilarTextResponseParams]) -> str: ...
    @overload
    def similar(self, **params: Unpack[GoogleplaySimilarDefaultParams]) -> GoogleplaySimilarResponse: ...
    @overload
    def suggest(self, **params: Unpack[GoogleplaySuggestStreamParams]) -> BinaryIO: ...
    @overload
    def suggest(self, **params: Unpack[GoogleplaySuggestTextResponseParams]) -> str: ...
    @overload
    def suggest(self, **params: Unpack[GoogleplaySuggestDefaultParams]) -> GoogleplaySuggestResponse: ...

OperationId = Literal[
    'googleplay-app',
    'googleplay-categories',
    'googleplay-datasafety',
    'googleplay-developer',
    'googleplay-list',
    'googleplay-permissions',
    'googleplay-ratings',
    'googleplay-reviews',
    'googleplay-search',
    'googleplay-similar',
    'googleplay-suggest',
]

class CrawloraClient:
    googleplay: GoogleplayGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-app'],
        params: GoogleplayAppParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplayAppResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-categories'],
        params: GoogleplayCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplayCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-datasafety'],
        params: GoogleplayDatasafetyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplayDatasafetyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-developer'],
        params: GoogleplayDeveloperParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplayDeveloperResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-list'],
        params: GoogleplayListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplayListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-permissions'],
        params: GoogleplayPermissionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplayPermissionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-ratings'],
        params: GoogleplayRatingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplayRatingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-reviews'],
        params: GoogleplayReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplayReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-search'],
        params: GoogleplaySearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplaySearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-similar'],
        params: GoogleplaySimilarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplaySimilarResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['googleplay-suggest'],
        params: GoogleplaySuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplaySuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-app'],
        params: GoogleplayAppParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplayAppResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-categories'],
        params: GoogleplayCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplayCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-datasafety'],
        params: GoogleplayDatasafetyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplayDatasafetyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-developer'],
        params: GoogleplayDeveloperParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplayDeveloperResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-list'],
        params: GoogleplayListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplayListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-permissions'],
        params: GoogleplayPermissionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplayPermissionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-ratings'],
        params: GoogleplayRatingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplayRatingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-reviews'],
        params: GoogleplayReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplayReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-search'],
        params: GoogleplaySearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplaySearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-similar'],
        params: GoogleplaySimilarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplaySimilarResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['googleplay-suggest'],
        params: GoogleplaySuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GoogleplaySuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class GooglePlayClient(CrawloraClient):
    def __enter__(self) -> GooglePlayClient: ...
    @overload
    def app(self, **params: Unpack[GoogleplayAppStreamParams]) -> BinaryIO: ...
    @overload
    def app(self, **params: Unpack[GoogleplayAppTextResponseParams]) -> str: ...
    @overload
    def app(self, **params: Unpack[GoogleplayAppDefaultParams]) -> GoogleplayAppResponse: ...
    @overload
    def categories(self, **params: Unpack[GoogleplayCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[GoogleplayCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[GoogleplayCategoriesDefaultParams]) -> GoogleplayCategoriesResponse: ...
    @overload
    def datasafety(self, **params: Unpack[GoogleplayDatasafetyStreamParams]) -> BinaryIO: ...
    @overload
    def datasafety(self, **params: Unpack[GoogleplayDatasafetyTextResponseParams]) -> str: ...
    @overload
    def datasafety(self, **params: Unpack[GoogleplayDatasafetyDefaultParams]) -> GoogleplayDatasafetyResponse: ...
    @overload
    def developer(self, **params: Unpack[GoogleplayDeveloperStreamParams]) -> BinaryIO: ...
    @overload
    def developer(self, **params: Unpack[GoogleplayDeveloperTextResponseParams]) -> str: ...
    @overload
    def developer(self, **params: Unpack[GoogleplayDeveloperDefaultParams]) -> GoogleplayDeveloperResponse: ...
    @overload
    def list(self, **params: Unpack[GoogleplayListStreamParams]) -> BinaryIO: ...
    @overload
    def list(self, **params: Unpack[GoogleplayListTextResponseParams]) -> str: ...
    @overload
    def list(self, **params: Unpack[GoogleplayListDefaultParams]) -> GoogleplayListResponse: ...
    @overload
    def permissions(self, **params: Unpack[GoogleplayPermissionsStreamParams]) -> BinaryIO: ...
    @overload
    def permissions(self, **params: Unpack[GoogleplayPermissionsTextResponseParams]) -> str: ...
    @overload
    def permissions(self, **params: Unpack[GoogleplayPermissionsDefaultParams]) -> GoogleplayPermissionsResponse: ...
    @overload
    def ratings(self, **params: Unpack[GoogleplayRatingsStreamParams]) -> BinaryIO: ...
    @overload
    def ratings(self, **params: Unpack[GoogleplayRatingsTextResponseParams]) -> str: ...
    @overload
    def ratings(self, **params: Unpack[GoogleplayRatingsDefaultParams]) -> GoogleplayRatingsResponse: ...
    @overload
    def reviews(self, **params: Unpack[GoogleplayReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def reviews(self, **params: Unpack[GoogleplayReviewsTextResponseParams]) -> str: ...
    @overload
    def reviews(self, **params: Unpack[GoogleplayReviewsDefaultParams]) -> GoogleplayReviewsResponse: ...
    @overload
    def search(self, **params: Unpack[GoogleplaySearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[GoogleplaySearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[GoogleplaySearchDefaultParams]) -> GoogleplaySearchResponse: ...
    @overload
    def similar(self, **params: Unpack[GoogleplaySimilarStreamParams]) -> BinaryIO: ...
    @overload
    def similar(self, **params: Unpack[GoogleplaySimilarTextResponseParams]) -> str: ...
    @overload
    def similar(self, **params: Unpack[GoogleplaySimilarDefaultParams]) -> GoogleplaySimilarResponse: ...
    @overload
    def suggest(self, **params: Unpack[GoogleplaySuggestStreamParams]) -> BinaryIO: ...
    @overload
    def suggest(self, **params: Unpack[GoogleplaySuggestTextResponseParams]) -> str: ...
    @overload
    def suggest(self, **params: Unpack[GoogleplaySuggestDefaultParams]) -> GoogleplaySuggestResponse: ...

class AsyncGooglePlayClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncGooglePlayClient: ...
    googleplay: _AsyncGoogleplayGroup
    @overload
    async def app(self, **params: Unpack[GoogleplayAppStreamParams]) -> BinaryIO: ...
    @overload
    async def app(self, **params: Unpack[GoogleplayAppTextResponseParams]) -> str: ...
    @overload
    async def app(self, **params: Unpack[GoogleplayAppDefaultParams]) -> GoogleplayAppResponse: ...
    @overload
    async def categories(self, **params: Unpack[GoogleplayCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[GoogleplayCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[GoogleplayCategoriesDefaultParams]) -> GoogleplayCategoriesResponse: ...
    @overload
    async def datasafety(self, **params: Unpack[GoogleplayDatasafetyStreamParams]) -> BinaryIO: ...
    @overload
    async def datasafety(self, **params: Unpack[GoogleplayDatasafetyTextResponseParams]) -> str: ...
    @overload
    async def datasafety(self, **params: Unpack[GoogleplayDatasafetyDefaultParams]) -> GoogleplayDatasafetyResponse: ...
    @overload
    async def developer(self, **params: Unpack[GoogleplayDeveloperStreamParams]) -> BinaryIO: ...
    @overload
    async def developer(self, **params: Unpack[GoogleplayDeveloperTextResponseParams]) -> str: ...
    @overload
    async def developer(self, **params: Unpack[GoogleplayDeveloperDefaultParams]) -> GoogleplayDeveloperResponse: ...
    @overload
    async def list(self, **params: Unpack[GoogleplayListStreamParams]) -> BinaryIO: ...
    @overload
    async def list(self, **params: Unpack[GoogleplayListTextResponseParams]) -> str: ...
    @overload
    async def list(self, **params: Unpack[GoogleplayListDefaultParams]) -> GoogleplayListResponse: ...
    @overload
    async def permissions(self, **params: Unpack[GoogleplayPermissionsStreamParams]) -> BinaryIO: ...
    @overload
    async def permissions(self, **params: Unpack[GoogleplayPermissionsTextResponseParams]) -> str: ...
    @overload
    async def permissions(self, **params: Unpack[GoogleplayPermissionsDefaultParams]) -> GoogleplayPermissionsResponse: ...
    @overload
    async def ratings(self, **params: Unpack[GoogleplayRatingsStreamParams]) -> BinaryIO: ...
    @overload
    async def ratings(self, **params: Unpack[GoogleplayRatingsTextResponseParams]) -> str: ...
    @overload
    async def ratings(self, **params: Unpack[GoogleplayRatingsDefaultParams]) -> GoogleplayRatingsResponse: ...
    @overload
    async def reviews(self, **params: Unpack[GoogleplayReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def reviews(self, **params: Unpack[GoogleplayReviewsTextResponseParams]) -> str: ...
    @overload
    async def reviews(self, **params: Unpack[GoogleplayReviewsDefaultParams]) -> GoogleplayReviewsResponse: ...
    @overload
    async def search(self, **params: Unpack[GoogleplaySearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[GoogleplaySearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[GoogleplaySearchDefaultParams]) -> GoogleplaySearchResponse: ...
    @overload
    async def similar(self, **params: Unpack[GoogleplaySimilarStreamParams]) -> BinaryIO: ...
    @overload
    async def similar(self, **params: Unpack[GoogleplaySimilarTextResponseParams]) -> str: ...
    @overload
    async def similar(self, **params: Unpack[GoogleplaySimilarDefaultParams]) -> GoogleplaySimilarResponse: ...
    @overload
    async def suggest(self, **params: Unpack[GoogleplaySuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def suggest(self, **params: Unpack[GoogleplaySuggestTextResponseParams]) -> str: ...
    @overload
    async def suggest(self, **params: Unpack[GoogleplaySuggestDefaultParams]) -> GoogleplaySuggestResponse: ...

class _AsyncGoogleplayGroup:
    @overload
    async def app(self, **params: Unpack[GoogleplayAppStreamParams]) -> BinaryIO: ...
    @overload
    async def app(self, **params: Unpack[GoogleplayAppTextResponseParams]) -> str: ...
    @overload
    async def app(self, **params: Unpack[GoogleplayAppDefaultParams]) -> GoogleplayAppResponse: ...
    @overload
    async def categories(self, **params: Unpack[GoogleplayCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[GoogleplayCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[GoogleplayCategoriesDefaultParams]) -> GoogleplayCategoriesResponse: ...
    @overload
    async def datasafety(self, **params: Unpack[GoogleplayDatasafetyStreamParams]) -> BinaryIO: ...
    @overload
    async def datasafety(self, **params: Unpack[GoogleplayDatasafetyTextResponseParams]) -> str: ...
    @overload
    async def datasafety(self, **params: Unpack[GoogleplayDatasafetyDefaultParams]) -> GoogleplayDatasafetyResponse: ...
    @overload
    async def developer(self, **params: Unpack[GoogleplayDeveloperStreamParams]) -> BinaryIO: ...
    @overload
    async def developer(self, **params: Unpack[GoogleplayDeveloperTextResponseParams]) -> str: ...
    @overload
    async def developer(self, **params: Unpack[GoogleplayDeveloperDefaultParams]) -> GoogleplayDeveloperResponse: ...
    @overload
    async def list(self, **params: Unpack[GoogleplayListStreamParams]) -> BinaryIO: ...
    @overload
    async def list(self, **params: Unpack[GoogleplayListTextResponseParams]) -> str: ...
    @overload
    async def list(self, **params: Unpack[GoogleplayListDefaultParams]) -> GoogleplayListResponse: ...
    @overload
    async def permissions(self, **params: Unpack[GoogleplayPermissionsStreamParams]) -> BinaryIO: ...
    @overload
    async def permissions(self, **params: Unpack[GoogleplayPermissionsTextResponseParams]) -> str: ...
    @overload
    async def permissions(self, **params: Unpack[GoogleplayPermissionsDefaultParams]) -> GoogleplayPermissionsResponse: ...
    @overload
    async def ratings(self, **params: Unpack[GoogleplayRatingsStreamParams]) -> BinaryIO: ...
    @overload
    async def ratings(self, **params: Unpack[GoogleplayRatingsTextResponseParams]) -> str: ...
    @overload
    async def ratings(self, **params: Unpack[GoogleplayRatingsDefaultParams]) -> GoogleplayRatingsResponse: ...
    @overload
    async def reviews(self, **params: Unpack[GoogleplayReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def reviews(self, **params: Unpack[GoogleplayReviewsTextResponseParams]) -> str: ...
    @overload
    async def reviews(self, **params: Unpack[GoogleplayReviewsDefaultParams]) -> GoogleplayReviewsResponse: ...
    @overload
    async def search(self, **params: Unpack[GoogleplaySearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[GoogleplaySearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[GoogleplaySearchDefaultParams]) -> GoogleplaySearchResponse: ...
    @overload
    async def similar(self, **params: Unpack[GoogleplaySimilarStreamParams]) -> BinaryIO: ...
    @overload
    async def similar(self, **params: Unpack[GoogleplaySimilarTextResponseParams]) -> str: ...
    @overload
    async def similar(self, **params: Unpack[GoogleplaySimilarDefaultParams]) -> GoogleplaySimilarResponse: ...
    @overload
    async def suggest(self, **params: Unpack[GoogleplaySuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def suggest(self, **params: Unpack[GoogleplaySuggestTextResponseParams]) -> str: ...
    @overload
    async def suggest(self, **params: Unpack[GoogleplaySuggestDefaultParams]) -> GoogleplaySuggestResponse: ...

GoogleplayAppDefaultParams = TypedDict('GoogleplayAppDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'app_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplayAppTextResponseParams = TypedDict('GoogleplayAppTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'app_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplayAppStreamParams = TypedDict('GoogleplayAppStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'app_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplayCategoriesDefaultParams = TypedDict('GoogleplayCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplayCategoriesTextResponseParams = TypedDict('GoogleplayCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplayCategoriesStreamParams = TypedDict('GoogleplayCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplayDatasafetyDefaultParams = TypedDict('GoogleplayDatasafetyDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'app_id': Required[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplayDatasafetyTextResponseParams = TypedDict('GoogleplayDatasafetyTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'app_id': Required[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplayDatasafetyStreamParams = TypedDict('GoogleplayDatasafetyStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'app_id': Required[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplayDeveloperDefaultParams = TypedDict('GoogleplayDeveloperDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'dev_id': Required[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
}, total=False)

GoogleplayDeveloperTextResponseParams = TypedDict('GoogleplayDeveloperTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'dev_id': Required[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
}, total=False)

GoogleplayDeveloperStreamParams = TypedDict('GoogleplayDeveloperStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'dev_id': Required[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
}, total=False)

GoogleplayListDefaultParams = TypedDict('GoogleplayListDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'collection': NotRequired[Literal['TOP_FREE', 'TOP_PAID', 'GROSSING', 'NEW_FREE', 'NEW_PAID']],
    'category': NotRequired[str],
    'device': NotRequired[Literal['phone', 'tablet', 'tv', 'chromebook', 'watch', 'xr', 'car']],
    'age': NotRequired[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
}, total=False)

GoogleplayListTextResponseParams = TypedDict('GoogleplayListTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'collection': NotRequired[Literal['TOP_FREE', 'TOP_PAID', 'GROSSING', 'NEW_FREE', 'NEW_PAID']],
    'category': NotRequired[str],
    'device': NotRequired[Literal['phone', 'tablet', 'tv', 'chromebook', 'watch', 'xr', 'car']],
    'age': NotRequired[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
}, total=False)

GoogleplayListStreamParams = TypedDict('GoogleplayListStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'collection': NotRequired[Literal['TOP_FREE', 'TOP_PAID', 'GROSSING', 'NEW_FREE', 'NEW_PAID']],
    'category': NotRequired[str],
    'device': NotRequired[Literal['phone', 'tablet', 'tv', 'chromebook', 'watch', 'xr', 'car']],
    'age': NotRequired[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
}, total=False)

GoogleplayPermissionsDefaultParams = TypedDict('GoogleplayPermissionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'app_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'short': NotRequired[bool],
}, total=False)

GoogleplayPermissionsTextResponseParams = TypedDict('GoogleplayPermissionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'app_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'short': NotRequired[bool],
}, total=False)

GoogleplayPermissionsStreamParams = TypedDict('GoogleplayPermissionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'app_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'short': NotRequired[bool],
}, total=False)

GoogleplayRatingsDefaultParams = TypedDict('GoogleplayRatingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'app_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplayRatingsTextResponseParams = TypedDict('GoogleplayRatingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'app_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplayRatingsStreamParams = TypedDict('GoogleplayRatingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'app_id': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplayReviewsDefaultParams = TypedDict('GoogleplayReviewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'app_id': Required[str],
    'sort': NotRequired[Literal['helpfulness', 'newest', 'rating']],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'paginate': NotRequired[bool],
    'next_pagination_token': NotRequired[str],
}, total=False)

GoogleplayReviewsTextResponseParams = TypedDict('GoogleplayReviewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'app_id': Required[str],
    'sort': NotRequired[Literal['helpfulness', 'newest', 'rating']],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'paginate': NotRequired[bool],
    'next_pagination_token': NotRequired[str],
}, total=False)

GoogleplayReviewsStreamParams = TypedDict('GoogleplayReviewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'app_id': Required[str],
    'sort': NotRequired[Literal['helpfulness', 'newest', 'rating']],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'paginate': NotRequired[bool],
    'next_pagination_token': NotRequired[str],
}, total=False)

GoogleplaySearchDefaultParams = TypedDict('GoogleplaySearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'term': Required[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
    'price': NotRequired[Literal['all', 'free', 'paid']],
}, total=False)

GoogleplaySearchTextResponseParams = TypedDict('GoogleplaySearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'term': Required[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
    'price': NotRequired[Literal['all', 'free', 'paid']],
}, total=False)

GoogleplaySearchStreamParams = TypedDict('GoogleplaySearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'term': Required[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
    'price': NotRequired[Literal['all', 'free', 'paid']],
}, total=False)

GoogleplaySimilarDefaultParams = TypedDict('GoogleplaySimilarDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'app_id': Required[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
}, total=False)

GoogleplaySimilarTextResponseParams = TypedDict('GoogleplaySimilarTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'app_id': Required[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
}, total=False)

GoogleplaySimilarStreamParams = TypedDict('GoogleplaySimilarStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'app_id': Required[str],
    'num': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'full_detail': NotRequired[bool],
}, total=False)

GoogleplaySuggestDefaultParams = TypedDict('GoogleplaySuggestDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'term': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplaySuggestTextResponseParams = TypedDict('GoogleplaySuggestTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'term': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

GoogleplaySuggestStreamParams = TypedDict('GoogleplaySuggestStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'term': Required[str],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)
