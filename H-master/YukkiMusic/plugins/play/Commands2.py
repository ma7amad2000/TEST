#test
import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InputMediaPhoto, InputMediaVideo
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from YukkiMusic import Telegram, YouTube, app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.plugins.play.playlist import del_plist_msg
from YukkiMusic.plugins.sudo.sudoers import sudoers_list
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from YukkiMusic.utils.decorators.language import LanguageStart
from YukkiMusic.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

from YukkiMusic import check_client


@app.on_callback_query(filters.regex("tt"))
async def gtt(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)


    await query.edit_message_text(
       f"""\n\n╭── • [𝗠𝗶𝗿𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/NvvvC) • ──╮\n\n ✧ **اوامر التشغيل بالقنوات**\n\n• **ق تشغيل + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني بالقناة\n\n• **ق ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• **ق تخطي**\n-› لتشغيل التالي بالانتظار\n\n • **ق اص**\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n• **ق كملي**\n-› لالغاء الكتم واكمال التشغيل\n\n• **ق ايقاف مؤقت**\n -› لايقاف التشغيل بشكل مؤقت\n\n• **ق استئناف**\n -› لاكمال التشغيل بعد الايقاف المؤقت\n\n╰── • [𝗠𝗶𝗿𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/NvvvC) • ──╯""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "", callback_data="fft"),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/so_alfaa")
                ],[
                    InlineKeyboardButton(
                        "رجوع", callback_data="am"),
                    InlineKeyboardButton(
                        "اغلاق", callback_data="close"),
                ],[

                    InlineKeyboardButton(
                        "", callback_data="save"),
                    InlineKeyboardButton(
                        "", callback_data="kdm"),
                ],[

                    InlineKeyboardButton(
                        "", callback_data=f"fft")


               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("am"))
async def am(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)

    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/94c43633525702295679d.mp4",None,
           "**✧ اهلين فيك في اوامر بوت ميرا**\n\n- عندك خمس ازرار وبعدها بتعرف تستخدم البوت ان شاء الله\n\n• مطور البوت -› @C_C_1\n• قناة البوت -› @NvvvC"
       ),
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

@app.on_callback_query(filters.regex("amm"))
async def am(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)

    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/94c43633525702295679d.mp4",None,
           "✧ اهلين فيك في اوامر بوت ميرا (:\n\n- **كل اوامر البوت عندك بالازرار تحت استكشفهم بنفسك**\n\n• Developer -› [𝑲𝒉𝒂𝒍𝒆𝒅](t.me/c_c_1)\n• Channel -› [𝑺𝒐𝒖𝒓𝒄𝒆 𝑴𝒊𝒓𝒂](t.me/NvvvC)"
       ),
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


@app.on_callback_query(filters.regex("sound"))
async def sound(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)

    await query.edit_message_media(
       InputMediaPhoto(
           "https://telegra.ph/file/e347318fd449b988911f8.jpg",
           "✶ **هلا فيك في قسم تشغيل اغاني الساوند ♪**\n\n• **تقدر تشغيل الاغاني عن طريق الرد على الرابط او وضعه مع الامر** .\n\n• مثال : [ `ميرا شغلي https://soundcloud.app.goo.gl/asiXLu19szSrVLFo9` ]\n\n• **وهذا قروب متخصص للساوند تقدر تدخل وتاخذ روابط منه** .\n-› [SoundCloud ♪](t.me/DownloadSound)"
      ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
   
                     InlineKeyboardButton(
                        "رجوع", callback_data=f"ko")
                ],[

                     InlineKeyboardButton(
                        "◌sᴏᴜʀᴄᴇ ᴍɪʀᴀ◌", callback_data=f"fft")

                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("cha"))
async def sound(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)

    await query.edit_message_media(
       InputMediaPhoto(
           "https://telegra.ph/file/4f5ddfee947f57d1d85a0.jpg",
           "- هلا والله\n◌**عشان تشغل بالقنوات لازم تسوي بعض الخطوات وهي◌** :\n\n1 -› تدخل البوت قناتك وترفعه مشرف\n2 -› ترجع للقروب وتكتب { **ربط + يوزر القناة** }\n3 -› **اضغط على زر اوامر التشغيل عشان تعرف كيف تشغل**..\n\n✶ **للاستفسار** - @C_C_1"
      ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "اوامر التشغيل بالقنوات", callback_data=f"tt"),

                ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("kdm"))
async def sound(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("معليش بس الطلب مو لك وخر !", show_alert=True)

    await query.edit_message_media(
       InputMediaPhoto(
           "https://telegra.ph/file/5306c1c651eb877f67c48.jpg",
           "✧ **اهلين فيك في قسم الاوامر الخدمية**\n-** عندك اوامر كثيرة للتسلية ومنها ↓**\n\n-› **غنيلي\n-› افتارات بنات\n-› افتارات عيال\n-› افتارات مكس\n -› هيدرات او هيدر\n-› اقتباس او اقتباسات\n-› كت**\n\n✶ **ايضا تقدر تتابع قناة ميرا فيها تشكلية كبيرة من كل الي ذكرتهم فوق**\n-› @JuuuT"
      ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "رجوع", callback_data=f"am"),
                ],[
                 
                     InlineKeyboardButton(
                        "• 𝑷𝒓𝒐𝒑𝒆𝒓𝒕𝒚 𝑴𝒊𝒓𝒂 •", url=f"t.me/JuuuT")

                ],
            ]
        ),
    )
