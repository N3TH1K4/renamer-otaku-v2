# (c) @Friend_A_Kousei

import asyncio
from helpers.database.access_db import db
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def OpenSettings(event: Message, user_id: int):
    try:
        await event.edit(
            text="Here is Your Settings⚙️.. Now It's On Your Hand😊.. ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(f"Upload as Doc {'✅' if ((await db.get_upload_as_doc(user_id)) is True) else '❌'}",
                                          callback_data="triggerUploadMode")],
                    [InlineKeyboardButton("Name Prefix ✏️", callback_data="triggerPrefix"),
                     InlineKeyboardButton("Thumbnail 🖼", callback_data="triggerThumbnail")],
                    [InlineKeyboardButton("Caption ✒", callback_data="triggerCaption")],
                    [InlineKeyboardButton("Close 🔐", callback_data="closeMeh")]
                ]
            )
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await OpenSettings(event, user_id)
    except MessageNotModified:
        pass
