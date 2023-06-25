---
title: iTerm2 && Oh My Zsh
date: 2017-11-01
tags:
  - linux
---

# iTerm2 && Oh My Zsh

安装过程 https://www.jianshu.com/p/7de00c73a2bb

## .bash_profile

```sh
alias l='ls -la'
alias dc='docker-compose'
alias gs='git status'
alias gd='git diff'
```

# mintty

vi ~/.bash_profile

```sh
alias ..='cd ..'
alias tfa='terraform apply --auto-approve'

export TF_PLUGIN_CACHE_DIR="$HOME/.terraform.d/plugin-cache"

export PATH=$PATH:/d/Toolbox/apps/IDEA-U/ch-0/192.7142.36/jbr/bin
```
