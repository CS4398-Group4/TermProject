import discord
from discord.ext import commands


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.__name__="Weather Cog"

    """
    COMMANDS
    """
    @commands.command(name="weather", brief="Find the weather by Zipcode!", description="Give a Zipcode argument to recieve the weekly weather summary in that area!")
    async def weather(self, ctx):
        embed = discord.Embed(title="Placeholder", description="Placeholder")

        await ctx.send(embed=embed)

    """
    EVENTS
    """
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'loaded cog: {self.__name__}')


def setup(bot):
    bot.add_cog(Weather(bot))