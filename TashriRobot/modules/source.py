from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from TashriRobot import OWNER_ID, dispatcher
from TashriRobot import pbot as client

Tashri = "https://te.legra.ph/file/ab836a124f9484c367697.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Tashri,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

╔═════ஜ۩۞۩ஜ════╗
**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [⚠ᙓᖇᖇටᖇ︵⚠⁴⁰⁴](https://t.me/i_am_dead_smile)
**» ᴩʏᴛʜᴏɴ  :** `{y()}`
**» ʟɪʙʀᴀʀʏ  :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ  :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ  :** `{z}`                                      
  
╚═════ஜ۩۞۩ஜ════╝

**[˹ᴍɪss 𝐑σႦσ𝐓 ✗ ᴍᴜꜱɪᴄ](t.me/{dispatcher.bot.username}) sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ",f"tg://user?id={OWNER_ID}"
                    ),
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ",
                        url="https://graph.org/file/9b0340dc3374bef96a162.mp4",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "⚡Rᴇᴩᴏ⚡"
_help__ = """
 /repo  ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 
 /source ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ
"""
