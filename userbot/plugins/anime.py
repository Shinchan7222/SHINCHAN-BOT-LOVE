import re

from shinchanbot import bot
from shinchanbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from shinchanbot.cmdhelp import CmdHelp
from shinchanbot.helpers.functions import deEmojify


@bot.on(admin_cmd(pattern="anime(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="anime(?: |$)(.*)", allow_sudo=True))
async def nope(Shinchan7222):
    shinchan = Shinchan7222.pattern_match.group(1)
    if not shinchan:
        if Shinchan7222.is_reply:
            (await Shinchan7222.get_reply_message()).message
        else:
            await edit_or_reply(Shinchan7222, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("animedb_bot", f"{(deEmojify(shinchan))}")

    await troll[0].click(
        Shinchan7222.chat_id,
        reply_to=Shinchan7222.reply_to_msg_id,
        silent=True if Shinchan7222.is_reply else False,
        hide_via=True,
    )
    await Shinchan7222.delete()
    

CmdHelp("anime").add_command(
  "anime", "<anime name>", "Searches for the given anime and sends the details."
).add()
