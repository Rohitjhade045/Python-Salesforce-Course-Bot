import os
from telethon import TelegramClient, events
import requests

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
