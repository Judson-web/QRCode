#!/usr/bin/env python3
# This is bot coded by Judson-web and used for educational purposes only
# https://github.com/Judson-web
# (c) Judson-web ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)


from pyrogram import Client
from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN
)

bot = Client(
    "QR CODE BOT",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins={
        "root": "bot/plugins"
    },
    parse_mode="html"
)
bot.run()
