# AutoKeg Bot - AI Coding Guidelines

## Project Overview
AutoKeg is a modular Discord bot built with `discord.py` (v2.3.2+). The architecture uses Discord's **cog system** for organizing commands and event handlers into separate modules that load dynamically at startup.

## Architecture & Core Patterns

### Cog-Based Command Structure
- **Cogs** are reusable command modules in the `cogs/` directory
- Each cog is a class inheriting from `commands.Cog` with an async `setup(bot)` function
- Cogs are loaded in `MyBot.setup_hook()` via `await self.load_extension("cogs.module_name")`
- Commands are synced to Discord during bot startup with `await self.tree.sync()`

**Example from `cogs/general.py`:**
```python
class General(commands.Cog):
    async def setup(bot):  # Async function, not def
        await bot.add_cog(General(bot))
```

### Slash Commands vs Prefix Commands
- **Slash commands**: Use `@app_commands.command()` decorator (Discord's modern interaction model)
- **Prefix commands**: Use `@commands.command()` decorator (legacy, less recommended)
- Both require different response patterns: slash uses `interaction.response.send_message()`, prefix uses `ctx.send()`

### Intent Configuration
- The bot uses `discord.Intents.default()` with `intents.message_content = True`
- Only enable `message_content` if reading raw message text in non-slash contexts
- This is configured once in `AutoKeg.py` and applies to all cogs

## Setup & Execution

### Environment Requirements
1. Create `.env` file with `DISCORD_TOKEN=your_token_here` (loaded by `python-dotenv`)
2. Install dependencies: `pip install -r requirements.txt`
3. Run bot: `python AutoKeg.py`

The bot will fail loudly if `DISCORD_TOKEN` is missing — this is intentional.

## Development Conventions

### Adding New Commands
1. Create new cog in `cogs/new_module.py` inheriting from `commands.Cog`
2. Add `async def setup(bot)` function at module level
3. Load in `MyBot.setup_hook()`: `await self.load_extension("cogs.new_module")`
4. Cogs always receive `self.bot` to access bot instance for latency, user lookups, etc.

### Error Handling
- Implement `on_command_error()` listener in each cog for command-specific error handling
- Slash command errors should send response via `interaction.response.send_message()`
- Prefix command errors use `ctx.send()`

### Testing Bot Locally
```bash
cd /home/flayv/Documents/code/AutoKeg
source venv/bin/activate
python AutoKeg.py
```

## Key Files & Their Roles
- **`AutoKeg.py`**: Bot initialization, intents, cog loader, command tree sync
- **`cogs/general.py`**: Starter cog with ping, hello (slash), echo (prefix) examples
- **`requirements.txt`**: discord.py==2.3.2, python-dotenv, pynacl
- **`.env`**: Not tracked in git — stores DISCORD_TOKEN

## Discord.py Version Notes
- Using discord.py 2.3.2+ (modern async syntax)
- Command tree syncing happens in `setup_hook()` (pre v2.4 pattern)
- `application_id` removed from bot init (auto-detected in v2.3+)
