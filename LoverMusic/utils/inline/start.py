from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from LoverMusic import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="๐ฅ โฃ๐ฉ๐ธDD ๐E ๐O ๐OUฦฆ ๐พฦฆOUืง๐ช ๐ฅ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="๐ฅ โแดแดแดแดษดแดสแดโ ๐ฅ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="๐ฅ ๐แดแดแดษชษดษข๊ฑ ๐ฅ", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="๐ฅ ๐แดแดแดแด๐ผ ๐ฅ", url=f"https://t.me/TheLoverMusic"),
            InlineKeyboardButton(
                text="๐ฅ ๐แดแดแดแดส๐ ๐ฅ", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = "https://t.me/shubhamsah1"):
    buttons = [
        [
            InlineKeyboardButton(
                text="๐ฅ ๐ฉ๐ธDD ๐E ๐O ๐OUฦฆ ๐พฦฆOUืง๐ช ๐ฅ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="๐ฅ โแดแดแดแดษดแดสแดโ ๐ฅ", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="๐ฅ ๐แดแดแดแด๐ผ ๐ฅ", url=f"https://t.me/TheLoverMusic"),
            InlineKeyboardButton(
                text="๐ฅ ๐แดแดแดแดส๐ ๐ฅ", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="๐๐ฅ๐ฅ๐ปeอฅัตeอฃlอซ๐ืงeโ๐ฅ๐ฅ๐", url=f"https://t.me/shubhamsah1"
                )
        ],
     ]
    return buttons
