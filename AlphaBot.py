from ast import Delete
from os import name
import discord
from discord.app_commands import command
from discord.ext import commands
import time 
import random
import string
import requests
from discord.ext import commands, tasks
import os
import asyncio


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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Communitys"))
    print(f'Logged in as {bot.user}!')



async def fake_web_server():
    port = int(os.environ.get("PORT", 8080))  # Render defaults to port 10000 or 8080
    server = await asyncio.start_server(lambda r, w: None, '0.0.0.0', port)
    async with server:
        await server.serve_forever()



user_id = 850383728022519859

@bot.command()
async def dm(ctx, *, message: str):
    if ctx.author.id == user_id:
     for member in ctx.guild.members:
            try:
              await member.create_dm()  
              await member.dm_channel.send(message)
            except Exception as e:
                await ctx.author.send("Message was failed sended to some users in the server")
     await ctx.author.send("Function Was Running")
    else:
        await ctx.send("You dont have a fucking permmission")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(clr, amount: int):
  try:
     deleted = await clr.channel.purge(limit=amount)
  except Exception:
        await clr.send("Unknown Message was failed deleted")

    

Alpha_id = 850383728022519859

@bot.command()
async def dconfig(cfn):
    server_id = cfn.guild.id
    time.sleep(1)
    if cfn.author.id == Alpha_id:
     await cfn.send(server_id)
    else: 
      await cfn.send("This command only for bot owner")
    


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    await member.ban(reason=reason)
    if reason == None:
        reason=("For No Reason")
    await member.send(f"You was banned from **{guild.name}** for {reason}")
    await ctx.send("Member was banned")
    


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user_id: int):
    try:
        user = await bot.fetch_user(user_id)
        await ctx.guild.unban(user)
        await ctx.author.send(f"{user.mention} is unbanned")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@bot.command()
async def cmds(hlp):
        help_text = (
        "**Available Commands:**\n"
        "`!cmds` - Displays this help message.\n"
        "`!clear <number>` - any amount.\n"
        "`!dm` - !dm (mention user) only works for some roles.\n"
        "`!genpass` - What this do is give you a strong password or a code that you can use for anything\n"
        "`!ban (mention_member) (reason)` - Banning any member in the server, using !ban\n"
        "`!pcTip` - The bot gives you a programed files that when downloading and open them, it will clean some none use files, in you're pc\n"
        "`!unban` - unban (userid)\n"
        "`!userid` - Gives you, you're discord userid\n"
    )
        await hlp.send(help_text)



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    words = ["شرموط", "nigga", "btich", "bitch", "jerk", "niggers", "كس", "تلحس طيزي", "تلحس بذاتي", "LGBTQ", "gay", "lesbain", "fucker", "fuck", "gyat", "منيك", "زب", "اري", "sex", "dick", "motherfucker", "motherair", "motherks", "fucking", "boobs"]

    

    
    if any(word in message.content.lower() for word in words):
           await message.delete()
           await message.channel.send("Message was deleted, for blocked content")
    

    
    if "https" in message.content.lower():
          await message.delete()
          await message.channel.send("https links are not allowed")


    if "www" in message.content.lower():
        await message.delete()
        await message.channel.send("links are not allowed")


    if "هل يجوز" in message.content.lower():
         await message.channel.send("يجوزززززز")


    await bot.process_commands(message)



channel_id = 1307762877872083035

@bot.event
async def on_member_join(member):
   guild = member.guild
   channel = discord.utils.get(guild.text_channels, name='🖐-welcome')
   if channel:
        await member.send("``Please verify the requirements``")
        await member.send("``يرجى التحقق من المتطلبات``")

        welcome_message = (
            f"```Welcome to {guild.name}```{member.mention}\n"
)

        room = bot.get_channel(channel_id)
        if room:
            await room.send(f"Member has joined the server {member.name}")

        await channel.send(welcome_message)
        print("New Member Joined")



blacklist_two = ["583636893401612319"]

ROLE_ID = 1246895667381801010

@bot.command()
async def verify(vm): 
    guild = vm.guild
    role = guild.get_role(ROLE_ID)
    member = vm.author  

    if role in member.roles:
     await vm.send("``You are already verified, you cannot be verified again``")
     return

    await vm.send("Checking user if blacklisted")
    time.sleep(3)

    if member.id in blacklist_two:
        member.ban("User is blacklisted")
        await vm.send("User was banned for blacklisted")
    else:
        await vm.send("User is not blacklisted")

    await vm.send("Checking User Info...")
    time.sleep(3)
    await vm.send("Roles added!")
    await vm.author.add_roles(role)


asyncio.create_task(fake_web_server())

bot.run(TOKEN)
