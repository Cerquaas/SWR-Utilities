import discord
from discord.ext import commands

async def dm_block(ctx):
    if ctx.guild is None:
        raise commands.NoPrivateMessage()
    return True

def setup(bot):
    bot.add_check(dm_block)