from beatrix.utils import camera_capture
from beatrix.constants import Beatrix
from beatrix.bot import bot

from pathlib import Path

from telebot.types import Message, InputFile


async def camera_capture_handler(message: Message, camera_index: int = 0):
    await bot.reply_to(message, "On it.")

    camera_capture(camera_index=camera_index)

    await bot.send_photo(
        Beatrix.admin_id, photo=InputFile(Path(Beatrix.cache_dir + "cam.png"))
    )
