---
id: learning.zephyr-docs.power.pmsamples-3
title: Nordic系统关闭示例
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nordic/system_off/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="nrf_system_off"></a>

# 第51章\_Nordic系统关闭示例

原文：[System Off](https://docs.zephyrproject.org/latest/samples/boards/nordic/system_off/README.html)。读取日期：2026-10-13，`latest`。

## 51.1\_概述

本示例用于基本功耗测量，并演示 Nordic 平台上的深度睡眠（Deep Sleep）。

## 51.2\_内存保持

示例也可以演示随机存取存储器保持（RAM Retention，RAM 为 Random Access Memory）。启用 Kconfig 配置 `CONFIG_APP_USE_RETAINED_MEM=y` 后，将启动次数、进入系统关闭（System Off）的次数，以及自首次上电以来的总运行时间保存在带校验和（Checksum）的数据结构中。

RAM 配置为在系统关闭模式下继续向包含该结构的内存区段供电。

## 51.3\_要求

演示使用 nRF51 DK、nRF52 DK 或 nRF54L15 DK 开发板。

## 51.4\_示例输出

以下为 nRF52 核心的原始输出，其中OS表示操作系统（Operating System）：

```text
*** Booting Zephyr OS build v2.3.0-rc1-204-g5f2eb85f728d  ***

nrf52dk system off demo
Entering system off; press sw0 to restart
```

## 51.5\_另请参阅

[系统关机接口](P063_系统关机接口.md)与[设备电源管理接口](P036_设备电源管理接口.md)。

---

[上一章：电源策略延迟示例](P050_电源策略延迟示例.md) · [下一章：NXP_MCX挂起到RAM示例](P052_NXP_MCX挂起到RAM示例.md) · [返回大纲](大纲.md)
