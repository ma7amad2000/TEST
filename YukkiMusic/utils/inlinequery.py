#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="ايقاف مؤقت",
            description=f"لايقاف الاغنية بشكل مؤقت",
            thumb_url="https://telegra.ph/file/c0a1c789def7b93f13745.png",
            input_message_content=InputTextMessageContent("ايقاف مؤقت"),
        ),
        InlineQueryResultArticle(
            title="استئناف التشغيل",
            description=f"لاستئناف التشغيل بعد الايقاف المؤقت",
            thumb_url="https://telegra.ph/file/02d1b7f967ca11404455a.png",
            input_message_content=InputTextMessageContent("كرستال كملي"),
        ),
        InlineQueryResultArticle(
            title="كتم الحساب المساعد",
            description=f"لكتم الصوت في المكالمة",
            thumb_url="https://telegra.ph/file/66516f2976cb6d87e20f9.png",
            input_message_content=InputTextMessageContent("كرستال اص"),
        ),
        InlineQueryResultArticle(
            title="إلغاء الكتم",
            description=f"لالغاء كتم الحساب المساعد",
            thumb_url="https://telegra.ph/file/3078794f9341ffd582e18.png",
            input_message_content=InputTextMessageContent("كرستال تكلم"),
        ),
        InlineQueryResultArticle(
            title="التخطي",
            description=f"تخطي وتشغيل الانتظار تقدر تستخدم الامر كذا | /تخطي 3",
            thumb_url="https://telegra.ph/file/98b88e52bc625903c7a2f.png",
            input_message_content=InputTextMessageContent("/تخطي"),
        ),
        InlineQueryResultArticle(
            title="ايقاف التشغيل",
            description="لانها التشغيل",
            thumb_url="https://telegra.ph/file/d2eb03211baaba8838cc4.png",
            input_message_content=InputTextMessageContent("كرستال طفيها"),
        ),
        InlineQueryResultArticle(
            title="تكرار التشغيل",
            description="لتكرار التشغيل مثال | /loop 4",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
