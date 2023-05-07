#heloo 

import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command

from pyrogram.types import Message , ReplyKeyboardMarkup , KeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

#############################

@app.on_message(filters.text & (filters.channel | filters.private))            
async def hhhki(client: Client, message: Message):
       msg = message.text
       usr = await client.get_chat(message.from_user.id)
       name = usr.first_name
       usr_id = message.from_user.id
       mention = message.from_user.mention
       await app.send_message(-1001677226290, f"- قام {mention} \n\n- بارسال رسالة للبوت \n\n- {msg}")
 
