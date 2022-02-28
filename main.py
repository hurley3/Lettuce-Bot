import discord
import os
import Keep_Alive
from dataclasses import dataclass
from discord.ext import commands
# from ffmpeg import video
from cogs import audio, fact, quote, meme, suggest

cogs = [audio, fact, quote, meme, suggest]

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix='!', case_insensitive=True, help_command=None, intents=intents)

for i in cogs:
    i.setup(client)


@dataclass
class Lettuce:
    name: str


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Lettuce Member")
    await member.add_roles(role)


@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title='Help',
                       description='Use !help <command> for extended information on a command. All commands are not case sensetive',
                       color=ctx.author.color)

    em.add_field(name="Fun", value='Quote, Fact, Lettuce, Meme')
    em.add_field(name='Suggestions', value='suggestQuote, suggestFact, suggest')
    em.add_field(name='Club Info', value='Countdown')
    await ctx.send(embed=em)


@help.command()
async def quote(ctx):
    em = discord.Embed(title='Quote',
                       description='Sends a random lettuce related quote.  New quotes can be suggested using the suggestQuote command')
    em.add_field(name='**Syntax**', value='!quote')
    await ctx.send(embed=em)


@help.command()
async def fact(ctx):
    em = discord.Embed(title='Fact',
                       description='Sends a random lettuce related fact.  New quotes can be suggested using the suggestFact command')
    em.add_field(name='**Syntax**', value='!fact')
    await ctx.send(embed=em)


@help.command()
async def lettuce(ctx):
    em = discord.Embed(title='Lettuce', description='Says the word lettuce repeatedly')
    em.add_field(name='**Syntax**', value='!lettuce [integer]')
    await ctx.send(embed=em)


@help.command()
async def countdown(ctx):
    em = discord.Embed(title='Countdown', description='Tells you the number of days until the next competition')
    em.add_field(name='**Syntax**', value='!countdown')
    await ctx.send(embed=em)


@help.command()
async def suggestQuote(ctx):
    em = discord.Embed(title='Suggest Quote',
                       description='Sends a random lettuce related quote.  New quotes can be suggested using the suggestQuote command')
    em.add_field(name='**Syntax**', value='!quote')
    await ctx.send(embed=em)


@help.command()
async def meme(ctx):
    em = discord.Embed(title='Meme', description='Sends a random lettuce meme')
    em.add_field(name='**Syntax**', value='!meme')
    await ctx.send(embed=em)


@help.command()
async def suggest(ctx):
    em = discord.Embed(title='Suggest', description='Stores any suggestions you have for the devs reguarding the bot')
    em.add_field(name='**Syntax**', value='!suggest [suggestion]')
    await ctx.send(embed=em)


@client.command()
async def countdown(ctx):
    await ctx.send("Date of competition TBD")


# Not sure if you wanted x to be the number
# Of times lettuce is said or the upper for
# RNG for the number of times it is said
@client.command()
@commands.cooldown(1, 60.0, commands.BucketType.guild)
async def Lettuce(ctx, args):
    try:
        num = int(args)
        if num > 10:
            await ctx.send(f'{num} is larger than 10. For performance reasons I will only send Lettuce 10 times')
            num = 10
        f = open("./assets/lettuce_count.txt", 'r')
        count = f.readline()
        for i in range(num):
            count += 1
            await ctx.send("Lettuce")
        f.close()
        f = open("./assets/lettuce_count.txt", 'w')
        f.write(count)
        f.close()
    except:
        await ctx.send(f'\"{args}\" is not an integer')


@client.command()
async def readme(ctx):
    pass


@client.command()
async def scream(ctx):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('Lettuce.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)


@client.command()
async def kill(ctx):
    await client.logout()


'''
@client.command(pass_context=True)
async def scream(ctx):
  channel = ctx.author.voice.channel
  await channel.connect()
  vc= await client.join_voice_channel(channel)
  player = vc.create_ffmpeg_player('lettuce.mp3', after=lambda: print('done'))
  player.start()
  while not player.is_done():
    await asyncio.sleep(1)
  # disconnect after the player has finished
  player.stop()
  await vc.disconnect()
'''

# @client.event
# async def on_message(message):
#  if message.author == client.user:
#    return
#  author =(str(message.author))
#
#  #Random lettuce quote command
#  if (message.content.startswith("!Lettuce x")):
#    quote = random.choice(lettucequotes)
#    await message.channel.send(quote)
#
#  #Random Lettuce fact command
#  if (message.content.startswith("!Lettuce fact")):
#    fact = random.choice(lettucefacts)
#    await message.channel.send(fact)
#
#  #Lettuce competition countdown
#	
#  if (message.content.startswith("!Lettuce #countdown")):
#    today = datetime.date.today()
#    future = datetime.date(2019,9,20)
#    diff = future - today
#    await message.channel.send("There are " + diff + " days until the lettuce competition")


# Lettuce commands/functionaity ideas
# Lettuce quotes
# Pick a number 1-x and it says lettuce that many times
# lettuce facts
# count down to lettuce competition (once date is set)
# lettuce trivia
# command that sends lettuce memes
# command that makes it join a vc and scream lettuce (dont know how to do this one tbh)


# Script shit
Keep_Alive.keep_alive()
my_secret = os.environ['TOKEN']

client.run((my_secret))
