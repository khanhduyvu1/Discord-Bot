import discord
import settings

class SearchBox(discord.ui.Modal):
    def __init__(self, title = None, placeholder = None, label = None):  # Default values for parameters
        super().__init__(title=title)
        self.add_item(discord.ui.TextInput(
            style=discord.TextStyle.short,
            label=label,
            required=False,
            placeholder=placeholder  # Using the placeholder parameter
        ))
    async def on_submit(self, interaction: discord.Interaction):
        channel = interaction.guild.get_channel(settings.LEAGUE_CHAT_ID)