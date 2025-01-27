import discord
from discord.ext import commands, tasks
import asyncio
import os
import http.server
import socketserver
from urllib.parse import urlparse

# Bot setup
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

# Web server setup
async def fake_web_server():
    port = int(os.environ.get("PORT", 8080))  # Ensure we use the right port dynamically
    print(f"Starting web server on port {port}")  # Debugging statement to confirm the port
    server = await asyncio.start_server(lambda r, w: None, '0.0.0.0', port)
    async with server:
        await server.serve_forever()

# Commands for the bot
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
    "`!dm` - Sends a DM to all members (owner only).\n"
    "`!ban (mention_member) (reason)` - Banning any member in the server.\n"
    "`!unban` - unban (userid)\n"
    )
    await hlp.send(help_text)

# Add more commands here

# Web server for favicon and static files
class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/favicon.ico':
            self.send_response(200)
            self.send_header('Content-Type', 'image/x-icon')
            self.end_headers()
            with open('favicon.ico', 'rb') as f:
                self.wfile.write(f.read())
        else:
            super().do_GET()

# Run both bot and web server concurrently
async def main():
    # Start the web server in the background
    web_server_task = asyncio.create_task(fake_web_server())

    # Start the bot
    bot_task = asyncio.create_task(bot.start(TOKEN))

    # Run both tasks concurrently
    await asyncio.gather(web_server_task, bot_task)

if __name__ == "__main__":
    # Start both the bot and web server using asyncio
    asyncio.run(main())
