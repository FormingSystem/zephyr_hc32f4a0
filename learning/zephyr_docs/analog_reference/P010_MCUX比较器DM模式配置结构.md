---
id: learning.zephyr-docs.analog_reference.analogheader-10
title: MCUX比较器DM模式配置结构
kind: reference
status: maintained
domains: [zephyr, analog_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcomp__mcux__acmp__dm__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第10章\_MCUX比较器DM模式配置结构

原文：[structcomp__mcux__acmp__dm__config](https://docs.zephyrproject.org/latest/doxygen/html/structcomp__mcux__acmp__dm__config.html)。读取日期：2026-10-13，`latest`。

结构体`comp_mcux_acmp_dm_config`保存MCUX模拟比较器（Analog Comparator，ACMP）的离散模式（Discrete Mode，DM）配置。官方结构体页列出字段声明，未附加字段说明；下表的中文含义为依据名称补充的译注，不代表额外的默认值、取值范围或时序保证。

## 10.1\_头文件与字段

该结构体来自以下头文件，字段类型和顺序全部保留。

```c
#include <zephyr/drivers/comparator/mcux_acmp.h>
```

| 类型 | 字段 | 中文名称释义 |
| --- | --- | --- |
| `bool` | `enable_positive_channel` | 使能正通道（Enable Positive Channel）。 |
| `bool` | `enable_negative_channel` | 使能负通道（Enable Negative Channel）。 |
| `bool` | `enable_resistor_divider` | 使能电阻分压器（Enable Resistor Divider）。 |
| `enum comp_mcux_acmp_dm_clock` | `clock_source` | 时钟源（Clock Source）。 |
| `enum comp_mcux_acmp_dm_sample_time` | `sample_time` | 采样时间（Sample Time）。 |
| `enum comp_mcux_acmp_dm_phase_time` | `phase1_time` | 第一阶段时间（Phase 1 Time）。 |
| `enum comp_mcux_acmp_dm_phase_time` | `phase2_time` | 第二阶段时间（Phase 2 Time）。 |

## 10.2\_对应设置函数

以下为使用该配置结构的函数声明。

```c
int comp_mcux_acmp_set_dm_config(const struct device *dev,
                                 const struct comp_mcux_acmp_dm_config *config);
```

函数接收设备指针`dev`和只读配置指针`config`。原结构体页没有定义该函数的返回约定；声明与相关枚举见[MCUX模拟比较器扩展参考](P003_MCUX模拟比较器扩展头文件参考.md)，完整结构体定义见[源码页](P004_MCUX模拟比较器扩展头文件源码.md)。

DM的离散模式名称参照[对应设备树绑定](../hardware/P745_NXPKinetis模拟比较器绑定.md)中的`discrete-mode-*`属性。保留T系列和ALT系列选项，未把它们换算为未经原文说明的时间数值。

---

[上一章：MCUX比较器DAC配置结构](P009_MCUX比较器DAC配置结构.md) · [下一章：MCUX比较器滤波配置结构](P011_MCUX比较器滤波配置结构.md) · [返回大纲](大纲.md)
