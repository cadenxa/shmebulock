import discord
import random

# ---------------------------------------------------------------
#   Shmebulock!
# ---------------------------------------------------------------
# A silly Discord bot inspired by Gravity Falls
# Free to use and modify for personal/educational purposes.

# Requirements: 
# - Python 3.8 or higher
# - Pycord https://docs.pycord.dev/en/master/
# - An application with a bot account on the Discord development portal https://discord.com/developers/applications 

# OAuth2 scopes needed: bot

bot = discord.Bot(intents=discord.Intents.all()) # Requires all of the privileged gateway intents in the Bot section of 
# the Discord developer portal (this should not be an issue as long as the bot is in fewer than 100 servers)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}") # Gives console feedback when the bot logs on
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Shmebulock!")) # Fun custom status

# When someone says "Shmebulock" in a message, Shmebulock responds with his name, an emoji of himself, or both.
# If you don't want to use an emoji, remove the <:EMOJI:ID> placeholder from the responses list.
@bot.event
async def on_message(message):
    matches = ["shmebulock", "schmebulock", "schmebulok", "shmebulok", "BOT'S USER ID"] # Accounts for some typos and for being pinged.
    responses = ["Shmebulock!", "Shmebulock.", "<:EMOJI:ID>", "Shmebulock! <:EMOJI:ID>", "Shmebulock. <:EMOJI:ID>"]
    messagecontent = message.content
    messagecontent = messagecontent.replace(" ", "").lower() # Ignores spaces and capitalization
    if message.author.bot:
        return
    for a in matches:
        if a in messagecontent:
            print("Found a match!") # Console feedback when the bot finds a message it can respond to.
            await message.channel.send(random.choice(responses)) # Chooses randomly from the list of responses
            await message.add_reaction("<:EMOJI:ID>") # If you don't the bot want to react with an emoji, comment out this line.
            return

bot.run("TOKEN")
# Replace "TOKEN" with your bot's token (found in your developer portal) with quotes
# so that the bot will come online when the program runs.

# Once you've installed all the dependencies and changed all the placeholders in the code, just save and launch this .py script.
# Resetting the token in the Discord developer portal is a good way to shut down the bot quickly so you can make changes in the code.