from beatrix.bot import bot

from webbrowser import open

from telebot.types import Message


async def handle_links(message: Message):
    await bot.reply_to(message, "On your screen.")
    open(message.text)
