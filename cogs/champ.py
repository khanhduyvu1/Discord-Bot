import discord
from discord.ext import commands
from info.champ_info import get_response

class getChamp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def champ(self, ctx, *,champion_name: str):
        response = get_response(champion_name)
        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(getChamp(bot))