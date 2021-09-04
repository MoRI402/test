from . import *
from telethon import events

chat = 1152077444

@asst.on(events.NewMessage(pattern="\\/search@copyninja2_bot ?(.*)"))
async def _(e):
    key = e.pattern_match.group(1)
    txt = ""
    async for x in bot.iter_messages(chat, search=key, reverse=True):
        txt += f"https://t.me/anime_ocean/{x.id}\n"
    if txt:
        await e.reply(txt, link_preview=False,)