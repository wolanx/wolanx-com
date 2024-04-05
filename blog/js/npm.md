---
title: npm & node
date: 2018-03-22 16:38:57
tags:
  - js
---

# install

```shell
#官方编译过的二进制数据包安装
wget https://nodejs.org/download/release/latest-v12.x/node-v12.13.1-linux-x64.tar.gz
tar --strip-components 1 -xzvf node-v* -C /usr
```

## proxy

```shell
#npm config set registry http://registry.npm.taobao.org --global
#npm config set disturl http://npm.taobao.org/dist --global
npm config set registry http://registry.npmmirror.com
npm install -g yarn
yarn config set "strict-ssl" false -g
yarn
```

## node 升级

```shell
npm install -g n
n stable

yum erase nodejs npm -y # 卸载旧版本的nodejs
rpm -qa 'node|npm' | grep -v nodesource # 确认nodejs是否卸载干净
```

# npx

npx webpack === ./node_modules/.bin/webpack

# publish

```shell
npm loging
npm publish --access public
```

# yarn

```shell
# dependencies
yarn add @wolanx/react-netron
# devDependencies
yarn add -D rollup
# delete
yarn remove @wolanx/react-netron

yarn link # lib path
yarn link @wolanx/react-netron # proj path
yarn unlink @wolanx/react-netron # proj path

yarn upgrade @tauri-apps/cli @tauri-apps/api --latest
yarn upgrade-interactive --latest
```

# esbuild

```shell
npm install --save-exact esbuild

esbuild src/test.js --bundle --outfile=dist/test.js
```
