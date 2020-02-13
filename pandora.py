
#  * Imports
import discord
from discord.ext import commands
import json
import os


# * Bot Initilization and Token Loading
bot = commands.Bot(command_prefix='!') # * we can change this prefix to whatever we want '-' maybe?

with open('config.json', 'r') as fin:
    data = json.load(fin)
    TOKEN = data["token"]

"""
EVENTS
"""
@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}') 
    print(f'With ID: {bot.user.id}')

"""
COMMANDS
"""
@bot.command(name="ping", brief="ping the bot!", description="A ping command to Pandora's Box, should respond with 'pong'.")
async def ping(ctx):
    await ctx.send('pong')

# * At a later date we should probably add permissions or 'hidden=True' to this command
@bot.command(name="clear", aliases=['purge'], brief="Remove messages [Admin Only]", description="Messages are annoying, if you're an Admin, use this to get rid of those pesky messages!")
async def clear(ctx, amount=2):
    if amount <= 0:
        await ctx.send("I can't purge 0 messages. Try again!")

    await ctx.channel.purge(limit=amount)

"""
COG LOADING
"""
@bot.command(hidden=True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command(hidden=True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command(hidden=True)
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print(f"{extension} cog, reloaded!")
    await ctx.send(f'{extension} cog, reloaded!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

"""
No need to touch this.
"""
bot.run(TOKEN)
