@echo off
REM NotebookLM Windows Authentication Script
REM Run this on Windows (not WSL) to authenticate with Google

echo ========================================
echo NotebookLM Windows Authentication
echo ========================================
echo.

REM Get the directory of this script
set SCRIPT_DIR=%~dp0

REM Check if Python exists on Windows
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed on Windows
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python found on Windows
echo.

REM Setup environment
echo Step 1: Setting up environment...
python scripts\setup_environment.py
if errorlevel 1 (
    echo ERROR: Environment setup failed
    pause
    exit /b 1
)

echo.
echo Step 2: Starting authentication...
echo A browser window will open for Google login
echo.

REM Run authentication
python scripts\run.py auth_manager.py setup

if errorlevel 1 (
    echo.
    echo ERROR: Authentication failed
    pause
    exit /b 1
)

echo.
echo ========================================
echo Authentication Complete!
echo ========================================
echo.
echo Next step: Copy auth files to WSL
echo Run these commands in WSL:
echo.
echo mkdir -p ~/.claude/skills/notebooklm/data
echo cp -r data/* ~/.claude/skills/notebooklm/data/
echo.
echo Or manually copy from:
echo %SCRIPT_DIR%data
echo to WSL: ~/.claude/skills/notebooklm/data/
echo.
pause
