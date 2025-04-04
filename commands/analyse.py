import discord
from discord.ext import commands
from discord import app_commands

class Analyse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="analyse", description="Analyseer een coin met simulatie")
    @app_commands.describe(coin="De naam van de coin (bv. kaspa, fet, etc.)")
    async def analyse(self, interaction: discord.Interaction, coin: str):
        naam = coin.upper()
        bericht = (
            f"**Technische analyse voor {naam}**\n"
            f"• 5m: RSI 38 — mogelijk herstel\n"
            f"• 10m: EMA20 > EMA50 — lichte bullish kruising\n"
            f"• 1h: zijwaarts met weerstand rond €0.42\n"
            f"• Sentiment: positief op sociale media\n"
            f"**Advies:** voorzichtig instappen bij dip rond €0.405"
        )
        await interaction.response.send_message(bericht)

async def setup(bot):
    await bot.add_cog(Analyse(bot))