import discord
from discord.ext import commands
import random


class fact(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def count(self, ctx):
        with open('./assets/lettuce_count.txt', 'r') as f:
            contents = f.readline()
        f.close()
        await ctx.send(f'Lettuce has been said {contents} times')

def setup(client):
    client.add_cog(fact(client))