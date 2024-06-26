import discord
from discord.ext import commands
from discord.ui import Button, Select, View, Modal, TextInput

options_list = [
    ("Champion", "Select a champion"),
    ("Items", "Select items"),
    ("Build", "Select a build")
]

class ChampionModal(Modal):
    def __init__(self):
        super().__init__(title="Champion Details")
        self.add_item(TextInput(label="Champion Name", placeholder="Enter the name of the champion here"))

    async def callback(self, interaction: discord.Interaction):
        try:
            champion_name = self.children[0].value
            await interaction.response.send_message(f'You have entered: {champion_name}', ephemeral=True)
        except Exception as e:
            await interaction.followup.send_message(f'An error occurred: {str(e)}', ephemeral=True)

class MenuView(View):
    @discord.ui.select(
        placeholder="Choose an option...",
        min_values=1,
        max_values=1,
        options=[discord.SelectOption(label=label, description=description) for label, description in options_list]
    )
    async def select_callback(self, interaction: discord.Interaction, select):
        try:
            selected_option = select.values[0]
            if selected_option == "Champion":
                await interaction.response.send_modal(ChampionModal())
        except Exception as e:
            await interaction.followup.send_message(f'An error occurred: {str(e)}', ephemeral=True)

class StartButton(Button):
    def __init__(self):
        super().__init__(label="Start", style=discord.ButtonStyle.primary)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Select an option:", view=MenuView(), ephemeral=True)

class getMenu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def start(self, ctx):
        view = View()
        view.add_item(StartButton())
        await ctx.send("Click to start the menu", view=view)

async def setup(bot):
    await bot.add_cog(getMenu(bot))
