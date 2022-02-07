import discord
from discord.ext import commands

class help(commands.Cog):
  def __init__(self, client):
    self.client = client

  @client.group(invoke_without_command=True)
  async def help(ctx):
    em = discord.Embed(title='Help', description='Use !help <command> for extended information on a command', color=ctx.author.color)

    em.add_field(name="Fun", value='quote, fact')
    em.add_field(name='Suggestions', value='suggestQuote, suggestFact, suggest')
    await ctx.send(embed=em)