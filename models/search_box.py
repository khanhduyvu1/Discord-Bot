import discord
import random
from discord.ui import Button, View

from info.champ_info import get_champion_data, champion_response

# class AdditionalOptions(discord.ui.View):
#     def __init__(self, champion_name):
#         super().__init__()
#         self.champion_name = champion_name

#     @discord.ui.button(label="More Info", style=discord.ButtonStyle.blurple)
#     async def more_info(self, interaction: discord.Interaction, button: discord.ui.Button):
#         # Placeholder for fetching more detailed info
#         await interaction.response.send_message(f"Fetching more details for {self.champion_name}...")

#     @discord.ui.button(label="Another Action", style=discord.ButtonStyle.grey)
#     async def another_action(self, interaction: discord.Interaction, button: discord.ui.Button):
#         # Another placeholder action
#         await interaction.response.send_message("Performing another action...", ephemeral=True)
        
class LevelView(View):
    def __init__(self, champion_name):
        super().__init__()
        self.champion_name = champion_name
        self.level = 1
        self.update_buttons()
        
    def update_buttons(self):
        for item in self.children:
            if item.label == "-1lv":
                item.disabled = self.level == 1
            elif item.label == "+1lv":
                item.disabled = self.level == 18

    async def update_embed(self, interaction: discord.Interaction):
        self.update_buttons()
        embed = champion_response(self.champion_name, self.level)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="-1lv", style=discord.ButtonStyle.primary)
    async def previous_button(self, interaction: discord.Interaction, button: Button):
        if self.level > 1:
            self.level -= 1
            await self.update_embed(interaction)

    @discord.ui.button(label="+1lv", style=discord.ButtonStyle.primary)
    async def next_button(self, interaction: discord.Interaction, button: Button):
        if self.level < 18:
            self.level += 1
            await self.update_embed(interaction)
    
    @discord.ui.button(label="lv1", style=discord.ButtonStyle.primary)
    async def lv1_button(self, interaction: discord.Interaction, button: Button):
        self.level = 1
        await self.update_embed(interaction)
        
    @discord.ui.button(label="lv18", style=discord.ButtonStyle.primary)
    async def lv18_button(self, interaction: discord.Interaction, button: Button):
        self.level = 18
        await self.update_embed(interaction)


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
        response_embed = champion_response(champion_name,1)
        response_embed.color = get_random_color()
        view = LevelView(champion_name)
        
        #view = AdditionalOptions(champion_name)
        await interaction.response.send_message(embed=response_embed, view=view)
    elif champion_data == None:
        await interaction.response.send_message(f"champion {champion_name} not found")
        
