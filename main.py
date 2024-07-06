import asyncio
import settings
import discord 
from discord.ext import commands
import os
    
logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event 
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        await bot.tree.sync()

    
    async def load_extensions():
        await bot.load_extension('cogs.direct_message') 
        await bot.load_extension('cogs.menu')   
        
    @bot.event
    async def on_connect():
        await load_extensions()
      
    bot.run(settings.DISCORD_TOKEN, root_logger=True)
    
if __name__ == "__main__":
    run()