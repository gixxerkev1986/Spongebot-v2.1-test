import discord
from discord.ext import commands
import os
import asyncio

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Ingelogd als {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"✅ Slash commands gesynchroniseerd ({len(synced)} commando's)")
    except Exception as e:
        print(f"⚠️  Fout bij sync: {e}")

    # Laad cogs
    await load_cogs()

async def load_cogs():
    await bot.load_extension("commands.ping")

async def main():
    async with bot:
        await main_startup()
        await bot.start(TOKEN)

async def main_startup():
    pass  # later voor logging of database

asyncio.run(main())