---
id: learning.zephyr-docs.bluetooth.page-39
title: GOEP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/classic/goep.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-classic-goep-shell"></a>

# 第39章\_GOEP\_Shell

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/classic/goep.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——使用前提：以下命令在启用了对应蓝牙功能的目标固件Zephyr Shell中执行，初始化与接入方式见[蓝牙Shell](P007_蓝牙Shell.md)。代码中的 `uart:~$` 是提示符，其后输出是原文预期结果；输入命令时不复制提示符和日志。若命令不可用或初始化失败，应先检查目标配置、控制器能力及当前版本帮助，再继续连接或传输步骤。本批仅翻译与核对文档，未连接设备或执行这些命令。

> 译注——术语：ACL 为异步面向连接链路（Asynchronous Connection-oriented Link），L2CAP 为逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol），RFCOMM 为串口仿真协议。OBEX 连接命令中的 `mopl` 指最大 OBEX 包长度（Maximum OBEX Packet Length）。

本文说明如何运行经典蓝牙（Bluetooth Classic）的通用对象交换配置文件（Generic Object Exchange Profile，GOEP）功能。`goep` 命令提供经典蓝牙 GOEP Shell 命令。

<a id="commands"></a>

## 39.1 命令（Commands）

`goep` 命令如下：

```text
uart:~$ goep
goep - Bluetooth GOEP shell commands
Subcommands:
  register-rfcomm    : <channel>
  connect-rfcomm     : <channel>
  disconnect-rfcomm  :
  register-l2cap     : <psm>
  connect-l2cap      : <psm>
  disconnect-l2cap   :
  alloc-buf          : Alloc tx buffer
  release-buf        : Free allocated tx buffer
  add-header         : Adding header sets
  client             : Client sets
  server             : Server sets
```

`goep client` 命令如下：

```text
uart:~$ goep client
client - Client sets
Subcommands:
  conn     : <mopl>
  disconn  :
  put      : <final: true, false>
  get      : <final: true, false>
  abort    :
  setpath  : [parent] [create]
  action   : <final: true, false>
```

`goep server` 命令如下：

```text
uart:~$ goep server
server - Server sets
Subcommands:
  reg      : [UUID 128]
  unreg    :
  conn     : <rsp: continue, success, error> <mopl> [rsp_code]
  disconn  : <rsp: continue, success, error> [rsp_code]
  put      : <rsp: continue, success, error> [rsp_code]
  get      : <rsp: continue, success, error> [rsp_code]
  abort    : <rsp: continue, success, error> [rsp_code]
  setpath  : <rsp: continue, success, error> [rsp_code]
  action   : <rsp: continue, success, error> [rsp_code]
```

<a id="connect-goep-transport"></a>

## 39.2 连接 GOEP 传输层（Connect GOEP Transport）

创建 GOEP 传输连接前，应先建立 ACL 连接。

使用 L2CAP 通道作为传输层：

**L2CAP 服务端（L2CAP Server）**

<a id="tab-0-TDJDQVAgU2VydmVy"></a>
<a id="panel-0-TDJDQVAgU2VydmVy"></a>

```text
uart:~$ goep register-l2cap 0
L2CAP server (psm 1001) is registered
Security changed: XX:XX:XX:XX:XX:XX level 2
GOEP 0x20005600 transport connected on 0x20004dc8
uart:~$
```

**L2CAP 客户端（L2CAP Client）**

<a id="tab-0-TDJDQVAgQ2xpZW50"></a>
<a id="panel-0-TDJDQVAgQ2xpZW50"></a>

```text
uart:~$ goep connect-l2cap 1001
GOEP L2CAP connection pending
Security changed: XX:XX:XX:XX:XX:XX level 2
GOEP 0x20005600 transport connected on 0x20004dc8
uart:~$
```

使用 RFCOMM 通道作为传输层：

**RFCOMM 服务端（RFCOMM Server）**

<a id="tab-1-UkZDT01NIFNlcnZlcg=="></a>
<a id="panel-1-UkZDT01NIFNlcnZlcg=="></a>

```text
uart:~$ goep register-rfcomm 0
RFCOMM server (channel 06) is registered
Security changed: XX:XX:XX:XX:XX:XX level 2
GOEP 0x20005600 transport connected on 0x20004dc8
uart:~$
```

**RFCOMM 客户端（RFCOMM Client）**

<a id="tab-1-UkZDT01NIENsaWVudA=="></a>
<a id="panel-1-UkZDT01NIENsaWVudA=="></a>

```text
uart:~$ goep connect-rfcomm 6
GOEP RFCOMM connection pending
Security changed: XX:XX:XX:XX:XX:XX level 2
GOEP 0x20005600 transport connected on 0x20004dc8
uart:~$
```

<a id="disconnect-goep-transport"></a>

## 39.3 断开 GOEP 传输层（Disconnect GOEP transport）

使用 L2CAP 通道作为传输层：

**其中一端（One Side）**

<a id="tab-2-T25lIFNpZGU="></a>
<a id="panel-2-T25lIFNpZGU="></a>

```text
GOEP 0x20005600 transport disconnected
uart:~$
```

**另一端（Another Side）**

<a id="tab-2-QW5vdGhlciBTaWRl"></a>
<a id="panel-2-QW5vdGhlciBTaWRl"></a>

```text
uart:~$ goep disconnect-l2cap
GOEP L2CAP disconnection pending
GOEP 0x20005600 transport disconnected
uart:~$
```

使用 RFCOMM 通道作为传输层：

**其中一端（One Side）**

<a id="tab-3-T25lIFNpZGU="></a>
<a id="panel-3-T25lIFNpZGU="></a>

