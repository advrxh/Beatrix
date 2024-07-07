import asyncio

from beatrix.bundles import *
from beatrix.utils import *
from beatrix.bot import bot


# register handlers
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


asyncio.run(bot.polling())
