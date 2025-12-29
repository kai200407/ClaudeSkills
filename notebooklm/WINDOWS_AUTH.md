# Windows Authentication Guide for NotebookLM Skill

Use this guide to authenticate on Windows and use the credentials in WSL.

## Why Windows Authentication?

WSL network routing may not work well with Google services. Authenticating on Windows
and copying the credentials to WSL is more reliable.

## Step-by-Step Guide

### Step 1: Copy the Skill to Windows

Open PowerShell on Windows (not WSL) and run:

```powershell
# Create the directory if it doesn't exist
mkdir -p C:\Users\$env:USERNAME\.claude\skills\notebooklm

# Copy from WSL to Windows
wsl cp -r /root/.claude/skills/notebooklm C:\Users\$env:USERNAME\.claude\skills\
```

### Step 2: Run Windows Authentication

```powershell
cd C:\Users\$env:USERNAME\.claude\skills\notebooklm
.\windows_auth.bat
```

Or manually:

```powershell
python scripts\setup_environment.py
python scripts\run.py auth_manager.py setup
```

A browser will open - log in to your Google account.

### Step 3: Copy Auth Files to WSL

After successful authentication, in **WSL** run:

```bash
# Create directory
mkdir -p ~/.claude/skills/notebooklm/data

# Copy auth files from Windows
cp -r /mnt/c/Users/你的Windows用户名/.claude/skills/notebooklm/data/* ~/.claude/skills/notebooklm/data/
```

Replace `你的Windows用户名` with your actual Windows username.

### Step 4: Verify in WSL

```bash
cd ~/.claude/skills/notebooklm
python3 scripts/run.py auth_manager.py status
```

Should show: `Authenticated: Yes`

## Quick One-Liner (After Windows Auth)

```bash
cp -r /mnt/c/Users/$USER/.claude/skills/notebooklm/data/* ~/.claude/skills/notebooklm/data/
```

## Troubleshooting

**Python not found on Windows:**
- Install from https://www.python.org/downloads/
- Check "Add Python to PATH" during installation

**"Access denied" error:**
- Run PowerShell as Administrator
- Or copy files manually using File Explorer

**Browser doesn't open:**
- Check your firewall/antivirus settings
- Try running: `python scripts\run.py auth_manager.py setup --timeout 15`

## File Locations

| Platform | Skill Path |
|----------|------------|
| Windows | `C:\Users\YourName\.claude\skills\notebooklm` |
| WSL | `/root/.claude/skills/notebooklm` |

**Auth files location:**
- Windows: `C:\Users\YourName\.claude\skills\notebooklm\data\`
- WSL: `/root/.claude/skills/notebooklm/data/`
