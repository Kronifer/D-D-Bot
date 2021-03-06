import discord
from discord.ext import commands
import os 
from replit import db
import keep_alive
import random
 
token = os.getenv('bottoken')

client = discord.Client()

bot = commands.Bot(command_prefix='!', help_command = None)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command(pass_context=True)
@commands.has_role('Bot Creator')
async def dm(ctx, args, User: discord.User):
  await ctx.send("Sent message to user.")
  await User.send(args)

@bot.command()
async def setcharname(ctx, args, User: discord.User):
  await User.send("Registering *" + args + "* as your character's name. If you do this again, your character's name will be overwritten.")
  newcharname = db[User.id] = args

@bot.command()
async def setcharclass(ctx, args, User: discord.User):
  await User.send("Registering *" + args + "* as your character's class. Will be overwritten if performed again.")
  newcharclass = db[User.id, 'charclass'] = args

@bot.command()
async def setcharlevel(ctx, args, User: discord.User):
  await User.send("Registering your character as level *" + args + "*.")
  newcharlevel = db [User.id, 'level'] = args
@bot.command()
async def setcharinventory(ctx, args, User: discord.User):
  await User.send("Registering *" + args + "* as items in your inventory. If you update your inventory, be sure to include any items that were previously registered.")
  newcharinv = db[User.id, 'inv'] = args

@bot.command()
async def charismaset(ctx, args, User: discord.User):
  await User.send("Setting *" + args + "* as your charisma stat.")
  newcharisma = db[User.id, 'charisma'] = args

@bot.command()
async def wisdomset(ctx, args, User: discord.User):
  await User.send("Setting *" + args + "* as your wisdom stat.")
  newwisdom = db[User.id, 'wisdom'] = args

@bot.command()
async def intelligenceset(ctx, args, User: discord.User):
  await User.send("Setting *" + args + "* as your intelligence stat.")
  newintelligence = db[User.id, 'intelligence'] = args

@bot.command()
async def constitutionset(ctx, args, User: discord.User):
  await User.send("Setting *" + args + "* as your constitution stat.")
  newconst = db[User.id, 'const'] = args  

@bot.command()
async def dexterityset(ctx, args, User: discord.User):
  await User.send("Setting *" + args + '* as your dexterity stat.')
  newdext = db[User.id, 'dext'] = args

@bot.command()
async def strengthset(ctx, args, User: discord.User):
  await User.send("Setting *" + args + "* as your strength stat.")
  newstrength = db[User.id, 'str'] = args

@bot.command()
async def dicerolld20(ctx):
  d20roll = random.randint(1, 20)
  embed = discord.Embed(title = "D20 roll", description=d20roll)
  await ctx.send(embed=embed)
@bot.command()
async def dicerolld8(ctx):
  d8roll = random.randint(1, 8)
  embed = discord.Embed(title = "D8 roll", description = d8roll)
  await ctx.send(embed = embed)

@bot.command()
async def setcharrace(ctx, args, User: discord.User):
  await User.send("Setting *" + args + "* as your character's race.")
  newrace = db[User.id, "race"] = args

@bot.command()
async def setcharalignment(ctx, args, User: discord.User):
  await User.send("Setting *" + args + "* as your character's alignment.")
  newalign = db[User.id, 'align'] = args

