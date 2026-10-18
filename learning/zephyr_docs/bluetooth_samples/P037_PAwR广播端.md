---
id: learning.zephyr-docs.bluetooth-samples.page-37
title: PAwR广播端
kind: reference
status: maintained
domains: [zephyr, bluetooth, samples]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/periodic_adv_rsp/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ble_periodic_adv_rsp"></a>

# 第37章\_PAwR 广播端（Periodic Advertising with Responses Advertiser）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/periodic_adv_rsp/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/periodic_adv_rsp/README.rst/..)

<a id="overview"></a>

## 37.1 概述（Overview）

本简单应用演示 Bluetooth LE 带响应的周期广播的广播端功能。

示例会扫描相应的同步端示例，并将所需同步信息发送给它。广播数据是一个计数器，每个子事件递增一次。

多个设备可以与一个广播端同步并响应。

> 译注——配套关系：本例与[PAwR同步端](P040_PAwR同步端.md)搭配，通过普通连接上的 PAST 和 GATT 分配同步与响应时序；不要改用仅接收普通周期广播的[周期广播同步](P038_周期广播同步.md)来期待响应。

监听哪个子事件、在哪个响应时隙（Response slot）回复，由应用决定。本示例由 PAwR 广播端决定；连接时，它通过写入 GATT 特征分配子事件及响应时隙。

<a id="requirements"></a>

## 37.2 前提条件（Requirements）

- 一块支持 Bluetooth LE 的开发板。

- 支持 PAwR 广播端（Advertiser）功能的控制器。

<a id="building-and-running"></a>

## 37.3 构建与运行（Building and Running）

> 译注——构建位置与前提：以下是官方示例命令，在读者自己的 Zephyr 源码根目录中，使用 UCRT64 Bash 或 Linux Bash 执行；先完成[入门环境](../getting_started/大纲.md)，并确认所选板及控制器支持本文所需蓝牙能力。`samples/...` 是官方已有示例目录，`<board>` 是须替换的板目标占位符；构建输出由工具生成，不在本中文目录创建同名源码。先检查构建成功及板目标，再按板文档烧录并观察本文行为或日志；构建、烧录或通信失败时，分别回查工具链／板配置、烧录器和两端角色／控制器能力。本次未构建或运行示例。

按以下方式构建并烧录，将 `<board>` 替换为目标开发板：

```text
west build -b <board> samples/bluetooth/periodic_adv_rsp
west flash
```

烧录后，设备开始 PAwR 广播，并扫描可连接的同步设备。发现同步设备后，与之连接，通过 PAST 传递同步信息，再写入 GATT 特征分配子事件和响应时隙，随后断开。之后，它会在各同步设备获分配的响应时隙内接收回送数据。

在一块或多块额外开发板上运行 PAwR 同步（Periodic Advertising with Responses Synchronization）示例，与本设备同步并响应。 相关链接：[PAwR 同步端（Periodic Advertising with Responses Synchronization）](P040_PAwR同步端.md#ble_periodic_adv_sync_rsp)。

<a id="see-also"></a>

## 37.4 另请参阅（See also）

[通用访问配置文件（Generic Access Profile，GAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html)

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

> 译注——实现入口：[src/main.c](../../../samples/bluetooth/periodic_adv_rsp/src/main.c)、[prj.conf](../../../samples/bluetooth/periodic_adv_rsp/prj.conf)为本仓库的相对源码入口。与本次上游快照的版本差异须分别核对，不能把译文当作本地硬件已支持的证明。

对应官方文档源码：[samples/bluetooth/periodic_adv_rsp/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/periodic_adv_rsp/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/bluetooth/periodic_adv_rsp/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或连接设备。

[上一章](P036_周期广播连接发起端.md) · [返回大纲](大纲.md) · [下一章](P038_周期广播同步.md)
