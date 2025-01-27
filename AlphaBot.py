import discord
from discord.ext import commands
import os
import asyncio
import requests
from alphabotflask import start_flask_thread
from alphabotflask import run_flask

# Setup bot intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if not TOKEN:
    print("Error: Bot token not found in environment variables.")
else:
    print("Token loaded successfully.")



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Communities"))
    print(f'Logged in as {bot.user}!')


@bot.command()
async def cmds(hlp):
        help_text = (
        "**Available Commands:**\n"
        "`!cmds` - Displays this help message.\n"
        "`!clear <number>` - any amount.\n"
        "`!dm` - !dm (mention user) only works for some roles.\n"
        "`!ban (mention_member) (reason)` - Banning any member in the server, using !ban\n"
        "`!unban` - unban (userid)\n"
    )
        await hlp.send(help_text)


async def main():
    start_flask_thread()  
    await bot.start(TOKEN)
    
    

# Only run if this file is executed directly
if __name__ == "__main__":
    asyncio.run(main())
