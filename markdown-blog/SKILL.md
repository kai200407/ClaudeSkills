---
name: markdown-blog
description: Write blog posts in Markdown format with Jekyll/Hugo frontmatter for static site generators
---

# Markdown Blog Writing Skill

Create blog posts in Markdown format, ready for static site generators like Jekyll, Hugo, or Hexo.

## Core Principles

1. **Pure Markdown** - No WYSIWYG, version-controlled
2. **Frontmatter first** - Metadata at the top
3. **SEO-friendly URLs** - Clean, descriptive slugs
4. **Image optimization** - Alt text, proper paths
5. **Code highlighting** - Language specification
6. **Cross-references** - Internal links work

## Post Structure

### Complete Format

```markdown
---
title: "Your Post Title"
date: 2025-12-26
description: "Post description for SEO (150-160 chars)"
tags: [tag1, tag2, tag3]
category: Development
draft: false
slug: your-post-url
author: Your Name
---

# Title

Opening hook that grabs attention.

## Subheading

Content with **bold**, *italic*, and `code`.

## Code Block

\`\`\`javascript
function example() {
  return "Hello, World!";
}
\`\`\`

## Lists

- Item 1
- Item 2
  - Nested item

## Links

[Link text](https://example.com "Title")

## Images

![Alt text](/images/image.jpg "Caption")

## Conclusion

Summary and CTA.

---

*Last updated: 2025-12-26*
```

## Frontmatter Fields

### Required
- `title` - Post title
- `date` - Publication date
- `description` - SEO description

### Optional (Recommended)
- `tags` - Array of tags
- `category` - Main category
- `slug` - URL slug (auto-generated if omitted)
- `author` - Author name
- `draft` - true/false (default: false)
- `featured` - true/false (for featured posts)

### Platform-Specific

**Jekyll:**
```yaml
---
layout: post
title: "Title"
date: 2025-12-26
categories: [category]
tags: [tag1, tag2]
---
```

**Hugo:**
```yaml
---
title: "Title"
date: 2025-12-26
draft: false
tags: [tag1, tag2]
categories: [category]
---
```

## Markdown Best Practices

### Headings
- Use # for title (in frontmatter)
- Start with ## for first heading
- Only one h1 per document
- Don't skip levels (## then ####)

### Emphasis
- **Bold** for emphasis
- *Italic* for titles, foreign words
- `Code` for technical terms, commands
- ~~Strikethrough~~ for deletions (rare)

### Links
```markdown
[Link text](URL "Title")

[Reference link][ref]

[ref]: https://example.com
```

### Code Blocks
```markdown
\`\`\`language
code here
\`\`\`

\`\`\`
code with no syntax highlighting
\`\`\`
```

### Blockquotes
```markdown
> Regular blockquote

> **Multi-line**
> Blockquote
> across multiple lines
```

### Tables
```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

## Image Guidelines

### Path Conventions
```
/images/post-name/image.jpg
../images/image.jpg  # Relative
https://cdn.example.com/image.jpg  # Absolute
```

### Alt Text
- Always descriptive
- Include context if helpful
- Empty alt="" for decorative images

### Figure with Caption
```markdown
![Alt text](image.jpg)

*Figure 1: Caption text*
```

## SEO for Markdown Blogs

### URL Structure
- Use lowercase, hyphens
- No special characters
- Descriptive but concise
```
your-post-slug.md
```

### Meta Information
```yaml
---
title: "Clear, Descriptive Title"
description: "150-160 character description"
tags: [specific, relevant, tags]
---
```

### Heading Keywords
- Include keyword in first heading (##)
- Don't force it if unnatural
- Use variations throughout

## Content Organization

### Short Posts (<500 words)
- Title
- 2-3 sections
- Brief conclusion

### Medium Posts (500-1500 words)
- Title
- 4-6 sections
- Examples/images
- Conclusion

### Long Posts (>1500 words)
- Title
- Table of contents
- 8+ sections
- Multiple examples
- Summary/conclusion

## Common Issues

### Images Not Loading
- Check path (relative vs absolute)
- Verify image exists
- Check build configuration

### Code Not Highlighting
- Specify language after opening \`\`\`
- Check syntax highlighter config
- Test with common languages

### Frontmatter Errors
- Validate YAML syntax
- Check for proper indentation
- Use quotes for strings with special chars

## Quality Checklist

- [ ] Frontmatter is valid YAML
- [ ] Slug is URL-friendly
- [ ] Description is 150-160 chars
- [ ] Images have alt text
- [ ] Code blocks have language
- [ ] Internal links work
- [ ] External links open in new tab
- [ ] Post renders correctly
- [ ] Mobile formatting looks good

## Commands

- `/md-blog post` - Create new blog post
- `/md-blog draft` - Create draft
- `/md-blog publish` - Mark as published
- `/md-blog update` - Update existing post

## Platform-Specific Tips

### Jekyll
- Posts go in `_posts/`
- Filename: `YYYY-MM-DD-title.md`
- Use `layout: post` in frontmatter

### Hugo
- Posts go in `content/posts/`
- Filename: `YYYY-MM-DD-title.md` or `title/index.md`
- Frontmatter in TOML, YAML, or JSON

### Hexo
- Posts go in `source/_posts/`
- Filename: `YYYY-MM-DD-title.md`
- Auto-generated excerpt available

## Notes

- Write in Markdown, not HTML when possible
- Test rendering locally before publishing
- Use linter (markdownlint) to catch errors
- Keep posts under 2000 words for better engagement
