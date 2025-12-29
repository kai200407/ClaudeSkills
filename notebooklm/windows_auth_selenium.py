#!/usr/bin/env python3
"""
Windows Authentication using Selenium
Alternative to patchright for better Python 3.13 compatibility
"""

import subprocess
import sys
import json
import time
from pathlib import Path

def main():
    print("=" * 50)
    print("NotebookLM Windows Authentication (Selenium)")
    print("=" * 50)
    print()

    # Step 1: Install selenium
    print("Step 1: Installing Selenium...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "selenium"], check=True)
        print("✅ Selenium installed")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed: {e}")
        input("Press Enter to exit...")
        return 1

    # Step 2: Check Chrome
    print()
    print("Step 2: Checking Chrome...")
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        print("✅ Chrome ready")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        input("Press Enter to exit...")
        return 1

    # Step 3: Manual authentication
    print()
    print("Step 3: Starting authentication...")
    print()
    print("==============================================")
    print("INSTRUCTIONS:")
    print("1. A Chrome window will open")
    print("2. Log in to your Google account")
    print("3. Once you see NotebookLM, come back here")
    print("4. Press Enter to save the session")
    print("==============================================")
    print()
    input("Press Enter to open browser...")

    # Create data directory
    data_dir = Path("data/browser_state")
    data_dir.mkdir(parents=True, exist_ok=True)

    # Launch Chrome with user data dir
    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={data_dir.absolute()}/browser_profile")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")
    # chrome_options.add_argument("--headless=new")  # Comment out to see browser

    try:
        print("Opening Chrome...")
        driver = webdriver.Chrome(options=chrome_options)

        # Navigate to NotebookLM
        print("Navigating to NotebookLM...")
        driver.get("https://notebooklm.google.com")

        print()
        print("==============================================")
        print("BROWSER IS OPEN")
        print("Please log in to Google if needed")
        print("Wait until you see the NotebookLM homepage")
        print()
        input("Press Enter when you see NotebookLM homepage...")

        # Get cookies
        print("Saving cookies...")
        cookies = driver.get_cookies()

        # Save to state.json
        state_file = data_dir / "state.json"
        with open(state_file, 'w') as f:
            json.dump({"cookies": cookies, "origins": []}, f, indent=2)

        print(f"✅ Saved to: {state_file}")

        # Close browser
        driver.quit()

        print()
        print("=" * 50)
        print("✅ Authentication Complete!")
        print("=" * 50)
        print()
        print("Next: Copy to WSL")
        print("Run in WSL:")
        print("  cp -r /mnt/c/Users/lenovo/.claude/skills/notebooklm/data/* ~/.claude/skills/notebooklm/data/")
        print()

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

    input("Press Enter to exit...")
    return 0

if __name__ == "__main__":
    sys.exit(main())
