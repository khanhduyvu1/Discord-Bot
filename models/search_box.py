import discord
import random

from info.champ_info import get_champion_data, champion_image, champion_response

class AdditionalOptions(discord.ui.View):
    def __init__(self, champion_name):
        super().__init__()
        self.champion_name = champion_name

    @discord.ui.button(label="More Info", style=discord.ButtonStyle.blurple)
    async def more_info(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Placeholder for fetching more detailed info
        await interaction.response.send_message(f"Fetching more details for {self.champion_name}...")

    @discord.ui.button(label="Another Action", style=discord.ButtonStyle.grey)
    async def another_action(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Another placeholder action
        await interaction.response.send_message("Performing another action...", ephemeral=True)

class SearchBox(discord.ui.Modal):
    def __init__(self, title=None, placeholder=None, label=None):  # Default values for parameters
        super().__init__(title=title)
        self.add_item(discord.ui.TextInput(
            style=discord.TextStyle.short,
            label=label,
            required=False,
            placeholder=placeholder  # Using the placeholder parameter
        ))

    async def on_submit(self, interaction: discord.Interaction):
        # Get the text input value
        champion_name = self.children[0].value
        
        # Call the get_champ function
        await get_champ(interaction, champion_name)

def get_random_color():
    return discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

async def get_champ(interaction: discord.Interaction, champion_name: str):
    champion_data = get_champion_data(champion_name)

    if champion_data:
        image_embed = champion_image(champion_name)
        response_embed = champion_response(champion_name)

        image_embed.color = get_random_color()
        response_embed.color = get_random_color()

        image_embed.description = response_embed.description
        view = AdditionalOptions(champion_name)
        await interaction.response.send_message(embed=image_embed, view = view)
    elif champion_data == None:
        await interaction.response.send_message(f"champion {champion_name} not found")
        
