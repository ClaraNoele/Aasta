import os
import disnake
from disnake import AllowedMentions
import disnake.ext
from disnake.ext import commands
import disnake.ui
import datetime
import d20

import functions.sheetstats
from functions.sheetstats import Stat_List as stl

addorremove = commands.option_enum({
  "Remove":"Remove",
  "Add":"Add"
})

feedback = os.environ['feedback']
GSF = os.environ['GSF']
Init_Form = os.environ['Init Form']

class Misc(commands.Cog):
  def __init__(self, bot: commands.Bot):
        self.bot = bot
  
  @commands.slash_command(name = "info",description = "My info about my creation and other information!")
  #Contains command information and Bot information
  async def info(inter: disnake.ApplicationCommandInteraction):
    await inter.response.defer()
    embed = disnake.Embed(
      title=f"About Me!",
      description=f"Hello! I am Aasta and I was created in Python to help you make rolls with your stats! Here's one thing to keep in mind: I will be fairly slow, so be patient with me. I know it's hard but please. \nIf you have problems please let my creator, <@!539623070202069023>, know about your problem. She'll do her best to help you out. If you have anything to suggest to be added let her know as well, just make sure you ping her. We've had problems with that. Anyway, please take a gander at the rest of the useful information I have on my info page, and have a nice day! \n\n**Commands:**\nHere is a list of my command functions (This will be updated when I gain more functionality):\n**/roadmap:** Take a look at my development and if you are so inclined join on my journey discovering new commands. This command contains a feedback link for those who wish to provide feedback!\n**/statsall:** This command is used to display all number based stats in a nice convenient window. Show off to other syndicate members! You know you want to. **This command has replaced the stats tree in favor of just a nice window instead of a messy command tree.**\n**/register:** This command will allow you to use the commands /check and /stats with characters you register with this command.\n**/check:** This command will allow you to roll your stat checks for QMs, etc.\nThe subcommands are: **Primary and Skills.**\n**/attack:** This command allows you to roll attacks with different Advantage types.\n**/initiative:** This command allows you to roll initiative.\n**/roll:** Your standard roll command.\n**/cast:** This command allows you to use any of the six elements spell list. Due to **limitations** this command has been split: /cast and /cast2.\n**/change:** This command will change your character to another of your choosing. It will only allow you to change to characters that aren't retired.\n**/fun:** This command is for fun, type in a word or two and try to find all the secrets!\n\n**Special Information:**\nThe **IASC** statement means **'Item/Ability Special Circumstance'** it means that when you are reprimanded or crit (Nat 20) if you have items the change this IASC comes into effect.",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_author(
      name=f"My info page",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    embed.set_thumbnail(url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
  # Regular Fields
    embed.add_field(name="Creator", value="<@!539623070202069023>", inline=False)
    embed.add_field(name="Director/Overseer", value="<@!280875996272525313>", inline=False)
    # Inline Fields
    embed.add_field(name="Tester/Gameplay", value="<@!235208969352642561>", inline=True)
    embed.add_field(name="Inspiration/Gameplay", value="<@!258601534584127498>", inline=True)
    embed.add_field(name="Judicator", value="<@!437390218564337664>", inline=True)
    embed.add_field(name="Special Thanks",value="<@!264595631065006080> <@!689326463580635192> <@!442786809194479646>", inline=False)
    
    await inter.edit_original_response(embed=embed,allowed_mentions=AllowedMentions.none())

  #This is the stat calling command block. It utilizes a function from another file to pick out a stat from a character sheet and enters it into a message to relay to the user in discord. Nifty huh?
  @commands.slash_command(name = "roadmap", description = "This is the Development Roadmap with useful information included!")
  async def road(inter:disnake.ApplicationCommandInteraction):
    await inter.response.defer()
    embed = disnake.Embed(
      title=f"Roadmap!",
      description=f"Hello! The truth is I am still in development, probably won't stop being... But if you would like to get involved as a tester for the things in development or even just offer ideas let my creator, <@!539623070202069023>, know about this in the Feedback form linked below. Any feedback would be helpful unless she gets too much of one thing then it might be annoying. So enough talk, here is the Roadmap:\n\n1. ~~Get her able to interact and read information off of Google Sheets~~(Complete)\n2. ~~Get her to respond to commands and return information~~(Complete)\n3. ~~Refine 1 and 2 with embeds to make it look nicer~~ (Complete)\n4. ~~Get her able to roll dice with the information from google sheets~~ (Complete)\n5. ~~Refine 4~~ (Complete)\n5.9. ~~Finishing Touches and Final Preparations for testing for level 6.~~ (Complete)\n6. ~~Move her to the main server (and Main Sheets with her functionality) and get her into use.~~ (Goal 1)(Complete)\n7. Incorporate User-D2 into her code and allow users to change their current character and guilds (Goal 2)(In Progress)\n8.  (Optional) Add functionality with spell casting and ability usage. (Make a python library with names and descriptions) (Goal 3)(In Progress)\n9. (Optional) Add fancy dialogue for stat levels",
      color=0x8d0d0d,
      timestamp=datetime.datetime.now())
    embed.set_author(
      name=f"My Development Roadmap!",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    embed.set_thumbnail(url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")

    embed.add_field(name="Feedback!", value=f"[Feedback Form]({feedback})", inline=True)
    await inter.edit_original_response(embed=embed,allowed_mentions=AllowedMentions.none())
  @commands.slash_command(name = "roll", description = "This is the standard roll command")
  async def rolly(inter: disnake.ApplicationCommandInteraction, die: str):
    did = inter.author.id
  
    didtrue = str(did)
    rollr = d20.roll(die)
    print(rollr)
    rollc = rollr.result
    rollt = rollr.total
    await inter.response.send_message(f"<@!{didtrue}>\n**Result:** {rollr}\n**Total:** {rollt}")

  @commands.slash_command(name = "fun",description = "Easter Eggs for y'all!")
  async def fun(inter: disnake.ApplicationCommandInteraction, egg: str):
    await inter.response.defer()
    if (egg == "Hmm"):
      await inter.edit_original_response(f"Hmm, I bet you are wondering what I'm thinking about. \n\nWell too bad! I'm gonna walk over here now.")
    elif (egg == "Goose"):
      await inter.edit_original_response(f"Goosen Morning!")
    elif (egg == "Honk"):
      await inter.edit_original_response(f"Honk! I'm a Goose and I'm gonna bite you! *Monch*")
    elif (egg == "Truth"):
      await inter.edit_original_response(f"The Truth is I'm tired. I'm tired, Boss.")
    elif (egg == "Hamilton"):
      await inter.edit_original_response(f"I would read the lyrics for my favorite song in Hamiliton, but that'd be copyright infringement. But... \n\n\U0001F3B6 You'll be back, soon, you'll see \nYou'll remember you belong to me \nYou'll be back, time will tell \nYou'll remember that I served you well \U0001F3B6")
    elif (egg == "One Ring"):
      await inter.edit_original_response(f"What? This ring? What... What are you doing?! \n\n*Hisses* Mine! My precious! **Precious!**")
    elif (egg == "Alon"):
      await inter.edit_original_response(f"That guy huh? The dragon man. He seems scary, though it's probably because he's been here for a long time. I would steer clear of him, unless you can get along with him or he's your guildmaster.")
    elif (egg == "Var"):
      await inter.edit_original_response(f"Ah the guy with a shield... and some large angel wings? I haven't looked too much into it. He's a nice guy and likes cake. Definitely someone you want on your team, that aura is a pain for the enemies he faces.")
    elif (egg == "Septimus"):
      await inter.edit_original_response(f"The old pirate. I've heard of him, I never heard what happened to him, however.")
    elif (egg == "Pit"):
      await inter.edit_original_response(f"The old captain and crook. I've heard of him, though his story is unknown to me. Maybe he'll return one day, maybe not.")
    elif (egg == "BORTH"):
      await inter.edit_original_response(f"BORTH?! WHO?! Either way Happy BORTH!!!")
    elif (egg == "Nemo"):
      await inter.edit_original_response(f"Scary feast lady... At least she was? Not completely sure. I hear she's sad now. Though she's been around for a long time. I hear she's real nice. Again up for speculation.")
    elif (egg == "Freya"):
      await inter.edit_original_response(f"Ah yes the guildmaster. She's in charge of a very big guild and she can be pretty terrifying. She kinda has to be, she is in charge of a military guild so it makes sense. Her guild is the oldest, I'm pretty sure.")
    elif (egg == "Vosalo"):
      await inter.edit_original_response(f"I hear she is almost as powerful if not more than Alon. Though I don't remember any battles between the two. She's been around for a long time.")
    elif (egg == "Ender"):
      await inter.edit_original_response(f"The Angelic Vanguardian. Been around a long time, even had someone a nemesis maybe. Named Void? or Enigma? They disappeared very quickly after. No one's seen Ender for a long time, I wonder where they went.\n\n*Apparently my creator and them met each other in a weird way, ask them about it sometime.*")
    elif (egg == "Phix"):
      await inter.edit_original_response(f"The Phoenix Lady! She has some skills with fire... It's fascinating. Anyway, where was I? Oh right, Phix. Ever noticed that if you take away the oen in Phoenix it spells Phix? Almost like she thought it out... Well, now a days she's married to Terravissen and is the Hand of the Vanguard. She's really gone places since she started.")
    else:
      await inter.edit_original_message(f"Trying to find a secret? Try again one of them may be something or someone you see every day...")
  #Ky

  @commands.slash_command(name = "testing",description="Testing purposes")
  async def test(inter: disnake.ApplicationCommandInteraction):
    await inter.response.defer()
    id = inter.author.id
    embed = disnake.Embed(
      title=f"Welcome to the Syndicate!",
      description=f"Greetings, <@!{id}>! If you follow the link below, you will be taken to our initial character creation form. Please read through the documents attached in the form along with those linked in the “Getting Started” folder below, to get a basic understanding of how to begin in-character play in our system.\n\nWhen you have completed this form, please tag an <@&563459756887638036> in this channel and they will review your application and help you get started. We look forward to seeing you in-game. Please do not hesitate to ask if you have any questions!",
       color=0x8d0d0d,
       timestamp=datetime.datetime.now())
    embed.set_footer(
      text="Aasta by Clara Noele",
      icon_url="https://images.pexels.com/photos/3041112/pexels-photo-3041112.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/565131192819646493/1062858993120329808/Syndicate_Logo_Alpha_lighter.jpg.png")
    embed.add_field(name="", value=f"[Initiation Form!]({Init_Form})", inline=True)
    embed.add_field(name="",value=f"[Getting Started!]({GSF})",inline=True)
    await inter.edit_original_response(embed=embed)




def setup(commands: commands.Bot):
    commands.add_cog(Misc(commands))