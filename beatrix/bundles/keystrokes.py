from beatrix.utils import screen_capture
from beatrix.constants import Beatrix
from beatrix.bot import bot

import keyboard
from pathlib import Path

from telebot.types import Message, InputFile


async def stroke_kbt(message: Message, all_screens: bool = False):
    commands = " ".join(message.text.split()[1:])
    keyboard.write(commands)

    await bot.reply_to(message, "Done.")

    screen_capture(all_screens=all_screens)

    await bot.send_photo(
        Beatrix.admin_id, photo=InputFile(Path(Beatrix.cache_dir + "scap.png"))
    )


async def stroke_kbb(message: Message, all_screens: bool = False):
    commands = "+".join(message.text.split()[1:])
    keyboard.send(commands)

    await bot.reply_to(message, "Done.")

    screen_capture(all_screens=all_screens)

    await bot.send_photo(
        Beatrix.admin_id, photo=InputFile(Path(Beatrix.cache_dir + "scap.png"))
    )
