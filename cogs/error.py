import discord
from discord.ext import commands

class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.MissingPermissions):
            await ctx.r("You don't have permission to use this command.")
        elif isinstance(error, commands.MissingRole):
            await ctx.r("You don't have the required role to use this command.")
        elif isinstance(error, commands.MissingAnyRole):
            await ctx.r("You don't have the required role to use this command.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.r("You are missing a required argument.")
        elif isinstance(error, commands.BadArgument):
            await ctx.r("You have provided an invalid argument.")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.r(f"This command is on cooldown. Try again in {round(error.retry_after)} seconds.")
        elif isinstance(error, commands.DisabledCommand):
            await ctx.r("This command is disabled.")
        elif isinstance(error, commands.NotOwner):
            await ctx.r("You are not the owner of this bot.")
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.r("Whoops! I do not accept DMs. Please DM an SHR or above if you need help!")
        else:
            await ctx.r("An unknown error has occured. This has been reported.")
            raise error

def setup(bot):
    bot.add_cog(Errors(bot))