# Command Testing Reference

Quick copy-paste commands for testing each feature.

---

## Testing Commands Checklist

Print this and check off each test as you complete it.

---

## 🔌 Startup Tests

```bash
# Start the bot
python3 bot.py

# Expected in console:
# Logged in as YourBot#1234
# Slash commands synced.
# Bot is ready.
```

---

## 🛠️ General Commands

```
Test: /ping
Expected: "Pong! `45 ms`" (or similar latency)

Test: /hello
Expected: "Hello, @YourName! 👋"

Test: /help
Expected: Shows all 6 categories

Test: /help rank
Expected: Shows rank system commands with examples

Test: /status
Expected: Shows Online status, latency, uptime, version

Test: /server_stats
Expected: Shows member count, channels, roles, creation date

Test: !ping
Expected: "Pong! `45 ms`"

Test: !echo hello world
Expected: "hello world"
```

---

## ⭐ XP & Rank System

```
Test: Send 5+ messages
Expected: See level-up message in chat (if level increased)

Test: /rank
Expected: Shows your level and XP

Test: /rank @user
Expected: Shows that user's level and XP

Test: /profile
Expected: Shows detailed profile

Test: /leaderboard
Expected: Shows top 10 users by XP

Test: /leaderboard 2
Expected: Shows users 11-20

Test: /topranks
Expected: Quick top 10 view

Test: /xp_leaderboard
Expected: XP-sorted ranking

Test: /next_level
Expected: Shows progress bar to next level with XP needed

Test: /xp_set @user 5000
Expected: Sets user's XP to 5000 (admin only)
Error if non-admin: "Missing permissions"

Test: /xp_add @user 1000
Expected: Adds 1000 XP to user (admin only)

Test: /xp_recalc
Expected: Recalculates all user levels (admin only)
```

---

## 👋 Welcome System

```
Test: /welcome_set Welcome {user} to {guild}!
Expected: "Welcome message updated."

Test: /welcome_set_channel #general
Expected: "Welcome messages will be sent to #general."

Test: /welcome_set_channel
Expected: "Welcome messages will be sent to DMs."

Test: /welcome_toggle true
Expected: "Welcome messages enabled."

Test: /welcome_toggle false
Expected: "Welcome messages disabled."

Test: /welcome_show
Expected: Shows current config with message, channel, enabled status

Test: /welcome_help
Expected: Shows guide with placeholders and examples

Test: Add new member to server (with welcome enabled)
Expected: Welcome message appears in configured channel or DM
         with placeholders replaced: {user}→@mention, {name}→displayname, {guild}→servername
```

---

## 🎮 Fun & Games

```
Test: /dice
Expected: Rolls 1d20, result 1-20

Test: /dice 3d6
Expected: Shows 3 individual rolls + total

Test: /dice 2d20
Expected: "Rolls: 15, 18
          Total: 33"

Test: /dice xyz
Error expected: "Invalid format. Use NdX"

Test: /coin
Expected: "Heads!" or "Tails!"

Test: /rps rock
Expected: Shows your choice, bot's choice, and result (win/loss/tie)

Test: /rps paper
Expected: Game result

Test: /rps scissors
Expected: Game result

Test: /8ball will the bot work?
Expected: Magic 8-ball response (random)

Test: /8ball should i deploy?
Expected: 🔮 Different response than before

Test: /choose pizza, tacos, sushi
Expected: "🎯 I choose: pizza" (or one of the options)

Test: /choose onlyoption
Error expected: "Provide at least 2 options"
```

---

## ℹ️ User & Server Info

```
Test: /userinfo
Expected: Shows your profile (ID, status, account age, roles, avatar)

Test: /userinfo @user
Expected: Shows @user's profile

Test: /serverinfo
Expected: Shows server name, members, channels, roles, creation date

Test: /avatar
Expected: Shows your avatar in large embed

Test: /avatar @user
Expected: Shows @user's avatar

Test: /whois yourname
Expected: Shows your profile (or multiple matches if ambiguous)

Test: /whois @user
Expected: Shows @user's profile

Test: /whois nonexistentname
Error expected: "No members found matching 'nonexistentname'"

Test: /roles
Expected: Lists all server roles with member counts
```

---

## ⚠️ Moderation System

```
Test: /warn @user spamming
Expected: "⚠️ Member Warned"
         Shows warning count

Test: /warn @bot any_reason
Error expected: "Cannot warn bots"

Test: /warns @user
Expected: Shows all warnings with reasons, issued by, timestamp

Test: /warns @newuser
Expected: "No warnings found"

Test: /clearwarn @user
Expected: "Cleared all warnings for @user"

Test: /timeout @user 1h
Expected: User is muted for 1 hour (cannot send messages)

Test: /timeout @user 30m
Expected: User is muted for 30 minutes

Test: /timeout @user invalid_duration
Error expected: "Invalid duration format"

Test: /untimeout @user
Expected: User can send messages again

Test: /purge 5
Expected: Deletes last 5 messages in channel

Test: /purge 0
Error expected: "Purge count must be between 1 and 100"

Test: /purge 150
Error expected: "Purge count must be between 1 and 100"

Test (non-admin): /warn @user
Error expected: "Missing permissions (moderate_members)"
```

---

