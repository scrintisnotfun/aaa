from threading import Thread
from app.bot import start_bot
from app.web import app
import requests

# List of slow endpoints
TARGETS = [
    "https://your-app.onrender.com/slow",
    "https://your-app.onrender.com/leak"
]

CONCURRENCY = 1000
TIMEOUT = 30  # seconds


# Function to send one request to a target
def stress_target(url, index):
    try:
        res = requests.get(url, timeout=TIMEOUT)
        print(f"[{index}] {url} → {res.status_code}")
    except Exception as e:
        print(f"[{index}] {url} → ERROR: {e}")


# Function to run stress test in loop
def run_slow_leak_stress():
    while True:
        threads = []
        for i in range(CONCURRENCY):
            for url in TARGETS:
                t = Thread(target=stress_target, args=(url, i))
                t.start()
                threads.append(t)
        
        # Wait for all threads to finish
        for t in threads:
            t.join()


# Start Discord bot
Thread(target=start_bot, daemon=True).start()

# Start stress test thread
Thread(target=run_slow_leak_stress, daemon=True).start()

# Start web server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
