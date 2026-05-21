from telethon import TelegramClient, events
import requests
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

KEYWORDS = ["salesforce", "lwc", "apex"]

CHANNELS = ["Udemy4"]

client = TelegramClient(
    'session_name',
    api_id,
    api_hash
)

def send_notification(message):

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url, data=payload)

@client.on(events.NewMessage(chats=CHANNELS))
async def handler(event):

    text = event.message.message.lower()

    print("New Message:", text)

    for keyword in KEYWORDS:

        if keyword in text:

            send_notification(
                f"Keyword Found: {keyword}\n\n{text}"
            )

            print("Notification sent")

            break

print("Starting bot...")

client.start()

print("Bot running...")

client.run_until_disconnected()
