import discord
from discord.ext import commands
from discord import app_commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Slash command: /ping
    @app_commands.command(name="ping", description="Check bot latency")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! `{latency} ms`")

    # Slash command: /hello
    @app_commands.command(name="hello", description="The bot says hello")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello, {interaction.user.mention}! 👋")

    # Slash command: /test — basic healthcheck for interactions
    @app_commands.command(name="test", description="Basic test command to verify slash functionality")
    async def test(self, interaction: discord.Interaction):
        """Simple slash command to confirm the bot receives interactions."""
        try:
            await interaction.response.send_message(f"Test OK — received from {interaction.user.mention}")
        except Exception as e:
            # If the immediate response fails, try to defer then follow up
            print(f"/test handler error: {e}")
            try:
                await interaction.response.defer()
                await interaction.followup.send(f"Test encountered an error: {e}")
            except Exception as e2:
                print(f"/test followup failed: {e2}")

    # Prefix command: !echo text
    @commands.command(name="echo")
    async def echo(self, ctx, *, message: str):
        await ctx.send(message)

    # Prefix command: !ping (checks latency)
    @commands.command(name="ping")
    async def ping_cmd(self, ctx):
        """Responds with bot latency for prefix command usage (!ping)."""
        try:
            latency = round(self.bot.latency * 1000)
            await ctx.send(f"Pong! `{latency} ms`")
        except Exception as e:
            # Keep prefix error handling simple and visible to the caller
            await ctx.send(f"Error: {e}")

    # Slash command: /server_stats — show basic guild statistics
    @app_commands.command(name="server_stats", description="Show basic server statistics")
    async def server_stats(self, interaction: discord.Interaction):
        guild = interaction.guild
        if not guild:
            await interaction.response.send_message("This command must be used in a server (guild).", ephemeral=True)
            return

        total = guild.member_count
        bots = sum(1 for m in guild.members if m.bot)
        humans = total - bots
        online = sum(1 for m in guild.members if getattr(m, "status", discord.Status.offline) != discord.Status.offline)
        text_channels = len([c for c in guild.channels if isinstance(c, discord.TextChannel)])
        voice_channels = len([c for c in guild.channels if isinstance(c, discord.VoiceChannel)])
        roles = len(guild.roles)
        owner = guild.owner

        embed = discord.Embed(title=f"{guild.name} — Server Stats", color=discord.Color.blurple())
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        embed.add_field(name="Total Members", value=str(total))
        embed.add_field(name="Humans", value=str(humans))
        embed.add_field(name="Bots", value=str(bots))
        embed.add_field(name="Online (approx)", value=str(online))
        embed.add_field(name="Text Channels", value=str(text_channels))
        embed.add_field(name="Voice Channels", value=str(voice_channels))
        embed.add_field(name="Roles", value=str(roles))
        embed.add_field(name="Owner", value=owner.mention if owner else "Unknown")
        embed.set_footer(text=f"Created: {guild.created_at.date()}")

        await interaction.response.send_message(embed=embed)

    # Log incoming interactions to help debug slash command delivery
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        try:
            name = None
            # interaction.data may be None for non-application interactions
            if getattr(interaction, "data", None):
                # data can contain the command name for application commands
                name = interaction.data.get("name") if isinstance(interaction.data, dict) else None
            print(f"[interaction] id={getattr(interaction, 'id', None)} user={getattr(interaction, 'user', None)} name={name} type={getattr(interaction, 'type', None)}")
        except Exception as e:
            print(f"on_interaction logging failed: {e}")

    # Error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(f"Error: {error}")

async def setup(bot):
    await bot.add_cog(General(bot))
