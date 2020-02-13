import discord
from discord.ext import commands


class Admin_Area(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.__name__ = "Admin Area Cog"


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'loaded cog: {self.__name__}')


def setup(bot):
    bot.add_cog(Admin_Area(bot))