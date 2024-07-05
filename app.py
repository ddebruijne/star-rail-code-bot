import os
import datetime
import discord
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from core.utils import (
    get_star_rail_codes,
    get_zzz_codes
)

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
sched = AsyncIOScheduler()


async def printStarRailCodes():
    codes = get_star_rail_codes()
    if len(codes) > 0:
        channelid = int(os.getenv("CHANNEL_ID"))
        print(channelid)
        channel = client.get_channel(channelid)
        await client.wait_until_ready()
        for code in codes:
            embed = discord.Embed(
                title="New code for Honkai Star Rail",
                timestamp=datetime.datetime.now()
            )
            embed.set_author(name="Prydwen.gg", url="https://www.prydwen.gg/star-rail/", icon_url="https://www.prydwen.gg/favicon-32x32.png?v=c3220c3ea85e0f6e55de4153c4b2303b")
            embed.add_field(name="Code", value=code[0])
            embed.add_field(name="Reward", value=code[1])
            embed.set_image(url="https://upload.wikimedia.org/wikipedia/en/thumb/b/b1/Honkai-Star-Rail.png/330px-Honkai-Star-Rail.png")
            await channel.send(embed=embed)

    return

async def printZenlessCodes():
    codes = get_zzz_codes()
    if len(codes) > 0:
        channelid = int(os.getenv("CHANNEL_ID"))
        print(channelid)
        channel = client.get_channel(channelid)
        await client.wait_until_ready()
        for code in codes:
            embed = discord.Embed(
                title="New code for Zenless Zone Zero",
                timestamp=datetime.datetime.now()
            )
            embed.set_author(name="Prydwen.gg", url="https://www.prydwen.gg/zenless/", icon_url="https://www.prydwen.gg/favicon-32x32.png?v=c3220c3ea85e0f6e55de4153c4b2303b")
            embed.add_field(name="Code", value=code[0])
            embed.add_field(name="Reward", value=code[1])
            embed.set_image(url="https://danny-filebrowser.cp02.cloudboxes.io/api/public/dl/ulFIJ91k?inline=true")
            await channel.send(embed=embed)

    return

@client.event
async def on_ready():
    await tree.sync()
    print(f"We have logged in as {client.user}")
    await printStarRailCodes()
    await printZenlessCodes()
    sched.add_job(printStarRailCodes, 'interval', minutes=60, end_date="2100-01-01 00:00:00", args=())
    sched.add_job(printZenlessCodes, 'interval', minutes=65, end_date="2100-01-01 00:00:00", args=())
    sched.start()


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

client.run(os.getenv("BOT_TOKEN"))
