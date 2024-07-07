from beatrix.bot import bot
from beatrix.constants import Beatrix
from beatrix.utils import *

from telebot.types import Message, InputFile

import requests
from pathlib import Path
import shutil


async def delete_file(message: Message = None, filename: str = None, idx: int = None):
    if filename is not None:

        try:
            if not Path(Beatrix.downloads_dir + filename).is_dir():
                Path(Beatrix.downloads_dir + filename).unlink()
            else:
                shutil.rmtree(Path(Beatrix.downloads_dir + filename))

            await bot.reply_to(
                message,
                f"Deleted the location! ```{filename}```",
                parse_mode="Markdown",
            )
            return
        except Exception as e:
            await bot.reply_to(message, e)
            return

    try:
        if idx is None:
            idx = int(message.text)
    except:
        await bot.reply_to(message, "Invalid file.")
        return

    file_list = get_file_list()

    if idx in file_list.keys():
        filename = file_list[idx]["file"]
        try:
            if not Path(Beatrix.downloads_dir + filename).is_dir():
                Path(Beatrix.downloads_dir + filename).unlink()
            else:
                shutil.rmtree(Path(Beatrix.downloads_dir + filename))

            await bot.reply_to(
                message,
                f"Deleted the location! ```{filename}```",
                parse_mode="Markdown",
            )
        except Exception as e:
            await bot.reply_to(message, e)
    else:
        await bot.reply_to(message, "Invalid file.")


async def upload_file(message: Message = None, filename: str = None, idx: int = None):
    if filename is not None:
        await bot.reply_to(message, "Here you go,")
        await bot.send_document(
            Beatrix.admin_id,
            InputFile(Beatrix.downloads_dir + filename),
            caption=filename,
        )
        return

    try:
        if idx is None:
            idx = int(message.text)
    except:
        await bot.reply_to(message, "Invalid file.")
        return

    file_list = get_file_list()

    if idx in file_list.keys() and file_list[idx]["is_dir"] is not True:
        await bot.reply_to(message, "Here you go,")
        await bot.send_document(
            Beatrix.admin_id,
            InputFile(Beatrix.downloads_dir + file_list[idx].get("file")),
            caption=file_list[idx].get("file"),
        )
    elif idx in file_list.keys() and file_list[idx]["is_dir"] is True:
        await bot.reply_to(message, "Here you go,")
        for _file in Path(Beatrix.downloads_dir + file_list[idx].get("file")).iterdir():
            await bot.send_document(
                Beatrix.admin_id,
                InputFile(
                    Beatrix.downloads_dir
                    + file_list[idx].get("file")
                    + r"\\"
                    + _file.name
                ),
                caption=_file.name,
            )
    else:
        await bot.reply_to(message, "Invalid file.")


async def list_files(message: Message):

    file_list_message = file_list_format()

    await bot.reply_to(
        message,
        f"Here are the list of files: {file_list_message}",
        parse_mode="Markdown",
    )


async def retrieve_file_by_name(message: Message):
    file_arg = None

    try:
        file_arg = message.text.split(" ")[1]
    except IndexError:
        pass

    else:
        file_name_list = [file["file"] for file in list(get_file_list().values())]
        close_match = get_closest_match(file_arg, file_name_list)

        if (file_arg in file_name_list) or (close_match is not None):
            await upload_file(message=message, filename=close_match)


async def retrieve_file_by_id(message: Message):
    file_arg = None

    try:
        file_arg = int(message.text.split(" ")[1])
    except IndexError:
        pass

    else:
        keys_list = [key for key in list(get_file_list().keys())]

        if file_arg in keys_list:
            await upload_file(message=message, idx=file_arg)


async def delete_file_by_name(message: Message):
    file_arg = None

    try:
        file_arg = message.text.split(" ")[1]
    except IndexError:
        pass

    else:
        file_name_list = [file["file"] for file in list(get_file_list().values())]
        close_match = get_closest_match(file_arg, file_name_list)

        if (file_arg in file_name_list) or (close_match is not None):
            await delete_file(message=message, filename=close_match)


async def delete_file_by_id(message: Message):
    file_arg = None

    try:
        file_arg = int(message.text.split(" ")[1])
    except IndexError:
        pass

    else:
        keys_list = [key for key in list(get_file_list().keys())]

        if file_arg in keys_list:
            await delete_file(message=message, idx=file_arg)


async def manage_image(message: Message):

    max_id = ""
    prev_size = 0

    for photo in message.photo:
        if photo.file_size > prev_size:
            max_id = photo.file_id

    dfile = await bot.get_file(max_id)

    f = requests.get(
        f"https://api.telegram.org/file/bot{Beatrix.token}/{dfile.file_path}",
        allow_redirects=True,
    )

    name = (
        f.url.split("/")[-1]
        if message.caption is None
        else message.caption + "".join(f.url.split("/")[-1].partition(".")[1:])
    )

    path = Path(Beatrix.downloads_dir + name)

    open(path, "wb").write(f.content)

    await bot.reply_to(
        message, f"I've downloaded it at as: ```{name}```", parse_mode="Markdown"
    )


async def manage_doc_video(message: Message):

    dtype = "video" if message.video is not None else "document"
    name = message.video.file_name if dtype == "video" else message.document.file_name
    name = name.partition(".")[0]

    if dtype == "video":
        dfile = await bot.get_file(message.video.file_id)
    else:
        dfile = await bot.get_file(message.document.file_id)

    f = requests.get(
        f"https://api.telegram.org/file/bot/{Beatrix.token}/{dfile.file_path}",
        allow_redirects=True,
    )

    if message.caption is not None:
        name = message.caption.partition(".")[0]

    if name is None and message.caption is None:
        name = f.url.split("/")[-1].partition(".")[0]

    file_type = "".join(f.url.split("/")[-1].partition(".")[1:])

    path = Path(Beatrix.downloads_dir + name + file_type)
    open(path, "wb").write(f.content)

    await bot.reply_to(
        message,
        f"I've downloaded it at as: ```{name + file_type}```",
        parse_mode="Markdown",
    )
