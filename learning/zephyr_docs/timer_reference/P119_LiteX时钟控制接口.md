---
id: learning.zephyr-docs.timer_reference.litexclock-119
title: LiteX时钟控制接口
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__litex.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第119章\_LiteX时钟控制接口

原文：[group__clock__control__litex](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__litex.html)。读取日期：2026-10-13，`latest`。

本页提供 LiteX 混合模式时钟管理器（Mixed Mode Clock Manager，MMCM）时钟发生器（Clock Generator）的时钟控制辅助定义（Clock Control Helpers）。

## 119.1\_头文件与数据结构

使用以下头文件：

```c
#include <zephyr/drivers/clock_control/clock_control_litex.h>
```

头文件参考见[`clock_control_litex.h`](P121_LiteX时钟控制头文件参考.md)。结构体[`litex_clk_setup`](P120_LiteX时钟设置结构.md)描述单个 MMCM 时钟输出的配置。

## 119.2\_MMCM节点宏

宏`MMCM`表示 LiteX MMCM 时钟发生器的设备树节点标识符（Devicetree Node Identifier）。

```c
#define MMCM DT_NODELABEL(clock0)
```

其中[`DT_NODELABEL`](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)通过节点标签（Node Label）取得节点标识符；本宏选用标签`clock0`。

## 119.3\_NCLKOUT输出数量宏

宏`NCLKOUT`给出 MMCM 提供的时钟输出数量（Number of Clock Outputs）。

```c
#define NCLKOUT DT_PROP_LEN(MMCM, clock_output_names)
```

[`DT_PROP_LEN`](../dt_property_reference/P001_设备树属性读取宏.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)取得属性长度，此处读取`MMCM`节点的`clock_output_names`属性标识。设备树源码中对应的属性拼写为`clock-output-names`。

---

[上一章：MicrochipXEC时钟控制示例](P118_MicrochipXEC时钟控制示例.md) · [下一章：LiteX时钟设置结构](P120_LiteX时钟设置结构.md) · [返回大纲](大纲.md)
