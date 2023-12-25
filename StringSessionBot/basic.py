from data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message


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

