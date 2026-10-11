import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class GooglePlayClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-googleplay-js/0.1.1" });
    this["app"] = (...args) => this.request("googleplay-app", ...args);
    this["categories"] = (...args) => this.request("googleplay-categories", ...args);
    this["datasafety"] = (...args) => this.request("googleplay-datasafety", ...args);
    this["developer"] = (...args) => this.request("googleplay-developer", ...args);
    this["list"] = (...args) => this.request("googleplay-list", ...args);
    this["permissions"] = (...args) => this.request("googleplay-permissions", ...args);
    this["ratings"] = (...args) => this.request("googleplay-ratings", ...args);
    this["reviews"] = (...args) => this.request("googleplay-reviews", ...args);
    this["search"] = (...args) => this.request("googleplay-search", ...args);
    this["similar"] = (...args) => this.request("googleplay-similar", ...args);
    this["suggest"] = (...args) => this.request("googleplay-suggest", ...args);
  }
}

export { GooglePlayClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.1";
export default GooglePlayClient;
