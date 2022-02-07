import discord
from discord.ext import commands

class suggest(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def suggest(self, ctx):
    with open('cogs/suggestions/suggestions.txt', 'a') as f:
      f.write(ctx.message.content[9:] + '\n')
    f.close()
    await ctx.send("Thank you for the suggestion")

def setup(client):
  client.add_cog(suggest(client))