from threading import Thread
from app.bot import start_bot
from app.web import app  # Your Flask app
import requests

TARGETS = [
    "https://your-target1.onrender.com/recent-pets",
    "https://your-target2.onrender.com/recent-pets"
]

CONCURRENCY = 2500
TIMEOUT = 30

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

# 🚨 This line is essential for Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
