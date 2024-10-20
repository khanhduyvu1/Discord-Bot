import discord
from discord.ui import Button, View
from info.player_info import get_player_url

class PlayerSearchBox(discord.ui.Modal):      
    def __init__(self, title=None, player_label=None, player_placeholder=None, player_tagline=None):  # Default values for parameters
        super().__init__(title=title)
        self.add_item(discord.ui.TextInput(
            style=discord.TextStyle.short,
            label=player_label,
            required=True,
            placeholder=player_placeholder  # Using the placeholder parameter
        ))
        self.add_item(discord.ui.TextInput(
            style=discord.TextStyle.short,
            label=player_tagline or "Tagline",
            required=True,
            placeholder=player_tagline
        ))

    async def on_submit(self, interaction: discord.Interaction):
        player_name = self.children[0].value
        player_tagline = self.children[1].value
        player_info =get_player_url(player_name, player_tagline)
        await interaction.response.send_message(player_info)

