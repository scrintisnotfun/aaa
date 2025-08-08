from threading import Thread
from app.bot import start_bot
from app.web import app
import requests
import time

# Ping premium and ere 100 times per second
def high_frequency_ping():
    while True:
        try:
            requests.get("https://ere-dv2x.onrender.com/recent-pets")
            requests.get("https://premium-github-io.onrender.com/recent-pets")
        except Exception as e:
            print(f"High frequency ping failed: {e}")
        time.sleep(0.002)  # 100 times per second (1/100 = 0.01s)



# Start the Discord bot
Thread(target=start_bot, daemon=True).start()

# Start the ping threads
Thread(target=high_frequency_ping, daemon=True).start()
Thread(target=low_frequency_ping, daemon=True).start()

# Start the Flask web app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
