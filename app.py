import os
import datetime
import discord
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from core.utils import (
    get_new_codes
)

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
sched = AsyncIOScheduler()


async def printnewcodes():
    codes = get_new_codes()
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

@client.event
async def on_ready():
    await tree.sync()
    print(f"We have logged in as {client.user}")
    await printnewcodes()
    sched.add_job(printnewcodes, 'interval', minutes=30, end_date="2100-01-01 00:00:00", args=())
    sched.start()


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

client.run(os.getenv("BOT_TOKEN"))
