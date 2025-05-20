from copy import deepcopy
from typing import Any, Dict

from gsuid_core.bot import Bot
from gsuid_core.sv import Plugins


async def send_diff_msg(bot: Bot, code: Any, data: Dict, at_sender=False):
    for retcode in data:
        if code == retcode:
            return await bot.send(data[retcode], at_sender)


def remove_prefix(plugin: Plugins, text: str):
    prefixs = deepcopy(plugin.prefix)
    if "" in prefixs:
        prefixs.remove("")

    if not plugin.disable_force_prefix:
        for pre in plugin.force_prefix:
            prefixs.append(pre)

    prefixs = list(set(prefixs))
    for pre in prefixs:
        if (text.startswith(pre)):
            text = text.replace(pre, "", 1)
            break
    return text
