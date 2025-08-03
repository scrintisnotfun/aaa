
import discord
import os
import re
import time
import threading
import requests

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", 1401663245936365699))

pet_servers = []

def parse_pet_embed(embed):
    name = mutation = dps = jobId = placeId = None
    for field in embed.fields:
        if "Name" in field.name:
            name = field.value.strip()
        elif "Mutation" in field.name:
            mutation = field.value.strip()
        elif "Money" in field.name or "Per Sec" in field.name:
            dps = field.value.strip()
        elif "JOBID" in field.name:
            jobId = field.value.strip()
        elif "Join Script" in field.name:
            m = re.search(r'TeleportToPlaceInstance\((\d+),\s*\"([\w-]+)', field.value)
            if m:
                placeId = m.group(1)
                jobId = m.group(2)
    if name and jobId and placeId:
        return {
            "name": name,
            "mutation": mutation or "",
            "dps": dps or "",
            "jobId": jobId,
            "placeId": placeId,
            "timestamp": time.time(),
        }
    return None

class PetClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if not message.channel or message.channel.id != CHANNEL_ID:
            return
        for embed in message.embeds:
            pet = parse_pet_embed(embed)
            if pet:
                if not any(p["jobId"] == pet["jobId"] and p["name"] == pet["name"] for p in pet_servers):
                    pet_servers.append(pet)
                    print(f"Added pet: {pet['name']} {pet['jobId']}")
                if len(pet_servers) > 20:
                    pet_servers.pop(0)
                break

def keep_alive_ping():
    url = os.environ.get("APP_URL")
    if not url:
        print("APP_URL env var not set, skipping keep-alive ping")
        return

    def ping_loop():
        while True:
            try:
                r = requests.get(f"{url}/ping", timeout=5)
                print(f"Keep-alive ping sent, status: {r.status_code}")
            except Exception as e:
                print(f"Keep-alive ping error: {e}")
            time.sleep(600)  # 10 minutes

    thread = threading.Thread(target=ping_loop, daemon=True)
    thread.start()

def start_bot():
    keep_alive_ping()
    intents = discord.Intents.default()
    intents.message_content = True
    client = PetClient(intents=intents)
    client.run(DISCORD_TOKEN)

def get_recent_pets():
    now = time.time()
    return [p for p in pet_servers if now - p["timestamp"] < 900]
