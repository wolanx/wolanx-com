---
title: WindowsTerminal
date: 2021-02-25
tags:
  - 工具
---

# WindowsTerminal git bash

```json
{
  "$schema": "https://aka.ms/terminal-profiles-schema",
  "defaultProfile": "{1c4de342-38b7-51cf-b940-2309a097f589}",
  "copyOnSelect": false,
  "copyFormatting": false,
  "profiles": {
    "defaults": {},
    "list": [
      {
        "acrylicOpacity": 0,
        "closeOnExit": true,
        "colorScheme": "Campbell",
        "commandline": "C:\\Program Files\\Git\\bin\\bash.exe",
        "cursorColor": "#FFFFFF",
        "cursorShape": "bar",
        "fontFace": "YaHei Consolas Hybrid",
        "fontSize": 13,
        "guid": "{1c4de342-38b7-51cf-b940-2309a097f589}",
        "historySize": 200,
        "icon": "C:\\Program Files\\Git\\mingw64\\share\\git\\git-for-windows.ico",
        "name": "git-bash",
        "padding": "0, 0, 0, 0",
        "snapOnInput": true,
        "startingDirectory": "%USERPROFILE%/Desktop",
        "useAcrylic": false
      },
      {
        "guid": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
        "name": "Windows PowerShell",
        "commandline": "powershell.exe",
        "hidden": false
      },
      {
        "guid": "{0caa0dad-35be-5f56-a8ff-afceeeaa6101}",
        "name": "Command Prompt",
        "commandline": "cmd.exe",
        "hidden": false
      },
      {
        "guid": "{b453ae62-4e3d-5e58-b989-0a998ec441b8}",
        "hidden": false,
        "name": "Azure Cloud Shell",
        "source": "Windows.Terminal.Azure"
      }
    ]
  },
  "schemes": [],
  "actions": [
    {
      "command": {
        "action": "copy",
        "singleLine": false
      },
      "keys": "ctrl+c"
    },
    {
      "command": "paste",
      "keys": "ctrl+v"
    },
    {
      "command": "find",
      "keys": "ctrl+f"
    },
    {
      "command": {
        "action": "splitPane",
        "split": "auto",
        "splitMode": "duplicate"
      },
      "keys": "alt+shift+d"
    }
  ]
}
```