@bot.command()
async def getcharinfo(ctx, args, User: discord.User):
  if(args == 'name'):
    try:
      charnameget = db[User.id]
      embed=discord.Embed(title="Character Name", description = charnameget)
      embed.set_footer(text="Made by D&D Bot")
      await ctx.send(embed=embed)
    except:
      await ctx.send("User does not have a character name set.")
  elif (args == 'alignment'):
    try:
      alignget = db[User.id, 'align']
      embed = discord.Embed(title="Character Alignment", description = alignget)
      await ctx.send(embed=embed)
    except:
      await ctx.send("User has not yet set an alignment.")
  elif(args == 'race'):
    try:
      charraceget = db[User.id, "race"]
      embed = discord.Embed(title="Character Race", description = charraceget)
      embed.set_footer(text='Made by D&D Bot')
      await ctx.send(embed=embed)
    except:
      await ctx.send("User does not yet have a set race.")
  elif(args == "class"):
    try:
      charclassget = db[User.id, 'charclass']
      embed=discord.Embed(title="Character Class", description=charclassget)
      embed.set_footer(text="Made by D&D Bot")
      await ctx.send(embed=embed)
    except:
      await ctx.send("User does not have a class set.")
  elif(args == "level"):
    try:
      charlevelget = db[User.id, 'level']
      embed = discord.Embed(title="Character Level", description = charlevelget)
      embed.set_footer(text="Made by D&D Bot")
      await ctx.send(embed=embed)
    except:
      await ctx.send("User does not have a level set.")
  elif(args == "inventory"):
    try:
      charinvget = db[User.id, 'inv']
      embed = discord.Embed(title="Character Inventory", description = charinvget)
      embed.set_footer(text="Made by D&D Bot")
      await ctx.send(embed = embed)
    except:
      await ctx.send("User does not have an inventory set.")
  elif(args == "stats"):
    try:
      charcharismaget = db[User.id, 'charisma']
      wisdomget = db[User.id, 'wisdom']
      intelligenceget = db[User.id, 'intelligence']
      constget = db[User.id, 'const']
      dextget = db[User.id, 'dext']
      strget = db[User.id, 'str']
      embed = discord.Embed(title = "Character Stats")
      embed.add_field(name='Charisma', value = charcharismaget, inline = True)
      embed.add_field(name='Wisdom', value = wisdomget, inline = True)
      embed.add_field(name='Intelligence', value = intelligenceget, inline = True)
      embed.add_field(name="Constitution", value = constget, inline = True)
      embed.add_field(name="Dexterity", value = dextget, inline = True)
      embed.add_field(name = "Strength", value = strget, inline = True)
      embed.set_footer(text="Made by D&D Bot")
      await ctx.send(embed=embed)
    except:
      await ctx.send("That user has not specified any stats yet.")
  elif(args == "all"):
    try:
      charnameget = db[User.id]
      charclassget = db[User.id, 'charclass']
      charlevelget = db[User.id, 'level']
      charinvget = db[User.id, 'inv']
      charcharismaget = db[User.id, 'charisma']
      wisdomget = db[User.id, 'wisdom']
      constget = db[User.id, 'const']
      dextget = db[User.id, 'dext']
      intelligenceget = db[User.id, 'intelligence']
      strget = db[User.id, 'str']
      charraceget = db[User.id, "race"]
      alignget = db[User.id, 'align']
      embed=discord.Embed(title= "Character Info")
      embed.add_field(name="Name", value=charnameget, inline=True)
      embed.add_field(name="Race", value = charraceget, inline=True)
      embed.add_field(name="Class", value=charclassget, inline=True)
      embed.add_field(name="Level", value = charlevelget, inline = True)
      embed.add_field(name="Inventory", value = charinvget, inline = True)
      embed.add_field(name="Alignment", value = alignget, inline = True)
      embed.add_field(name="Stats", value = "Charisma:  " + charcharismaget +"  Wisdom:  " + wisdomget + "   Intelligence:  " + intelligenceget + "  Constitution:  " + constget + "  Dexterity:  " + dextget + "  Strength:  " + strget, inline=True)
      embed.set_footer(text="Made by D&D Bot")
      await ctx.send(embed=embed)
    except:
      await ctx.send("Not enough data to get character info.")
  else:
    await ctx.send("Argument not accepted.")

@bot.command()
async def help(ctx):
  embed = discord.Embed(title = "Commands")
  embed.add_field(name="!ping", value = "Every bot has this I guess.", inline=False)
  embed.add_field(name="!setcharname <character name> [@mention yourself]", value = "Sets your character name.", inline=False)
  embed.add_field(name="!setcharrace \"<Character Race>\" [@mention yourself]", value = "Sets your characters race.", inline = False)
  embed.add_field(name="!setcharclass <character class> [@mention yourself]", value="Set's your character's class. Only useable once.", inline = False)
  embed.add_field(name="!setcharinventory \"<item, item, item, etc.>\" [@mention yourself]", value="Sets items in your inventory. Separate items with commas for ease of readibility.", inline=False)
  embed.add_field(name="!setcharalignment \"<Alignment>\" [@mention yourself]", value = "Set's your characters Alignment.", inline = False)
  embed.add_field(name="!charismaset <value> [@mention yourself]", value="Sets your character's charisma stat.", inline = False)
  embed.add_field(name="!wisdomset <value> [@mention yourself]", value="Sets your character's wisdom stat.", inline = False)
  embed.add_field(name = "!intelligenceset <value> [@mention yourself]", value="Sets your character's intelligence stat.", inline = False)
  embed.add_field(name = "!constitutionset <value> [@mention yourself]", value="Sets your character's constitution stat.", inline = False)
  embed.add_field(name="!dexterityset <value> [@mention yourself]", value = "Sets your character's dexterity stat.", inline = False)
  embed.add_field(name="!strengthset <value> [@mention yourself]", value = "Sets your character's strength stat.", inline = False)
  embed.add_field(name="!dicerolld20", value = "Rolls a D20.", inline = False)
  embed.add_field(name="!getcharinfo <name, class, level, inventory, stats, all> [@mention yourself]", value="Gathers and sends character info.", inline = False)
  embed.add_field(name="!help", value = "This help message.", inline = False)
  embed.set_footer(text="Made by D&D Bot")
  await ctx.send(embed=embed)

@bot.command()
async def setstatus(ctx):
  await ctx.send("Set status.")
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for !help"))

@bot.command(pass_context=True)
@commands.has_role("Bot Creator")
async def delchar(ctx, User: discord.User):
  await ctx.send("Deleted requested users character.")
  try:
    del db[User.id]
  except:
    print("Error 1")
  try:
    del db[User.id, 'charclass']
  except:
    print("Error 2")
  try:
    del db[User.id, 'level']
  except:
    print("Error 3")
  try:
    del db[User.id, 'inv']
  except:
    print("Error 4")  
  try:
    del db[User.id, 'charisma']
  except:
    print("Error 5")
  try:
    del db[User.id, 'wisdom']
  except:
    print("Error 5")


keep_alive.keep_alive()

bot.run(token)