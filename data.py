from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("Click Here To Generate!", callback_data="generate")]

    START = """
Hey {}, I can Generate Pyrogram & Telethon String Session!
    """

    HELP = """
✨ **Available Commands** ✨

/help - This Message
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
This String Session Generator is Created By @HeisenBerg_TG !
    """
