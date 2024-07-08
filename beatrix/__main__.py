import asyncio

from beatrix.bundles import *
from beatrix.utils import *
from beatrix.bot import bot
from beatrix.state import Beatrix as BeatrixState
from beatrix.constants import Beatrix


# register handlers

## Files Bundle
bot.register_message_handler(manage_image, content_types=["photo"])
bot.register_message_handler(manage_doc_video, content_types=["document", "video"])
bot.register_message_handler(
    list_files, func=parse_for(["list", "files"], whitespace=False)
)
bot.register_message_handler(retrieve_file_by_name, func=parse_for(["retf", "getf"]))
bot.register_message_handler(
    retrieve_file_by_id,
    func=parse_for(["reti", "retid" "geti", "getid"]),
)
bot.register_message_handler(delete_file_by_name, func=parse_for(["delf", "remf"]))
bot.register_message_handler(
    delete_file_by_id, func=parse_for(["deli", "delid" "remi", "remid"])
)

## Keystrokes bundle
bot.register_message_handler(
    lambda message: stroke_kbt(message, all_screens=False), func=parse_for(["kbt"])
)
bot.register_message_handler(
    lambda message: stroke_kbb(message, all_screens=False), func=parse_for(["kbb"])
)
bot.register_message_handler(
    lambda message: stroke_kbt(message, all_screens=True), func=parse_for(["akbt"])
)
bot.register_message_handler(
    lambda message: stroke_kbb(message, all_screens=True), func=parse_for(["akbb"])
)

## camera and screen capture bundle
bot.register_message_handler(
    camera_capture_handler,
    func=parse_for(["cam", "pic", "cap", "camera", "photo"], whitespace=False),
)
bot.register_message_handler(
    screen_capture_handler,
    func=parse_for(["scap", "spic", "screenshot"], whitespace=False),
)
bot.register_message_handler(
    lambda message: screen_capture_handler(message, all_screens=True),
    func=parse_for(["ascap", "aspic", "ascreenshot"], whitespace=False),
)

## gmeet bundle
bot.register_message_handler(
    lambda message: gmeet_link_handler(message, code=True),
    func=parse_for(["meet", "gmeet"], whitespace=False),
)

## zoom bundle
bot.register_message_handler(handle_zoom_links, func=parse_for("zoom"))

## duck bundle
bot.register_message_handler(duck_it, func=parse_for(["duck", "duckduckgo"]))

## power bundle
bot.register_message_handler(
    handle_shutdown, func=parse_for(["shut", "shutdown"], whitespace=False)
)
bot.register_message_handler(
    handle_sleep, func=parse_for(["sleep", "snooze"], whitespace=False)
)

## broswer bundle
bot.register_message_handler(
    handle_links, func=parse_for(["http://", "https://"], whitespace=False)
)

## volume bundle
bot.register_message_handler(handle_volume, func=parse_for("vol"))

## torrent bundle

if BeatrixState.qb:
    bot.register_message_handler(
        list_torrents,
        func=parse_for(["all torrents", "list tor", "all tor"], whitespace=False),
    )

    bot.register_message_handler(
        lambda message: list_torrents(message, filter="downloading"),
        func=parse_for(["downloads", "list downloads", "dall tor"], whitespace=False),
    )

    bot.register_message_handler(
        download_torrent, func=parse_for(["dwld", "tor", "torrent"])
    )

    bot.register_message_handler(
        lambda message: download_torrent(message, series=True),
        func=parse_for(["sdwld", "stor", "storrent"]),
    )


async def main():
    await bot.send_message(Beatrix.admin_id, "I'm up and running!")
    await bot.infinity_polling()


if __name__ == "__main__":
    asyncio.run(main())
