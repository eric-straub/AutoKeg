import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
import logging

# Load env variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Setup logging
logging.basicConfig(level=logging.INFO)

# Bot Intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize bot
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents,
            application_id=os.getenv("APPLICATION_ID")
        )

    async def on_error(self, event_method, *args, **kwargs):
        # Generic event error logger to capture uncaught exceptions in event handlers
        import traceback
        print(f"Unhandled exception in event: {event_method}")
        traceback.print_exc()

    async def setup_hook(self):
        # Load cogs
        await self.load_extension("cogs.general")

        # # Sync slash commands
        # await self.tree.sync()
        # print("Slash commands synced.")

# Create bot instance
bot = MyBot()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    await bot.tree.sync()
    print("Slash commands synced.")
    print("Bot is ready.")


bot.run(TOKEN)
