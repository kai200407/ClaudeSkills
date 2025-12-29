#!/usr/bin/env python3
"""
Read cookies from existing Chrome installation
Handles encrypted cookies in newer Chrome versions
"""

import json
import sys
import os
import shutil
import sqlite3
import struct
from pathlib import Path
import tempfile

# Try to import Windows crypto
try:
    import win32crypt
    HAS_WIN32CRYPT = True
except ImportError:
    HAS_WIN32CRYPT = False

def get_chrome_cookie_path():
    """Find Chrome's cookie database"""
    base_path = Path(os.environ.get('LOCALAPPDATA', '')) / "Google" / "Chrome" / "User Data"

    # Try different profiles
    for profile in ["Default", "Profile 1", "Profile 2"]:
        # Newer Chrome path
        cookie_path = base_path / profile / "Network" / "Cookies"
        if cookie_path.exists():
            return cookie_path, base_path

        # Older Chrome path
        cookie_path = base_path / profile / "Cookies"
        if cookie_path.exists():
            return cookie_path, base_path

    # Fallback to Default
    return base_path / "Default" / "Network" / "Cookies", base_path

def copy_cookie_db(cookie_path):
    """Copy cookie database to temp (Chrome locks the original)"""
    temp_dir = Path(tempfile.gettempdir())
    temp_cookie = temp_dir / "chrome_cookies_copy.db"

    if cookie_path.exists():
        shutil.copy(cookie_path, temp_cookie)
        return temp_cookie
    return None

def decrypt_cookie(encrypted_value):
    """Decrypt Chrome cookie value on Windows"""
    if not encrypted_value:
        return ""

    # Check if it's encrypted (starts with 'v10' or 'v11')
    if encrypted_value[:3] in [b'v10', b'v11']:
        if not HAS_WIN32CRYPT:
            return None  # Need pywin32

        try:
            return win32crypt.CryptUnprotectData(encrypted_value, None, None, None, 0)[1].decode('utf-8')
        except Exception as e:
            return None

    # Not encrypted, return as-is
    if isinstance(encrypted_value, bytes):
        try:
            return encrypted_value.decode('utf-8')
        except:
            return ""
    return encrypted_value

def read_cookies(host="google.com"):
    """Read cookies from Chrome database"""
    global HAS_WIN32CRYPT

    cookie_path, base_path = get_chrome_cookie_path()

    print(f"Chrome 路径: {base_path}")
    print(f"Cookie 数据库: {cookie_path}")
    print()

    if not cookie_path.exists():
        print(f"❌ 找不到 Chrome cookie 数据库")
        return None

    # Check if we need pywin32
    if not HAS_WIN32CRYPT:
        print("⚠️ 需要安装 pywin32 来解密 cookies")
        print("   安装命令: pip install pywin32")
        print()
        response = input("是否现在安装? (y/n): ")
        if response.lower() == 'y':
            import subprocess
            subprocess.run([sys.executable, "-m", "pip", "install", "pywin32"], check=True)
            import win32crypt
            HAS_WIN32CRYPT = True
            print("✅ pywin32 已安装")
        else:
            return None

    # Copy to temp (Chrome locks the file)
    print("📋 复制 cookie 数据库...")
    temp_cookie = copy_cookie_db(cookie_path)
    if not temp_cookie:
        print("❌ 无法复制 cookie 数据库")
        return None

    try:
        conn = sqlite3.connect(temp_cookie)
        cursor = conn.cursor()

        # Get table structure
        cursor.execute("PRAGMA table_info(cookies)")
        columns = [row[1] for row in cursor.fetchall()]
        print(f"📊 Cookie 表结构: {columns}")

        # Check for encrypted_value column
        has_encrypted = 'encrypted_value' in columns
        has_value = 'value' in columns

        print(f"🔒 加密 cookies: {'是' if has_encrypted else '否'}")

        # Build query based on available columns
        if has_encrypted:
            query = """
                SELECT name, encrypted_value, host_key, path, expires_utc, is_secure, is_httponly
                FROM cookies
            """
        else:
            query = """
                SELECT name, value, host_key, path, expires_utc, is_secure, is_httponly
                FROM cookies
            """

        cursor.execute(query)
        rows = cursor.fetchall()

        cookies = []
        important_names = ['SID', 'HSID', 'SSID', 'APISID', 'SAPISID',
                          '__Secure-1PSID', '__Secure-1PSIDCC', '__Secure-3PSID',
                          '__Secure-1PAPISID', '__Secure-3PAPISID']

        decrypted_count = 0
        failed_count = 0

        for row in rows:
            name, value, host, path, expires, secure, httponly = row

            # Skip if not google domain
            if not host or (host not in f".{host}" and not host.endswith(host)):
                continue

            # Decrypt if needed
            if has_encrypted:
                decrypted = decrypt_cookie(value)
                if decrypted is None:
                    failed_count += 1
                    continue
                value = decrypted
                decrypted_count += 1

            if not value:
                continue

            cookie = {
                "name": name,
                "value": value,
                "domain": host,
                "path": path,
                "expires": expires if expires > 0 else -1,
                "httpOnly": bool(httponly),
                "secure": bool(secure),
                "sameSite": "None"
            }

            # Only include important cookies
            if name in important_names:
                cookies.append(cookie)

        print(f"✅ 成功解密 {decrypted_count} 个 cookies")
        if failed_count > 0:
            print(f"⚠️ {failed_count} 个 cookies 解密失败")
        print(f"📦 找到 {len(cookies)} 个重要的 Google cookies")

        conn.close()
        return cookies

    except Exception as e:
        print(f"❌ 读取 cookies 失败: {e}")
        import traceback
        traceback.print_exc()
        return None
    finally:
        # Clean up temp file
        if temp_cookie and temp_cookie.exists():
            temp_cookie.unlink()

def main():
    print("=" * 60)
    print("从 Chrome 读取 NotebookLM Cookies")
    print("=" * 60)
    print()

    print("⚠️ 前置条件:")
    print("1. 请确保 Chrome 已关闭 (运行: taskkill /F /IM chrome.exe)")
    print("2. 或者在 Chrome 中已经登录了 Google 账户")
    print()
    input("按 Enter 继续...")
    print()

    # Read cookies
    cookies = read_cookies("google.com")

    if not cookies:
        print("❌ 无法读取 cookies")
        input("按 Enter 退出...")
        return 1

    print()
    print("找到的 Cookies:")
    for c in cookies:
        print(f"  - {c['name']}: {c['value'][:20]}...")
    print()

    if len(cookies) == 0:
        print("❌ 没有找到 Google 认证 cookies")
        print("   请确保:")
        print("   1. Chrome 已完全关闭")
        print("   2. 你已经在 Chrome 中登录了 Google")
        input("按 Enter 退出...")
        return 1

    # Create state.json
    data_dir = Path("data/browser_state")
    data_dir.mkdir(parents=True, exist_ok=True)
    state_file = data_dir / "state.json"

    state = {
        "cookies": cookies,
        "origins": []
    }

    with open(state_file, 'w') as f:
        json.dump(state, f, indent=2)

    print(f"✅ Cookies 已保存到: {state_file}")
    print()
    print("=" * 60)
    print("下一步: 复制到 WSL")
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
