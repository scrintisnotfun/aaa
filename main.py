from threading import Thread
from app.bot import start_bot
from app.web import app
import requests
import time

def ping_site():
    while True:
        try:
            requests.get("https://ere-dv2x.onrender.com/recent-pets")
            requests.get("https://aaa-l8lt.onrender.com/recent-pets")

        except Exception as e:
            print(f"Ping failed: {e}")
        time.sleep(300)  # 5 minutes = 300 seconds

# Start the Discord bot
Thread(target=start_bot, daemon=True).start()

# Start the ping thread
Thread(target=ping_site, daemon=True).start()

# Start the Flask web app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
