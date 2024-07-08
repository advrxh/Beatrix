from beatrix.constants import Beatrix
from beatrix.state import Beatrix as BeatrixState

from telebot.async_telebot import AsyncTeleBot
from qbittorrent import Client

try:
    qb = Client(f"http://127.0.0.1:{Beatrix.qbit_port}")
    BeatrixState.qb = True
except ConnectionError:
    BeatrixState.qb = False


bot = AsyncTeleBot(Beatrix.token)
