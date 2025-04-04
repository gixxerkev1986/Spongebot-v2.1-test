import discord
from discord.ext import commands
from discord import app_commands

class Sentiment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="sentiment", description="Toon het sentiment over een coin")
    @app_commands.describe(coin="De naam van de coin (bv. kaspa, fet, etc.)")
    async def sentiment(self, interaction: discord.Interaction, coin: str):
        await interaction.response.send_message(
            f"Sentiment voor {coin.upper()}: positief — veel buzz over toekomstige updates!"
        )

async def setup(bot):
    await bot.add_cog(Sentiment(bot))