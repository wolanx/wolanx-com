---
title: systemctl
date: 2026-08-26
tags:
  - linux
---

# systemctl

## user service

```shell
mkdir -p ~/.config/systemd/user

# 创建 service
cat > ~/.config/systemd/user/myjob.service << 'EOF'
[Unit]
Description=gis-job

[Service]
Type=oneshot
WorkingDirectory=/home/28009030/jump-server
ExecStart=/home/28009030/jump-server/.venv/bin/python /home/28009030/jump-server/pg2gis.py

[Install]
WantedBy=default.target
EOF

# 创建 timer（每30分钟执行一次，按需改）
cat > ~/.config/systemd/user/myjob.timer << 'EOF'
[Unit]
Description=Run My Job Every 60 Minutes

[Timer]
OnCalendar=hourly
Persistent=true

[Install]
WantedBy=timers.target
EOF


systemctl --user daemon-reload
systemctl --user start myjob.service  # run

systemctl --user status myjob.service  # status
journalctl --user -u myjob.service -e  # log

# 加载并启动
systemctl --user enable --now myjob.timer
systemctl --user restart myjob.timer

# 确认下次触发时间
systemctl --user list-timers -all
```

## keep session

```shell
# enable
loginctl enable-linger $UID

# check
loginctl show-user $USER | grep Linger
```
