import discord
from discord.ext import commands
import asyncio
import os
import time
import random
import alphabotflask 
import requests
from alphabotflask import start_flask_thread
from alphabotflask import run_flask


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
        reason = "No reason was provide"
        return
    
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
        "`!ban (mention_member) (reason)` - Banning any member in the server, using !ban\n"
        "`!unban` - unban (userid)\n"
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




color_random = [
    3092790, 16777215, 0, 8421504, 16711680, 9109504, 65280,
    25600, 255, 139, 65535, 32896, 16776960, 16766720,
    16753920, 8388736, 16711935, 16761035, 10824234, 11393254,
    65407, 15132410, 5793266, 5763719, 16705372, 15323838, 15548997
]

colorget = random.choice(color_random)

channel_id = 1307762877872083035

im_url = "https://cdn.discordapp.com/attachments/1294007395747500064/1304454016826081332/Screenshot_1.png?ex=677fde79&is=677e8cf9&hm=f7a24ca9173611d109eb984334fa7b1e96a88c090ee42bc72b492cb2d73c853c&"

@bot.event
async def on_member_join(member):
   guild = member.guild
   channel = discord.utils.get(guild.text_channels, name='🖐-welcome')
   if channel:
        await member.send("``Please verify the requirements``")
        await member.send("``يرجى التحقق من المتطلبات``")

        embed = discord.Embed(title=f"**WELCOME TO {guild.name}**", description=f"**Member Joined:** {member.mention}",  color=colorget)
        embed.set_footer(text="Don't forgot to read the rules", icon_url=im_url)


        time.sleep(0.50)


        room = bot.get_channel(channel_id)
        if room:
            await room.send(f"@here\n**Member has joined the server**\n\n**Member User:** {member.name}\n**Member Userid:** {member.id}")
        await channel.send(embed=embed)



blacklist_two = ["583636893401612319", ]

ROLE_ID = 1246895667381801010

role_2_id = 1326617591665655818

@bot.command()
async def verify(vm): 
    guild = vm.guild
    role2 = guild.get_role(ROLE_ID)
    member = vm.author  

    if role2 in member.roles:
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
    await vm.author.add_roles(role2)

    if role_2_id in member.roles:
        await member.remove_roles(role_2_id)
        return


verification = "Enabled"

RANKID = 1325100668373041257

serverid = 1317542281800057014

@bot.command()
async def vr(ctx):
 guild = ctx.guild
 rank = guild.get_role(RANKID)
 member = ctx.author
 if guild.id == serverid:
     if verification == "Enabled":
      if rank in member.roles:
        await ctx.send("You already have been verified")
        return
        
 try:
    if guild.id == serverid:
       await ctx.send("Checking if verification is enabled...")
       time.sleep(1)
       await ctx.send("Verification is enabled")
       time.sleep(1)
       await ctx.send("Checking Roles..")
       time.sleep(1)
       await ctx.send("Welcome To Managers (OFFICIAL 2)")
       await ctx.send("You're roles were added")
       await ctx.author.add_roles(rank)

 except Exception as e:
    await ctx.send("ERROR Found, While Running Command")
 except PermissionError as e:
    await ctx.send("I don't have permission to give roles, high my role")


def keep_alive():
    while True:
        try:
            requests.get("http://127.0.0.1:10000")
        except requests.exceptions.RequestException as e:
            print(f"Error pinging Flask: {e}")
        time.sleep(60) 


@bot.event
async def on_disconnect():
    await bot.close()  
    await asyncio.sleep(5)  
    await bot.start(TOKEN)


async def main():
    start_flask_thread()
    
    await bot.start(TOKEN)
    

if __name__ == "__main__":
    asyncio.run(main())
