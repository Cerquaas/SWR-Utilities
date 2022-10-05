import os
import discord
from discord.ext import commands

class UContext(commands.Context):
    async def r(self, message):
        await self.send(message)
    
    async def e(self, embed):
        await self.send(embed=embed)
    
class UBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def get_context(self, message, *, cls=UContext):
        return await super().get_context(message, cls=UContext)
    
    async def on_ready(self):
        print("Ready!")

bot = UBot(
    command_prefix="-",
    intents=discord.Intents.all(),
    status=discord.Status.dnd,
    activity=discord.Activity(
        type=discord.ActivityType.watching,
        name="over SWR"
    ),
    case_insensitive=True,
    help_command=None
)

bot.run(os.environ['TOKEN'])