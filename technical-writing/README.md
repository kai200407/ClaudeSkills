# Technical Writing / 技术写作

[English](#english) | [中文](#中文)

---

## English

Create clear, accurate technical documentation that developers actually want to read.

### What It Does

Creates user-focused technical documentation including README files, API docs, tutorials, and code comments.

### Document Types

**README.md**
- Project description
- Quick start guide
- Features list
- Usage examples
- Contributing guidelines

**API Documentation**
- Overview
- Authentication
- Endpoints (grouped by resource)
- Request/Response examples
- Error codes

**Tutorial/How-To**
- Prerequisites
- Objective
- Step-by-step instructions
- Code examples with output
- Troubleshooting

### How to Use

```
/tech-doc readme
[Describe your project]
```

```
/tech-doc api
[Describe your endpoints]
```

```
/tech-doc tutorial
[What will users learn?]
```

### Best Practices

- Write for the user (not yourself)
- Be specific with real examples
- Show code, then explain
- Keep it scannable
- Include expected output
- Add troubleshooting sections

### Example

```
You: /tech-doc readme

I have a Node.js CLI tool that manages environment variables.
Features: encrypt/decrypt, git-safe, team sharing.

Claude: [Generates complete README with:
        - Clear project description
        - Installation instructions
        - Usage examples
        - Command reference
        - Contributing section]
```

---

## 中文

创建清晰、准确的技术文档，让开发者愿意阅读。

### 功能说明

创建以用户为中心的技术文档，包括 README 文件、API 文档、教程和代码注释。

### 文档类型

**README.md**
- 项目描述
- 快速入门指南
- 功能列表
- 使用示例
- 贡献指南

**API 文档**
- 概述
- 身份验证
- 端点（按资源分组）
- 请求/响应示例
- 错误代码

**教程/操作指南**
- 前提条件
- 目标
- 分步说明
- 带输出的代码示例
- 故障排除

### 使用方法

```
/tech-doc readme
[描述你的项目]
```

```
/tech-doc api
[描述你的端点]
```

```
/tech-doc tutorial
[用户将学到什么？]
```

### 最佳实践

- 为用户写作（而不是自己）
- 用真实示例具体说明
- 先展示代码，再解释
- 保持可扫描性
- 包含预期输出
- 添加故障排除部分

### 示例

```
你: /tech-doc readme

我有一个管理环境变量的 Node.js CLI 工具。
功能：加密/解密、git 安全、团队共享。

Claude: [生成完整的 README，包含：
        - 清晰的项目描述
        - 安装说明
        - 使用示例
        - 命令参考
        - 贡献部分]
```
