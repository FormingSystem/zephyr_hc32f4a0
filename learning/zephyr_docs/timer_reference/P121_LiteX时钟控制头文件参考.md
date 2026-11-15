---
id: learning.zephyr-docs.timer_reference.litexclock-121
title: LiteX时钟控制头文件参考
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__litex_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第121章\_LiteX时钟控制头文件参考

原文：[clock__control__litex_8h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__litex_8h.html)。读取日期：2026-10-13，`latest`。

头文件`zephyr/drivers/clock_control/clock_control_litex.h`提供 LiteX 混合模式时钟管理器（Mixed Mode Clock Manager，MMCM）时钟发生器的时钟控制辅助定义（Clock Control Helpers）。

## 121.1\_依赖与源码

文件包含 Zephyr 类型定义头文件[`zephyr/types.h`](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)：

```c
#include <zephyr/types.h>
```

[查看本文件的完整可见源码](P122_LiteX时钟控制完整头文件.md)。

## 121.2\_数据结构

结构体[`litex_clk_setup`](P120_LiteX时钟设置结构.md)用于配置单个 MMCM 时钟输出（Clock Output）。

## 121.3\_宏定义

| 宏 | 原始展开 | 含义 |
| --- | --- | --- |
| `MMCM` | `DT_NODELABEL(clock0)` | LiteX MMCM 时钟发生器的设备树节点标识符（Devicetree Node Identifier） |
| `NCLKOUT` | `DT_PROP_LEN(MMCM, clock_output_names)` | MMCM 提供的时钟输出数量（Number of Clock Outputs） |

节点查找宏`DT_NODELABEL`使用标签`clock0`；属性长度宏`DT_PROP_LEN`读取`clock_output_names`。逐项说明及设备树辅助宏参考见[LiteX时钟控制接口](P119_LiteX时钟控制接口.md)。

---

[上一章：LiteX时钟设置结构](P120_LiteX时钟设置结构.md) · [下一章：LiteX时钟控制完整头文件](P122_LiteX时钟控制完整头文件.md) · [返回大纲](大纲.md)
