from beatrix.constants import Beatrix
from beatrix.bot import bot

from webbrowser import open
import time
import keyboard

import win32clipboard as clip

from telebot.types import Message


async def gmeet_link_handler(message: Message, code: bool = False):
    try:
        code = message.text.split(" ")[1]
        open(f"https://meet.google.com/{code}")
    except IndexError:
        open("https://meet.google.com/new")
        await bot.reply_to(message, "Wait a moment.")
        time.sleep(5)
        keyboard.send("ctrl+l")
        time.sleep(0.5)
        keyboard.send("ctrl+c")
        time.sleep(0.5)
        clip.OpenClipboard()
        await bot.reply_to(message, clip.GetClipboardData())
        clip.CloseClipboard()
        await bot.send_message(Beatrix.admin_id, "Here you go!")
