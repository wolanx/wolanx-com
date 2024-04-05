---
title: rust
date: 2019-10-31T20:43:41+08:00
tags: [ rust ]
---

- [x] 官网 https://www.rust-lang.org/zh-CN/learn
- [ ] en 文档 https://doc.rust-lang.org/book/
- [ ] cn 文档 https://kaisery.github.io/trpl-zh-cn/

Cargo：Rust 的构建工具和包管理器

- cargo new hello-rust
- cargo build 可以构建项目
- cargo run 可以运行项目
- cargo test 可以测试项目
- cargo doc 可以为项目构建文档
- cargo publish 可以将库发布到 crates.io
- cargo --version

# install

```shell
# proxy bash
echo 'export RUSTUP_UPDATE_ROOT=https://mirrors.tuna.tsinghua.edu.cn/rustup/rustup' >> ~/.bash_profile
echo 'export RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup' >> ~/.bash_profile

# linux macos
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# windows
https://rustup.rs/

# rust update 自更新
rustc -V
rustup update

# dep update
cargo update
```

# 交叉编译

## win => linux

```shell
rustup target list # (installed)
rustup target add x86_64-unknown-linux-musl

# musl 静态编译 lld statically linked
apt install musl-tools -y # 核心
cargo build --target x86_64-unknown-linux-musl
```

```toml title="~/.cargo/config.toml"
# ~/.cargo/config.toml
[target.x86_64-unknown-linux-musl]
linker = "rust-lld"
```

## wasm

```shell
# install wasmtime
curl https://wasmtime.dev/install.sh -sSf | bash

fn main() {
    println!("Hello, world!");
}

rustup target add wasm32-wasi
rustc hello.rs --target wasm32-wasi
wasmtime hello.wasm
# Hello, world!
```

# bind clang

- Rust与C/C++混合编程 https://zhuanlan.zhihu.com/p/622405994
- bindgen https://rust-lang.github.io/rust-bindgen/introduction.html

## vcpkg windows

> C++ Library Manager for Windows, Linux, and MacOS

```shell
# ~/.vcpkg-clion
# git set https://stackoverflow.com/a/70942119
git clone --progress https://github.com/microsoft/vcpkg vcpkg
# git fetch --unshallow
# run ./bootstrap-vcpkg.sh

export VCPKG_ROOT="C:\Users\106006\.vcpkg-clion\vcpkg"
vcpkg search openssl
vcpkg install openssl
```
