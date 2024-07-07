from beatrix.constants import Beatrix
from telebot.types import Message

from typing import List
from pathlib import Path
import difflib


def get_closest_match(input_str, possibilities):
    matches = difflib.get_close_matches(input_str, possibilities, n=1, cutoff=0.6)
    return matches[0] if matches else None


def file_list_format():
    file_list = get_file_list()
    file_names = []

    for file in file_list:
        file_names.append(file_list[file]["file"])

    file_list_message = "```"

    for idx in file_list:
        if file_list[idx]["is_dir"]:
            file_list_message += f"\n{idx}. {file_list[idx]['file']}/"

    for idx in file_list:
        if not file_list[idx]["is_dir"]:
            file_list_message += f"\n{idx}. {file_list[idx]['file']}"

    file_list_message += "```"

    return file_list_message


def get_file_list(cdir=Beatrix.downloads_dir):

    files = {}

    for i, cfile in enumerate(Path(cdir).iterdir()):
        files[i + 1] = {"file": cfile.name}
        files[i + 1]["is_dir"] = Path(cdir + cfile.name).is_dir()

    return files


def parse_for(keys: List[str] | str, case_sensitive: bool = False):

    def callback(message: Message):

        if isinstance(keys, str):
            if case_sensitive:
                if message.text.startswith(keys):
                    return True
                else:
                    return False
            else:
                if message.text.lower().startswith(keys):
                    return True
                else:
                    return False

        if isinstance(keys, list):
            for key in keys:
                if case_sensitive:
                    if message.text.startswith(key):
                        return True
                else:
                    if message.text.lower().startswith(key):
                        return True

        return False

    return callback
