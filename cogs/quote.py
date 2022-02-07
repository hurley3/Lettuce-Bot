import discord
from discord.ext import commands
import random

class quote(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def quote(self, ctx):
    with open('./assets/lettuce_quotes.txt', 'r') as f:
      contents = f.readlines()
    f.close()
    quote = random.choice(contents)
    await ctx.send(quote)

  @commands.command()
  async def suggestQuote(self, ctx):
    with open('cogs/suggestions/quote_suggestions.txt', 'a') as f:
      f.write(f'\"{ctx.message.content[14:]}\" - {ctx.message.author.display_name}\n')
    f.close()
    await ctx.send("Thank you for the suggestion")


def setup(client):
  client.add_cog(quote(client))