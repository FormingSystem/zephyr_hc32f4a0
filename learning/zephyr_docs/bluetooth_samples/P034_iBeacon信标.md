---
id: learning.zephyr-docs.bluetooth-samples.page-34
title: iBeacon信标
kind: reference
status: maintained
domains: [zephyr, bluetooth, samples]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/ibeacon/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth_ibeacon"></a>

# 第34章\_iBeacon 信标（iBeacon）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/ibeacon/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/ibeacon/README.rst/..)

<a id="overview"></a>

## 34.1 概述（Overview）

本简单应用通过广播 Apple iBeacon，演示 GAP 广播者（Broadcaster）角色。距离一米处的校准接收信号强度指示（Received Signal Strength Indicator，RSSI）可通过构建变量 IBEACON_RSSI 设置，例如 IBEACON_RSSI=0xb8 表示一米处 -72 dBm 的 RSSI；也可手工修改 `main.c` 中的默认值。

> 译注——RSSI 参数：`IBEACON_RSSI` 是该示例 CMakeLists.txt 读取的构建变量，不是 Kconfig 符号。本次默认宏为 0xc8，即有符号八位数 -56；原文举例的 0xb8 为 -72。此字段表达一米处的校准接收强度，不是直接设置射频发射功率，也不是接收器即时测到的 RSSI。源码可从[示例 CMake](../../../samples/bluetooth/ibeacon/CMakeLists.txt)和[main.c](../../../samples/bluetooth/ibeacon/src/main.c)追踪。

iBeacon 的 UUID、major 和 minor 值被写死，因此本应用不适合直接用于生产，但很适合快速演示 iBeacon 功能。

<a id="requirements"></a>

## 34.2 前提条件（Requirements）

- 一块支持 Bluetooth LE 的开发板；或者

- QEMU，以及主机上运行的 BlueZ。

<a id="building-and-running"></a>

## 34.3 构建与运行（Building and Running）

> 译注——构建位置与前提：以下是官方示例命令，在读者自己的 Zephyr 源码根目录中，使用 UCRT64 Bash 或 Linux Bash 执行；先完成[入门环境](../getting_started/大纲.md)，并确认所选板及控制器支持本文所需蓝牙能力。`samples/...` 是官方已有示例目录，`<board>` 是须替换的板目标占位符；构建输出由工具生成，不在本中文目录创建同名源码。先检查构建成功及板目标，再按板文档烧录并观察本文行为或日志；构建、烧录或通信失败时，分别回查工具链／板配置、烧录器和两端角色／控制器能力。本次未构建或运行示例。

在 QEMU 中运行本示例的方法，参见[蓝牙示例（Bluetooth samples）](https://docs.zephyrproject.org/latest/samples/bluetooth/bluetooth.html#bluetooth)。

其他开发板可按以下方式构建并烧录应用：

```text
west build -b <board> samples/bluetooth/ibeacon
west flash
```

若开发板不支持 `flash` 目标，请查阅[该板文档](https://docs.zephyrproject.org/latest/boards/index.html#boards)中的其他烧录方法。

<a id="see-also"></a>

## 34.4 另请参阅（See also）

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

> 译注——实现入口：[src/main.c](../../../samples/bluetooth/ibeacon/src/main.c)、[prj.conf](../../../samples/bluetooth/ibeacon/prj.conf)为本仓库的相对源码入口。与本次上游快照的版本差异须分别核对，不能把译文当作本地硬件已支持的证明。

对应官方文档源码：[samples/bluetooth/ibeacon/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/ibeacon/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/bluetooth/ibeacon/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或连接设备。

[上一章](P033_扩展广播.md) · [返回大纲](大纲.md) · [下一章](P035_周期广播.md)
