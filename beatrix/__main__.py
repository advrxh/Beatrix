import asyncio

from beatrix.bundles import *
from beatrix.utils import *
from beatrix.bot import bot


# register handlers

## Files Bundle
bot.register_message_handler(manage_image, content_types=["photo"])
bot.register_message_handler(manage_doc_video, content_types=["document", "video"])
bot.register_message_handler(list_files, func=parse_for(["list", "files"]))
bot.register_message_handler(retrieve_file_by_name, func=parse_for(["retf", "getf"]))
bot.register_message_handler(
    retrieve_file_by_id, func=parse_for(["reti", "retid" "geti", "getid"])
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
    camera_capture_handler, func=parse_for(["cam", "pic", "cap", "camera", "photo"])
)
bot.register_message_handler(
    screen_capture_handler, func=parse_for(["scap", "spic", "screenshot"])
)
bot.register_message_handler(
    lambda message: screen_capture_handler(message, all_screens=True),
    func=parse_for(["ascap", "aspic", "ascreenshot"]),
)

## gmeet bundle
bot.register_message_handler(
    lambda message: gmeet_link_handler(message, code=True),
    func=parse_for(["meet", "gmeet"]),
)

## zoom bundle
bot.register_message_handler(handle_zoom_links, func=parse_for("zoom"))

## duck bundle
bot.register_message_handler(duck_it, func=parse_for(["duck", "duckduckgo"]))

asyncio.run(bot.polling())
