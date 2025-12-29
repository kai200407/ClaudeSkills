---
name: technical-writing
description: Create technical documentation, API docs, README files, and code tutorials
---

# Technical Writing Skill

Create clear, accurate technical documentation that developers actually want to read.

## Core Principles

1. **Write for the user** - What do they need to know right now?
2. **Be specific** - Concrete examples, real commands, actual output
3. **Stay current** - Document what exists, not what should exist
4. **Show, then explain** - Code first, explanation second
5. **Keep it scannable** - Short sections, clear hierarchy
6. **Include examples** - Every concept needs an example

## Document Types

### README.md

```markdown
# Project Name

Short description (what it does, why it exists)

## Quick Start
\`\`\`bash
# Install
npm install

# Run
npm start
\`\`\`

## Features
- Feature 1
- Feature 2

## Usage
Basic example with code

## API
If applicable

## Contributing
How to contribute

## License
License type
```

### API Documentation

```
Structure:
1. Overview
2. Authentication
3. Endpoints (grouped by resource)
4. Request/Response examples
5. Error codes
6. Rate limits
```

### Tutorial/How-To Guide

```
Structure:
1. Prerequisites (what user needs before starting)
2. Objective (what we'll build)
3. Step-by-step instructions
4. Code examples with actual output
5. Troubleshooting common issues
```

## Code Documentation Style

### Function Documentation

\```javascript
/**
 * Calculates the Fibonacci number at index n
 * @param {number} n - The index to calculate
 * @returns {number} The Fibonacci number at index n
 * @example
 * fibonacci(7) // returns 13
 */
function fibonacci(n) {
  // implementation
}
\`\`\`

### Inline Comments

```javascript
// ❌ Bad: obvious comment
// Increment i by 1
i++;

// ✅ Good: explains why
// Use +1 to skip the header row (index 0)
i++;
```

## Best Practices

### Headings
- Use ATX style (# for h1, ## for h2)
- Start with h2 (# Title is h1)
- Descriptive and specific
- Parallel structure (same level of granularity)

### Code Blocks
- Always specify language
- Show expected output when helpful
- Keep examples short but complete
- Use real data, not foo/bar

### Links
- Descriptive link text
- Check that links work
- Prefer relative links for internal docs

### Diagrams
- Use ASCII art when simple
- Use Mermaid for complex flows
- Include a text description

## Common Sections

### Prerequisites
What users need before starting:
- Software versions
- Required accounts
- System requirements
- Knowledge assumptions

### Installation
Step-by-step setup:
1. Command to run
2. Expected output
3. How to verify it worked

### Troubleshooting
Common issues and solutions:
- Error message
- Possible causes
- How to fix

### Examples
Real-world usage:
- Complete example
- Expected output
- Explanation

## Tone Guidelines

- **Objective** - Facts over opinions
- **Clear** - No ambiguity
- **Concise** - Get to the point
- **Friendly** - But not casual

## Anti-Patterns to Avoid

- ### Outdated docs
  Docs that don't match current code

- ### Vague instructions
  "Configure the server appropriately"

- ### Missing context
  Code without explanation of what it does

- ### Assumptions
  Assuming reader knows things they might not

## Quality Checklist

- [ ] All code examples are tested and accurate
- [ ] Links work and go to the right place
- [ ] Diagrams have text descriptions
- [ ] Prerequisites are clearly stated
- [ ] Troubleshooting section exists
- [ ] Examples show expected output
- [ ] API changes are documented
- [ ] Version number is included

## Commands

- `/tech-doc readme` - Generate README.md
- `/tech-doc api` - Document API endpoints
- `/tech-doc tutorial` - Create tutorial
- `/tech-doc comment` - Add code comments

## Notes

- Always document from user perspective
- Update docs when code changes
- Delete outdated docs immediately
- Use version control for docs
