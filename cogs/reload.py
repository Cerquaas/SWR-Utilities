import datetime
import discord
from discord.ext import commands

class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx):
        start = datetime.datetime.now()
        self.bot.reload_extensions()
        end = datetime.datetime.now()

        time = (end - start).total_seconds() * 1000

        await ctx.r(f"Reloaded extensions in `{time}`ms.")

def setup(bot):
    bot.add_cog(Reload(bot))