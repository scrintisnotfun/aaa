from threading import Thread
from app.bot import start_bot
from app.web import app
import requests

# Your actual ping targets
TARGETS = [
    "https://ere-dv2x.onrender.com/recent-pets",
    "https://premium-github-io.onrender.com/recent-pets"
]

CONCURRENCY = 1000
TIMEOUT = 30  # seconds

def ping_site_continuous(url, thread_index):
    while True:
        try:
            response = requests.get(url, timeout=TIMEOUT)
            print(f"[Thread {thread_index}] Pinged {url} with status {response.status_code}")
        except Exception as e:
            print(f"[Thread {thread_index}] Error pinging {url}: {e}")

# Start Discord bot
Thread(target=start_bot, daemon=True).start()

# Start ping threads
for url in TARGETS:
    for i in range(CONCURRENCY):
        Thread(target=ping_site_continuous, args=(url, i), daemon=True).start()

# Start Flask web app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
