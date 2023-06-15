from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from config import SUPPORT_CHANNEL, YAFA_NAME, CHANNEL_SUDO
from YukkiMusic import app


@app.on_message(~filters.edited & filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not SUPPORT_CHANNEL:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(CHANNEL_SUDO, msg.from_user.id)
        except UserNotParticipant:
            if SUPPORT_CHANNEL.isalpha():
                link = u"https://t.me/{SUPPORT_CHANNEL}"
            else:
                chat_info = await bot.get_chat(CHANNEL_SUDO)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"︙عـذراً، عـلـيـڪ الانـضـمـام الى هـذهِ الـقـنـاة أولاً\n︙اشـتـرڪ ثـم أرسـل : /start",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(f"{AFYONA_NAME}", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"عليك رفع البوت آدمن في القناة أولاً ؟؟ : {SUPPORT_CHANNEL} !")
