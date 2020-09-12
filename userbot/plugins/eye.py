"""COMMAND : .eye"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd



@borg.on(admin_cmd(pattern="eye"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    #input_str = event.pattern_match.group(1)

    #if input_str == "eye":

    await event.edit("👁👁")

    animation_chars = [

            "👁👁\n  👄  =====> Abey Ja Na Gandu",
            "👁👁\n  👅  =====> Abey Ja Na Madarchod gndu h tu",    
            "👁👁\n  💋  =====> Abey Ja Na Randi maa chuda sale",
            "👁👁\n  👄  =====> Abey Ja Na Betichod sala phattu",
            "👁👁\n  👅  =====> Abey Ja Na Behenchod kha kha se ajate h bhdwe",    
            "👁👁\n  💋  =====> Abey Ja Na Na Mard maradangi k naam par kalank",
            "👁👁\n  👄  =====> Abey Ja Na Randi gand mra bc tu",
            "👁👁\n  👅  =====> Abey Ja Na Bhosdk bhn chuda",    
            "👁👁\n  💋  =====> Abey Ja Na Chutiye gandu khe ka",
            "👁👁\n  👄  =====> Hi All, How Are You Guys..."
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 103])
