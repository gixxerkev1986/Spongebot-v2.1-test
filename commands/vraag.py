import discord
from discord.ext import commands
from discord import app_commands

class Vraag(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="vraag", description="Stel een AI-vraag over crypto (mock)")
    @app_commands.describe(tekst="Jouw vraag aan de AI")
    async def vraag(self, interaction: discord.Interaction, tekst: str):
        await interaction.response.send_message(f"AI antwoord (mock): Interessante vraag! ({tekst})")

async def setup(bot):
    await bot.add_cog(Vraag(bot))