import discord
from discord.ext import commands
import asyncio

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'YOUR_BOT_TOKEN'
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

async def get_console_input():
    await bot.wait_until_ready()
    channel = bot.get_channel(YOUR_CHANNEL_ID)  # Replace with your channel ID
    while not bot.is_closed():
        message = input("Enter message to send to Discord: ")
        await channel.send(message)

bot.loop.create_task(get_console_input())
bot.run(TOKEN)
