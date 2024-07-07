from beatrix.utils import screen_capture
from beatrix.constants import Beatrix
from beatrix.bot import bot

from pathlib import Path

from telebot.types import Message, InputFile


async def screen_capture_handler(message: Message, all_screens: bool = False):
    await bot.reply_to(message, "On it.")

    screen_capture(all_screens=all_screens)

    await bot.send_photo(
        Beatrix.admin_id, photo=InputFile(Path(Beatrix.cache_dir + "scap.png"))
    )
