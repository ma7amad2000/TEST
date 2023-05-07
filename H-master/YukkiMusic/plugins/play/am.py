import asyncio
from pyrogram import Client, filters
from config import BANNED_USERS
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)

from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

AM_COMMAND = get_command("AM_COMMAND")


@app.on_message(
    command(AM_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
async def khalid(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/94c43633525702295679d.mp4",
        caption=f"""✧ اهلين فيك في اوامر بوت ميرا\n\n -› **جميع اوامر البوت موجودة بالقائمة هذي ، اضغط الازرار الي تحت واستكشف ياوحش**\n\n• Developer -› [𝑲𝒉𝒂𝒍𝒆𝒅](t.me/c_c_1)\n• Channel -› [𝑺𝒐𝒖𝒓𝒄𝒆 𝑴𝒊𝒓𝒂](t.me/NvvvC)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "شرح التشغيل بمنصات الاغاني", callback_data=f"ko"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"ddd"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"tt"),

                ],[
                    InlineKeyboardButton(
                        "ربط القنوات", callback_data=f"cha"),

                    InlineKeyboardButton(
                        "اوامر البحث", callback_data=f"don"),
                ],[

                    InlineKeyboardButton(
                        "حفظ التشغيل", callback_data=f"save"),

                    InlineKeyboardButton(
                        "اوامر خدمية", callback_data=f"kdm"),
                ],[

                    InlineKeyboardButton(
                        "تحديثات ميرا 🥢", url=f"https://t.me/NvvvC"),

                ],
            ]
        ),
    )
