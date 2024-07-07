from beatrix.constants import Beatrix
from beatrix.bot import bot

import subprocess

from telebot.types import Message


async def handle_zoom_links(message: Message):
    await bot.reply_to(message, "We're gonna go zooming.")

    try:
        subprocess.run(
            [
                Beatrix.zoom_executable,
                f'--url="{message.text.split()[1]}"',
            ]
        )
    except IndexError:
        await bot.reply_to(
            message,
            "Invalid Link ```Syntax:\nzoom <meeting-link>```",
            parse_mode="Markdown",
        )
