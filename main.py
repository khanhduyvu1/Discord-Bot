import discord 
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
    
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
RESPONSE = os.getenv('LEAGUE_CHAT_ID')

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event 
    async def on_ready():
        print(f"User: {bot.user} (ID: {bot.user.id})")
        await bot.tree.sync()

    
    async def load_extensions():
        await bot.load_extension('cogs.button')   
        
    @bot.event
    async def on_connect():
        await load_extensions()

    bot.run(DISCORD_TOKEN)
    
if __name__ == "__main__":
    run()