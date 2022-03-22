import discord
from discord.ext import commands
import random

#from main import client

maxGuess = 6  # number of rounds
filepath = "./assets/discordle_words.txt"  # path to words file (entries) must be newline separated)

bs = ":black_large_square:"  # HINT wrong letter emoji
ys = ":yellow_square:"  # HINT present letter emoji
gs = ":green_square:"  # HINT correct letter emoji
ng = ":blue_square:"  # GUESS no guess emoji
rs = ":red_square:"  # FORMAT final guess separator emoji

words = []
with open(filepath, 'r') as f:
    for line in f:
        words.append(line[0:-1])
guessList = []
hintList = []


class discordle(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def discordle(self, ctx):
        ri = ":regional_indicator_"
        wordPos = random.randint(0, len(words) - 1)
        correctWord = words[wordPos]
        correctLetters = list(correctWord)
        for i in range(len(correctLetters)):
            correctLetters[i] = ri + correctLetters[i] + ":"
        hintList = []
        guessList = []
        output = ""
        for i in range(maxGuess):
            hintList.append([bs, bs, bs, bs, bs])
            guessList.append([ng, ng, ng, ng, ng])
            output += "".join(x for x in guessList[i]) + "\n" + "".join(y for y in hintList[i]) + "\n"
        output += "".join(x for x in [rs, rs, rs, rs, rs])
        gameEmbed = discord.Embed(title="DISCORDLE", description=output)
        gameScreen = await ctx.send(embed=gameEmbed)
        for attempt in range(maxGuess):
            guess = "9"
            while guess not in words or list(guess) in guessList:
                guessPrompt = await ctx.send("Guess a word: (type \"quit\" to quit)")
                playerIn = await client.wait_for("message")
                try:
                    await error.delete()
                except:
                    pass
                guess = str(playerIn.content)
                await playerIn.delete()
                await guessPrompt.delete()
                if guess == "quit":
                    return
                if guess not in words:
                    error = await ctx.send("That word is not in the list")
                if list(guess) in guessList:
                    error = await ctx.send("That word has already been guessed")
            currentGuess = list(guess)
            for i in range(len(currentGuess)):
                currentGuess[i] = ri + currentGuess[i] + ":"
            guessList[attempt] = currentGuess

            hintOutput = [bs, bs, bs, bs, bs]
            for i in range(len(currentGuess)):
                if currentGuess[i] == correctLetters[i]:
                    hintOutput[i] = (gs)
                elif currentGuess[i] in correctLetters:
                    hintOutput[i] = (ys)
                else:
                    pass
            hintList[attempt] = hintOutput
            output = ""
            for i in range(attempt + 1):
                output += "".join(x for x in guessList[i]) + "\n" + "".join(y for y in hintList[i]) + "\n"
            for j in range(maxGuess - attempt - 1):
                output += "".join(x for x in [ng, ng, ng, ng, ng]) + "\n" + "".join(
                    y for y in [bs, bs, bs, bs, bs]) + "\n"
            output += "".join(x for x in [rs, rs, rs, rs, rs]) + "\n"
            if [gs, gs, gs, gs, gs] in hintList:
                break
            gameEmbed = discord.Embed(title="DISCORDLE", description=output)
            await gameScreen.edit(embed=gameEmbed)
        output += "".join(c for c in correctLetters)
        gameEmbed = discord.Embed(title="DISCORDLE", description=output)
        await gameScreen.edit(embed=gameEmbed)


def setup(client):
    client.add_cog(discordle(client))
