# Discord Bot Testing Guide

Complete pre-release testing checklist for all bot components.

---

## Phase 1: Startup & Connection Tests

Run the bot and verify it starts cleanly:

```bash
python3 bot.py
```

**Checklist**:
- [ ] Bot logs in successfully (`Logged in as YourBot#XXXX`)
- [ ] All cogs load without errors
- [ ] Slash commands sync (`Slash commands synced.`)
- [ ] Bot status shows as **Online** in Discord
- [ ] No error messages in console after "Bot is ready."

**Expected Output**:
```
Logged in as YourBot#1234 (ID: 123456789)
Slash commands synced.
Bot is ready.
```

---

## Phase 2: General Commands Testing

### Test: `/ping`
- [ ] Command appears in slash menu
- [ ] Returns latency in milliseconds (e.g., "Pong! `45 ms`")
- [ ] Response time is reasonable (<500ms)

### Test: `/hello`
- [ ] Returns greeting with user mention
- [ ] Includes wave emoji (👋)

### Test: `/test`
- [ ] Slash command test command works
- [ ] Returns confirmation message

### Test: `/help`
- [ ] Shows all command categories
- [ ] `/help general` shows general commands
- [ ] `/help rank` shows rank system commands
- [ ] `/help fun` shows fun commands
- [ ] `/help info` shows info commands
- [ ] `/help moderation` shows moderation commands
- [ ] `/help economy` shows economy commands
- [ ] Invalid category returns error message

### Test: `/status`
- [ ] Shows bot status (Online)
- [ ] Shows latency in ms
- [ ] Shows uptime in HH:MM:SS format
- [ ] Shows version number

### Test: `/server_stats`
- [ ] Shows server name
- [ ] Displays correct member count
- [ ] Shows breakdown of humans vs bots
- [ ] Lists text and voice channel counts
- [ ] Shows role count
- [ ] Displays owner mention
- [ ] Shows creation date

### Test: `!ping` (Prefix Command)
- [ ] Returns latency when typing `!ping`
- [ ] Works in channels where bot has message permissions

### Test: `!echo <text>` (Prefix Command)
- [ ] Repeats back exactly what user types
- [ ] Works with spaces and special characters

---

## Phase 3: XP & Rank System Testing

### Test: Automatic XP Award
- [ ] Send 5+ messages in a channel
  - [ ] First message awards XP (15-25 range)
  - [ ] Second message within 10 seconds: no XP awarded (cooldown works)
  - [ ] Wait 11 seconds, send another message: XP awarded
- [ ] Check `data/ranks.json` file — user should be present with XP data
- [ ] Level-up announcements appear in channel when user levels up

### Test: `/rank`
- [ ] `/rank` shows your own stats
- [ ] `/rank @user` shows target user's stats
- [ ] Displays current level and total XP
- [ ] Shows user avatar
- [ ] Stats match what's in `data/ranks.json`

### Test: `/profile`
- [ ] Returns user profile with level and XP
- [ ] Similar to `/rank` command

