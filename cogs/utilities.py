import discord
from discord.ext import commands

masslock_categories = [
            1006668280066494484,
            1019722888321966140,
            1006680654773239858,
            1006703511377035336,
            1006668448832700497,
            1006673827188711576,
            1006920180942770196
        ]

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
        await ctx.r(f"Pong! `{round(self.bot.latency * 1000)}ms`")
    
    @commands.command(
        aliases=["purge"]
    )
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 5):
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Cleared `{amount}` messages.", delete_after=5)

    @commands.command()
    @commands.has_permissions(manage_channel=True)
    async def slowmode(self, ctx, seconds: int = 0):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Set slowmode delay to `{seconds}` seconds.")
    
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            channel = ctx.channel
        
        await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send(f"Locked `{channel.name}`.")
    
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            channel = ctx.channel
        
        await channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(f"Unlocked `{channel.name}`.")
    
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def masslock(self, ctx):
        for category in masslock_categories:
            for channel in ctx.guild.get_channel(category).channels:
                await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        
        await ctx.send("Masslocked all MR and below channels.")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def massunlock(self, ctx):
        for category in masslock_categories:
            for channel in ctx.guild.get_channel(category).channels:
                await channel.set_permissions(ctx.guild.default_role, send_messages=True)
        
        await ctx.send("Unmassunlocked all MR and below channels.")

def setup(bot):
    bot.add_cog(Utilities(bot))