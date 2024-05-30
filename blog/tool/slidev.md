---
title: ppt slidev
date: 2024-05-30T22:17:51+08:00
tags: [ tool ]
---

## intro

```shell
# install
npm i -g @slidev/cli

# open
slidev test.md
# http://localhost:3030/
```

## cli

- dev: "slidev example.md",
- build: "slidev build example.md",
- export: "slidev export example.md",
- screenshot: "slidev export example.md --format png"

## demo file

```markdown
---
theme: default
---

# Slidev

Hello World

---

# Page 2

Directly use code blocks for highlighting

```ts
console.log('Hello, World!')
```

---

# Page 3

```
