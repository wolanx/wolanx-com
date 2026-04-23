---
title: neovim
date: 2023-08-07
tags:
  - linux
---

## config

```shell
:help config

# windows
	Unix			~/.config/nvim/init.vim		(or init.lua)
	Windows			~/AppData/Local/nvim/init.vim	(or init.lua)
```

## 在 Neovim 中直接运行命令

```vim
:!命令                      # 运行单条命令
:terminal                  # 打开内置终端
:split | terminal          # 分屏打开终端
```

```lua C:\Users\你的用户名\AppData\Local\nvim\init.lua
-- 基础设置
vim.opt.number = true          -- 显示行号
vim.opt.relativenumber = true  -- 相对行号
vim.opt.tabstop = 4           -- Tab 4空格
vim.opt.shiftwidth = 4
vim.opt.expandtab = true      -- Tab转空格

-- 简单快捷键
vim.g.mapleader = " "

-- 文件树
vim.keymap.set('n', '<leader>e', ':Explore<CR>')

-- 保存退出
vim.keymap.set('n', '<leader>w', ':w<CR>')
vim.keymap.set('n', '<leader>q', ':q<CR>')

-- 在终端运行当前文件
vim.keymap.set('n', '<leader>r', ':!python %<CR>')  -- 根据文件类型改
```
