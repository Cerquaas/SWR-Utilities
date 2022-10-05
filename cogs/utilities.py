import discord
from discord.ext import commands

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.r(f"Pong! {round(self.bot.latency * 1000)}ms")

def setup(bot):
    bot.add_cog(Utilities(bot))