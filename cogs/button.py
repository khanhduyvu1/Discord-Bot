import discord
from models.search_box import SearchBox
from discord.ext import commands

class StartButton(discord.ui.View):
    foo : bool = None
    
    @discord.ui.button(label="Champion", 
                       style=discord.ButtonStyle.success)
    async def Champion(self, interaction: discord.Interaction, button: discord.ui.Button):
        search_box = SearchBox(
            title="Champion Information",
            placeholder="Please enter champion's name",
            label="Champion"
        )
        await interaction.response.send_modal(search_box)
        self.foo = True
        self.stop()
        
    @discord.ui.button(label="Items", 
                       style=discord.ButtonStyle.red)
    async def Items(self, interaction: discord.Interaction, button: discord.ui.Button):
        search_box = SearchBox(
            title="Item Information",
            placeholder="Please enter item",
            label="Items"
        )
        await interaction.response.send_message(search_box)
        self.foo = False
        self.stop()
        
class getButton(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def start(self, ctx):
        view = StartButton()
        await ctx.message.author.send(view=view)

async def setup(bot):
    await bot.add_cog(getButton(bot))
