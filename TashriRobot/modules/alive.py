import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from TashriRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID

PHOTO = [
    "https://graph.org/file/c0b2daa066d96d61571e4.jpg",
    "https://graph.org/file/7d3f01482155b1e1eb344.jpg",
    "https://graph.org/file/704f892c63d58e6f12a80.jpg",
    "https://graph.org/file/ec2c38e61ce2a0b84d484.jpg",
    "https://graph.org/file/e602356bafe2799f708bd.jpg",
]

MissXRobotMusic = [
    [
        InlineKeyboardButton(text="𝐎𝐰𝐧𝐞𝐫", url=f"tg://user?id="1138802391"),
        InlineKeyboardButton(text="𝐆𝐫𝐨𝐮𝐩", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="α∂∂ мє ιη уσυ ¢нαт",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

lol = "https://graph.org/file/ec2c38e61ce2a0b84d484.jpg"


@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.5)
    await accha.edit("Radhe Radhe..")
    await asyncio.sleep(0.5)
    await accha.edit("Radhe Krishna......")
    await asyncio.sleep(0.5)
    await accha.edit("Krishna Radhe..")
    await asyncio.sleep(0.5)
    await accha.edit("Krishna Krishna......")
    await accha.delete()
    await asyncio.sleep(0.5)
    umm = await m.reply_sticker(
        "CAACAgUAAxkDAAJHbmLuy2NEfrfh6lZSohacEGrVjd5wAAIOBAACl42QVKnra4sdzC_uKQQ"
    )
    await umm.delete()
    await asyncio.sleep(0.8)
    await m.reply_photo(
        lol,
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ♥️ 『[ᴍɪss 𝐑σႦσ𝐓 ✗ ᴍᴜꜱɪᴄ ](f"t.me/{BOT_USERNAME}")』**
   ♥️
  » ᴍʏ ᴏᴡɴᴇʀ : [⚠ᙓᖇᖇටᖇ︵⚠⁴⁰⁴](https://t.me/i_am_dead_smile)
  
  
  » ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : {tver}
  
  » ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : {pver}
  
  » ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : {pyver()}
   ♥️💛""",                                                
        reply_markup=InlineKeyboardMarkup(Tashri),
    )
__mod_name__ = "ᴀʟɪᴠᴇ"
__help__ = """

*ᴜsᴇʀ ᴄᴏᴍᴍᴀɴᴅs*:
» /alive*:* ᴛᴏ ᴄʜᴇᴀᴋ ❓  ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ?

☆............©️𝙱𝚈 » [⚠ᙓᖇᖇටᖇ︵⚠⁴⁰⁴](https://t.me/i_am_dead_smile)............☆"""
