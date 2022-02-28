import discord
from discord.ext import commands

class lettuce(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    #@commands.cooldown(1, 60.0, commands.BucketType.guild)
    async def lettuce(self, ctx, args):
        try:
            num = int(args)
            if num > 10:
                await ctx.send(f'{num} is larger than 10. For performance reasons I will only send Lettuce 10 times')
                num = 10
                for i in range(num):
                    await ctx.send("Lettuce")
        except:
            await ctx.send(f'\"{args}\" is not an integer')

def setup(client):
    client.add_cog(lettuce(client))