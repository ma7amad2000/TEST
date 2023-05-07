import asyncio
import pyrogram
from pyrogram import Client, filters
from YukkiMusic import settingsApp
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME
from YukkiMusic.misc import SUDOERS
import re
import sys
import os
import random
from time import time
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters




load_dotenv()




def get_file_id(msg: Message):

    if msg.media:

        for message_type in (

            "photo",

            "animation",

            "audio",

            "document",

            "video",

            "video_note",

            "voice",

            # "contact",

            # "dice",

            # "poll",

            # "location",

            # "venue",

            "sticker",

        ):

            obj = getattr(msg, message_type)

            if obj:

                setattr(obj, "message_type", message_type)

                return obj







#@app.on_message(command([""]) & filters.group &
#async def khalid(client: Client, message: Message):
    #usr = await client.get_users(message.from_user.id)
    #name = usr.first_name
    #async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    #await message.reply_photo(photo.file_id,       caption=f"""ᴜsᴇʀ -› {message.from_user.mention}\n𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲 -› @{message.from_user.username}\nɪᴅ -› {message.from_user.id}\nbio » {bio}""", 
        #reply_markup=InlineKeyboardMarkup(

            #[

                #[

                    #InlineKeyboardButton(

                        #name, url=f"https://t.me/{message.from_user.id}")

                #],

            #]

        #),

    #)

@app.on_message(filters.regex("^$") & filters.group & SUDOERS)
async def khalid(client: Client, message: Message):

    usr = await client.get_chat(message.from_user.id)

    name = usr.first_name

    bio = usr.bio




    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):

                    await message.reply_photo(photo.file_id,       caption=f"""• In the end, you are the bad, and they are the innocent\n\n• 𝑵𝒂𝒎𝒆 -› {message.from_user.mention}\n• 𝑼𝒔𝒆𝒓 -› @{message.from_user.username}\n• 𝑺𝒕𝒂𝒕𝒔 -› Developer Mira\n• 𝑩𝒊𝒐 -› {bio}""", 

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        name, user_id=2089102006)

                ],

            ]

        ),

    )

@app.on_message(filters.regex("^لونلي$") & filters.group & SUDOERS)
async def khalid(client: Client, message: Message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    bio = usr.bio
    await message.reply_video(
        video=f"https://telegra.ph/file/f12360f05eefd9399bd0b.mp4",
        caption=f"""• In the end, you are the bad, and they are the innocent\n\n• 𝑵𝒂𝒎𝒆 -› {message.from_user.mention}\n• 𝑼𝒔𝒆𝒓 -› @{message.from_user.username}\n• 𝑺𝒕𝒂𝒕𝒔 -› Developer Mira\n• 𝑩𝒊𝒐 -› {bio}""",
        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        name, user_id=2089102006)

                ],

            ]

        ),

    )

@app.on_message(filters.command("ايدي المجموعة", ["", "."]) & ~filters.edited)
async def mira(client: Client, message: Message):
    m_reply = await message.reply_text(f"ID chat** [`{message.chat.id}`]")
    await m_reply_text("")


#السورس - المطور


@app.on_message(filters.regex("^السورس$") & filters.group & ~filters.edited)
async def sourc(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/588d70e34b51710ae8dce.jpg",
        caption=f"""✧ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑺𝒐𝒖𝒓𝒄𝒆 𝑴𝒊𝒓𝒂 ♪\n\n• ᴅᴇᴠᴇʟᴏᴘᴇʀ -› @PsPsP\n• ᴄʜᴀɴɴᴇʟ ᴍɪʀᴀ -› @NvvvC\n\n**- للتنصيب او للاستفسار تواصل مع مطور السورس**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "مطور السورس", user_id=2089102006)
                ],[
                    InlineKeyboardButton(
                       "تحديثات ميرا", url=f"https://t.me/NvvvC")
                
                 ],

            ]

        ),

    )


@app.on_message(filters.regex("^المطور$") & filters.group & ~filters.edited)
async def aboutd5ev(client: Client, message: Message):
    usr = await client.get_chat(2089102006)
    name = usr.first_name
    bio = (await client.get_chat(2089102006)).bio
    async for photo in client.iter_profile_photos(2089102006, limit=1):
                    await message.reply_photo(photo.file_id, caption=f"""- 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 𝑻𝒐 𝑩𝒐𝒕 𝑴𝒊𝒓𝒂 ♪ -› @PsPsP\n\n- 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓'𝒔 𝑩𝒊𝒐 -› {bio}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, user_id=2089102006)
                ],
            ]
        ),
    )

