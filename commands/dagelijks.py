import discord
from discord.ext import commands
from discord import app_commands
from utils.ta import fetch_ohlc_data, calculate_ta
import traceback

class Dagelijks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="dagelijks", description="Toon dagelijkse TA voor een coin (binance)")
    @app_commands.describe(coin="Bijv. kaspa, fet, link")
    async def dagelijks(self, interaction: discord.Interaction, coin: str):
        await interaction.response.defer()
        symbol = f"{coin.lower()}usdt"
        try:
            df = fetch_ohlc_data(symbol=symbol, interval='1h', limit=100)
            ta = calculate_ta(df)

            embed = discord.Embed(
                title=f"Dagelijkse TA: {coin.upper()}",
                description=(
                    f"**RSI (14):** {ta['rsi']:.2f}\n"
                    f"**EMA20:** {ta['ema20']:.5f}\n"
                    f"**Laatste prijs:** {ta['close']:.5f}"
                ),
                color=0x1abc9c
            )
            await interaction.followup.send(embed=embed)

        except Exception as e:
            traceback.print_exc()
            await interaction.followup.send(f"Kon geen TA ophalen voor `{symbol}`. Mogelijk niet op Binance?")

async def setup(bot):
    await bot.add_cog(Dagelijks(bot))