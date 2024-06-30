import discord
from discord.ext import commands
from discord.ui import Button, Select, View, Modal, TextInput

from cogs.button import StartButton


# class ChampionModal(Modal):
#     def __init__(self):
#         super().__init__(title="Champion Details")
#         self.add_item(TextInput(label="Champion Name", placeholder="Enter the name of the champion here"))

#     async def callback(self, interaction: discord.Interaction):
#         try:
#             champion_name = self.children[0].value
#             await interaction.response.send_message(f'You have entered: {champion_name}', ephemeral=True)
#         except Exception as e:
#             await interaction.followup.send_message(f'An error occurred: {str(e)}', ephemeral=True)



class getMenu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def start(self, ctx):
        # view = View()
        # view.add_item(StartButton(timeout = 50))
        # await ctx.send("Click to start the menu", view=view)
        view = StartButton(timeout = 3)
        message = await ctx.send(view=view)
        view.message = message
        
        await view.wait()
        await view.disable_all_items()

async def setup(bot):
    await bot.add_cog(getMenu(bot))
