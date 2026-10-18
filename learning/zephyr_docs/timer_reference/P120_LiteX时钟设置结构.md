---
id: learning.zephyr-docs.timer_reference.litexclock-120
title: LiteX时钟设置结构
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlitex__clk__setup.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第120章\_LiteX时钟设置结构

原文：[structlitex__clk__setup](https://docs.zephyrproject.org/latest/doxygen/html/structlitex__clk__setup.html)。读取日期：2026-10-13，`latest`。

结构体`litex_clk_setup`描述单个混合模式时钟管理器（Mixed Mode Clock Manager，MMCM）时钟输出的配置（Configuration）。

## 120.1\_声明位置

```c
#include <zephyr/drivers/clock_control/clock_control_litex.h>
```

本结构体文档由`zephyr/drivers/clock_control/clock_control_litex.h`生成；可查阅[完整可见源码](P122_LiteX时钟控制完整头文件.md)。

## 120.2\_成员字段

下表按原页数据字段（Data Fields）列表的顺序列出全部四项：

| 成员 | C类型 | 中文说明 |
| --- | --- | --- |
| `clkout_nr` | `uint8_t` | 待配置的时钟输出索引（Clock Output Index） |
| `rate` | `uint32_t` | 要设置的频率（Frequency），单位为赫兹（Hertz，Hz） |
| `phase` | `uint16_t` | 相位偏移（Phase Offset），单位为度（Degree） |
| `duty` | `uint8_t` | 时钟信号的占空比（Duty Cycle），以百分数表示 |

`uint8_t`、`uint16_t`和`uint32_t`分别为8位、16位和32位无符号整数类型（Unsigned Integer Type）。原页逐成员说明采用`clkout_nr`、`duty`、`phase`、`rate`的显示顺序，其说明与表中一致。

原页没有额外规定这些字段的有效范围、默认值或错误处理方式。整数类型的可表示范围不能直接当作硬件允许的参数范围。

---

[上一章：LiteX时钟控制接口](P119_LiteX时钟控制接口.md) · [下一章：LiteX时钟控制头文件参考](P121_LiteX时钟控制头文件参考.md) · [返回大纲](大纲.md)
