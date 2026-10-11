import os

from crawlora_googleplay import GooglePlayClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with GooglePlayClient(api_key=api_key) as client:
    search = client.search(term='podcast player')
    print('search', search)
    app = client.app(app_id='com.spotify.music')
    print('app', app)
