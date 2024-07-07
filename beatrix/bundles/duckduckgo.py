from beatrix.constants import Beatrix
from beatrix.bot import bot

from webbrowser import open

from telebot.types import Message


async def duck_it(message: Message):
    await bot.reply_to(message, "oooohyeah, I like to duck it nice.")
    open(f"https://duckduckgo.com?q={message.text.split()[1]}")
