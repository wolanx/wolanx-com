---
title: atom
date: 2018-04-04 16:26:02
tags:
  - 工具
---

# theme color

- atom-material-syntax
- material-ui

- atom必备插件及主题 https://www.jianshu.com/p/eac1879cb2e9

# beautify

config.cson

```cson
"*":
  "atom-beautify":
    bash: {}
    php: {}
    nginx:
      indent_size: 4
      brace_style: "expand"
```

# keymap.cson

```
'.platform-darwin':
  'cmd-e': 'fuzzy-finder:toggle-file-finder'
  'cmd-t': 'tree-view:reveal-active-file'
  'cmd-b': 'script:run'
```
