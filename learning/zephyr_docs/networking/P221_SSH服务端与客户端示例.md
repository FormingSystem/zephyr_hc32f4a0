---
id: learning.zephyr-docs.networking.page-221
title: SSH服务端与客户端示例
kind: reference
status: maintained
domains: [zephyr, networking, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/net/ssh/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ssh-server-client"></a>

# 第221章\_SSH服务端与客户端示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/ssh/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 221.1 概述（Overview）

Zephyr的安全外壳协议（Secure Shell，SSH）示例启用SSH服务端与客户端功能。通过网络Shell，可以监听传入SSH连接，也可以连接外部SSH主机。

源码位于[samples/net/ssh](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ssh)。

<a id="requirements"></a>

## 221.2 要求（Requirements）

先完成[与主机系统联网（Networking with the host system）](P007_与主机系统联网.md#networking-with-host)所述准备。

<a id="building"></a>

## 221.3 构建（Building）

按以下方式构建SSH示例：

```sh
west build -b <board to use> samples/net/ssh -- -DCONF_FILE=<config file to use>
```

用常用终端模拟器连接Zephyr UART Shell。将`/dev/pts/12`替换为Zephyr实际输出的伪终端（Pseudotty）路径，例如`uart connected to pseudotty: /dev/pts/12`：

```sh
python -m serial.tools.miniterm /dev/pts/12 --raw --eol CRLF
```

<a id="generating-keys"></a>

## 221.4 生成密钥（Generating Keys）

首次运行时，在网络Shell中生成并保存主机密钥（Host key）。本例使用密钥索引0：

```sh
net ssh_key gen 0 rsa 2048
net ssh_key save 0 priv id_rsa
```

后续运行可以加载已有主机密钥：

```sh
net ssh_key load 0 priv id_rsa
```

> 译注——存储对象：这里的`id_rsa`是Zephyr Settings中的键名，不是自动写入主机当前目录的文件。当前实现以DER格式导出密钥，并通过`settings_save_one()`保存到`ssh/keys/<key-name>`。本示例启用NVS设置后端，具体持久化位置取决于目标存储配置；主机上的`~/.ssh/id_rsa`是另一对象。当前主函数还会调用`net_config_init_sshd()`初始化服务，执行原手动步骤前应确认当前服务与密钥状态。

<a id="ssh-server"></a>

## 221.5 SSH服务器（SSH Server）

启动SSH服务器，使用服务实例0和主机密钥索引0：

```sh
net sshd start -i 0 -b 192.0.2.1 -k 0 -p password123
```

省略`-b`或绑定到`0.0.0.0`时，服务器监听所有地址。绑定本地地址时也可以使用IPv6地址。

在主机Shell中输入：

```sh
ssh root@192.0.2.1
```

退出时依次按回车、`~`和`.`，即“回车、波浪号、点”。

<a id="ssh-client"></a>

## 221.6 SSH客户端（SSH Client）

从Zephyr SSH客户端连接主机，使用客户端实例0。将示例中的`username`替换为目标主机用户：

```sh
net ssh start username@192.0.2.2
```

按`Ctrl+d`或输入`exit`退出交互会话并回到Zephyr。目标地址也可使用IPv6地址或主机名：

```sh
net ssh start username@2001:db8::2
net ssh start username@[2001:db8::2]:22
net ssh start username@example.com
net ssh start username@example.com:22
```

<a id="client-public-key-auth"></a>

### 221.6.1 客户端公钥认证（Client Public Key Auth）

导出索引0对应的公钥（Public key）：

```sh
net ssh_key pub export 0
```

在主机Shell中，原文要求将导出的密钥“转换成RFC4716格式并追加到`authorized_keys`”，给出的命令如下：

```sh
ssh-keygen -i -f /dev/stdin -m pkcs8 <<< \
'-----BEGIN PUBLIC KEY-----
<your base-64 encoded host key>
------END PUBLIC KEY-----' \
>> ~/.ssh/authorized_keys
```

> 译注——格式与结束行：原文说明与命令不一致。依据[OpenSSH的ssh-keygen手册](https://man.openbsd.org/ssh-keygen)，`-i -m PKCS8`读取PKCS8格式并输出OpenSSH兼容格式，用于主机的`authorized_keys`，并非输出RFC4716。原命令的PEM结束行还多了一个连字符，应为`-----END PUBLIC KEY-----`。下方仅修复格式名称及输入方式，使用Bash here-document保存多行公钥；中间占位内容仍须替换为完整导出公钥，不可原样执行。

```sh
ssh-keygen -i -f /dev/stdin -m PKCS8 <<'EOF' >> ~/.ssh/authorized_keys
-----BEGIN PUBLIC KEY-----
<your base-64 encoded host key>
-----END PUBLIC KEY-----
EOF
```

随后停止并重新启动SSH客户端，增加主机密钥参数；公钥已被目标账户授权时不再需要密码。使用客户端实例0、密钥索引0：

```sh
net ssh stop
net ssh start -k 0 username@192.0.2.2
```

<a id="server-public-key-auth"></a>

### 221.6.2 服务端公钥认证（Server Public Key Auth）

在主机Shell中，将主机公钥转换为PEM表示：

```sh
ssh-keygen -e -f ~/.ssh/id_rsa.pub -m PKCS8
```

在Zephyr Shell中将该公钥导入索引1；索引0保留给先前生成的服务器主机密钥：

```sh
net ssh_key pub import 1
```

粘贴上面命令的输出，再按`Ctrl+C`结束。然后保存索引1的公钥：

```sh
net ssh_key save 1 pub authorized_key_0
```

后续运行可加载保存的公钥：

```sh
net ssh_key load 1 pub authorized_key_0
```

重新启动SSH服务器，不提供密码参数以禁用密码认证，并传入授权公钥参数。使用服务实例0、主机密钥索引0、授权公钥索引1：

```sh
net sshd stop -i 0
net sshd start -i 0 -b 192.0.2.1:22 -k 0 -a 1
```

在主机Shell中，使用相应私钥连接Zephyr SSH服务器，不再输入密码：

```sh
ssh -i ~/.ssh/id_rsa root@192.0.2.1
```

退出时依次按回车、`~`和`.`。

<a id="creating-ssh-channels"></a>

## 221.7 创建SSH通道（Creating SSH Channels）

除内置`net ssh`与`net sshd`命令外，示例注册了一组`sample`命令，演示如何在已有客户端连接上创建和删除SSH通道（Channel）。连接管理仍由前述SSH客户端命令负责。

先建立客户端连接，完成认证并打开一个交互会话通道：

```sh
net ssh start username@192.0.2.2
```

按`Ctrl+d`或输入`exit`回到Zephyr Shell，同时保持连接打开。然后在该连接上创建附加通道：

```sh
sample open
```

查看已打开通道、活动的服务端与客户端连接：

```sh
sample info
```

最后，按照`sample info`显示的编号移除通道：

```sh
sample close 1
```

这些命令依赖SSH传输回调（Transport callback）。示例分别注册服务端与客户端传输回调，跟踪连接，并调用[`ssh_transport_channel_open()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga1e8ec722a451a466904d077fd4b22a16)和[`ssh_channel_close()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#ga7c510e44353e7e791c8f13af3a554739)创建、删除通道。

> 译注——操作层次：退出交互会话、关闭某个通道和停止整个SSH客户端不是同一动作。上面的`sample close 1`使用显示出的通道编号，不是密钥索引。示例中的`password123`是原文演示密码；本文没有生成密钥、修改主机`authorized_keys`、启用服务或建立SSH连接。


> 译注——实现依据：[samples/net/ssh/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/ssh/Kconfig)、[samples/net/ssh/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/ssh/prj.conf)、[samples/net/ssh/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/ssh/src/main.c)、[subsys/net/lib/shell/ssh_keygen_shell.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/net/lib/shell/ssh_keygen_shell.c)。以上为本次核对的官方来源；分支内容可能继续变化，保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库相对链接用于版本对照。

对应官方文档源码：[samples/net/ssh/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/ssh/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/net/ssh/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/net/ssh/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P220_Prometheus指标示例.md) · [返回大纲](大纲.md)
