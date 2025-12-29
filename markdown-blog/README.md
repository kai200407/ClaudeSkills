# Markdown Blog / Markdown 博客

[English](#english) | [中文](#中文)

---

## English

Write blog posts in Markdown format with Jekyll/Hugo frontmatter for static site generators.

### What It Does

Creates properly formatted Markdown blog posts ready for static site generators like Jekyll, Hugo, or Hexo.

### Supported Platforms

- **Jekyll** - GitHub Pages default
- **Hugo** - Fast static site generator
- **Hexo** - Node.js based SSG

### Post Structure

```markdown
---
title: "Your Post Title"
date: 2025-12-29
description: "Post description for SEO"
tags: [tag1, tag2]
category: Development
draft: false
slug: your-post-url
---

# Title

Opening hook.

## Subheading

Content with **bold**, *italic*, and `code`.

## Code Block

\`\`\`javascript
function example() {
  return "Hello";
}
\`\`\`
```

### How to Use

```
/md-blog post
Write a tutorial about setting up Redis caching in Node.js
```

```
/md-blog draft
Create a draft about my thoughts on WebAssembly
```

### Features

- Pure Markdown (version controlled)
- SEO-friendly URLs
- Image optimization guidelines
- Code highlighting
- Cross-references

### Example

```
You: /md-blog post

Write a blog post about migrating from Jest to Vitest.

Claude: [Generates complete Markdown post with:
        - Proper frontmatter
        - Code examples
        - SEO description
        - Tags and categories]
```

---

## 中文

撰写带有 Jekyll/Hugo Frontmatter 的 Markdown 格式博客文章。

### 功能说明

创建格式正确的 Markdown 博客文章，可直接用于 Jekyll、Hugo 或 Hexo 等静态站点生成器。

### 支持平台

- **Jekyll** - GitHub Pages 默认
- **Hugo** - 快速静态站点生成器
- **Hexo** - 基于 Node.js 的 SSG

### 文章结构

```markdown
---
title: "你的文章标题"
date: 2025-12-29
description: "SEO 描述"
tags: [标签1, 标签2]
category: 开发
draft: false
slug: your-post-url
---

# 标题

吸引人的开头。

## 小标题

包含**粗体**、*斜体*和`代码`的内容。

## 代码块

\`\`\`javascript
function example() {
  return "你好";
}
\`\`\`
```

### 使用方法

```
/md-blog post
写一篇关于在 Node.js 中设置 Redis 缓存的教程
```

```
/md-blog draft
创建一篇关于我对 WebAssembly 看法的草稿
```

### 功能特性

- 纯 Markdown（版本控制）
- SEO 友好 URL
- 图片优化指南
- 代码高亮
- 交叉引用

### 示例

```
你: /md-blog post

写一篇关于从 Jest 迁移到 Vitest 的博客文章。

Claude: [生成完整的 Markdown 文章，包含：
        - 正确的 frontmatter
        - 代码示例
        - SEO 描述
        - 标签和分类]
```
