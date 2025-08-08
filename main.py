from threading import Thread
from app.bot import start_bot
from app.web import app
import requests
import time

# Function for one thread to ping one site 100 times per second
def ping_target(url):
    while True:
        try:
            requests.get(url)
        except Exception as e:
            print(f"Ping to {url} failed: {e}")
        time.sleep(0.0025)  # 100 per second per thread

# Start the Discord bot
Thread(target=start_bot, daemon=True).start()

# Start 10 threads for ere
for _ in range(25):
    Thread(target=ping_target, args=("https://ere-dv2x.onrender.com/recent-pets",), daemon=True).start()

# Start 10 threads for premium
for _ in range(25):
    Thread(target=ping_target, args=("https://premium-github-io.onrender.com/recent-pets",), daemon=True).start()

# Start the Flask web app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
