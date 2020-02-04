
"""
The beginning of every python file, the imports! Can't get anything done without libraries.
You'll need to install discordpy to develop with the discord bot library
You can find the necessary documentation at https://discordpy.readthedocs.io/en/latest/
"""
import discord
from discord.ext import commands

"""
Our unique bot token is given to us by discord and we should NEVER face it outward to the public.
This will be stored in 'config.json' which we also will NOT push to the github. (see .gitignore)
- commands.Bot() modifies the framework that we will use to create the bot (it's simpler and easier IMO)
- more information about our commands framework at https://discordpy.readthedocs.io/en/latest/ext/commands/index.html
"""
TOKEN = ''
bot = commands.Bot(command_prefix='!') # * we can change this to whatever we want '&' maybe?

"""
EVENTS

Our first event! on_ready(), called whenever the bot is ready!
If you're unfamiliar with decorators, that is what is comes before every function definition
(For now) There are two types of decorators:
- Events (when something happens in discord)
- Commands (when a user addresses our bot directly)

All that is important for now is that Event References do NOT have custom names.
You can find a full list of the Event References at https://discordpy.readthedocs.io/en/latest/api.html#event-reference
We'll probably be using these a lot.
"""
@bot.event  # * this is the decorator
async def on_ready(): # * this is the beginning of the Event Reference defintion.
    print(f'Logged in as: {bot.user.name}') # * How to print to console, if you need to error test
    print(f'With ID: {bot.user.id}') 
    # * the f'' changes a string into a format string. Format strings are Very important in bots. Just make sure your variable is inside of curly braces {}
    



"""
COMMANDS

Our first command. We need another decorator so the bot can recognize the function beneath
the decorator as a command!

Commands DO allow for custom names. So to access this function the user would have to type
our command_prefix along with the function name.

Unlike events, commands have one REQURIED parameter and that is context (ctx) which you will see below.
Context is described in the documentation so I won't get into it deep here but to be brief
we will use ctx as the beginning of our 'bread-crumb' that allows the bot to see the ENTIRE discord server.

In this exact scenario ctx.send() translates to 'send this back to the context it was called from'
meaning, whichever server/channel this command was called from the bot will reply with 'pong', but ctx
leads to MUCH bigger things
"""
@bot.command() # * decorator
async def ping(ctx): # * command name = ping. So to call this function the user must type !ping and the bot will respond 'pong'
    await ctx.send('pong')


"""
Lastly, the bot object declared above has a run method, which must taken in the token defined above.
And there you go, our bot is awake.

Literally no need to touch this.
"""
bot.run(TOKEN)
