import logging
import os
import platform
import psutil
import time
import random
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import BOT_USERNAME, OWNER_ID
from PROTECTOR import PROTECTOR as app
from config import *
# Constants
FORBIDDEN_KEYWORDS = ["porn", "xxx", "NCERT", "ncert", "ans", "Pre-Medical", "kinematics", "Experiments", "Experiment", "experiment", "experimens", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt", "JEE", "ALLEN", "NEET", "jee", "neet", "ans"]
START_TEXT = """**╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼────⏤͟͟͞͞★**\n**┆◍ ʜᴇʏ, ɪ ᴀᴍ : [𝐆ʀᴏᴜᴘ ꭙ 𝐒ʜɪᴇʟᴅ](https://t.me/GroupXshieldBot) **\n**┆● ᴡᴇ ᴇɴsᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ sᴇᴄᴜʀɪᴛʏ💻 !\n**┊● ᴛʜɪs ʙᴏᴛ ᴄᴀɴ ʀᴇᴍᴏᴠᴇ ʟᴏɴɢ ᴛᴇxᴛ**\n**╰─────────────────────────**\n**──────────────────────────**\n**❖ ᴛʜɪs ʙᴏᴛ ᴄᴀɴ ʀᴇᴍᴏᴠᴇ ᴇᴅɪᴛᴇᴅ ᴍsɢs **\n**──────────────────────────**\n**❖ ᴛʜɪs ʙᴏᴛ ᴄᴀɴ ʀᴇᴍᴏᴠᴇ ᴄᴏᴘʏʀɪɢʜᴛ ᴍᴀᴛᴇʀɪᴀʟ...!**\n**──────────────────────────**\n**❖ ᴊᴜsᴛ ᴀᴅᴅ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴀᴅᴍɪɴ !!**\n**──────────────────────────**\n**❖ Uᴘᴅᴀᴛᴇ ⏤͟͟͞͞  [❖ ∣ Tʜᴇ sᴛʀᴀɴɢᴇʀ ∣ ❖](https://t.me/StrangerAssociation) **\n**──────────────────────────**"""

SHUKLA = [
    "https://graph.org/file/9bba2b7ee9ba3806de65d.jpg",
    "https://graph.org/file/ef82f289043a4fa74f8ff.jpg",
    "https://graph.org/file/9c27c68958e06ae074c38.jpg",
    "https://graph.org/file/0ff325b1d2efe80299aa3.jpg",
    "https://graph.org/file/41167b953cf3579853d47.jpg",
    "https://graph.org/file/bd93ab42e69305f274028.jpg",
    "https://graph.org/file/97575db5586c05d6b2898.jpg",
    "https://graph.org/file/07c393fdf931a407c9bc0.jpg",
    "https://graph.org/file/f332767490ad3a5ca20e8.jpg",
    "https://graph.org/file/f3449e9069667f647d14e.jpg",
    "https://graph.org/file/9f51cdc739f907cbd2c7e.jpg",
    "https://telegra.ph/file/d7a6a923c38e051ce35f3.jpg",
    "https://graph.org/file/f86b71018196c5cfe7344.jpg",
    "https://graph.org/file/a3db9af88f25bb1b99325.jpg",
    "https://graph.org/file/5b344a55f3d5199b63fa5.jpg",
    "https://graph.org/file/84de4b440300297a8ecb3.jpg",
    "https://graph.org/file/84e84ff778b045879d24f.jpg",
    "https://graph.org/file/a4a8f0e5c0e6b18249ffc.jpg",
    "https://graph.org/file/ed92cada78099c9c3a4f7.jpg",
    "https://graph.org/file/d6360613d0fa7a9d2f90b.jpg",
    "https://graph.org/file/37248e7bdff70c662a702.jpg",
    "https://graph.org/file/0bfe29d15e918917d1305.jpg",
    "https://graph.org/file/16b1a2828cc507f8048bd.jpg",
    "https://graph.org/file/e6b01f23f2871e128dad8.jpg",
    "https://graph.org/file/cacbdddee77784d9ed2b7.jpg",
    "https://graph.org/file/ddc5d6ec1c33276507b19.jpg",
    "https://graph.org/file/39d7277189360d2c85b62.jpg",
    "https://graph.org/file/5846b9214eaf12c3ed100.jpg",
    "https://graph.org/file/ad4f9beb4d526e6615e18.jpg",
    "https://graph.org/file/3514efaabe774e4f181f2.jpg",    
]

##---------------------------------------------------------------------------------
@app.on_message(filters.command("start"))
async def start_command_handler(_, msg):
    buttons = [
        [InlineKeyboardButton("▪️ ᴀᴅᴅ ᴍᴇ  ▪️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [InlineKeyboardButton("▪️ ʜᴀɴᴅʟᴇʀ ▪️", callback_data="vip_back")]
        
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await msg.reply_photo(
        random.choice(SHUKLA),
        caption=START_TEXT,
        reply_markup=reply_markup
    )

# Callback Query Handler
gd_buttons = [
    [InlineKeyboardButton("▪️ ᴏᴡɴᴇʀ ▪️", url=f"https://t.me/SHIVANSHDEVS"),
     InlineKeyboardButton("▪️ ʙᴀᴄᴋ ▪", callback_data="back_to_start"),
     InlineKeyboardButton(" ▪️sᴜᴘᴘᴏʀᴛ ▪️", url="https://t.me/MASTIWITHFRIENDSXD")]
]

@app.on_callback_query(filters.regex("vip_back"))
async def vip_back_callback_handler(_, query: CallbackQuery):
    await query.message.edit_caption(caption=START_TEXT, reply_markup=InlineKeyboardMarkup(gd_buttons))

@app.on_callback_query(filters.regex("back_to_start"))
async def back_to_start_callback_handler(_, query: CallbackQuery):
    await query.answer()
    await query.message.delete()
    await start_command_handler(_, query.message)


##---------------------------------------------------------------------------------
# Bot Functionality

start_time = time.time()

def time_formatter(milliseconds: float) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def size_formatter(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {unit}"

@app.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')

    python_version = platform.python_version()

    reply_text = (
        f"❖ ᴄᴏᴘʏʀɪɢʜᴛ ʙᴏᴛ ᴘɪɴɢ sᴛᴀᴛs ⏤͟͟͞͞★\n\n"
        f"● ᴜᴘᴛɪᴍᴇ ➥ {uptime}\n"
        f"● ᴄᴘᴜ ➥ {cpu}%\n"
        f"● ᴛᴏᴛᴇʟ ꜱᴛᴏʀᴀɢᴇ ➥ {size_formatter(storage.total)}\n"
        f"● ᴜsᴇᴅ ➥ {size_formatter(storage.used)}\n"
        f"● ғʀᴇᴇ ➥ {size_formatter(storage.free)}\n"
        f"● ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ➥ {python_version}\n\n"
        f"❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ sʜɪᴠᴀɴsʜ-xᴅ"
    )

    await message.reply(reply_text, quote=True)

# Handle Forbidden Keywords

@app.on_message()
async def handle_message(client, message):
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")
    elif any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")

# Delete long edited messages but keep short messages and emoji reactions

async def delete_long_edited_messages(client, edited_message: Message):
    if edited_message.text:
        if len(edited_message.text.split()) > 20:
            await edited_message.delete()
    else:
        if edited_message.sticker or edited_message.animation or edited_message.emoji:
            return

@app.on_edited_message(filters.group & ~filters.me)
async def handle_edited_messages(_, edited_message: Message):
    await delete_long_edited_messages(_, edited_message)

# Delete long messages in groups and reply with a warning

MAX_MESSAGE_LENGTH = 25 # Define the maximum allowed length for a message

async def delete_long_messages(client, message: Message):
    if message.text:
        if len(message.text.split()) > MAX_MESSAGE_LENGTH:
            await message.delete()

@app.on_message(filters.group & ~filters.me)
async def handle_messages(_, message: Message):
    await delete_long_messages(_, message)

# -----------------------------------------------------------------------------------


async def delete_pdf_files(client, message):
    if message.document and message.document.mime_type == "application/pdf":
        warning_message = f"⬤ ʜᴇʏ {user_mention} ᴅᴏɴ'ᴛ sᴇɴᴅ ᴘᴅғ ғɪʟᴇs ʙᴀʙʏ, ғᴏʀ ᴄᴏᴘʏʀɪɢʜᴛ ᴄʟɪᴍʙ."
        await message.reply_text(warning_message)
        await message.delete()
    else:  
        pass

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    await delete_pdf_files(client, message)
