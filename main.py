import asyncio
import settings
import discord 
from discord.ext import commands
import os
#from info.menu import SurveyView
    
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
        await bot.load_extension('cogs.champ')
        await bot.load_extension('cogs.direct_message')    
        
    @bot.event
    async def on_connect():
        await load_extensions()
    
        
    # @bot.command()
    # async def survey(ctx):
    #     view = SurveyView()
    #     await ctx.send(view=view)
        
    #     await view.wait()
        
    #     results = {
    #         "a1": view.answer1,
    #         "a2": view.answer2,
    #     }
        
    #     await ctx.send(f"{results}")
    #     await ctx.message.author.send("Thank you for the particitation")
      
    bot.run(settings.DISCORD_TOKEN, root_logger=True)
    
if __name__ == "__main__":
    run()