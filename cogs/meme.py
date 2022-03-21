import discord
from discord.ext import commands
import random

class meme(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def meme(self, ctx):
    img = f'./assets/memes/{random.randint(0, 17)}.jpg'
    await ctx.send(file=discord.File(img))

def setup(client):
  client.add_cog(meme(client))