```text
GOEP 0x20005600 transport disconnected
uart:~$
```

**另一端（Another Side）**

<a id="tab-3-QW5vdGhlciBTaWRl"></a>
<a id="panel-3-QW5vdGhlciBTaWRl"></a>

```text
uart:~$ goep disconnect-rfcomm
GOEP RFCOMM disconnection pending
GOEP 0x20005600 transport disconnected
uart:~$
```

<a id="connect-to-obex-server"></a>

## 39.4 连接 OBEX 服务端（Connect to OBEX Server）

**OBEX 服务端（OBEX Server）**

<a id="tab-4-T0JFWCBTZXJ2ZXI="></a>
<a id="panel-4-T0JFWCBTZXJ2ZXI="></a>

```text
uart:~$ goep server reg
uart:~$
OBEX server 0x20005850 conn req, version 10, mopl 00ff
uart:~$ goep server conn success 255
uart:~$
```

**OBEX 客户端（OBEX Client）**

<a id="tab-4-T0JFWCBDbGllbnQ="></a>
<a id="panel-4-T0JFWCBDbGllbnQ="></a>

```text
uart:~$ goep client conn 255
OBEX client 0x20005818 conn rsp, rsp_code Success, version 10, mopl 00ff
uart:~$
```

<a id="disconnect-from-obex-server"></a>

## 39.5 断开与 OBEX 服务端的连接（Disconnect from OBEX Server）

**OBEX 服务端（OBEX Server）**

<a id="tab-5-T0JFWCBTZXJ2ZXI="></a>
<a id="panel-5-T0JFWCBTZXJ2ZXI="></a>

```text
OBEX server 0x20005850 disconn req
uart:~$ goep server disconn success
uart:~$
```

**OBEX 客户端（OBEX Client）**

<a id="tab-5-T0JFWCBDbGllbnQ="></a>
<a id="panel-5-T0JFWCBDbGllbnQ="></a>

```text
uart:~$ goep client disconn
OBEX client 0x20005818 disconn rsp, rsp_code Success
uart:~$
```

<a id="obex-put-operation"></a>

## 39.6 OBEX 写入操作（OBEX Put Operation）

**OBEX 服务端（OBEX Server）**

<a id="tab-6-T0JFWCBTZXJ2ZXI="></a>
<a id="panel-6-T0JFWCBTZXJ2ZXI="></a>

```text
uart:~$
OBEX server 0x20005850 put req, final false, data len 12
HI c3 Len 4
00000000: 00 00 00 09                                      |....             |
HI 48 Len 4
00000000: 12 34 56 78                                      |.4Vx             |
uart:~$ goep server put continue
OBEX server 0x20005850 put req, final true, data len 8
HI 49 Len 5
00000000: 12 34 56 78 90                                   |.4Vx.            |
uart:~$ goep server put success
uart:~$
```

**OBEX 客户端（OBEX Client）**

<a id="tab-6-T0JFWCBDbGllbnQ="></a>
<a id="panel-6-T0JFWCBDbGllbnQ="></a>

```text
uart:~$ goep alloc-buf
uart:~$ goep add-header len 9
uart:~$ goep add-header body 12345678
uart:~$ goep client put false
OBEX client 0x20005818 put rsp, rsp_code Continue, data len 0
uart:~$ goep alloc-buf
uart:~$ goep add-header end_body 1234567890
uart:~$ goep client put true
OBEX client 0x20005818 put rsp, rsp_code Success, data len 0
uart:~$
```

<a id="obex-get-operation"></a>

## 39.7 OBEX 获取操作（OBEX Get Operation）

**OBEX 服务端（OBEX Server）**

<a id="tab-7-T0JFWCBTZXJ2ZXI="></a>
<a id="panel-7-T0JFWCBTZXJ2ZXI="></a>

```text
uart:~$ goep alloc-buf
uart:~$ goep add-header len 9
uart:~$ goep add-header body 12345678
uart:~$ goep server get continue
OBEX server 0x20005850 get req, final true, data len 0
uart:~$ goep alloc-buf
uart:~$ goep add-header end_body 1234567890
uart:~$
uart:~$ goep server get success
uart:~$
```

**OBEX 客户端（OBEX Client）**

<a id="tab-7-T0JFWCBDbGllbnQ="></a>
<a id="panel-7-T0JFWCBDbGllbnQ="></a>

```text
uart:~$ goep client get true
OBEX client 0x20005818 get rsp, rsp_code Continue, data len 12
HI c3 Len 4
00000000: 00 00 00 09                                      |....             |
HI 48 Len 4
00000000: 12 34 56 78                                      |.4Vx             |
uart:~$ goep client get true
OBEX client 0x20005818 get rsp, rsp_code Success, data len 8
HI 49 Len 5
00000000: 12 34 56 78 90                                   |.4Vx.            |
uart:~$
```

> 译注——传输与会话：L2CAP／RFCOMM 传输连接与对象交换协议（Object Exchange Protocol，OBEX）会话分两步建立。先按对应传输示例连接，再执行 OBEX `conn`；对端收到请求后按其服务端示例响应。`Continue` 表示继续传输，`Success` 表示操作成功。PUT 示例中的 `12345678`、`1234567890` 是十六进制字节数据，分别为 4 和 5 字节，与长度 9 对应。


对应官方文档源码：[doc/services/connectivity/bluetooth/shell/classic/goep.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/classic/goep.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/shell/classic/goep.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：AVRCP_Shell](P038_AVRCP_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：HFP_Shell](P040_HFP_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P038_AVRCP_Shell.md) · [返回大纲](大纲.md) · [下一章](P040_HFP_Shell.md)

</details>

<!-- reading-navigation:end -->
