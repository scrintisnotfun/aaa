
from threading import Thread
from app.bot import start_bot
from app.web import app

Thread(target=start_bot, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
