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

# Constants
FORBIDDEN_KEYWORDS = [
    "porn", "xxx", "NCERT", "ncert", "ans", "Pre-Medical", "kinematics",
    "Experiments", "Experiment", "experiment", "experimens", "XII", "page",
    "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt",
    "JEE", "ALLEN", "NEET", "jee", "neet", "ans"
]
START_TEXT = """..."""  # Your START_TEXT content here.
SHUKLA = ["..."]  # List of image URLs.

# Start Command
@app.on_message(filters.command("start"))
async def start_command_handler(_, msg):
    buttons = [
        [InlineKeyboardButton("▪️ ᴀᴅᴅ ᴍᴇ ▪️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [InlineKeyboardButton("▪️ ʜᴀɴᴅʟᴇʀ ▪️", callback_data="vip_back")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await msg.reply_photo(
        random.choice(SHUKLA),
        caption=START_TEXT,
        reply_markup=reply_markup
    )

# Callback Query Handlers
@app.on_callback_query(filters.regex("vip_back"))
async def vip_back_callback_handler(_, query: CallbackQuery):
    gd_buttons = [
        [InlineKeyboardButton("▪️ ᴏᴡɴᴇʀ ▪️", url="https://t.me/SHIVANSHDEVS"),
         InlineKeyboardButton("▪️ ʙᴀᴄᴋ ▪", callback_data="back_to_start"),
         InlineKeyboardButton("▪️ sᴜᴘᴘᴏʀᴛ ▪️", url="https://t.me/MASTIWITHFRIENDSXD")]
    ]
    await query.message.edit_caption(caption=START_TEXT, reply_markup=InlineKeyboardMarkup(gd_buttons))

@app.on_callback_query(filters.regex("back_to_start"))
async def back_to_start_callback_handler(_, query: CallbackQuery):
    await query.answer()
    await query.message.delete()
    await start_command_handler(_, query.message)

# Uptime and Bot Stats
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

# Message Handlers
@app.on_message()
async def handle_message(client, message):
    if message.text and any(keyword.lower() in message.text.lower() for keyword in FORBIDDEN_KEYWORDS):
        await message.delete()
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")

@app.on_edited_message(filters.group & ~filters.me)
async def handle_edited_messages(_, edited_message: Message):
    if edited_message.text and len(edited_message.text.split()) > 20:
        await edited_message.delete()

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    if message.document and message.document.mime_type == "application/pdf":
        await message.reply_text(f"⬤ ʜᴇʏ @{message.from_user.username}, ᴅᴏɴ'ᴛ sᴇɴᴅ ᴘᴅғ ғɪʟᴇs ʜᴇʀᴇ!")
        await message.delete()
