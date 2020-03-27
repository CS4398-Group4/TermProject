import json
import os
from datetime import datetime
import discord
from discord.ext import commands


class MLB(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__name__ = "MLB Schedule"
        self.schedule = []
        self.today = datetime.now().date

    def load_mlb_schedule(self):
        with open(os.path.join(os.path.dirname(__file__), 'assets/mlb_schedule.json')) as infile:
            data = json.load(infile)
        for game in data:
            self.schedule.append(game);

    # listener
    @commands.Cog.listener()
    async def on_ready(self):
        self.load_mlb_schedule()
        print(f'loaded cog: {self.__name__}')

    # command
    @commands.command(aliases=['mlb sch', 'mlb'], brief="See The MLB Schedule for today")
    async def get_schedule(self, ctx):
        count = 1
        current1 = self.today.strftime("%B %-d, %Y")
        current = self.today.strftime("%Y-%m-%d")
        current_games = []

        for games in self.schedule:
            if games['date'] == current:
                current_games.append(games)
        embed = discord.Embed(title=f"MLB Games for {current1}")

        for games in current_games:
            embed.add_field(name=f"Game {count}", value=f"{games['Visitor']} vs {games['Home']} @ {games['GameTimeET']} ET")
            count += 1
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(MLB(bot))
