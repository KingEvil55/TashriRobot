import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from TashriRobot import BOT_NAME, BOT_USERNAME
from TashriRobot import pbot as Tashri


@Tashri.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
        m = await Tashri.send_message(
            message.chat.id, "`Please wait...,\n\nWriting your text...`"
        )
        API = f"https://api.sdbots.tk/write?text={text}"
        req = requests.get(API).url
        caption = f"""
sᴜᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘

✨ **ᴡʀɪᴛᴛᴇɴ ʙʏ :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
❄ **ʟɪɴᴋ :** `{req}`
"""
        await m.delete()
        await Tashri.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🍁ᴛᴇʟᴇɢʀᴀᴩʜ🍁", url=f"{req}")]]
            ),
        )
    else:
        lol = message.reply_to_message.text
        m = await Tashri.send_message(
            message.chat.id, "`Please wait...,\n\nWriting your text...`"
        )
        API = f"https://api.sdbots.tk/write?text={lol}"
        req = requests.get(API).url
        caption = f"""
sᴜᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘

✨ **ᴡʀɪᴛᴛᴇɴ ʙʏ :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
❄ **ʟɪɴᴋ :** `{req}`
"""
        await m.delete()
        await Tashri.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🌷ᴛᴇʟᴇɢʀᴀᴩʜ🌷", url=f"{req}")]]
            ),
        )


__mod_name__ = "WʀɪᴛᴇTᴏᴏʟ"

__help__ = """

 ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴡʜɪᴛᴇ ᴘᴀɢᴇ ᴡɪᴛʜ ᴀ ᴘᴇɴ 🖊

❍ /write <ᴛᴇxᴛ> *:* ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.

☆............𝙱𝚈 » [⚠ᙓᖇᖇටᖇ︵⚠⁴⁰⁴](https://t.me/I_am_dead_smile)............☆
 """
