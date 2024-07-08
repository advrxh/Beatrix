from beatrix.constants import Beatrix

from telebot.types import Message
import cv2
import pyautogui

from typing import List
from pathlib import Path
import difflib
import urllib.parse


def extract_torrent_name(magnet_link):
    start_index = magnet_link.find("dn=")
    if start_index == -1:
        return None

    start_index += 3  # Move past "dn="
    end_index = magnet_link.find("&", start_index)
    if end_index == -1:
        return urllib.parse.unquote(magnet_link[start_index:])

    return urllib.parse.unquote(magnet_link[start_index:end_index])


def create_progress_bars(progress):
    completed = round(25 * progress)
    return completed * "=" + (25 - completed) * "."


def camera_capture(camera_index: int = 0):
    cap = cv2.VideoCapture(camera_index)
    _, frame = cap.read()
    cv2.imwrite(Beatrix.cache_dir + "cam.png", frame)
    cap.release()


def screen_capture(all_screens: bool = False):
    pyautogui.screenshot(Beatrix.cache_dir + "scap.png", allScreens=all_screens)


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


def parse_for(
    keys: List[str] | str, case_sensitive: bool = False, whitespace: bool = True
):

    def callback(message: Message):

        if message.from_user.id != int(Beatrix.admin_id):
            return False

        if isinstance(keys, str):
            if case_sensitive:
                if message.text.startswith(keys + (" " if whitespace else "")):
                    return True
                else:
                    return False
            else:
                if message.text.lower().startswith(keys + (" " if whitespace else "")):
                    return True
                else:
                    return False

        elif isinstance(keys, list):
            for key in keys:
                if case_sensitive:
                    if message.text.startswith(key + (" " if whitespace else "")):
                        return True
                else:
                    if message.text.lower().startswith(
                        key + (" " if whitespace else "")
                    ):
                        return True
        return False

    return callback
