import os
import discord
from discord.ext import commands

class UContext(commands.Context):
    async def r(self, message):
        await self.send(message)
    
    async def e(self, embed):
        await self.send(embed=embed)
    
    async def m(self, lines):
        return "\n".join(lines)
    
class UBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def get_context(self, message, *, cls=UContext):
        return await super().get_context(message, cls=UContext)

    def load_extensions(self):
        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                try:
                    self.load_extension(f"cogs.{file[:-3]}")
                except Exception as e:
                    print(f"Error loading {file}: {e}")
    
    def reload_extensions(self):
        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                try:
                    self.reload_extension(f"cogs.{file[:-3]}")
                except discord.ExtensionNotLoaded:
                    self.load_extension(f"cogs.{file[:-3]}")
                except Exception as e:
                    print(f"Error reloading {file}: {e}")
    
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

bot.load_extensions()
bot.run(os.environ['TOKEN'])