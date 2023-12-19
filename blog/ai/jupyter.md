---
title: jupyter
date: 2019-05-08T17:15:51+08:00
tags: [python, ml]
---

## notebook

```shell
cat > config.json
{
  "NotebookApp": {
    "password": "argon2:$argon2id$v=19$m=10240,t=10,p=8$TvqWSGeQsqj2qsztGA7rmw$k0YNPHZM/u8V67dVVst9pw"
  }
}
pwd: 1~8
notebook --ip=0.0.0.0 --port=5000 --allow-root --config=./config.json
nohup jupyter notebook --ip=0.0.0.0 --port=5000 --allow-root --config=./config.json &
http://10.231.9.124:5000/tree
```

```shell
# 把 a.ipynb 提取出 a.py
jupyter nbconvert --to script a.ipynb
# 把 a.ipynb 提取出 a.html
jupyter nbconvert --to html a.ipynb
```
