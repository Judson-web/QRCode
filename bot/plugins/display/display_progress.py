#!/usr/bin/env python3
# This is bot coded by Judson-web and used for educational purposes only
# https://github.com/Judson-web
# (c) Judson-web ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)

async def progress(current, total, up_msg, message):
    try:
        await message.edit(
            text=f"{up_msg} {ᴄᴜʀʀᴇɴᴛ * 100 / ᴛᴏᴛᴀʟ:.1f}%"
        )
    except:
        pass
