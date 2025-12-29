# NotebookLM 手动认证指南

当自动认证失败时，可以使用这个手动方法。

## 方法：使用浏览器开发者工具导出 Cookies

### 步骤 1：登录 NotebookLM

1. 在 Chrome 浏览器中打开 https://notebooklm.google.com
2. 登录你的 Google 账户
3. 确保能看到 NotebookLM 主页

### 步骤 2：导出 Cookies

#### 方法 A：使用 Chrome 扩展（最简单）

1. 安装 "EditThisCookie" 扩展
2. 点击扩展图标
3. 点击 "导出" → "JSON"
4. 复制内容保存到文件

#### 方法 B：使用开发者工具

1. 按 F12 打开开发者工具
2. 切换到 "Application" 或 "应用" 标签
3. 左侧找到 "Cookies" → "https://notebooklm.google.com"
4. 手动复制需要的 cookies（SID, HSID, SSID, APISID, SAPISID 等）

### 步骤 3：创建认证文件

在 PowerShell 中运行：

```powershell
# 创建目录
mkdir C:\Users\lenovo\.claude\skills\notebooklm\data\browser_state -Force

# 创建 state.json 文件（使用你导出的 cookies）
# 注意：需要将导出的 cookies 转换为正确的 JSON 格式
```

### 步骤 4：复制到 WSL

```bash
cp -r /mnt/c/Users/lenovo/.claude/skills/notebooklm/data/* ~/.claude/skills/notebooklm/data/
```

---

## 替代方案：修复 Python 脚本

如果上面的手动方法太复杂，可以尝试：

1. 使用 Python 3.11 或 3.12（而不是 3.13）
2. 或者使用现有的 Google 认证工具

你想用哪种方法？
