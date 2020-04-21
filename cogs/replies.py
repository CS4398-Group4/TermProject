import discord
from discord.ext import commands





class Replies(commands.Cog):

    def __init__(self, bot):
        self.bot=bot
        self.__name__ = "Greeting Cog"

    @commands.command(name="brb", brief="Be Right Back!", description="Going AFK for a bit? Let Pandora's Box know and I'll remind other users.", aliases=['afk', 'back'])
    async def brb(self, ctx, args):
        await ctx.send(f"Got it! You'll be back in {args} minutes")
