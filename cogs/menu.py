import discord
from discord.ext import commands
from discord.ui import Button, Select, View, Modal, TextInput

from cogs.button import StartButton
from info.champ_info import get_champion_data, champion_image, champion_response




class getMenu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def start(self, ctx):
        # view = View()
        # view.add_item(StartButton(timeout = 50))
        # await ctx.send("Click to start the menu", view=view)
        view = StartButton()
        message = await ctx.send(view=view)
        view.message = message
        
        await view.wait()
        await view.disable_all_items()

async def setup(bot):
    await bot.add_cog(getMenu(bot))