### Test: `/leaderboard`
- [ ] Shows top 10 users by XP
- [ ] `/leaderboard 1` shows first page
- [ ] `/leaderboard 2` shows next set of users
- [ ] Displays user ranks correctly (#1, #2, etc.)
- [ ] Shows level and XP for each user

### Test: `/topranks`
- [ ] Returns quick top 10 view
- [ ] Formats nicely with rank numbers

### Test: `/xp_leaderboard`
- [ ] Shows users sorted by total XP (not level)
- [ ] Includes up to 15 users

### Test: `/next_level @user`
- [ ] Shows progress to next level
- [ ] Displays progress bar (Unicode characters)
- [ ] Shows XP needed remaining
- [ ] Calculates correctly (should match level formula: `sqrt(xp/50)`)

### Test: Admin XP Commands (require `manage_guild` permission)
- [ ] `/xp_set @user 5000` — sets user XP to exactly 5000
  - [ ] Verify in `/rank` that it changed
  - [ ] Check `data/ranks.json` to confirm
- [ ] `/xp_add @user 1000` — adds 1000 XP to user
  - [ ] Old level + new level shown correctly
- [ ] `/xp_recalc` — recalculates all user levels
  - [ ] Verify `data/ranks.json` levels are recalculated

### Test: Permission Denied Cases
- [ ] Non-admin tries `/xp_set` → shows "Missing permissions"
- [ ] Error message is ephemeral (only visible to user)

---

## Phase 4: Welcome System Testing

### Test: `/welcome_set <message>`
- [ ] Set message: `/welcome_set Welcome {user} to {guild}!`
- [ ] Command confirms message was set
- [ ] Check `data/welcome.json` to verify storage

### Test: `/welcome_set_channel #channel`
- [ ] Set channel: `/welcome_set_channel #welcome`
- [ ] Confirmation shows channel mention
- [ ] `/welcome_set_channel` (without channel) switches to DM mode

### Test: `/welcome_toggle true/false`
- [ ] Enable: `/welcome_toggle true` → confirms enabled
- [ ] Disable: `/welcome_toggle false` → confirms disabled
- [ ] Disabled state prevents welcome messages

### Test: `/welcome_show`
- [ ] Displays current configuration
- [ ] Shows enabled/disabled status
- [ ] Shows channel or "DMs"
- [ ] Shows current message template

### Test: `/welcome_help`
- [ ] Shows placeholders: `{user}`, `{name}`, `{guild}`
- [ ] Lists common commands
- [ ] Provides usage tips

### Test: Member Join Event (Requires Test Member)
- [ ] Add a test user account to server
- [ ] Configure welcome message: `/welcome_set Welcome {user}!`
- [ ] Configure channel: `/welcome_set_channel #general`
- [ ] Have test user join the server
  - [ ] Welcome message appears in channel
  - [ ] All placeholders are replaced correctly
- [ ] Switch to DM mode and test again:
  - `/welcome_set_channel` (remove channel)
  - Have another test user join
  - [ ] DM is sent to new member

---

## Phase 5: Fun & Games Testing

### Test: `/dice` and `/dice 2d6`
- [ ] `/dice` rolls d20 (result 1-20)
- [ ] `/dice 3d6` rolls 3d6 (shows individual rolls + total)
- [ ] `/dice 1d100` rolls d100
- [ ] Invalid format (e.g., `/dice xyz`) returns error
- [ ] Excessive rolls (e.g., `/dice 1000d1000`) rejected with message

### Test: `/coin`
- [ ] Returns "Heads" or "Tails"
- [ ] Includes coin emoji

### Test: `/rps rock` (Rock-Paper-Scissors)
- [ ] `/rps rock` returns embed with choices and result
- [ ] `/rps paper` can win, tie, or lose
- [ ] `/rps scissors` can win, tie, or lose
- [ ] Invalid choice rejected

### Test: `/8ball <question>`
- [ ] `/8ball will I pass the test?` returns a response
- [ ] Different questions return different responses
- [ ] Includes magic ball emoji (🔮)

### Test: `/choose option1, option2, option3`
- [ ] Returns one of the options randomly
- [ ] `/choose` with less than 2 options returns error
- [ ] Works with spaces in options

---

## Phase 6: User & Server Info Testing

### Test: `/userinfo`
- [ ] `/userinfo` shows your own info
- [ ] `/userinfo @user` shows target user's info
- [ ] Displays: ID, status, account age, join date, roles, avatar
- [ ] Status emoji shows correct state (🟢 online, 🟡 idle, 🔴 dnd, ⚫ offline)

### Test: `/serverinfo`
- [ ] Shows server name and icon
- [ ] Member count (humans vs bots)
- [ ] Channel counts (text, voice, categories)
- [ ] Role count
- [ ] Created date and age
- [ ] Boost tier

### Test: `/avatar @user`
- [ ] Displays user's avatar in large embed
- [ ] Includes link to avatar
- [ ] Works with users without custom avatars

### Test: `/whois <name>`
- [ ] `/whois partialname` finds users by partial name match
- [ ] `/whois @user` finds by mention
- [ ] Multiple matches show all options
- [ ] No matches return error

### Test: `/roles`
- [ ] Lists all server roles
- [ ] Shows member count for each role
- [ ] Large role lists are paginated

---

## Phase 7: Moderation System Testing

### Test: `/warn @user <reason>`
- [ ] Warning is recorded
- [ ] User gets warning count
- [ ] Check `data/warns.json` to verify storage
- [ ] User receives DM notification (if DMs open)

### Test: `/warns @user`
- [ ] Shows all warnings for user
- [ ] Displays reason, issued by, and timestamp
- [ ] Empty warns list if user has no warnings

### Test: `/clearwarn @user`
- [ ] Removes all warnings
- [ ] Verification message shows
- [ ] `data/warns.json` updated

### Test: `/timeout @user 1h`
- [ ] User is muted for 1 hour
- [ ] User cannot send messages (verify in Discord)
- [ ] Different durations: `30m`, `2h`, `1d`
- [ ] Invalid format returns error

### Test: `/untimeout @user`
- [ ] Removes mute from user
- [ ] User can send messages again

### Test: `/purge 5`
- [ ] Deletes last 5 messages
- [ ] Only works with `moderate_members` permission
- [ ] Non-admins get permission error
- [ ] Count limited to 1-100

### Test: Permission Checks
- [ ] Non-mods cannot use `/warn` → shows permission error
- [ ] Permission error is ephemeral

---

## Phase 8: Economy System Testing

### Test: `/balance`
- [ ] Shows your own balance (should be 0 initially)
- [ ] `/balance @user` shows target balance
- [ ] Displays total earned also

### Test: `/daily`
- [ ] First claim: awards 100 Credits
  - [ ] Verification message shows amount
  - [ ] Check `data/economy.json` balance increased
- [ ] Second claim within 24h: returns cooldown error
- [ ] Shows hours remaining until next claim
- [ ] After 24h: can claim again

### Test: `/pay @user 50`
- [ ] Transfers 50 credits from you to target
- [ ] Your balance decreases
- [ ] Target balance increases
- [ ] Target receives DM notification
- [ ] Insufficient balance returns error
- [ ] Can't pay yourself (optional validation)
- [ ] Can't pay bots

### Test: `/rich`
- [ ] Shows top 10 richest users
- [ ] Users ranked by balance (not XP)
- [ ] Displays balance amounts

### Test: Admin Economy Commands (requires `administrator`)
- [ ] `/give_currency @user 500` — gives 500 credits
  - [ ] Balance updates
- [ ] `/reset_economy confirm:False` — asks for confirmation
- [ ] `/reset_economy confirm:True` — resets all balances (verify in JSON)

---

## Phase 9: Server Settings Testing

### Test: `/config_show`
- [ ] Displays all current settings
- [ ] Shows XP enabled status
- [ ] Shows modlog channel (if set)
- [ ] Shows autorole (if set)

### Test: `/set_xp_enabled true/false`
- [ ] Enable: `/set_xp_enabled true`
  - [ ] Send messages and verify XP is awarded
- [ ] Disable: `/set_xp_enabled false`
  - [ ] Send messages and verify NO XP is awarded
  - [ ] Check `data/settings.json`

### Test: `/set_modlog_channel #channel`
- [ ] Set to a channel: `/set_modlog_channel #mod-logs`
- [ ] Confirmation shows channel
- [ ] `/set_modlog_channel` (no channel) disables modlog
- [ ] Check `data/settings.json` for channel ID

### Test: `/set_autorole @role`
- [ ] Set to a role: `/set_autorole @Member`
- [ ] Confirmation shows role
- [ ] Add a test user to server
  - [ ] Test user automatically gets the role
- [ ] `/set_autorole` (no role) disables autorole
- [ ] Check `data/settings.json`

### Test: Permission Checks
- [ ] Non-admins get permission error for all settings commands
- [ ] Errors are ephemeral

---

## Phase 10: Data Persistence Testing

### Test: Rank Data Persistence
- [ ] Send messages and gain XP
- [ ] Restart the bot
- [ ] Check `/rank` — XP and level still there
- [ ] Verify `data/ranks.json` exists and has data

### Test: Economy Data Persistence
- [ ] Claim `/daily`
- [ ] Restart bot
- [ ] `/balance` still shows the credited amount
- [ ] Verify `data/economy.json` exists and has data

### Test: Welcome Config Persistence
- [ ] Set welcome message and channel
- [ ] Restart bot
- [ ] `/welcome_show` still shows configuration
- [ ] Verify `data/welcome.json` exists

### Test: Warns Data Persistence
- [ ] Warn a user
- [ ] Restart bot
- [ ] `/warns @user` still shows the warning
- [ ] Verify `data/warns.json` exists

### Test: Settings Data Persistence
- [ ] Configure XP, autorole, modlog
- [ ] Restart bot
- [ ] `/config_show` shows same settings
- [ ] Verify `data/settings.json` exists

### Test: JSON File Integrity
```bash
# Validate all JSON files
python3 -m json.tool data/ranks.json > /dev/null && echo "✅ ranks.json valid"
python3 -m json.tool data/economy.json > /dev/null && echo "✅ economy.json valid"
python3 -m json.tool data/welcome.json > /dev/null && echo "✅ welcome.json valid"
python3 -m json.tool data/warns.json > /dev/null && echo "✅ warns.json valid"
python3 -m json.tool data/settings.json > /dev/null && echo "✅ settings.json valid"
```

---

## Phase 11: Error Handling & Edge Cases

### Test: Permission Denied Gracefully
- [ ] Non-admin tries `/xp_set` → ephemeral error only visible to them
- [ ] Non-mod tries `/warn` → ephemeral error
- [ ] Non-mod tries `/purge` → ephemeral error

### Test: Invalid Inputs
- [ ] `/dice xyz` → error message
- [ ] `/rps invalid_choice` → error message
- [ ] `/timeout @user invalid_duration` → error message
- [ ] `/choose onlyoption` (< 2 options) → error message

### Test: Missing Data Gracefully
- [ ] `/warns @newuser` (never warned) → shows "no warnings"
- [ ] `/balance @newuser` (never claimed daily) → shows 0
- [ ] User not in leaderboard → doesn't show in list

### Test: Bot Limitations
- [ ] `/timeout @bot` → rejects with message (can't timeout bots)
- [ ] `/warn @bot` → rejects with message (can't warn bots)
- [ ] `/pay @bot` → rejects with message (can't pay bots)

---

## Phase 12: Multi-Server Testing (Optional)

If bot is in multiple servers:

- [ ] `/rank` shows correct per-user (not per-server) XP
- [ ] `/balance` shows correct per-user (not per-server) balance
- [ ] `/warns` shows correct per-guild warnings
- [ ] `/config_show` shows different settings per server
- [ ] Welcome message sends correctly in each server

---

## Phase 13: Performance Testing

### Test: High Message Volume
- [ ] Have multiple users send messages rapidly
  - [ ] All XP awards are credited
  - [ ] Cooldowns work correctly
  - [ ] No messages are skipped
  - [ ] Bot doesn't lag or disconnect

### Test: Large Data Files
- [ ] Simulate 1000+ users with XP data
  - [ ] Leaderboard loads quickly
  - [ ] `/rank` command responds fast
  - [ ] No timeout errors

---

## Phase 14: Pre-Release Checklist

### Code Quality
- [ ] No console errors on startup
- [ ] All cogs load successfully
- [ ] No unhandled exceptions
- [ ] All JSON files validate

### Feature Completeness
- [ ] All 48 commands work as documented
- [ ] All commands have descriptions
- [ ] Help system covers all categories
- [ ] Data persists across restarts

### Documentation
- [ ] README.md is up-to-date
- [ ] Command examples are accurate
- [ ] Troubleshooting section is helpful
- [ ] Setup instructions work

### Security
- [ ] Bot token is in `.env` (not committed to git)
- [ ] `.gitignore` includes `data/`, `.env`, `__pycache__/`
- [ ] Permission checks work correctly
- [ ] Sensitive commands are ephemeral

### User Experience
- [ ] All messages are clear and helpful
- [ ] Error messages explain what went wrong
- [ ] Emojis are used consistently
- [ ] Embeds are formatted nicely

---

## Quick Test Script

Run this to test core functionality quickly:

```bash
#!/bin/bash
# test_bot.sh

echo "🧪 Running quick bot tests..."
echo ""

# Syntax check
echo "✓ Checking syntax..."
python3 -m py_compile bot.py
python3 -m py_compile cogs/*.py

# JSON validation
echo "✓ Validating JSON files..."
python3 -m json.tool data/ranks.json > /dev/null 2>&1 || echo "  ranks.json is valid or doesn't exist yet"
python3 -m json.tool data/economy.json > /dev/null 2>&1 || echo "  economy.json is valid or doesn't exist yet"
python3 -m json.tool data/welcome.json > /dev/null 2>&1 || echo "  welcome.json is valid or doesn't exist yet"
python3 -m json.tool data/warns.json > /dev/null 2>&1 || echo "  warns.json is valid or doesn't exist yet"
python3 -m json.tool data/settings.json > /dev/null 2>&1 || echo "  settings.json is valid or doesn't exist yet"

# Import check
echo "✓ Checking imports..."
python3 -c "import discord; print(f'  discord.py version: {discord.__version__}')"
python3 -c "import dotenv; print('  python-dotenv OK')"

echo ""
echo "✅ Pre-flight checks passed!"
echo ""
echo "Next steps:"
echo "1. Create a Discord test server"
echo "2. Run: python3 bot.py"
echo "3. Test commands in Discord"
echo "4. Check data/ directory for created JSON files"
```

Save as `test_bot.sh` and run:
```bash
chmod +x test_bot.sh
./test_bot.sh
```

---

## Debugging Tips

### Enable Debug Logging
Add to `bot.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check Cog Loading
Look for these in console:
```
DEBUG:discord.client:on_ready has successfully been registered as an event
[interaction] ... (shows interactions received)
[socket] ... (shows gateway events)
```

### Inspect Data Files
```bash
# Pretty-print JSON
python3 -m json.tool data/ranks.json | head -20

# Check file sizes
du -h data/*.json
```

### Test Single Command
```python
# Add to bot.py for testing
@bot.tree.command(name="test_debug")
async def test_debug(interaction: discord.Interaction):
    await interaction.response.send_message("Debug test successful!")
```

---

## Sign-Off Checklist

Before releasing:

- [ ] All 14 phases completed
- [ ] No errors in console logs
- [ ] Data persists across restarts
- [ ] All 48 commands work correctly
- [ ] Permissions are enforced
- [ ] README is accurate
- [ ] No bot token in git history
- [ ] Ready for production!

---

## Post-Release Monitoring

After release, monitor:

1. **Console Logs**: Watch for repeated errors
2. **Data Files**: Ensure they're growing (users gaining XP, etc.)
3. **Discord Errors**: Check Discord's error messages
4. **User Feedback**: Listen for bug reports
5. **Performance**: Monitor response times under load

---

Good luck with your release! 🚀