## 💰 Economy System

```
Test: /balance
Expected: "Balance: 🪙 Credits 0" (initially)

Test: /balance @user
Expected: Shows @user's balance

Test: /daily
Expected: "💸 Daily Bonus Claimed!
          You received 🪙 Credits 100"

Test: /balance
Expected: "Balance: 🪙 Credits 100"

Test: /daily (again immediately)
Error expected: "You've already claimed today! Come back in 23.9 hours."

Test: /pay @user 50
Expected: "Sent 🪙 Credits 50 to @user"

Test: /balance
Expected: "Balance: 🪙 Credits 50" (100 - 50)

Test: /pay @user 100 (when you have 50)
Error expected: "Insufficient balance"

Test: /rich
Expected: Shows top 10 richest users

Test: /give_currency @user 500 (admin only)
Expected: "Gave 🪙 Credits 500 to @user"

Test (non-admin): /give_currency @user 100
Error expected: "Missing permissions (administrator)"

Test: /reset_economy confirm:False (admin)
Expected: "⚠️ This will reset all user balances!"

Test: /reset_economy confirm:True (admin)
Expected: "✅ Economy data reset."
```

---

## ⚙️ Server Settings

```
Test: /config_show
Expected: Shows current settings (XP enabled, channels, roles)

Test: /set_xp_enabled false
Expected: "XP rewards disabled for this server"

Test: Send messages (with XP disabled)
Expected: No XP is awarded, no level-up messages

Test: /set_xp_enabled true
Expected: "XP rewards enabled for this server"

Test: Send messages (with XP enabled)
Expected: XP is awarded again

Test: /set_modlog_channel #mod-logs
Expected: "Modlog channel set to #mod-logs"

Test: /set_modlog_channel
Expected: "Modlog channel disabled"

Test: /set_autorole @Member
Expected: "New members will be assigned @Member"

Test: Add new member to server
Expected: New member automatically gets @Member role

Test: /set_autorole
Expected: "Autorole disabled"

Test (non-admin): /set_xp_enabled false
Error expected: "Missing permissions (administrator)"
```

---

## 📊 Data Persistence Tests

```
# After running tests above, check data files:

Test: cat data/ranks.json
Expected: JSON with user IDs, XP, levels

Test: cat data/economy.json
Expected: JSON with user IDs, balances, total earned

Test: cat data/welcome.json
Expected: JSON with guild config (enabled, channel_id, message)

Test: cat data/warns.json
Expected: JSON with guild ID → user ID → array of warnings

Test: cat data/settings.json
Expected: JSON with guild ID → settings (prefix, xp_enabled, etc)

# Validate all JSON is valid:
Test: python3 -m json.tool data/ranks.json > /dev/null && echo "✅"
Expected: ✅ (no error output)

Test: Restart bot
Expected: All data persists (XP, balance, warnings still there)
```

---

## ✅ Final Verification Tests

```
Test: python3 validate_bot.py
Expected: "✅ All checks passed! Bot is ready to run."

Test: All 48 commands respond
Expected: Every command has a response (not "unknown command")

Test: Bot doesn't crash
Expected: No "Traceback" in console after running tests

Test: No token in git
Command: grep -r "DISCORD_TOKEN" cogs/ bot.py
Expected: (no output = good!)

Test: .env not committed
Command: git ls-files | grep ".env"
Expected: (no output = good!)

Test: All JSON files valid
Expected: ✅ marks for all 5 data files
```

---

## 🚨 Error Handling Tests

```
Test: /dice 1000d1000
Error expected: "Keep it reasonable: 1-100 dice, 1-1000 sides."

Test: /rps invalid_choice
Error expected: "Choose: rock, paper, scissors"

Test: /choose onlyoption
Error expected: "Provide at least 2 options"

Test: /timeout @user invalid
Error expected: "Invalid duration format. Use: 1h, 30m, 1d, etc."

Test: /warn @bot
Error expected: "Cannot warn bots"

Test: /pay @bot 50
Error expected: "Cannot send currency to bots"

Test (non-admin): /xp_set @user 5000
Error expected: "Missing permissions (manage_guild)." (ephemeral)

Test: All permission errors are ephemeral
Expected: Error only visible to user who triggered it
```

---

## Test Completion Checklist

Mark these off as you complete each category:

- [ ] 🔌 Startup Tests (all pass)
- [ ] 🛠️ General Commands (all respond)
- [ ] ⭐ XP & Rank System (data persists in ranks.json)
- [ ] 👋 Welcome System (config saves, member gets message)
- [ ] 🎮 Fun & Games (all commands work)
- [ ] ℹ️ User & Server Info (displays correct data)
- [ ] ⚠️ Moderation System (warnings save to warns.json)
- [ ] 💰 Economy System (daily works, balance persists in economy.json)
- [ ] ⚙️ Server Settings (config persists in settings.json)
- [ ] 📊 Data Persistence (all JSON files valid after restart)
- [ ] ✅ Final Verification (validate_bot.py passes)
- [ ] 🚨 Error Handling (all errors handled gracefully)

---

## Ready to Deploy?

When all checkboxes are complete: ✅ **Bot is ready for release!**

Next step: Follow **RELEASE_CHECKLIST.md** for go/no-go decision.
