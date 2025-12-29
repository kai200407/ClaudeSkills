# Claude Skills / Claude 技能集合

A collection of custom skills for Claude Code to enhance your writing and productivity. / 一套为 Claude Code 打造的自定义技能集合，提升写作效率与生产力。

## 📦 Skills / 技能列表

| Skill / 技能 | Description / 描述 | Language / 语言 |
|-------------|-------------------|----------------|
| [Analytical Blog Writing](#analytical-blog-writing) | Write data-driven analytical articles / 撰写数据驱动的深度分析文章 | EN/CN |
| [Blog Writer](#blog-writer) | Write human-like blog posts / 撰写自然流畅的博客文章 | EN/CN |
| [Content Research Writer](#content-research-writer) | Collaborative writing partner / 协作式写作助手 | EN/CN |
| [Copywriter](#copywriter) | Marketing and sales copy / 营销文案与销售页面 | EN/CN |
| [Markdown Blog](#markdown-blog) | Markdown posts with frontmatter / 带 Frontmatter 的 Markdown 博客 | EN/CN |
| [NotebookLM](#notebooklm) | Query your notebooks / 查询 NotebookLM 笔记 | EN/CN |
| [Social Media Writer](#social-media-writer) | Social media content / 社交媒体内容创作 | EN/CN |
| [Technical Writing](#technical-writing) | Technical documentation / 技术文档编写 | EN/CN |

---

## 📚 Detailed Skills / 详细技能说明

### Analytical Blog Writing / 深度分析写作

Write in-depth analytical articles with data, research, and professional insights.

/ 撰写包含数据、研究和专业见解的深度分析文章。

**Features / 特性:**
- Data-driven content / 数据驱动内容
- Research methodology / 研究方法论
- Source citations / 来源引用
- Clear structure / 清晰结构

**Usage / 使用:**
```
/analytical [topic]     # Write analytical article / 撰写分析文章
/analyze-data [dataset]  # Analyze data / 分析数据
/case-study [project]   # Write case study / 撰写案例研究
```

**Link / 链接:** [Read more / 阅读更多](analytical-blog-writing/README.md)

---

### Blog Writer / 博客作者

Write human-like blog posts without AI-generated patterns.

/ 撰写自然流畅、避免 AI 写作痕迹的博客文章。

**Features / 特性:**
- Natural voice / 自然语调
- SEO optimized / SEO 优化
- Banned AI words / 禁用 AI 惯用词
- Personal style / 个人风格

**Usage / 使用:**
```
/blog "topic"     # Write blog post / 撰写博客
/tweet "content"  # Convert to tweet / 转推文
/linkedin "article"  # Create LinkedIn post / 创建 LinkedIn 帖子
```

**Link / 链接:** [Read more / 阅读更多](blog-writer/README.md)

---

### Content Research Writer / 内容研究写作助手

Collaborative writing partner for research, outlines, and real-time feedback.

/ 用于研究、大纲和实时反馈的协作式写作伙伴。

**Features / 特性:**
- Research assistance / 研究辅助
- Citation management / 引用管理
- Hook improvement / 开头优化
- Section feedback / 逐段反馈

**Usage / 使用:**
```
Help me create an outline for [topic]
Research [specific topic] and add citations
Review this section and give feedback
```

**Link / 链接:** [Read more / 阅读更多](content-research-writer/README.md)

---

### Copywriter / 文案策划

Write compelling copy for products, marketing, UX, and sales pages.

/ 撰写产品、营销、用户体验和销售页面的吸引人文案。

**Features / 特性:**
- Conversion-focused / 转化导向
- AIDA & PAS frameworks / AIDA 和 PAS 框架
- CTA optimization / CTA 优化
- UX microcopy / UX 微文案

**Usage / 使用:**
```
/copywriter product   # Product description / 产品描述
/copywriter ux        # UX writing / UX 文案
/copywriter sales-page  # Sales page / 销售页面
/copywriter email     # Email sequence / 邮件序列
```

**Link / 链接:** [Read more / 阅读更多](copywriter/README.md)

---

### Markdown Blog / Markdown 博客

Write blog posts in Markdown with Jekyll/Hugo frontmatter.

/ 撰写带有 Jekyll/Hugo Frontmatter 的 Markdown 博客文章。

**Features / 特性:**
- Pure Markdown / 纯 Markdown
- Frontmatter support / Frontmatter 支持
- SEO friendly / SEO 友好
- Multi-platform / 多平台支持

**Supported Platforms / 支持平台:**
- Jekyll
- Hugo
- Hexo

**Usage / 使用:**
```
/md-blog post    # Create new post / 创建新文章
/md-blog draft   # Create draft / 创建草稿
/md-blog publish # Mark published / 标记已发布
```

**Link / 链接:** [Read more / 阅读更多](markdown-blog/README.md)

---

### NotebookLM / NotebookLM 集成

Query your Google NotebookLM notebooks directly from Claude Code.

/ 直接从 Claude Code 查询你的 Google NotebookLM 笔记。

**Features / 特性:**
- Source-grounded answers / 基于来源的回答
- Citation-backed / 引用支持
- Browser automation / 浏览器自动化
- Reduced hallucinations / 减少幻觉

**Usage / 使用:**
```bash
python scripts/run.py auth_manager.py setup           # First time setup / 首次设置
python scripts/run.py notebook_manager.py list        # List notebooks / 列出笔记
python scripts/run.py ask_question.py --question "..."  # Ask question / 提问
```

**Link / 链接:** [Read more / 阅读更多](notebooklm/README.md)

---

### Social Media Writer / 社交媒体写作

Write engaging posts for Twitter/X, LinkedIn, and other platforms.

/ 为 Twitter/X、LinkedIn 等平台撰写吸引人的帖子。

**Features / 特性:**
- Platform-specific / 平台专属
- Thread format / 推文串格式
- Hashtag strategy / 话题标签策略
- Engagement hooks / 吸引钩子

**Supported Platforms / 支持平台:**
- Twitter/X
- LinkedIn
- Instagram
- Facebook
- Threads
- Bluesky

**Usage / 使用:**
```
/tweet [content]    # Create tweet / 创建推文
/thread [article]   # Create thread / 创建推文串
/linkedin [post]    # Create LinkedIn post / 创建 LinkedIn 帖子
```

**Link / 链接:** [Read more / 阅读更多](social-media-writer/README.md)

---

### Technical Writing / 技术写作

Create technical documentation, API docs, README files, and tutorials.

/ 创建技术文档、API 文档、README 文件和教程。

**Features / 特性:**
- User-focused / 以用户为中心
- Code examples / 代码示例
- Clear structure / 清晰结构
- Troubleshooting / 故障排除

**Usage / 使用:**
```
/tech-doc readme   # Generate README / 生成 README
/tech-doc api      # Document API / 文档化 API
/tech-doc tutorial # Create tutorial / 创建教程
/tech-doc comment  # Add comments / 添加注释
```

**Link / 链接:** [Read more / 阅读更多](technical-writing/README.md)

---

## 🚀 Installation / 安装

### Clone the repository / 克隆仓库

```bash
# Clone to your Claude skills directory / 克隆到 Claude skills 目录
git clone https://github.com/kai200407/ClaudeSkills ~/.claude/skills
```

### Or use symlink (recommended for sync)/ 或使用软链接（推荐用于同步）

```bash
# Clone to a separate location first / 先克隆到单独位置
git clone https://github.com/kai200407/ClaudeSkills ~/claude-skills

# Create symlink / 创建软链接
ln -s ~/claude-skills ~/.claude/skills
```

---

## 🔄 Updates / 更新

```bash
cd ~/.claude/skills
git pull
```

---

## 📝 Contributing / 贡献

Contributions are welcome! Please feel free to submit a Pull Request.

/ 欢迎贡献！请随时提交 Pull Request。

---

## 📄 License / 许可证

MIT License

---

## 🙏 Acknowledgments / 致谢

Built for use with [Claude Code](https://claude.com/claude-code).

/ 为配合 [Claude Code](https://claude.com/claude-code) 使用而构建。
