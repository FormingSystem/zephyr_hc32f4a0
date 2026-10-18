---
id: learning.zephyr-docs.hardware.cansample-2
title: CAN_ISO-TP传输示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/canbus/isotp/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="isotp"></a>

# 第377章\_CAN_ISO-TP传输示例

## 377.1\_概述

原文：[ISO-TP library](https://docs.zephyrproject.org/latest/samples/subsys/canbus/isotp/README.html)。读取日期：2026-10-13，`latest`。

本示例演示如何使用 [ISO-TP 库](P379_CAN_ISO-TP协议.md)。ISO-TP 是 ISO 15765-2 定义的传输协议（Transport Protocol），用于通过控制器局域网（Controller Area Network，CAN）传输消息。

两块开发板之间交换两种消息：长消息采用 8 帧的块大小（Block Size，BS）；短消息采用 5 毫秒的最小帧间隔（Minimum Separation Time，STmin）。短消息的发送函数调用是非阻塞（Non-blocking）的，长消息的发送函数调用是阻塞（Blocking）的。

[在 GitHub 上浏览示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/canbus/isotp)。

## 377.2\_构建与运行

下列说明适用于具有集成 CAN 控制器的开发板，例如 NXP TWR-KE18F 或 Nucleo-F746ZG。

对于 NXP TWR-KE18F，在 Zephyr 仓库根目录执行：

> 译注：以下为官方命令原文。使用已配置好 Zephyr 环境的终端；Linux 可使用 Bash，Windows 可使用已完成本仓库环境配置的 UCRT64 终端。翻译过程没有执行构建或烧录。

```bash
# From the root of the zephyr repository
west build -b twr_ke18f samples/subsys/canbus/isotp
west flash
```

## 377.3\_硬件要求

两块支持 CAN 总线的开发板，彼此连接。

## 377.4\_示例输出

原日志中的 `CAN_1` 是 CAN 控制器设备名，`TX` 表示发送（Transmit），`cb` 表示回调（Callback）。

```text
Start sending data
[00:00:00.000,000] <inf> can_driver: Init of CAN_1 done
========================================
|   ____  ___  ____       ____  ____   |
|  |_  _|/ __||    | ___ |_  _||  _ \  |
|   _||_ \__ \| || | ___   ||  | ___/  |
|  |____||___/|____|       ||  |_|     |
========================================
Got 248 bytes in total
This is the sample test for the short payload
TX complete cb [0]
```

上面显示的数值可能不同。输出中的 `Got 248 bytes in total` 表示共收到 248 字节；`TX complete cb [0]` 是发送（Transmit，TX）完成回调（Callback）的输出。

## 377.5\_另请参阅

[CAN ISO-TP 协议接口](P380_CAN_ISO-TP接口参考.md)。

---

[上一章：CAN总线子系统示例目录](P376_CAN总线子系统示例目录.md) · [下一章：CAN总线子系统](P378_CAN总线子系统.md) · [返回大纲](大纲.md)
