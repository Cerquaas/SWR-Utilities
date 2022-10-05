import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        h = [
            "__**Help**__",
            "",
            "`-help` - Shows this message.",
            "`-reload` - Reloads all extensions.",
            "`-ping` - Shows the bot's latency.",
            "`-say <message>` - Makes the bot say something.",
            "`-clear <amount>` - Clears a specified amount of messages.",
            "`-slowmode <seconds>` - Sets the slowmode delay of the current channel.",
            "`-lock <channel>` - Locks a channel.",
            "`-unlock <channel>` - Unlocks a channel.",
            "`-masslock` - Locks all channels in the server.",
            "`-massunlock` - Unlocks all channels in the server.",
            "`-kick <member> <reason>` - Kicks a member.",
            "`-ban <member> <reason>` - Bans a member.",
            "`-unban <member> <reason>` - Unbans a member.",
            "`-warn <member> <reason>` - Warns a member.",
            "`-warnings <member>` - Shows a member's warnings.",
            "`-clearwarnings <member>` - Clears a member's warnings."
        ]

        await ctx.r(ctx.m(h))

def setup(bot):
    bot.add_cog(Help(bot))