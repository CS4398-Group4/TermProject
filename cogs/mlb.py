import json
import os
from datetime import datetime
import discord
from discord.ext import commands




class MLB(commands.Cog):

    def __init__(self, bot):
        self.__name__ = "MLB Extension"
        self.bot = bot
        self.schedule_array = []
        self.today = datetime.now().date()

    # * Listeners
    @commands.Cog.listener()
    async def on_ready(self):
        self.load_schedule()
        print(f'loaded cog: {self.__name__}')

    # * Commands
    @commands.command(aliases=['mlb'], brief="See The MLB Schedule for Today")
    async def schedule(self, ctx):
        today_str = self.today.strftime("%B %-d, %Y")
        today_compare = self.today.strftime("%Y-%m-%d")
        todays_games = []

        for game in self.schedule_array:
            if game['date'] == today_compare:
                todays_games.append(game)

        embed = discord.Embed(
            title=f"NBA Games for {today_str}")

        count = 1
        for game in todays_games:
            embed.add_field(name=f"Game {count}",
                            value=f"{game['visitor_name']} vs {game['home_name']} @ {game['gametimeET']} ET")
            count += 1

        await ctx.send(embed=embed)

    #  * Helpers
    def load_schedule(self):
        with open(os.path.join(os.path.dirname(__file__), 'assets/mlb_schedule.json')) as infile:
            data = json.load(infile)

            for game in data:
                self.schedule_array.append(game)


def setup(bot):
    bot.add_cog(MLB(bot))
