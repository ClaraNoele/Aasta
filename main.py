#Main Imports
import os
import disnake
from disnake import AllowedMentions, Intents
from disnake.ext import commands, tasks
from enum import Enum
import pytz
from datetime import datetime
import d20
import subprocess
import ast
#Other Sheet Imports
from functions.important.keepalive import keep_alive, myiter, killiter
import functions.log
from functions.log import filemanage, errorlog, printing

#This area is for setting up Aasta at the very beginning. She'll even tell you in the console over there. >>
print(f"Starting up, give me a second!")
bot = commands.InteractionBot(allowed_mentions=AllowedMentions(everyone=False,users=True,roles=True,replied_user=True),intents=Intents.all())

GSF = os.environ['GSF']
Init_Form = os.environ['Init Form']
token = os.environ['discord_id']
server = os.environ['discord_server']

min = 0
roleslist = []
timezone = pytz.timezone('America/Denver')
killer = ["alive","alive","alive","alive","alive","alive","alive","alive","kill"]
status = ['with Python!','with The Syndicate!','with the Fun command!','with My Info!','Hamiliton on my Screen!',"with Nemo!","with Erik, Ender and Clara!","KeepAlive","with the Judicators!","Sleepy Time"]

filemanage()

COGS = (
  "cogs.combat",
  "cogs.misc",
  "cogs.ud2",
  "cogs.register",
  "cogs.weavers",
  "cogs.spellscog",
  "cogs.stats",
  "cogs.library"
)
#This area handles events such as logging in or logging off
@bot.event
async def on_ready():
  remind_channel = bot.get_channel(1028462625065017374)    
  await remind_channel.send("Logging in...")
  change_status.start()
  await printing(f"We have logged in as {bot.user}.")
@tasks.loop(minutes=6.0)
async def change_status():
  await bot.change_presence(activity=disnake.Game(status[next(myiter)]))
  killery = killer[next(killiter)]
  if killery == "kill":
    await bot.close()
    print("kill 1")
    subprocess.call("kill 1", shell=True)
  else:
    time = datetime.now(timezone).strftime('%m\%d\%Y %H:%M')
    await printing(f"The time is now {time}")

#@bot.event
#async def on_error(event, *args, **kwargs):
#  await errorlog(event,args)

@bot.event
async def on_disconnect():
  await errorlog("Timeout",None)
  await bot.close()
  print("kill 1")
  subprocess.call("kill 1", shell=True)
  
@bot.event
async def on_slash_command_error(inter: disnake.ApplicationCommandInteraction, error):
  if isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
    errorstr = str(error)
    errors = errorstr.replace("' is required to run this command.",'')
    errorf = errors.replace("Role '",'')
    if errorf == "Judicator":
      await inter.send("You aren't a Judicator! No being sneaky!")
    if errorf == "Questmaster":
      await inter.send("Halt! You do not have access to this information! You're not a Questmaster!")
@bot.event
async def on_member_update(before,after):
  if after.guild.id == 563442211623010304:
    realms = await bot.fetch_guild(558375078258147349)
    roles = await realms.fetch_roles()
    memid = after.id
    realmmember = await realms.fetch_member(memid)
    for role in range(len(roles)):
      name = roles[role].name
      id = roles[role].id
      roleslist.append([name,id])
    bef = set(before.roles)
    aft = set(after.roles)
    removed = bef.difference(aft)
    added = aft.difference(bef)
    if removed == set() and added != set():
      rolename = list(added)[0].name
      for role in range(len(roleslist)):
        if rolename == roleslist[role][0]:
          roleid = roleslist[role][1]
          role = await realms.get_role(roleid)
          await realmmember.add_roles(role)
    elif removed != set() and added == set():
      rolename = list(removed)[0].name
      for role in range(len(roleslist)):
        if rolename == roleslist[role][0]:
          roleid = roleslist[role][1]
          role = await realms.get_role(roleid)
          await realmmember.remove_roles(role)
    else:
      bnick = before.nick
      anick = after.nick
      if anick != bnick:
        await realmmember.edit(nick=anick)
      elif anick == bnick:
        pass
  else:
    pass
@bot.event
async def on_member_join(member):
  id = member.id
  autolog = await bot.fetch_channel(577603764513669142)
  startarea = await bot.fetch_channel(563442211623010306)
  embed = disnake.Embed(
    title=f"Welcome to the Syndicate!",
    description=f"Greetings, <@!{id}>! If you follow the link below, you will be taken to our initial character creation form. Please read through the documents attached in the form along with those linked in the “Getting Started” folder below, to get a basic understanding of how to begin in-character play in our system.\n\nWhen you have completed this form, please tag an <@&563459756887638036> in this channel and they will review your application and help you get started. We look forward to seeing you in-game. Please do not hesitate to ask if you have any questions!",
     color=0x8d0d0d,
     timestamp=datetime.now())
  embed.set_footer(
    text="Aasta by Clara Noele",
    icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/565131192819646493/1062858993120329808/Syndicate_Logo_Alpha_lighter.jpg.png")
  embed.add_field(name="", value=f"[Initiation Form!]({Init_Form})", inline=True)
  embed.add_field(name="",value=f"[Getting Started!]({GSF})",inline=True) 
  await startarea.send(embed=embed)
  embed = disnake.Embed(
    title=f"New Member!",
    description=f"<@!{id}> has joined the guild and been briefed!",
    color=0x8d0d0d,
      timestamp=datetime.now())
  embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
  await autolog.send(embed=embed)
keep_alive()

#This area loads the commands and then logs Aasta in
for cog in COGS:
  bot.load_extension(cog)
try:
  bot.run(token)
except:
  print("kill 1")
  subprocess.call("kill 1", shell=True)