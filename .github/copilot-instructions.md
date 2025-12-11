# Discord-Bot — AI Coding Guidelines (repo-specific)

This repo is a small, modular Discord bot using `discord.py`. The entrypoint is `bot.py`, cogs live in `cogs/`, and runtime state is stored as small JSON files under `data/`.

Key points for AI contributors:

- **Entrypoint & lifecycle**: `bot.py` builds `MyBot`, configures `intents`, loads cogs in `MyBot.setup_hook()` (via `await self.load_extension("cogs.NAME")`), and syncs application commands in `on_ready()` using `await bot.tree.sync()`.
- **Cogs pattern**: Every cog exports `async def setup(bot)` and registers itself with `await bot.add_cog(MyCog(bot))`. Follow existing naming and pass `bot` into cog constructors.
- **Commands mix**: The codebase uses both application (slash) commands (`@app_commands.command`) and legacy prefix commands (`@commands.command`). Prefer `interaction.response.send_message()` for immediate replies; use `await interaction.response.defer()` + `interaction.followup.send()` for long-running work.
- **Persistent state**: Small JSON files in `data/` (notably `ranks.json`, `welcome.json`). Helpers like `load_ranks()`/`save_ranks()` read/write synchronously with `json.dump(..., indent=4)`. Always ensure `data/` exists (`os.makedirs('data', exist_ok=True)`).
- **Tests**: There are small unit tests in `tests/test_rank.py` (e.g., `calculate_level(xp)`). Run targeted tests with `pytest tests/test_rank.py::test_calculate_level_examples` or `pytest -q`.

Developer workflows & commands:

- Create a `.env` with `DISCORD_TOKEN` (and optional `APPLICATION_ID`).
- Install deps: `pip install -r requirements.txt`.
- Run locally: `python3 bot.py` (look for "Slash commands synced." and "Bot is ready.").
- Run tests: `pytest tests/test_rank.py`.

Repo-specific conventions:

- Cog setup must use `async def setup(bot)` and call `await bot.add_cog(...)`.
- Event listeners use `@commands.Cog.listener()`; handlers should catch/log errors rather than raise (see `welcome.py` patterns).
- Permission checks follow Discord `interaction.user.guild_permissions` (e.g., `manage_guild`) for admin commands.
- Small synchronous JSON persists are acceptable here — if you change shape, update all consumers (search for `RANK_FILE` / `WELCOME_FILE`).

Integration & runtime notes:

- Logging: codebase uses `logging.basicConfig(level=logging.DEBUG)`; gateway events may be printed in `MyBot.on_socket_response` — keep this while debugging slash command delivery.

Examples to reference:

- Add a new cog: mirror `cogs/general.py` and add `await self.load_extension('cogs.my_cog')` inside `MyBot.setup_hook()` in `bot.py`.
- XP system: see `cogs/rank.py::calculate_level(xp)` and persistence in `data/ranks.json`.

Minimal editing checklist for AI agents:

- Preserve public API: `setup` functions and Cog class names.
- When changing JSON formats, update loaders/savers and run `tests/test_rank.py`.
- Document external dependencies (system binaries like `ffmpeg`) and add Python deps to `requirements.txt`.

If you'd like, I can expand any section (testing, adding a new cog template, CI steps). Please tell me which parts to clarify or extend.
