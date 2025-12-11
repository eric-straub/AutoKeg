# Discord Bot - Testing & Release Guide

Complete guide for testing and releasing the Discord bot.

---

## Quick Start: Testing Your Bot

### 1. Pre-Flight Validation (30 seconds)

```bash
python3 validate_bot.py
```

This automated script checks:
- ✅ All required files exist
- ✅ Python syntax is valid
- ✅ Dependencies are installed
- ✅ `.env` configuration exists
- ✅ Data files are valid JSON
- ✅ Security checks (no token in git)

**Expected Output**: 
```
✅ All checks passed! Bot is ready to run.
```

---

### 2. Start the Bot (5 seconds)

```bash
python3 bot.py
```

**Expected Output**:
```
Logged in as YourBot#1234 (ID: 123456789)
Slash commands synced.
Bot is ready.
```

**Verify**:
- Bot appears online in Discord
- No error messages in console after "Bot is ready."

---

### 3. Quick Command Test (2 minutes)

In Discord, run these 3 commands:

| Command | Expected Result |
|---------|-----------------|
| `/ping` | Shows latency (e.g., "Pong! `45 ms`") |
| `/help` | Shows all 6 command categories |
| `!echo hello` | Responds with "hello" |

If all three work, the bot is functioning! ✅

---

## Full Testing Guide

For comprehensive pre-release testing, use **TESTING.md**:

```bash
# Read the full testing guide
cat TESTING.md
```

**14 Testing Phases** (each ~5-10 minutes):

1. ✅ Startup & Connection Tests
2. ✅ General Commands Testing
3. ✅ XP & Rank System Testing
4. ✅ Welcome System Testing
5. ✅ Fun & Games Testing
6. ✅ User & Server Info Testing
7. ✅ Moderation System Testing
8. ✅ Economy System Testing
9. ✅ Server Settings Testing
10. ✅ Data Persistence Testing
11. ✅ Error Handling & Edge Cases
12. ✅ Multi-Server Testing (optional)
13. ✅ Performance Testing
14. ✅ Pre-Release Checklist

**Estimated Time**: 60-90 minutes for complete testing

---

## Release Checklist

Before going live, use **RELEASE_CHECKLIST.md**:

```bash
# Read the release checklist
cat RELEASE_CHECKLIST.md
```

**12-Step Verification**:

1. Code Quality & Validation
2. Environment Setup
3. Discord Server Setup
4. Discord Developer Portal
5. Feature Testing
6. Error Handling
7. Performance Testing
8. Documentation
9. Security & Privacy
10. Final Validation
11. Deployment Readiness
12. Go/No-Go Decision

**Estimated Time**: 20-30 minutes

---

## Testing by Category

### Quick Category Tests

If you only have 15 minutes, test these core features:

```
⏱️ 3 min:   Startup & /ping command
⏱️ 2 min:   /help system
⏱️ 2 min:   Send messages → /rank (XP system)
⏱️ 2 min:   /balance → /daily (economy)
⏱️ 2 min:   /userinfo (info system)
⏱️ 2 min:   /welcome_set (welcome system)
```

### Testing Each System

**XP & Ranks** (5 min):
```
1. Send 5+ messages in a channel
2. Run /rank — check XP increased
3. Wait 11 seconds, send another — XP awarded again
4. Run /leaderboard — you should appear
5. Verify data in data/ranks.json
```

**Economy** (5 min):
```
1. Run /balance — shows 0 initially
2. Run /daily — get 100 Credits
3. Run /balance — shows 100
4. Run /pay @testuser 50 — transfer credits
5. Verify data in data/economy.json
```

**Moderation** (3 min):
```
1. Run /warn @user spam
2. Run /warns @user — see the warning
3. Run /clearwarn @user — warning removed
4. Verify data in data/warns.json
```

**Settings** (3 min):
```
1. Run /config_show — see current settings
2. Run /set_xp_enabled false
3. Send messages — no XP awarded
4. Run /set_xp_enabled true — XP works again
5. Verify data in data/settings.json
```

---

## Data File Validation

After testing, verify data files are valid:

```bash
# Check all JSON files are valid
python3 -m json.tool data/ranks.json > /dev/null && echo "✅ ranks.json"
python3 -m json.tool data/economy.json > /dev/null && echo "✅ economy.json"
python3 -m json.tool data/welcome.json > /dev/null && echo "✅ welcome.json"
python3 -m json.tool data/warns.json > /dev/null && echo "✅ warns.json"
python3 -m json.tool data/settings.json > /dev/null && echo "✅ settings.json"

# View sample data
python3 -m json.tool data/ranks.json | head -20
```

---

## Automated Test Script

For continuous testing, create a test loop:

```bash
#!/bin/bash
# test_loop.sh - Run bot tests continuously

while true; do
    echo "🧪 Running tests..."
    
    # Validate
    python3 validate_bot.py
    
    if [ $? -ne 0 ]; then
        echo "❌ Validation failed"
        break
    fi
    
    # Quick test
    echo "✅ Validation passed"
    sleep 5
done
```

