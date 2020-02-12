
#  * Imports
import discord
from discord.ext import commands
import json
import os


# * Token Loading
TOKEN = ''
bot = commands.Bot(command_prefix='!') # * we can change this to whatever we want '&' maybe?


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





# * COMMANDS
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command(aliases=['hi', 'hey'])
async def hello(ctx):
    await ctx.send(f"Hi There {ctx.author.mention}")


@bot.command(aliases=['purge'])
async def clear(ctx, amount=2):
    if amount <= 0:
        await ctx.send("I can't purge 0 messages. Try again!")

    await ctx.channel.purge(limit=amount)


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
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
Literally no need to touch this.
"""
bot.run(TOKEN)
