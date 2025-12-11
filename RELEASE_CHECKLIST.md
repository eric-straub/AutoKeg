# Pre-Release Checklist

Use this checklist to ensure the bot is production-ready before release.

---

## 1. Code Quality & Validation

- [ ] Run syntax validator: `python3 validate_bot.py`
- [ ] All checks pass (no ❌ errors)
- [ ] No unresolved ⚠️ warnings (or reviewed and approved)
- [ ] All cogs compile without errors
- [ ] bot.py compiles without errors

**Command**:
```bash
python3 validate_bot.py
```

---

## 2. Environment Setup

- [ ] `.env` file created with `DISCORD_TOKEN` and `APPLICATION_ID`
- [ ] `.env` file is NOT committed to git (check `.gitignore`)
- [ ] Bot token is valid and belongs to your bot
- [ ] Application ID is correct
- [ ] `.gitignore` includes: `.env`, `data/`, `__pycache__/`, `venv/`

**Verify**:
```bash
cat .gitignore | grep -E "\.env|data/|__pycache__|venv"
```

---

## 3. Discord Server Setup

- [ ] Created a test Discord server
- [ ] Bot is invited to the test server
- [ ] Bot has these permissions:
  - [ ] Send Messages
  - [ ] View Channels
  - [ ] Read Messages
  - [ ] Manage Messages (for `/purge`)
  - [ ] Moderate Members (for `/warn`, `/timeout`)
  - [ ] Manage Roles (for `/set_autorole`)

**Check Permissions in Discord**:
- Server Settings → Roles → Find your bot role
- Ensure all required permissions are enabled

---

## 4. Discord Developer Portal

- [ ] Application found in Developer Portal
- [ ] Bot tab shows correct token
- [ ] **Privileged Intents** enabled:
  - [ ] Message Content Intent (for XP system)
  - [ ] Server Members Intent (for member info)
  - [ ] Presence Intent (for status info)
- [ ] OAuth2 scope configured: `bot` + `applications.commands`
- [ ] Permissions match Discord server setup

**Link**: https://discord.com/developers/applications

---

## 5. Feature Testing

Run through **TESTING.md** phases:

### Phase 1: Startup
- [ ] Bot starts without errors
- [ ] All cogs load successfully
- [ ] Slash commands sync
- [ ] Bot appears online

### Phase 2: General Commands
- [ ] `/ping` works
- [ ] `/hello` works
- [ ] `/help` shows all categories
- [ ] `/status` shows uptime
- [ ] `/server_stats` shows server info
- [ ] `!ping` prefix command works
- [ ] `!echo` prefix command works

### Phase 3: XP & Rank System
- [ ] Send messages and gain XP
- [ ] Cooldown prevents spam XP
- [ ] `/rank` shows correct level/XP
- [ ] `/leaderboard` displays users
- [ ] `/next_level` shows progress
- [ ] Admin commands work: `/xp_set`, `/xp_add`, `/xp_recalc`
- [ ] XP data persists in `data/ranks.json`

### Phase 4: Welcome System
- [ ] `/welcome_set <message>` works
- [ ] `/welcome_set_channel <channel>` works
- [ ] `/welcome_show` displays config
- [ ] Welcome message sends on member join
- [ ] Placeholders replaced: `{user}`, `{name}`, `{guild}`

### Phase 5: Fun & Games
- [ ] `/dice` rolls d20
- [ ] `/dice 2d6` rolls custom dice
- [ ] `/coin` flips coin
- [ ] `/rps rock` plays game
- [ ] `/8ball <question>` answers
- [ ] `/choose` picks randomly

### Phase 6: User & Server Info
- [ ] `/userinfo` shows user details
- [ ] `/serverinfo` shows server details
- [ ] `/avatar` displays avatar
- [ ] `/whois` finds users
- [ ] `/roles` lists roles

### Phase 7: Moderation
- [ ] `/warn <user>` records warning
- [ ] `/warns <user>` shows all warnings
- [ ] `/timeout <user> 1h` mutes user
- [ ] `/untimeout <user>` removes mute
- [ ] `/purge 5` deletes messages
- [ ] Warnings persist in `data/warns.json`

### Phase 8: Economy
- [ ] `/daily` awards 100 Credits
- [ ] `/daily` 24h cooldown works
- [ ] `/balance` shows correct amount
- [ ] `/pay <user> 50` transfers credits
- [ ] `/rich` shows leaderboard
- [ ] Economy data persists in `data/economy.json`

### Phase 9: Server Settings
- [ ] `/config_show` displays settings
- [ ] `/set_xp_enabled false` disables XP
- [ ] `/set_autorole <role>` assigns role to new members
- [ ] Settings persist in `data/settings.json`

### Phase 10: Data Persistence
- [ ] All data files in `data/` directory
- [ ] Files are valid JSON
- [ ] Data persists after bot restart
- [ ] Files don't get committed to git

