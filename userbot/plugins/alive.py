
# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in Shinchan Userbot by @H1M4N5HU0P

import asyncio
import random
from telethon import events
from userbot import ALIVE_NAME, shinchanversion
from shinchanbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# ๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "๐โ๐โโโ๐ธโ๐น๐๐"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for รรลฎ$HรณpBรศ

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

shinchan = bot.uid

edit_time = 10
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/a341395e71bc0cd5b2db5.jpg"
file2 = "https://telegra.ph/file/a341395e71bc0cd5b2db5.jpg"
file3 = "https://telegra.ph/file/a341395e71bc0cd5b2db5.jpg"
file4 = "https://telegra.ph/file/a341395e71bc0cd5b2db5.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "  __**๐ฅ๐ฅ๐โ๐โโโ๐ธโ๐น๐๐ ๐๐ ๐ธ๐๐๐๐ผ๐ฅ๐ฅ**__\n\n"

pm_caption += (
    f"                 ๐๐๐ธ๐๐๐ผโ๐\n**  ใ๐[{DEFAULTUSER}](tg://user?id={shinchan})๐ใ**\n\n"
)

pm_caption += "๐ก๏ธTELETHON๐ก๏ธ : `1.15.0` \n\n"

pm_caption += f"๐๐โ๐โโโ๐ธโ๐น๐๐๐ : `{shinchanversion}`\n\n"

pm_caption += f"๐ฑSUDO๐ฑ            : `{sudou}`\n\n"

pm_caption += "๐CHANNEL๐๏ธ   : [แดแดษชษด](https://t.me/Shinchan_USERBOT)\n\n"

pm_caption += "๐CREATOR๐    : [Shinchan](https://t.me/Shinchan7222)\n\n"

pm_caption += "๐คฉSUPPORTER๐คฉ    :[HIMANSHU](https://t.me/H1M4N5HU0P)\n\n"

pm_caption += "      [๐ฅREPO๐ฅ](https://github.com/Shinchan7222/ShinchanOP) ๐น [๐License๐](https://github.com/Shinchan7222/ShinchanOP/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file4)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file1)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "shinchan", None, "To check am i alive with your favorite alive pic"
).add()
