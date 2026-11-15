---
id: learning.zephyr-docs.bluetooth.page-41
title: 经典蓝牙L2CAP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/classic/l2cap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-classic-l2cap-shell"></a>

# 第41章\_经典蓝牙L2CAP\_Shell

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/classic/l2cap.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——使用前提：以下命令在启用了对应蓝牙功能的目标固件Zephyr Shell中执行，初始化与接入方式见[蓝牙Shell](P007_蓝牙Shell.md)。代码中的 `uart:~$` 是提示符，其后输出是原文预期结果；输入命令时不复制提示符和日志。若命令不可用或初始化失败，应先检查目标配置、控制器能力及当前版本帮助，再继续连接或传输步骤。本批仅翻译与核对文档，未连接设备或执行这些命令。

> 译注——通道关系：ACL 为异步面向连接链路（Asynchronous Connection-oriented Link）。本页“无连接”是无需建立面向连接的 L2CAP 通道，仍要求底层 ACL 已连接。示例 `register 1001` 对应日志中的十进制 PSM 4097，即十六进制 `0x1001`；PSM 是协议／服务复用器（Protocol/Service Multiplexer）。

本文说明如何运行经典蓝牙（Bluetooth Classic）的逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）功能。`br l2cap` 命令提供经典蓝牙 L2CAP Shell 命令。

<a id="commands"></a>

## 41.1 命令（Commands）

`br l2cap` 命令如下：

```text
uart:~$ br l2cap
l2cap - [none]
Subcommands:
  register    : <psm> <mode: none, ret, fc, eret, stream> [hold_credit]
                [mode_optional] [extended_control]
  connect     : <psm> <mode: none, ret, fc, eret, stream> [hold_credit]
                [mode_optional] [extended_control]
  disconnect  : [none]
  send        : [number of packets] [length of packet(s)]
  credits     : [none]
  echo        : L2CAP BR ECHO commands
  connless    : L2CAP connectionless commands
```

`br l2cap echo` 命令如下：

```text
uart:~$ br l2cap echo
echo - L2CAP BR ECHO commands
Subcommands:
  register    : [none]
  unregister  : [none]
  req         : <length of data>
  rsp         : <identifier> <length of data>
```

`br l2cap connless` 命令如下：

```text
uart:~$ br l2cap connless
connless - L2CAP connectionless commands
Subcommands:
  register    : <psm> [sec level]
  unregister  : [none]
  send        : <psm> <length of data>
```

<a id="connection-oriented-l2cap"></a>

## 41.2 面向连接的 L2CAP（Connection-oriented L2CAP）

【服务端（Server）】注册 L2CAP 服务端：

蓝牙协议栈通过 `bt init` 初始化后，可以调用 `br l2cap register` 注册 L2CAP 服务端。

```text
uart:~$ br l2cap register 1001 none
L2CAP psm 4097 registered
```

【客户端（Client）】创建 L2CAP 连接：

此命令只能在建立 ACL 连接后使用。

```text
uart:~$ br l2cap connect 1001 none
L2CAP connection pending
```

L2CAP 连接已建立：

```text
uart:~$
Security changed: XX:XX:XX:XX:XX:XX level 2
Incoming BR/EDR conn 0x20004848
Channel 0x20000b18 connected
It is basic mode
```

向远端发送 L2CAP 数据：

```text
uart:~$ br l2cap send
Rem 0
```

已收到 L2CAP 数据：

```text
uart:~$
Incoming data channel 0x20000b18 len 200
00000000: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00 |........ ........|
00000010: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00 |........ ........|
00000020: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00 |........ ........|
00000030: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00 |........ ........|
00000040: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00 |........ ........|
00000050: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00 |........ ........|
00000060: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00 |........ ........|
00000070: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00 |........ ........|
00000080: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00 |........ ........|
00000090: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00 |........ ........|
000000A0: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00 |........ ........|
000000B0: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00 |........ ........|
000000C0: 00 00 00 00 00 00 00 00                          |........         |
```

断开 L2CAP 连接：

```text
uart:~$ br l2cap disconnect
```

L2CAP 连接已断开：

```text
Channel 0x20000b18 disconnected
```

<a id="l2cap-echo"></a>

## 41.3 L2CAP 回显（L2CAP echo）

`echo` 子命令提供经典蓝牙 L2CAP 回显（echo）请求和响应功能。

这些命令只能在建立 ACL 连接后使用。

监听 L2CAP 回显请求和回显响应：

```text
uart:~$ br l2cap echo register
```

停止监听 L2CAP 回显请求和回显响应：

```text
uart:~$ br l2cap echo unregister
```

> 译注——操作顺序：注册与注销监听是两种独立操作。若已执行 `unregister`，要观察后面的接收回调日志，须重新注册监听；不能把本节所有命令不加区分地连续粘贴执行。

发送 L2CAP 回显请求：

```text
uart:~$ br l2cap echo req 1
```

已收到回显请求：

```text
Incoming ECHO REQ data identifier 4 len 1
00000000: 00                                               |.                |
```

发送 L2CAP 回显响应：

```text
uart:~$ br l2cap echo rsp 4 1
```

已收到回显响应：

```text
uart:~$
Incoming ECHO RSP data len 1
00000000: 00                                               |.                |
```

<a id="connectionless-l2cap"></a>

## 41.4 无连接 L2CAP（Connectionless L2CAP）

`connless` 子命令提供经典蓝牙的无连接 L2CAP 通信功能，允许在不建立 L2CAP 连接的情况下传输数据包。

此子命令由 [`CONFIG_BT_L2CAP_CONNLESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_CONNLESS) 控制。

这些命令只能在建立 ACL 连接后使用。

监听无连接 L2CAP 数据包：

```text
uart:~$ br l2cap connless register 1001
Register connectionless callbacks with PSM 0x1001
```

发送数据：

```text
uart:~$ br l2cap connless send 1001 1
Sending connectionless data with PSM 0x1001
```

已收到无连接数据：

```text
Incoming connectionless data psm 0x1001 len 1
00000000: 00                                               |.                |
```


对应官方文档源码：[doc/services/connectivity/bluetooth/shell/classic/l2cap.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/classic/l2cap.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/shell/classic/l2cap.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：HFP_Shell](P040_HFP_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：消息访问配置文件MAP_Shell](P042_消息访问配置文件MAP_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P040_HFP_Shell.md) · [返回大纲](大纲.md) · [下一章](P042_消息访问配置文件MAP_Shell.md)

</details>

<!-- reading-navigation:end -->
