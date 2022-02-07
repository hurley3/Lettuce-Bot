import discord
from discord.ext import commands
import random

class fact(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def fact(self, ctx):
    with open('./assets/lettuce_facts.txt', 'r') as f:
      contents = f.readlines()
    f.close()
    fact = random.choice(contents)
    await ctx.send(fact)

  @commands.command()
  async def suggestFact(self, ctx):
    with open('cogs/suggestions/fact_suggestions.txt', 'a') as f:
      f.write(ctx.message.content[13:] + '\n')
    f.close
    await ctx.send("Thank you for the suggestion")
    

def setup(client):
  client.add_cog(fact(client))