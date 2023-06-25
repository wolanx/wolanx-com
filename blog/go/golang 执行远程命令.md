---
title: go 远程执行
date: 2018-03-20 16:34:12
tags:
  - go
---

# 概述

远程执行命令有什么用？为什么要远程执行命令？ 如果你只有2，3台服务器需要管理的时候，远程执行命令确实没有没多大作用，你可以登录到每台服务器上去完成各种操作。
当你的服务器大于3台的时候，远程执行的命令的方式就可以大大提高你的生产力了。

如果你有一个可以远程执行命令的工具，那么就可以像操作单台机器那样操作多台机器，机器越多，效率提高的越多。 远程执行命令最常用的方法就是利用
SSH 协议，将命令发送到远程机器上执行，并获取返回结果。

本文介绍如何使用 golang 实现远程执行命令。

# 一般命令

所谓一般命令，就是在一定时间内会执行完的命令。比如 grep, cat 等等。 执行命令的步骤是：连接，执行，获取结果

## 连接

连接包含了认证，可以使用 password 或者 sshkey 2种方式来认证。下面的示例为了简单，使用了密码认证的方式来完成连接。

```text
import (  
  "fmt"
  "time"

  "golang.org/x/crypto/ssh"
)

func connect(user, password, host string, port int) (*ssh.Session, error) {  
  var (
    auth         []ssh.AuthMethod
    addr         string
    clientConfig *ssh.ClientConfig
    client       *ssh.Client
    session      *ssh.Session
    err          error
  )
  // get auth method
  auth = make([]ssh.AuthMethod, 0)
  auth = append(auth, ssh.Password(password))

  clientConfig = &ssh.ClientConfig{
    User:    user,
    Auth:    auth,
    Timeout: 30 * time.Second,
  }

  // connet to ssh
  addr = fmt.Sprintf("%s:%d", host, port)

  if client, err = ssh.Dial("tcp", addr, clientConfig); err != nil {
    return nil, err
  }

  // create session
  if session, err = client.NewSession(); err != nil {
    return nil, err
  }

  return session, nil
}

```

连接的方法很简单，只要提供登录主机的 *用户*， *密码*， *主机名或者IP*  *SSH端口*

## 执行，命令获取结果

连接成功后，执行命令很简单

```text
import (  
  "fmt"
  "log"
  "os"
  "time"

  "golang.org/x/crypto/ssh"
)

func main() {  
  session, err := connect("root", "xxxxx", "127.0.0.1", 22)
  if err != nil {
    log.Fatal(err)
  }
  defer session.Close()

  session.Run("ls /; ls /abc")
}

```

上面代码运行之后，虽然命令正常执行了，但是没有正常输出的结果，也没有异常输出的结果。 要想显示结果，需要将 **session** 的
Stdout 和 Stderr 重定向 修改 **func main** 为如下：

```text
func main() {  
  session, err := connect("root", "xxxxx", "127.0.0.1", 22)
  if err != nil {
    log.Fatal(err)
  }
  defer session.Close()

  session.Stdout = os.Stdout
  session.Stderr = os.Stderr
  session.Run("ls /; ls /abc")
}

```

这样就能在屏幕上显示正常，异常的信息了。

# 交互式命令

上面的方式无法远程执行交互式命令，比如 **top** ， 远程编辑一个文件，比如 **vi /etc/nginx/nginx.conf**
如果要支持交互式的命令，需要当前的terminal来接管远程的 PTY。

```
package main

import (
  "fmt"
  "log"
  "os"
  "time"

  "golang.org/x/crypto/ssh"
  "golang.org/x/crypto/ssh/terminal"
)

func connect(user, password, host string, port int) (*ssh.Session, error) {
  var (
    auth         []ssh.AuthMethod
    addr         string
    clientConfig *ssh.ClientConfig
    client       *ssh.Client
    session      *ssh.Session
    err          error
  )
  // get auth method
  auth = make([]ssh.AuthMethod, 0)
  auth = append(auth, ssh.Password(password))
  clientConfig = &ssh.ClientConfig{
    User:    user,
    Auth:    auth,
    Timeout: 30 * time.Second,
  }
  // connet to ssh
  addr = fmt.Sprintf("%s:%d", host, port)
  if client, err = ssh.Dial("tcp", addr, clientConfig); err != nil {
    return nil, err
  }
  // create session
  if session, err = client.NewSession(); err != nil {
    return nil, err
  }
  return session, nil
}

func main() {
  session, err := connect("root", "123", "139.196.14.10", 22)
  if err != nil {
    log.Fatal(err)
  }
  defer session.Close()

  fd := int(os.Stdin.Fd())
  oldState, err := terminal.MakeRaw(fd)
  if err != nil {
    panic(err)
  }
  defer terminal.Restore(fd, oldState)
  // excute command
  session.Stdout = os.Stdout
  session.Stderr = os.Stderr
  session.Stdin = os.Stdin
  termWidth, termHeight, err := terminal.GetSize(fd)
  if err != nil {
    panic(err)
  }
  // Set up terminal modes
  modes := ssh.TerminalModes{
    ssh.ECHO:          1,     // enable echoing
    ssh.TTY_OP_ISPEED: 14400, // input speed = 14.4kbaud
    ssh.TTY_OP_OSPEED: 14400, // output speed = 14.4kbaud
  }
  // Request pseudo terminal
  if err := session.RequestPty("xterm", termHeight, termWidth, modes); err != nil {
    log.Fatal(err)
  }
  session.Run("htop")
}
```

这样就可以执行交互式命令了，比如上面的 **top** 也可以通过 **vi /etc/nginx/nignx.conf** 之类的命令来远程编辑文件。