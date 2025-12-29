#!/usr/bin/env python3
"""
Manual Cookie Authentication for NotebookLM
You copy cookies from browser, this script saves them in correct format
"""

import json
import sys
from pathlib import Path

def main():
    print("=" * 60)
    print("NotebookLM 手动 Cookie 认证")
    print("=" * 60)
    print()

    # Create data directory
    data_dir = Path("data/browser_state")
    data_dir.mkdir(parents=True, exist_ok=True)
    state_file = data_dir / "state.json"

    print("步骤 1: 获取 Cookies")
    print("-" * 60)
    print()
    print("请按以下步骤操作：")
    print()
    print("1. 在 Chrome 浏览器中打开: https://notebooklm.google.com")
    print("2. 登录你的 Google 账户")
    print("3. 按 F12 打开开发者工具")
    print("4. 切换到 'Application' 或 '应用' 标签页")
    print("5. 左侧找到 'Cookies' → 'https://notebooklm.google.com'")
    print("6. 复制以下 cookies 的值 (name 和 value):")
    print("   - SID 或 __Secure-1PSID")
    print("   - HSID 或 __Secure-1PSIDCC")
    print("   - SSID 或 __Secure-3PSID")
    print("   - APISID 或 __Secure-1PAPISID")
    print("   - SAPISID 或 __Secure-3PAPISID")
    print()
    input("按 Enter 继续...")
    print()

    # Get cookies from user
    cookies = []

    important_cookies = [
        ("SID", "SID"),
        ("HSID", "HSID"),
        ("SSID", "SSID"),
        ("APISID", "APISID"),
        ("SAPISID", "SAPISID"),
        ("__Secure-1PSID", "__Secure-1PSID"),
        ("__Secure-1PSIDCC", "__Secure-1PSIDCC"),
        ("__Secure-3PSID", "__Secure-3PSID"),
        ("__Secure-1PAPISID", "__Secure-1PAPISID"),
        ("__Secure-3PAPISID", "__Secure-3PAPISID"),
    ]

    print("步骤 2: 输入 Cookies (如果没有可以跳过，直接按 Enter)")
    print("-" * 60)

    for name, cookie_name in important_cookies:
        value = input(f"{cookie_name}: ").strip()
        if value:
            cookies.append({
                "name": cookie_name,
                "value": value,
                "domain": ".google.com",
                "path": "/",
                "expires": -1,
                "httpOnly": True,
                "secure": True,
                "sameSite": "None"
            })

    if not cookies:
        print("❌ 没有输入任何 cookies!")
        input("按 Enter 退出...")
        return 1

    # Save to state.json
    state = {
        "cookies": cookies,
        "origins": []
    }

    with open(state_file, 'w') as f:
        json.dump(state, f, indent=2)

    print()
    print("✅ Cookies 已保存到:", state_file)
    print()
    print("=" * 60)
    print("步骤 3: 复制到 WSL")
    print("=" * 60)
    print()
    print("在 WSL 中运行:")
    print()
    print("  cp -r /mnt/c/Users/lenovo/.claude/skills/notebooklm/data/* \\")
    print("      ~/.claude/skills/notebooklm/data/")
    print()
    print("然后验证:")
    print("  cd ~/.claude/skills/notebooklm")
    print("  python3 scripts/run.py auth_manager.py status")
    print()

    input("按 Enter 退出...")
    return 0

if __name__ == "__main__":
    sys.exit(main())
