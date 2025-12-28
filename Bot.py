import feedparser
from telegram import Bot
import time
import os

TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL = os.environ.get("CHANNEL_NAME")
RSS_URL = "https://cointelegraph.com/rss"

bot = Bot(token=TOKEN)
posted_links = set()

while True:
    feed = feedparser.parse(RSS_URL)

    for entry in feed.entries[:3]:
        if entry.link not in posted_links:
            message = f"""
📰 خبر جديد

{entry.title}

🔗 المصدر:
{entry.link}

#Crypto #Bitcoin
            """
            bot.send_message(chat_id=CHANNEL, text=message)
            posted_links.add(entry.link)
            time.sleep(10)

    time.sleep(1800)
