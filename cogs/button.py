import discord
from models.search_box import SearchBox

class StartButton(discord.ui.View):
    foo : bool = None
    
    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)
    
    async def on_timeout(self) -> None:
        await self.message.channel.send("Timeout")
        await self.disable_all_items()
    
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