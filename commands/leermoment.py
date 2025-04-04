import discord
from discord.ext import commands
from discord import app_commands

leermoment_log = {}

class Leermoment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="leermoment", description="Geef feedback op een coin-analyse")
    @app_commands.describe(coin="De coin waarvoor je feedback geeft", resultaat="Resultaat: winst/verlies")
    async def leermoment(self, interaction: discord.Interaction, coin: str, resultaat: str):
        leermoment_log[coin.upper()] = resultaat.lower()
        await interaction.response.send_message(
            f"SpongeBot onthoudt: jouw analyse op {coin.upper()} eindigde in **{resultaat.upper()}**."
        )

async def setup(bot):
    await bot.add_cog(Leermoment(bot))