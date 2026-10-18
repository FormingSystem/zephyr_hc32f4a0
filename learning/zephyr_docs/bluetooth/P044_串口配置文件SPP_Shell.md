---
id: learning.zephyr-docs.bluetooth.page-44
title: 串口配置文件SPP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/classic/spp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-classic-spp-shell"></a>

# 第44章\_串口配置文件SPP\_Shell

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/classic/spp.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——使用前提：以下命令在启用了对应蓝牙功能的目标固件Zephyr Shell中执行，初始化与接入方式见[蓝牙Shell](P007_蓝牙Shell.md)。代码中的 `uart:~$` 是提示符，其后输出是原文预期结果；输入命令时不复制提示符和日志。若命令不可用或初始化失败，应先检查目标配置、控制器能力及当前版本帮助，再继续连接或传输步骤。本批仅翻译与核对文档，未连接设备或执行这些命令。

> 译注——术语：ACL 为异步面向连接链路（Asynchronous Connection-oriented Link）；UUID 为通用唯一标识符（Universally Unique Identifier）。流量控制（flow control）示例中的 `hold_credit` 和 `recv_complete` 分别展示接收额度保留与接收完成通知，操作时需对照两端日志。

本文说明如何运行经典蓝牙（Bluetooth Classic）的串口配置文件（Serial Port Profile，SPP）功能。`spp` 命令提供经典蓝牙 SPP Shell 命令。

<a id="commands"></a>

## 44.1 命令（Commands）

`spp` 命令如下：

```text
uart:~$ spp
spp - Bluetooth SPP sh commands
Subcommands:
  register_with_channel  : <channel> [limited credit value] [hold_credit]
  register_with_uuid     : <bt-uuid16(e.g. 1101)|bt-uuid32|bt-uuid128(e.g.
                           00001101-0000-1000-8000-00805F9B34FB)> [limited
                           credit value] [hold_credit]
  connect_by_channel     : <channel> [limited credit value] [hold_credit]
  connect_by_uuid        : <bt-uuid16(e.g. 1101)|bt-uuid32|bt-uuid128(e.g.
                           00001101-0000-1000-8000-00805F9B34FB)> [limited
                           credit value] [hold_credit]
  send                   : send [length of packet(s)]
  rls                    : [overrun|parity|framing]
  disconnect             : [none]
  recv_complete          : [none]
```

<a id="server-register"></a>

## 44.2 注册服务端（Server Register）

**按通道注册（Register with channel）**

<a id="tab-0-UmVnaXN0ZXIgd2l0aCBjaGFubmVs"></a>
<a id="panel-0-UmVnaXN0ZXIgd2l0aCBjaGFubmVs"></a>

```text
uart:~$ spp register_with_channel 9
SPP: server registered (channel=9)
```

**按 UUID 注册（Register with UUID）**

<a id="tab-0-UmVnaXN0ZXIgd2l0aCBVVUlE"></a>
<a id="panel-0-UmVnaXN0ZXIgd2l0aCBVVUlE"></a>

```text
uart:~$ spp register_with_uuid 00001101-0000-1000-8000-00805F9B34FB
SPP: server registered (uuid=00001101-0000-1000-8000-00805f9b34fb, channel=9)
```

<a id="connect"></a>

## 44.3 连接（Connect）

创建 SPP 连接前，应先建立 ACL 连接。

**服务端：接受传入连接（Server (incoming)）**

<a id="tab-1-U2VydmVyIChpbmNvbWluZyk="></a>
<a id="panel-1-U2VydmVyIChpbmNvbWluZyk="></a>

```text
uart:~$ spp register_with_channel 9
SPP: server registered (channel=9)
SPP: accepted incoming connection (conn=0x20004dc8)
SPP: connected (ep=0x20000d20, channel=9)
```

**客户端：按通道连接（Client by channel）**

<a id="tab-1-Q2xpZW50IGJ5IGNoYW5uZWw="></a>
<a id="panel-1-Q2xpZW50IGJ5IGNoYW5uZWw="></a>

```text
uart:~$ spp connect_by_channel 9
SPP: connect started (channel=9)
SPP: connected (ep=0x20000d20, channel=9)
```

**客户端：按 UUID 连接（Client by UUID）**

<a id="tab-1-Q2xpZW50IGJ5IFVVSUQ="></a>
<a id="panel-1-Q2xpZW50IGJ5IFVVSUQ="></a>

```text
uart:~$ spp connect_by_uuid 00001101-0000-1000-8000-00805F9B34FB
SPP: connect started (uuid=00001101-0000-1000-8000-00805f9b34fb)
SPP: connected (ep=0x20000d20, channel=9)
```

<a id="send-data"></a>

## 44.4 发送数据（Send Data）

```text
uart:~$ spp send 5
SPP: tx data (len=5)
```

> 译注——参数含义：`spp send 5` 中的 `5` 是发送长度（len），不是字符串内容。应结合对端接收日志核对实际传输；本页保留的成功日志来自官方示例。

<a id="disconnect"></a>

## 44.5 断开连接（Disconnect）

```text
uart:~$ spp disconnect
SPP: disconnecting...
SPP: disconnected (ep=0x20000d20)
```

<a id="flow-control"></a>

## 44.6 流量控制（Flow Control）

**服务端（Server）**

<a id="tab-2-U2VydmVy"></a>
<a id="panel-2-U2VydmVy"></a>

```text
uart:~$ spp register_with_channel 0 1 hold_credit
SPP: server registered (channel=6)
SPP: accepted incoming connection (conn=0x20005c70)
SPP: connected (ep=0x20006508, channel=6)
SPP: rx data (ep=0x20006508, len=10)
00000000: ff ff ff ff ff ff ff ff  ff ff                   |........ ..      |
uart:~$ spp recv_complete
SPP: rx data (ep=0x20006508, len=10)
00000000: ff ff ff ff ff ff ff ff  ff ff                   |........ ..      |
uart:~$ spp recv_complete
uart:~$ spp recv_complete
SPP: no inprogress buffer
uart:~$ spp send 10
SPP: tx data (len=10)
uart:~$ spp send 10
SPP: tx data (len=10)
```

**客户端（Client）**

<a id="tab-2-Q2xpZW50"></a>
<a id="panel-2-Q2xpZW50"></a>

```text
uart:~$ spp connect_by_channel 6 1 hold_credit
SPP: connect started (channel=6)
Security changed: A0:CD:F3:77:F3:A0 level 2
SPP: connected (ep=0x20006448, channel=6)
uart:~$ spp send 10
SPP: tx data (len=10)
uart:~$ spp send 10
SPP: tx data (len=10)
uart:~$
uart:~$ spp recv_complete
SPP: rx data (ep=0x20006448, len=10)
00000000: ff ff ff ff ff ff ff ff  ff ff                   |........ ..      |
uart:~$ spp recv_complete
SPP: rx data (ep=0x20006448, len=10)
00000000: ff ff ff ff ff ff ff ff  ff ff                   |........ ..      |
uart:~$ spp recv_complete
uart:~$ spp recv_complete
SPP: no inprogress buffer
```


对应官方文档源码：[doc/services/connectivity/bluetooth/shell/classic/spp.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/classic/spp.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/shell/classic/spp.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：电话簿访问配置文件PBAP_Shell](P043_电话簿访问配置文件PBAP_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：蓝牙音频总览](P045_蓝牙音频总览.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P043_电话簿访问配置文件PBAP_Shell.md) · [返回大纲](大纲.md) · [下一章](P045_蓝牙音频总览.md)

</details>

<!-- reading-navigation:end -->
