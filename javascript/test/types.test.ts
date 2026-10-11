import { GooglePlayClient } from "../src/index.js";

const client = new GooglePlayClient({ apiKey: "test-key" });
void client.app({"app_id": "sample"});
void client.request("googleplay-app", {"app_id": "sample"});
const streamResponse: Promise<Response> = client.request("googleplay-app", {"app_id": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("googleplay-app", {"app_id": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.app({"app_id": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("googleplay-app", {"app_id": "sample", "country": "sample", "lang": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("googleplay-app", {"app_id": "sample"}, { responseType: "text" });
void rawText;


void client.categories();
void client.request("googleplay-categories");
// @ts-expect-error The selected operation requires its documented params.
void client.app();
