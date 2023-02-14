import functions.important.client
import disnake
import disnake.ext
from disnake.ui import Button
from functions.important.client import client
import datetime
from helpers.d2helpers.basichelpers import helpers



async def yesask(did,name,author,autochoice,guilds):
  done1 = await helpers.change(did,name)
  time = datetime.datetime.now()
  if done1 != "Done":
    embed = disnake.Embed(
      title=f"**Error Occured!**",
      description=f"Hey, <@!{did}>! It seems I was unable to change your character on the main sheet.\nDon't worry, I'm not dead... *It's just a flesh wound!*\nId:{time}",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    return ("Error",embed)
  done2, time= await helpers.timetrack(did,name,autochoice)
  if done2 != "Done":
    embed = disnake.Embed(
      title=f"**Error Occured!**",
      description=f"Hey, <@!{did}>! It seems I was unable to keep track of your change time.\nDon't worry, I'm not dead... *It's just a flesh wound!*\nId:{time}",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    return ("Error",embed)
  done3 = await helpers.guild(name,author,guilds)
  if done3 != "Done":
    embed = disnake.Embed(
      title=f"**Error Occured!**",
      description=f"Hey, <@!{did}>! It seems I was unable to change your guild.\nDon't worry, I'm not dead... *It's just a flesh wound!*\nId:{time}",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    return ("Error",embed)
  if done1 and done2 and done3 == "Done":
    embed = disnake.Embed(
      title=f"**Change Successful!**",
      description=f"Thank you,<@!{did}>!\nYour guild will be changed automatically in both servers when you change your character. \nYour character change to **{name}** was successful! You will be able to change again in one week.\n\n**Disclaimer:** Please update your **nickname** to reflect this change! \n\nHave a nice day! Id:{time}",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    return ("Done",embed)
async def no(did,name,author,autochoice):
  done1 = await helpers.change(did,name)
  time = datetime.datetime.now()
  if done1 != "Done":
    embed = disnake.Embed(
      title=f"**Error Occured!**",
      description=f"Hey, <@!{did}>! It seems I was unable to change your character on the main sheet.\nDon't worry, I'm not dead... *It's just a flesh wound!*\nId:{time}",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    return ("Error",embed)
  done2, time= await helpers.timetrack(did,name,autochoice)
  if done2 != "Done":
    embed = disnake.Embed(
      title=f"**Error Occured!**",
      description=f"Hey, <@!{did}>! It seems I was unable to keep track of your change time.\nDon't worry, I'm not dead... *It's just a flesh wound!*\nId:{time}",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    return ("Error",embed)
  if done1 and done2 == "Done":
    embed = disnake.Embed(
      title=f"**Change Successful!**",
      description=f"Thank you,<@!{did}>!\nYour guild was not changed so please contact a Judicator if you wish to change your guild tags. \nYour character change to **{name}** was successful! You will be able to change again in one week.\n\n**Disclaimer:** Please update your **nickname** to reflect this change! \n\nHave a nice day! Id:{time}",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    return ("Done",embed)
async def auto(did,name,author,autochoice,guilds):
  done1 = await helpers.change(did,name)
  time = datetime.datetime.now()
  if done1 != "Done":
    embed = disnake.Embed(
      title=f"**Error Occured!**",
      description=f"Hey, <@!{did}>! It seems I was unable to change your character on the main sheet.\nDon't worry, I'm not dead... *It's just a flesh wound!*\nId:{time}",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    return ("Error",embed)
  done2, time= await helpers.timetrack(did,name,autochoice)
  if done2 != "Done":
    embed = disnake.Embed(
      title=f"**Error Occured!**",
      description=f"Hey, <@!{did}>! It seems I was unable to keep track of your change time.\nDon't worry, I'm not dead... *It's just a flesh wound!*\nId:{time}",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    return ("Error",embed)
  done3 = await helpers.guild(name,author,guilds)
  if done3 != "Done":
    embed = disnake.Embed(
      title=f"**Error Occured!**",
      description=f"Hey, <@!{did}>! It seems I was unable to change your guild.\nDon't worry, I'm not dead... *It's just a flesh wound!*\nId:{time}",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    return ("Error",embed)
  if done1 and done2 and done3 == "Done":
    embed = disnake.Embed(
      title=f"**Change Successful!**",
      description=f"Thank you,<@!{did}>! \nYour character change to **{name}** was successful! You will be able to change again in one week.\n\n**Disclaimer:** Please update your **nickname** to reflect this change! \n\nHave a nice day! Id:{time}",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    return ("Done",embed)
async def autono(did,name,author,autochoice):
  done1 = await helpers.change(did,name)
  time = datetime.datetime.now()
  if done1 != "Done":
    embed = disnake.Embed(
      title=f"**Error Occured!**",
      description=f"Hey, <@!{did}>! It seems I was unable to change your character on the main sheet.\nDon't worry, I'm not dead... *It's just a flesh wound!*\nId:{time}",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    return ("Error",embed)
  done2, time= await helpers.timetrack(did,name,autochoice)
  if done2 != "Done":
    embed = disnake.Embed(
      title=f"**Error Occured!**",
      description=f"Hey, <@!{did}>! It seems I was unable to keep track of your change time.\nDon't worry, I'm not dead... *It's just a flesh wound!*\nId:{time}",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    return ("Error",embed)
  if done1 and done2 == "Done":
    embed = disnake.Embed(
      title=f"**Change Successful!**",
      description=f"Thank you,<@!{did}>! \nYour character change to **{name}** was successful! You will be able to change again in one week.\nThis did not include your guild role change!\n\n**Disclaimer:** Please update your **nickname** to reflect this change! \n\nHave a nice day! Id: {time}",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    return ("Done",embed)

  