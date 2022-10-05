import discord
from discord.ext import commands
from replit import db

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
    @commands.has_permissions(manage_messages=True)
    async def send(self, ctx, channel: discord.TextChannel, *, message):
        await ctx.message.delete()
        await channel.send(message)
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def dm(self, ctx, user: discord.Member, *, message):
        try:
            await user.send(message)
            await ctx.r(f"DM setnt to `{user.name}#{user.discriminator}`.")
        except:
            await ctx.r(f"Failed to send DM to `{user.name}#{user.discriminator}`.")
    
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
    @commands.has_permissions(manage_channels=True)
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
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason):
        try:
            await member.send(f"You were kicked from `{ctx.guild.name}` for `{reason}`.")
        except discord.Forbidden:
            pass

        try:
            await member.kick(reason=reason)
        except discord.Forbidden:
            await ctx.r("I don't have permission to kick that member.")
            return

        await ctx.send(f"Kicked `{member.name}#{member.discriminator}` for `{reason}`.")
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason):
        try:
            await member.send(f"You were banned from `{ctx.guild.name}` for `{reason}`.")
        except discord.Forbidden:
            pass

        try:
            await member.ban(reason=reason)
        except discord.Forbidden:
            await ctx.r("I don't have permission to ban that member.")
            return

        await ctx.send(f"Banned `{member.name}#{member.discriminator}` for `{reason}`.")
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, user: discord.User):
        bans = await ctx.guild.bans()
        for ban in bans:
            if ban.user == user:
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned `{user}`.")
                return
        
        await ctx.send(f"`{user.name}#{user.discriminator}` is not banned.")
    
    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason):
        if str(member.id) not in db.keys():
            db[str(member.id)] = {}

            if "warnings" not in db[str(member.id)]:
                db[str(member.id)]["warnings"] = 1
        else:
            db[str(member.id)]["warnings"] += 1
        
        await ctx.send(f"Warned `{member.name}#{member.discriminator}` for `{reason}`. They now have `{db[str(member.id)]['warnings']}` warnings.")
    
    @commands.command()
    async def warnings(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        
        if member != ctx.author:
            if not ctx.author.guild_permissions.manage_messages:
                await ctx.r("You don't have permission to view other people's warnings.")
                return
        
        if str(member.id) not in db.keys():
            await ctx.r(f"`{member.name}#{member.discriminator}` has no warnings.")
        elif "warnings" not in db[str(member.id)]:
            await ctx.r(f"`{member.name}#{member.discriminator}` has no warnings.")
        else:
            await ctx.r(f"`{member.name}#{member.discriminator}` has `{db[str(member.id)]['warnings']}` warnings.")
    
    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def clearwarnings(self, ctx, member: discord.Member):
        if str(member.id) not in db.keys():
            await ctx.r(f"`{member.name}#{member.discriminator}` has no warnings.")
        elif "warnings" not in db[str(member.id)]:
            await ctx.r(f"`{member.name}#{member.discriminator}` has no warnings.")
        else:
            del db[str(member.id)]["warnings"]
            await ctx.r(f"Cleared warnings of `{member.name}#{member.discriminator}`.")


def setup(bot):
    bot.add_cog(Utilities(bot))