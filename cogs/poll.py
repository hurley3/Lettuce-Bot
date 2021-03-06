import asyncio

import discord
from discord.ext import commands
import datetime


def embed_constructor(title, description, author, footer):
    embed = discord.Embed(title=title, description=description)
    embed.set_author(name=author, icon_url=author.avatar_url)
    embed.set_footer(text=footer)
    return embed


class poll(commands.Cog):
    def __init__(self, client):
        self.client = client

    # helper method

    @commands.command()
    async def poll(self, ctx, duration='0:0:0', multiple="single", question="", *options: str):
        if ctx.message.author.id in [593089008255631400,
                                     540009474920939520,
                                     461330847287476226,
                                     236289100749996033,
                                     461329912557731841,
                                     317792131366518784]:
            await ctx.message.delete()
            answers = ''
            emoji_answer = {}
            votes = {}
            voters = []
            total_votes = 0
            multi = False
            if multiple.lower() == "multiple":
                multi = True
            reactions = ['1️⃣',
                         '2️⃣',
                         '3️⃣',
                         '4️⃣',
                         '5️⃣',
                         '6️⃣',
                         '7️⃣',
                         '8️⃣',
                         '9️⃣',
                         '🔟']
            # figure out when the poll should end
            duration = list(map(int, duration.split(":")))
            start_time = datetime.datetime.now()
            end_time = datetime.datetime.now() + datetime.timedelta(hours=duration[0], minutes=duration[1],
                                                                    seconds=duration[2])

            # concat answers
            for i, answer in enumerate(options):
                answers += reactions[i] + "     " + answer + "\n"
                emoji_answer[reactions[i]] = answer

            description = "*Voting open until " + "`" + end_time.strftime("%b %d, %Y, %I:%M %p") + "`*\n\n" + answers

            for option in options:
                votes[option] = []

            message = await ctx.send(embed=
                                     embed_constructor(question, description, ctx.author,
                                                       "# of voters: " + str(len(voters)) + "\n# of votes: " + str(
                                                           total_votes)))

            for i, answer in enumerate(options):
                await message.add_reaction(reactions[i])

            def check(reaction, user):
                return reaction.message.id == message.id and user.id != 938987074286145536

            while True:
                try:
                    reaction, user = await self.client.wait_for('reaction_add', timeout=0.1, check=check)
                    await message.remove_reaction(reaction, user)

                    # Check if the user has already voted
                    if multi:
                        if user not in voters:
                            voters.append(user)
                        if user not in votes[emoji_answer[reaction.emoji]]:
                            votes[emoji_answer[reaction.emoji]].append(user)
                            total_votes += 1
                            await message.edit(
                                embed=embed_constructor(question, description, ctx.author,
                                                        "# of voters: " + str(len(voters)) + "\n# of votes: " + str(
                                                            total_votes)))

                    if user not in voters:
                        voters.append(user)
                        votes[emoji_answer[reaction.emoji]].append(user)
                        total_votes += 1
                        await message.edit(
                            embed=embed_constructor(question, description, ctx.author,
                                                    "# of voters: " + str(len(voters)) + "\n# of votes: " + str(
                                                        total_votes)))

                    print(str(votes) + " Total votes: " + str(total_votes))

                except asyncio.TimeoutError:
                    if datetime.datetime.now() > start_time + datetime.timedelta(hours=duration[0], minutes=duration[1],
                                                                                 seconds=duration[2]):
                        break

            await message.delete()

            results = ""
            for i, answer in enumerate(votes):
                results += reactions[i] + "`" + str(len(votes[answer])) + "` | "

            description = "*Voting results*\n\n" + answers + "\n" + results

            await ctx.send(embed=embed_constructor(question, description[:-2], ctx.author,
                                                   "# of voters: " + str(len(voters)) + "\n# of votes: " + str(
                                                       total_votes)))


def setup(client):
    client.add_cog(poll(client))
