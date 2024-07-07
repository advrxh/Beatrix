from beatrix.constants import Beatrix
from beatrix.bot import bot

import keyboard
import time

from telebot.types import Message


async def handle_volume(message: Message):

    try:
        change = int(message.text[3:])

        if change > 0:
            for i in range(abs(change)):
                time.sleep(0.5)
                keyboard.press("volume up")

        else:
            for i in range(abs(change)):
                time.sleep(0.5)
                keyboard.press("volume down")

        await bot.reply_to(message, "Done.")

    except ValueError:
        change = message.text[3:]

        if change.startswith("d"):
            keyboard.press("volume down")
        else:
            keyboard.press("volume up")

        await bot.reply_to(message, "Done.")
