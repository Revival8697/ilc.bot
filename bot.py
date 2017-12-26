################################### Imports
import string, os, discord, asyncio
from discord.ext import commands
from random import randrange, uniform
import random
import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

################################### Settings
email = "Your user bot's email"
password = "Your user bot password"
token = """Mzk1MDcxNTUzMTk0MTY0MjM0.DSORyg.MoicewgHZzwTe8iRtBx2yVU264E""" #Do not remove the quotes
cmdpf = "+" # the command prefix # (cmdpf) is a variable for the command prefix that you set.
operators = ["228112572082028545"]
playedgame = 'Use %shelp for commands' % (cmdpf) #the played game message
description = 'Bot description' # bot's description

################################### Bot Codes
bot = commands.Bot(command_prefix=cmdpf, description=description)
@bot.event
async def on_ready():
    print(" Your Bot had successfully logged in as %s - %s"%(bot.user.name,bot.user.id))
    print(" Discord version is", discord.__version__)
    print(" ------------------------------------------------")
    print(" Hello there")
    print(" How are you today?")
    await bot.change_presence(game=discord.Game(name=playedgame,url="""https://www.twitch.tv/twitch""",type=1))

@bot.event
async def on_command_error(error, ctx):
    if ctx.message.author.id in operators:
        print (" Error: %s"%(error))
        return await bot.send_message(ctx.message.channel,"""```
    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    ████▌▄▌▄▐▐▌█████
    ████▌▄▌▄▐▐▌▀████
    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀```
    Try again ^_^""")
    await bot.send_message(ctx.message.channel,"""```py\n%s\n```\n%s, an error occurred."""%(error,ctx.message.author.mention))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return False
    if message.content.startswith('Hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await bot.send_message(message.channel, msg)

################################### Test COMMAND -- test if your bot is working or not
@bot.command()
async def ping():
    """The bot reply with a "Pong!"."""
    await bot.say("""Do you realy think that I will reply with a "Pong"?
What an idot :P""")

################################### Bot COMMANDS -- the bot commands
@bot.command()
async def joined(user : discord.Member):
    """Says when a user joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(user))

@bot.command()
async def say(*text):
    """Make the Bot say something."""
    await ctx.message.author.id
    await bot.say(" ".join(text))


@bot.command()
async def reverse(*text):
    """Make the Bot reverse something."""
    await bot.say(" ".join(text)[::-1])


@bot.command()
async def welcome(user : discord.Member):
    """Say "Welcome" to a user."""
    await bot.say("Welcome %s"%user.mention)


@bot.command()
async def hello(user : discord.Member):
    """Say "Hello" to a user."""
    if not user:
        await bot.say("Use %shello [user]"%cmdpf)
        return False
    await bot.say("Hello there %s"%user.mention)


@bot.command()
async def cya(user : discord.Member):
    """Say "Cya" to a user."""
    await bot.say("Gtg cya %s"%user.mention)


@bot.command()
async def tell(user : discord.Member,*text):
    """Send message to a user."""
    await bot.say("%s %s"%(user.mention," ".join(text)))

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def op(user : discord.Member):

        if user.id in operators:
            return await bot.say("%s is a operator"%(user))
        if not user.id in operators:
            await bot.say("%s is not a operator"%(user))

################################### Ctx COMMANDS -- The commands that only can be run by operators
@bot.command(pass_context = True)
async def endrun(ctx):
    """Turn off the Bot."""
    if ctx.message.author.id in operators:
        print(" Bot is OFFLINE")
        await os._exit(1)
    if not ctx.message.author.id in operators:
        await bot.say("You are not authorized to use that command.")

@bot.command(pass_context=True)
async def connect(ctx):
    """Connect the bot to the voice channel that the operators in."""
    if bot.is_voice_connected(ctx.message.server):
        return await bot.say("I am already connected to a voice channel.")
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await bot.join_voice_channel(voice_channel)

@bot.command(pass_context = True)
async def nick(ctx,user : discord.Member,*text):
    """Change other user's nickname."""
    if ctx.message.author.id in operators:
        await bot.change_nickname(ctx.message.server.get_member(user.id)," ".join(text))
    if not ctx.message.author.id in operators:
        await bot.say("You are not authorized to use that command.")

@bot.command(pass_context = True)
async def warn(ctx, user : discord.Member,*text):
    """Warn a user."""
    if ctx.message.author.id in operators:
        await bot.say("%s %s %s"%(user.mention,"! You just been WARNED for"," ".join(text)))
    if not ctx.message.author.id in operators:
        await bot.say("You are not authorized to use that command.")


@bot.command(pass_context = True)
async def kick(ctx, user : discord.Member,*text):
    """Kick a user."""
    if ctx.message.author.id in operators:
        await bot.kick(user)
        await bot.say("%s %s %s"%(user.mention," just been KICKED for"," ".join(text)))
        return print(" %s just been kicked for %s."%(user.name, text))
    if not ctx.message.author.id in operators:
        await bot.say('You are not authorized to use that command.')


@bot.command(pass_context = True)
async def ban(ctx, user : discord.Member,*text):
    """Ban a user."""
    if ctx.message.author.id in operators:
        await bot.ban(user)
        await bot.say("%s %s %s"%(user.mention," just been BANNED for"," ".join(text)))
        return print(" %s just been banned for %s."%(user.name, text))
    if not ctx.message.author.id in operators:
        await bot.say('You are not authorized to use that command.')

@bot.command(pass_context = True)
async def unban(ctx, user : discord.Member,*text):
    """Unban a user."""
    if ctx.message.author.id in operators:
        await bot.unban(user)
        await bot.say("%s %s %s"%(user.mention," just been UNBANNED for"," ".join(text)))
        return print(" %s just been unbanned for %s."%(user.name, text))
    if not ctx.message.author.id in operators:
        await bot.say('You are not authorized to use that command.')

@bot.command(pass_context = True)
async def spam(ctx,times : int, *text):
    """Spams a message multiple times."""
    if ctx.message.author.id in operators:
        for i in range(times):
            await bot.say(" ".join(text))
            return print(" WARNING: Your Bot is spamming!")
    if not ctx.message.author.id in operators:
        await bot.say("You are not authorized to use that command.")

@bot.command(pass_context = True)
async def change_game(ctx,*text):
    """Change the bot's playing game."""
    if ctx.message.author.id in operators:
        await bot.change_presence(game=discord.Game(name=(" ".join(text)),url="""https://www.twitch.tv/twitch""",type=1), status=discord.Status.online, afk=False)
        return print(" The playing game had successfully changed to %s"%(text))
    if not ctx.message.author.id in operators:
        await bot.say("You are not authorized to use that command.")

################################### Meme COMMANDS -- the meme commands
@bot.command()
async def kat():
    """Show a Katten meme"""
    await bot.say(random.choice(["https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif","https://media.giphy.com/media/8tR6hfDnVOh1u/giphy.gif","https://media.giphy.com/media/yAqdjThdDEMF2/giphy.gif"]))

@bot.command()
async def doge():
    """Show a Dogen meme"""
    await bot.say(random.choice(["https://media.giphy.com/media/fvM5D7vFoACAM/giphy.gif","https://media.giphy.com/media/ZO8upuwNKfpm0/giphy.gif","https://media.giphy.com/media/xT9DPEPymVhAwi0mJy/giphy.gif"]))

@bot.command()
async def katvsdoge():
    """Show the unlimate katten vs dogen meme"""
    await bot.say('https://media.giphy.com/media/xtGpIp4ixR6Gk/giphy.gif')

###################################
###################################
################################### Bot run -- Make the bot run as a bot or a user bot
bot.run(token) #remove this if your bot is a user bot
#bot.run(email, password) #remove this if your bot is a bot
