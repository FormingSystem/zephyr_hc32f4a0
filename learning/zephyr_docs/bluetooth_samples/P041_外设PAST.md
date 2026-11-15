---
id: learning.zephyr-docs.bluetooth-samples.page-41
title: 外设PAST
kind: reference
status: maintained
domains: [zephyr, bluetooth, samples]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/peripheral_past/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ble_peripheral_past"></a>

# 第41章\_周期广播同步传输外设（Periodic Advertising Synchronization Transfer Peripheral）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/peripheral_past/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/peripheral_past/README.rst/..)

<a id="overview"></a>

## 41.1 概述（Overview）

本简单应用演示作为接收端的 Bluetooth LE 周期广播同步传输（PAST）功能。

<a id="requirements"></a>

## 41.2 前提条件（Requirements）

- 一块支持 Bluetooth LE 5.1 的开发板。

<a id="building-and-running"></a>

## 41.3 构建与运行（Building and Running）

> 译注——构建位置与前提：以下是官方示例命令，在读者自己的 Zephyr 源码根目录中，使用 UCRT64 Bash 或 Linux Bash 执行；先完成[入门环境](../getting_started/大纲.md)，并确认所选板及控制器支持本文所需蓝牙能力。`samples/...` 是官方已有示例目录，`<board>` 是须替换的板目标占位符；构建输出由工具生成，不在本中文目录创建同名源码。先检查构建成功及板目标，再按板文档烧录并观察本文行为或日志；构建、烧录或通信失败时，分别回查工具链／板配置、烧录器和两端角色／控制器能力。本次未构建或运行示例。

按以下方式构建并烧录，将 `<board>` 替换为目标开发板：

```text
west build -b <board> samples/bluetooth/peripheral_past
west flash
```

可在另一块开发板上运行中心设备 PAST 示例，它会连接本设备并传递周期广播同步信息。 相关链接：[中心设备周期广播同步传输（Central Periodic Advertising Sync Transfer，PAST）](P029_中心设备PAST.md#ble_central_past)。

> 译注——接收端的上游角色：此设备通过现有 LE 连接接收同步参数，完整演示还需让中心设备获得一个正在工作的周期广播源。详见[中心设备PAST](P029_中心设备PAST.md)的三角色说明；只运行传输端和接收端，不一定具备可传输的周期同步。

详情参见[蓝牙示例（Bluetooth samples）](https://docs.zephyrproject.org/latest/samples/bluetooth/bluetooth.html#bluetooth)。

<a id="see-also"></a>

## 41.4 另请参阅（See also）

[通用访问配置文件（Generic Access Profile，GAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html)

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

> 译注——实现入口：[src/main.c](../../../samples/bluetooth/peripheral_past/src/main.c)、[prj.conf](../../../samples/bluetooth/peripheral_past/prj.conf)为本仓库的相对源码入口。与本次上游快照的版本差异须分别核对，不能把译文当作本地硬件已支持的证明。

对应官方文档源码：[samples/bluetooth/peripheral_past/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/peripheral_past/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/bluetooth/peripheral_past/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或连接设备。

[上一章](P040_PAwR同步端.md) · [返回大纲](大纲.md) · [下一章](P042_体温计中心设备.md)