Run with:
```bash
chmod +x test_loop.sh
./test_loop.sh
```

---

## Monitoring After Release

Once deployed, monitor with:

```bash
# Watch console output for errors
python3 bot.py 2>&1 | tee bot.log

# In another terminal, watch data growth
watch -n 5 'ls -lah data/'

# Check for errors
grep -i "error\|exception" bot.log
```

---

## Troubleshooting

### Bot won't start?

```bash
# 1. Run validator
python3 validate_bot.py

# 2. Check .env file
cat .env

# 3. Check Python version
python3 --version  # Should be 3.8+

# 4. Check dependencies
pip list | grep -i discord
```

### Commands not appearing?

```
1. Restart bot (messages sync on startup)
2. Check bot permissions in Discord
3. Check intents in Developer Portal:
   - Message Content Intent ✅
   - Server Members Intent ✅
   - Presence Intent ✅
```

### XP not awarding?

```
1. Ensure Message Content Intent is enabled
2. Check bot permissions (send messages)
3. Run /config_show — is XP enabled?
4. Check console for errors
```

### Data lost on restart?

```
1. Verify data/ directory exists
2. Check data files aren't empty
3. Run: python3 -m json.tool data/ranks.json
4. Ensure proper file permissions
```

---

## Release Workflow

### Step 1: Validate (5 min)
```bash
python3 validate_bot.py
# All checks should pass ✅
```

### Step 2: Test (60-90 min)
Follow **TESTING.md** phases 1-10
- Each phase should pass
- Take notes on any issues

### Step 3: Review (10 min)
- Check RELEASE_CHECKLIST.md
- Verify security (no token in git)
- Confirm documentation is accurate

### Step 4: Deploy (5 min)
```bash
# Ensure .env exists
ls -la .env

# Start bot
python3 bot.py

# Monitor for 5+ minutes
# Check Discord server - bot online?
```

### Step 5: Monitor (24h)
- Watch console for errors
- Test commands every few hours
- Check data/ directory is growing
- Gather user feedback

---

## Full Test Execution (90 min)

For a complete pre-release test cycle:

```bash
#!/bin/bash
echo "🤖 Discord Bot - Complete Test Cycle"
echo ""

# Phase 1: Validation (5 min)
echo "Phase 1: Validation..."
python3 validate_bot.py || exit 1
echo ""

# Phase 2: Startup (5 min)
echo "Phase 2: Starting bot (Ctrl+C after 30 seconds)..."
timeout 30 python3 bot.py || true
echo ""

# Phase 3: Data Validation (5 min)
echo "Phase 3: Data validation..."
for file in ranks.json economy.json welcome.json warns.json settings.json; do
    if [ -f "data/$file" ]; then
        python3 -m json.tool "data/$file" > /dev/null && echo "✅ $file valid" || echo "❌ $file invalid"
    fi
done
echo ""

# Phase 4: Summary
echo "==============================================="
echo "✅ Pre-release testing complete!"
echo ""
echo "Next steps:"
echo "1. Review TESTING.md for manual tests"
echo "2. Check RELEASE_CHECKLIST.md for go/no-go"
echo "3. Deploy with: python3 bot.py"
echo "==============================================="
```

Save as `full_test.sh` and run:
```bash
chmod +x full_test.sh
./full_test.sh
```

---

## Files in This Testing Suite

| File | Purpose | Time |
|------|---------|------|
| `validate_bot.py` | Automated pre-flight checks | 30s |
| `TESTING.md` | Complete test guide (14 phases) | 60-90m |
| `RELEASE_CHECKLIST.md` | Go/no-go verification | 20-30m |
| `README.md` | User documentation | - |
| `EXPANSION_SUMMARY.md` | Feature overview | - |
| `.github/copilot-instructions.md` | AI coding guide | - |

---

## Success Criteria ✅

Bot is ready to release when:

- [ ] `python3 validate_bot.py` shows all checks passing
- [ ] All 14 TESTING.md phases completed successfully
- [ ] All RELEASE_CHECKLIST.md items are checked
- [ ] Bot has been running for 24+ hours without errors
- [ ] All 48 commands respond correctly
- [ ] Data persists across restarts
- [ ] No sensitive data in git history

---

## Questions?

- **Setup issues?** → See README.md "Troubleshooting"
- **Command not working?** → See TESTING.md for that feature
- **Ready to release?** → See RELEASE_CHECKLIST.md
- **Want AI help?** → See `.github/copilot-instructions.md`

---

## Next Steps

1. ✅ Read this guide
2. ✅ Run `python3 validate_bot.py`
3. ✅ Follow TESTING.md phases
4. ✅ Check RELEASE_CHECKLIST.md
5. ✅ Deploy with confidence!

Good luck! 🚀
