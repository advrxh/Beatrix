from beatrix.constants import Beatrix
from beatrix.bot import bot
from beatrix.utils import create_progress_bars, extract_torrent_name

import time

from telebot.types import Message
from qbittorrent import Client

qb = Client(f"http://127.0.0.1:{Beatrix.qbit_port}")


info_headers = [
    "name",
    "progress",
    "state",
    "eta",
    "size",
    "downloaded",
    "amount_left",
    "magnet_uri",
]


def format_torrent_deets(torrent):

    formatted_message = ""

    for header in info_headers:
        if header == "progress":
            formatted_message += f"\n*{header.title()}: * ``` ({round(100*torrent[header])}%) {create_progress_bars(torrent[header])}```"
            continue

        if header == "eta":
            eta = torrent["eta"]

            if eta != 8640000:
                eta %= 3600
                minutes = round(eta / 60, 2)
            else:
                minutes = 0

            formatted_message += f"\n*{header.title()}:* ``` {minutes} m```"
            continue

        if header in ["size", "downloaded", "amount_left"]:
            formatted_message += (
                f"\n*{header.title()}:* `{round(torrent[header]/(1024 ** 2), 2)}` MB"
            )
            continue

        if header == "state":
            formatted_message += f"\n*{header.title()}:* `{torrent[header]}`"

        else:
            formatted_message += f"\n*{header.title()}:* ``` {torrent[header]}```"

    return formatted_message


async def list_torrents(message: Message, filter: str = "all"):
    for torrent in qb.torrents(filter=filter):
        await bot.send_message(
            Beatrix.admin_id, text=format_torrent_deets(torrent), parse_mode="Markdown"
        )


async def download_torrent(message: Message, series: bool = False):
    magnet = message.text.split()[1]
    name = extract_torrent_name(magnet)

    qb.download_from_link(
        magnet, savepath=Beatrix.binge_box_dir + ("Series/" if series else "") + name
    )

    info = qb.torrents(sort="added_on", reverse=True)[0]

    await bot.reply_to(message, "Downloading now...")

    while info.get("state", None) != "downloading":
        time.sleep(0.5)
        info = qb.torrents(sort="added_on", reverse=True)[0]

    info = qb.torrents(sort="added_on", reverse=True)[0]
    info_message = await bot.send_message(
        Beatrix.admin_id, text=format_torrent_deets(info), parse_mode="Markdown"
    )

    while info.get("state", None) != "pausedUP":
        time.sleep(10)
        info = qb.torrents(sort="added_on", reverse=True)[0]
        await bot.edit_message_text(
            format_torrent_deets(info),
            parse_mode="Markdown",
            message_id=info_message.id,
            chat_id=info_message.chat.id,
        )

    await bot.reply_to(message, "Finished downloading!")
