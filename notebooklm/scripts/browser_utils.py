"""
Browser Utilities for NotebookLM Skill
Handles browser launching, stealth features, and common interactions
"""

import json
import time
import random
import os
from typing import Optional, List

from patchright.sync_api import Playwright, BrowserContext, Page
from config import BROWSER_PROFILE_DIR, STATE_FILE, BROWSER_ARGS, USER_AGENT


def get_proxy_config():
    """Get proxy configuration from environment"""
    https_proxy = os.environ.get('https_proxy') or os.environ.get('HTTPS_PROXY') or os.environ.get('all_proxy') or os.environ.get('ALL_PROXY')
    if https_proxy:
        return {"server": https_proxy}
    return None


class BrowserFactory:
    """Factory for creating configured browser contexts"""

    @staticmethod
    def launch_persistent_context(
        playwright: Playwright,
        headless: bool = True,
        user_data_dir: str = str(BROWSER_PROFILE_DIR)
    ) -> BrowserContext:
        """
        Launch a browser context with anti-detection features
        Uses launch+new_context for better WSL2 compatibility
        """
        # Launch browser
        browser = playwright.chromium.launch(
            headless=headless,
            args=BROWSER_ARGS
        )

        # Get proxy configuration
        proxy_config = get_proxy_config()

        # Create context with user agent and proxy
        context = browser.new_context(
            user_agent=USER_AGENT,
            viewport=None,
            ignore_https_errors=True,
            proxy=proxy_config
        )

        # Store browser for cleanup
        context._browser = browser

        # Cookie Workaround for Playwright bug #36139
        # Session cookies (expires=-1) don't persist in user_data_dir automatically
        BrowserFactory._inject_cookies(context)

        return context

    @staticmethod
    def _inject_cookies(context: BrowserContext):
        """Inject cookies from state.json if available"""
        if STATE_FILE.exists():
            try:
                with open(STATE_FILE, 'r') as f:
                    state = json.load(f)
                    if 'cookies' in state and len(state['cookies']) > 0:
                        context.add_cookies(state['cookies'])
                        # print(f"  🔧 Injected {len(state['cookies'])} cookies from state.json")
            except Exception as e:
                print(f"  ⚠️  Could not load state.json: {e}")


class StealthUtils:
    """Human-like interaction utilities"""

    @staticmethod
    def random_delay(min_ms: int = 100, max_ms: int = 500):
        """Add random delay"""
        time.sleep(random.uniform(min_ms / 1000, max_ms / 1000))

    @staticmethod
    def human_type(page: Page, selector: str, text: str, wpm_min: int = 320, wpm_max: int = 480):
        """Type with human-like speed"""
        element = page.query_selector(selector)
        if not element:
            # Try waiting if not immediately found
            try:
                element = page.wait_for_selector(selector, timeout=2000)
            except:
                pass
        
        if not element:
            print(f"⚠️ Element not found for typing: {selector}")
            return

        # Click to focus
        element.click()
        
        # Type
        for char in text:
            element.type(char, delay=random.uniform(25, 75))
            if random.random() < 0.05:
                time.sleep(random.uniform(0.15, 0.4))

    @staticmethod
    def realistic_click(page: Page, selector: str):
        """Click with realistic movement"""
        element = page.query_selector(selector)
        if not element:
            return

        # Optional: Move mouse to element (simplified)
        box = element.bounding_box()
        if box:
            x = box['x'] + box['width'] / 2
            y = box['y'] + box['height'] / 2
            page.mouse.move(x, y, steps=5)

        StealthUtils.random_delay(100, 300)
        element.click()
        StealthUtils.random_delay(100, 300)