---

## 6. Error Handling

- [ ] Non-admins can't use admin commands
- [ ] Error messages are helpful
- [ ] Bot doesn't crash on invalid input
- [ ] Permission errors are ephemeral
- [ ] Bot recovers from failures gracefully

**Test**:
```
/xp_set @user 5000  # (as non-admin)
# Should return: "Missing permissions (manage_guild)."
```

---

## 7. Performance Testing

- [ ] Bot responds to commands in <1 second
- [ ] Multiple simultaneous messages don't cause lag
- [ ] Leaderboards load quickly
- [ ] No memory leaks (monitor task manager)
- [ ] Bot doesn't disconnect unexpectedly

**Stress Test**:
- Have 5+ users send messages rapidly
- Verify XP awards all messages
- Check response times

---

## 8. Documentation

- [ ] README.md is accurate
- [ ] Command descriptions match actual behavior
- [ ] Troubleshooting section covers common issues
- [ ] Setup instructions are clear
- [ ] TESTING.md is comprehensive

**Review**:
```bash
cat README.md | head -50
cat TESTING.md | head -50
```

---

## 9. Security & Privacy

- [ ] No bot token in code (only in `.env`)
- [ ] No personal data logged
- [ ] `.env` in `.gitignore`
- [ ] `data/` in `.gitignore`
- [ ] No hardcoded user IDs
- [ ] Permission checks enforced
- [ ] Sensitive responses are ephemeral

**Verify Git**:
```bash
git log --oneline | head -10
grep -r "DISCORD_TOKEN" cogs/ bot.py  # Should find nothing
```

---

## 10. Final Validation

Run the automated validator one more time:

```bash
python3 validate_bot.py
```

**Expected Output**:
```
✅ All checks passed! Bot is ready to run.
```

---

## 11. Deployment Readiness

### Before Going Live:

- [ ] `.env` file is created and populated
- [ ] Bot token is **never** shared or committed
- [ ] All code changes committed to git
- [ ] No uncommitted changes: `git status` shows clean
- [ ] Latest code pushed to repository

### Commands to Run:

```bash
# Verify clean git status
git status

# Verify no token in git
git log -p | grep -i "token" | head -5  # Should find nothing

# Verify .env is in gitignore
cat .gitignore | grep ".env"

# Verify no data files are committed
git ls-files data/  # Should show nothing
```

---

## 12. Go/No-Go Decision

**GO conditions** (all must be true):
- ✅ All validation checks pass
- ✅ All 14 testing phases completed
- ✅ No errors in 48 hours of monitoring
- ✅ Documentation is accurate
- ✅ No sensitive data in git history
- ✅ Bot responds to all 48 commands correctly
- ✅ Data persists across restarts
- ✅ Permission system works

**NO-GO conditions** (stop if any are true):
- ❌ Syntax errors in code
- ❌ Missing dependencies
- ❌ Bot token in git history
- ❌ Data files lost on restart
- ❌ Permission system broken
- ❌ Commands hang or timeout
- ❌ Console shows repeated errors

---

## 13. Post-Release Monitoring

After releasing (first week):

- [ ] Monitor console for errors
- [ ] Check `data/` directory is growing (users gaining XP)
- [ ] Verify commands still respond quickly
- [ ] Watch for user reports of issues
- [ ] Monitor bot uptime
- [ ] Check Discord API status if problems occur

**Monitoring Commands**:
```bash
# Check data directory growth
du -sh data/

# Check latest data files
ls -lah data/

# Monitor console output in real-time
python3 bot.py 2>&1 | tee bot.log
```

---

## Release Sign-Off

✅ **Ready to Release When**:

1. All checklist items above are checked ☑️
2. Bot has been running without errors for 24+ hours
3. All users in test server report no issues
4. Code review is complete
5. Deployment runbook exists (see below)

---

## Quick Deploy Checklist

When deploying to production:

```bash
# 1. Pull latest code
git pull origin dev

# 2. Verify dependencies
pip install -r requirements.txt

# 3. Validate environment
python3 validate_bot.py

# 4. Start bot (in screen or tmux)
screen -S discord-bot
python3 bot.py

# 5. Monitor initial startup (watch for 5 minutes)
# Ctrl-A then D to detach from screen

# 6. Verify bot is online
# Check Discord server - bot should show as online

# 7. Test a simple command
# In Discord: /ping
# Should return latency

echo "✅ Bot deployed successfully!"
```

---

## Rollback Plan

If critical issues occur:

```bash
# Kill the bot
screen -X -S discord-bot kill

# Revert to last known good commit
git checkout HEAD~1

# Restart bot
python3 bot.py
```

---

Good luck with your release! 🚀

Questions? Review **TESTING.md** and **README.md** for detailed information.
