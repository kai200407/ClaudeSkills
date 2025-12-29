#!/usr/bin/env python3
"""
Simple Windows Authentication for NotebookLM
Run directly on Windows without venv
"""

import subprocess
import sys

def main():
    print("=" * 50)
    print("NotebookLM Windows Authentication")
    print("=" * 50)
    print()

    # Step 1: Install dependencies
    print("Step 1: Installing dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "patchright==1.55.2", "python-dotenv==1.0.0"], check=True)
        print("✅ Dependencies installed")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        input("Press Enter to exit...")
        return 1

    # Step 2: Install Chrome
    print()
    print("Step 2: Installing Chrome for Patchright...")
    try:
        subprocess.run([sys.executable, "-m", "patchright", "install", "chrome"], check=True)
        print("✅ Chrome installed")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Chrome install warning: {e}")
        print("   Continuing anyway...")

    # Step 3: Run authentication
    print()
    print("Step 3: Starting authentication...")
    print("⚠️ IMPORTANT: Close ALL Chrome windows before continuing!")
    print("A browser window will open - log in to your Google account")
    print()

    input("Press Enter after closing all Chrome windows...")

    # Use direct import to avoid subprocess issues
    print("Launching browser...")
    import os
    os.environ["HEADLESS"] = "false"

    try:
        # Import and run auth directly
        sys.path.insert(0, "scripts")
        from auth_manager import AuthManager

        auth = AuthManager()
        success = auth.setup_auth(headless=False, timeout_minutes=10)

        if success:
            print()
            print("=" * 50)
            print("✅ Authentication Complete!")
            print("=" * 50)
            print()
            print("Next: Copy auth files to WSL")
            print("Run in WSL:")
            print("  cp -r /mnt/c/Users/lenovo/.claude/skills/notebooklm/data/* ~/.claude/skills/notebooklm/data/")
            print()
        else:
            print()
            print("❌ Authentication failed")
    except Exception as e:
        print(f"❌ Error: {e}")

    input("Press Enter to exit...")
    return 0

if __name__ == "__main__":
    sys.exit(main())
