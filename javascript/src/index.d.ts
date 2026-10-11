import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class GooglePlayClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  app(params: OperationParamsMap["googleplay-app"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  categories(params?: OperationParamsMap["googleplay-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  datasafety(params: OperationParamsMap["googleplay-datasafety"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  developer(params: OperationParamsMap["googleplay-developer"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  list(params?: OperationParamsMap["googleplay-list"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  permissions(params: OperationParamsMap["googleplay-permissions"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  ratings(params: OperationParamsMap["googleplay-ratings"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  reviews(params: OperationParamsMap["googleplay-reviews"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["googleplay-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  similar(params: OperationParamsMap["googleplay-similar"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  suggest(params: OperationParamsMap["googleplay-suggest"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  app(params: OperationParamsMap["googleplay-app"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  categories(params?: OperationParamsMap["googleplay-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  datasafety(params: OperationParamsMap["googleplay-datasafety"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  developer(params: OperationParamsMap["googleplay-developer"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  list(params?: OperationParamsMap["googleplay-list"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  permissions(params: OperationParamsMap["googleplay-permissions"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  ratings(params: OperationParamsMap["googleplay-ratings"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  reviews(params: OperationParamsMap["googleplay-reviews"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["googleplay-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  similar(params: OperationParamsMap["googleplay-similar"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  suggest(params: OperationParamsMap["googleplay-suggest"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  app(...args: OperationRequestArgs<"googleplay-app">): Promise<OperationResponseMap["googleplay-app"]>;
  categories(...args: OperationRequestArgs<"googleplay-categories">): Promise<OperationResponseMap["googleplay-categories"]>;
  datasafety(...args: OperationRequestArgs<"googleplay-datasafety">): Promise<OperationResponseMap["googleplay-datasafety"]>;
  developer(...args: OperationRequestArgs<"googleplay-developer">): Promise<OperationResponseMap["googleplay-developer"]>;
  list(...args: OperationRequestArgs<"googleplay-list">): Promise<OperationResponseMap["googleplay-list"]>;
  permissions(...args: OperationRequestArgs<"googleplay-permissions">): Promise<OperationResponseMap["googleplay-permissions"]>;
  ratings(...args: OperationRequestArgs<"googleplay-ratings">): Promise<OperationResponseMap["googleplay-ratings"]>;
  reviews(...args: OperationRequestArgs<"googleplay-reviews">): Promise<OperationResponseMap["googleplay-reviews"]>;
  search(...args: OperationRequestArgs<"googleplay-search">): Promise<OperationResponseMap["googleplay-search"]>;
  similar(...args: OperationRequestArgs<"googleplay-similar">): Promise<OperationResponseMap["googleplay-similar"]>;
  suggest(...args: OperationRequestArgs<"googleplay-suggest">): Promise<OperationResponseMap["googleplay-suggest"]>;
}
export { GooglePlayClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default GooglePlayClient;
