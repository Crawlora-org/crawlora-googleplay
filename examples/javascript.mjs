import { GooglePlayClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new GooglePlayClient({ apiKey });

  const search = await client.search({ term: "podcast player" });
  console.log("search", search);
  const app = await client.app({ app_id: "com.spotify.music" });
  console.log("app", app);
