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

    async def setup_hook(self):
        # Load cogs
        await self.load_extension("cogs.general")

        # Sync slash commands
        await self.tree.sync()
        print("Slash commands synced.")

# Create bot instance
bot = MyBot()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Bot is ready.")


bot.run(TOKEN)
