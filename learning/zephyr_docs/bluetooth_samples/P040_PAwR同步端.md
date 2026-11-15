---
id: learning.zephyr-docs.bluetooth-samples.page-40
title: PAwR同步端
kind: reference
status: maintained
domains: [zephyr, bluetooth, samples]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/periodic_sync_rsp/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ble_periodic_adv_sync_rsp"></a>

# 第40章\_PAwR 同步端（Periodic Advertising with Responses Synchronization）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/periodic_sync_rsp/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/periodic_sync_rsp/README.rst/..)

<a id="overview"></a>

## 40.1 概述（Overview）

本简单应用演示 Bluetooth LE 带响应的周期广播的同步功能。

本示例将子事件指示（Subevent indication）中收到的数据回送给广播端。

监听哪个子事件、在哪个响应时隙（Response slot）回复，由应用决定。本示例由 PAwR 广播端决定；连接时，它通过写入 GATT 特征分配子事件及响应时隙。

可将本示例烧录到多个设备；它们将获分配不同子事件和响应时隙，从而并发地与广播端通信。

> 译注——并发含义：各设备在分配给自己的子事件和响应时隙回复；“并发”指共同参加同一 PAwR 过程，不表示所有设备在同一个时隙同时发射。应与[PAwR广播端](P037_PAwR广播端.md)配套，并先确认每个设备完成时序分配。

<a id="requirements"></a>

## 40.2 前提条件（Requirements）

- 一块支持 Bluetooth LE 的开发板。

- 支持 PAwR 扫描端（Scanner）功能的控制器。

<a id="building-and-running"></a>

## 40.3 构建与运行（Building and Running）

> 译注——构建位置与前提：以下是官方示例命令，在读者自己的 Zephyr 源码根目录中，使用 UCRT64 Bash 或 Linux Bash 执行；先完成[入门环境](../getting_started/大纲.md)，并确认所选板及控制器支持本文所需蓝牙能力。`samples/...` 是官方已有示例目录，`<board>` 是须替换的板目标占位符；构建输出由工具生成，不在本中文目录创建同名源码。先检查构建成功及板目标，再按板文档烧录并观察本文行为或日志；构建、烧录或通信失败时，分别回查工具链／板配置、烧录器和两端角色／控制器能力。本次未构建或运行示例。

按以下方式构建并烧录，将 `<board>` 替换为目标开发板：

```text
west build -b <board> samples/bluetooth/periodic_sync_rsp
west flash
```

烧录后，设备进行可连接广播，等待 PAwR 广播端连接并通过 GATT 分配子事件和响应时隙。分配完成后，它通过 PAST 同步到 PAwR 广播序列（Train），并在自己的响应时隙回送收到的子事件数据。可同时在多块开发板上运行本示例，每块板获分配不同子事件和响应时隙。

在另一块开发板上运行 PAwR 广播端示例，启动 PAwR 广播并为本设备分配时序。 相关链接：[PAwR 广播端（Periodic Advertising with Responses Advertiser）](P037_PAwR广播端.md#ble_periodic_adv_rsp)。

<a id="see-also"></a>

## 40.4 另请参阅（See also）

[通用访问配置文件（Generic Access Profile，GAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html)

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

> 译注——实现入口：[src/main.c](../../../samples/bluetooth/periodic_sync_rsp/src/main.c)、[prj.conf](../../../samples/bluetooth/periodic_sync_rsp/prj.conf)为本仓库的相对源码入口。与本次上游快照的版本差异须分别核对，不能把译文当作本地硬件已支持的证明。

对应官方文档源码：[samples/bluetooth/periodic_sync_rsp/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/periodic_sync_rsp/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/bluetooth/periodic_sync_rsp/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或连接设备。

[上一章](P039_周期广播连接响应端.md) · [返回大纲](大纲.md) · [下一章](P041_外设PAST.md)
