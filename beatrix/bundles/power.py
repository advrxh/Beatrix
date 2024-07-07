from beatrix.constants import Beatrix
from beatrix.bot import bot

import time
import subprocess

from telebot.types import Message


async def handle_shutdown(message: Message):

    countdown = 3

    try:
        countdown = message.text.split()[1]
    except IndexError:
        pass

    await bot.reply_to(message, " Heard, Shutting down in...")

    time.sleep(1)
    for i in range(countdown):
        await bot.send_message(Beatrix.admin_id, f"{i+1}...")
        time.sleep(1)

    await bot.send_message(Beatrix.admin_id, "bye bye.")

    subprocess.run(["shutdown", "/s", "/t", "1"])


async def handle_sleep(message: Message):
    countdown = 3

    try:
        countdown = message.text.split()[1]
    except IndexError:
        pass

    await bot.reply_to(message, "I get it, even lovers need a holiday.")
    await bot.send_message(Beatrix.admin_id, "Countdown for sleep in...")

    time.sleep(1)
    for i in range(countdown):
        await bot.send_message(Beatrix.admin_id, f"{i+1}...")
        time.sleep(1)

    await bot.send_message(Beatrix.admin_id, "buh-bye.")
    subprocess.run("rundll32.exe powrprof.dll,SetSuspendState 0,1,0".split())
