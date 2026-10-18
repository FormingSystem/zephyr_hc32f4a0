---
id: learning.zephyr-docs.bluetooth.page-27
title: L2CAP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/host/l2cap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-l2cap-shell"></a>

# 第27章\_L2CAP\_Shell

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/host/l2cap.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——使用前提：以下命令在启用了对应蓝牙功能的目标固件Zephyr Shell中执行，初始化与接入方式见[蓝牙Shell](P007_蓝牙Shell.md)。代码中的 `uart:~$` 是提示符，其后输出是原文预期结果；输入命令时不复制提示符和日志。若命令不可用或初始化失败，应先检查目标配置、控制器能力及当前版本帮助，再继续连接或传输步骤。本批仅翻译与核对文档，未连接设备或执行这些命令。

`l2cap` 命令开放逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）的部分API。下例演示注册低功耗蓝牙（Bluetooth Low Energy，LE）的协议／服务复用器（Protocol/Service Multiplexer，PSM），从另一设备连接它，并发送3个包，每包14个八位字节（Octet）。

前提是两台设备已经建立连接。

设备A注册LE PSM：

```text
uart:~$ l2cap register 29
L2CAP psm 41 sec_level 1 registered
```

> 译注——PSM进制：[官方Shell实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/host/shell/l2cap.c)按十六进制解析 `register` 和 `connect` 的PSM参数，因此输入29表示0x29，日志中的41是相同值的十进制形式。sec_level 1表示安全等级1。

设备B连接注册的LE PSM，并发送数据：

```text
uart:~$ l2cap connect 29
Chan sec: 1
L2CAP connection pending
Channel 0x20000210 connected
Channel 0x20000210 status 1
uart:~$ l2cap send 3 14
Rem 2
Rem 1
Rem 0
Outgoing data channel 0x20000210 transmitted
Outgoing data channel 0x20000210 transmitted
Outgoing data channel 0x20000210 transmitted
```

> 译注——发送日志：connection pending表示连接处理中，connected表示信道已连接；`l2cap send 3 14` 请求发送3包、每包14字节，Rem是剩余包数，transmitted表示对应发送完成。

设备A应收到如下数据：

```text
Incoming conn 0x20002398
Channel 0x20000210 status 1
Channel 0x20000210 connected
Channel 0x20000210 requires buffer
Incoming data channel 0x20000210 len 14
00000000: ff ff ff ff ff ff ff ff  ff ff ff ff ff ff       |........ ......  |
Channel 0x20000210 requires buffer
Incoming data channel 0x20000210 len 14
00000000: ff ff ff ff ff ff ff ff  ff ff ff ff ff ff       |........ ......  |
Channel 0x20000210 requires buffer
Incoming data channel 0x20000210 len 14
00000000: ff ff ff ff ff ff ff ff  ff ff ff ff ff ff       |........ ......  |
```

> 译注——接收日志：Incoming conn为收到连接，requires buffer为信道需要缓冲区；Incoming data与len 14表示收到14字节。三段十六进制转储各含14个0xff。指针地址和信道状态数值按原日志保留，不是本批实际连接的输出。


对应官方文档源码：[doc/services/connectivity/bluetooth/shell/host/l2cap.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/host/l2cap.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/shell/host/l2cap.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：GATT_Shell](P026_GATT_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：等时信道Shell](P028_等时信道Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P026_GATT_Shell.md) · [返回大纲](大纲.md) · [下一章](P028_等时信道Shell.md)

</details>

<!-- reading-navigation:end -->
