#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from YukkiMusic.plugins.play.filters import command
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.database import is_muted, mute_on
from YukkiMusic.utils.decorators import AdminRightsCheckCB

# Commands
MUTE_COMMAND = get_command("MUTE_COMMAND")


@app.on_message(
    command(MUTE_COMMAND)
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheckCB
async def mute_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if await is_muted(chat_id):
        return await message.reply_text(_["admin_5"])
    await mute_on(chat_id)
    await Yukki.mute_stream(chat_id)
    if message.sender_chat:
        mention = f'<a href=tg://user?id={message.chat.id}>{message.chat.title}</a>'
    else:
        mention = message.from_user.mention
    await message.reply_text(
        _["admin_6"].format(mention)
    )
