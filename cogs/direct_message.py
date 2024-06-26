# direct message
import discord
from discord.ext import commands

class GetMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def DM(self, ctx):
        await ctx.message.author.send("Nothing here!")

async def setup(bot):
    await bot.add_cog(GetMessage(bot))
