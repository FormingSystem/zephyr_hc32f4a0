---
id: learning.zephyr-docs.analog_reference.analogheader-12
title: MCUX比较器输入配置结构
kind: reference
status: maintained
domains: [zephyr, analog_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcomp__mcux__acmp__input__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第12章\_MCUX比较器输入配置结构

原文：[structcomp__mcux__acmp__input__config](https://docs.zephyrproject.org/latest/doxygen/html/structcomp__mcux__acmp__input__config.html)。读取日期：2026-10-13，`latest`。

结构体`comp_mcux_acmp_input_config`保存MCUX模拟比较器（Analog Comparator，ACMP）的输入选择（Input Selection）配置。官方结构体页列出字段声明，未附加字段说明；下表的中文含义为依据名称补充的译注，不代表额外的默认值、取值范围或时序保证。

## 12.1\_头文件与字段

该结构体来自以下头文件，字段类型和顺序全部保留。

```c
#include <zephyr/drivers/comparator/mcux_acmp.h>
```

| 类型 | 字段 | 中文名称释义 |
| --- | --- | --- |
| `enum comp_mcux_acmp_mux_input` | `positive_mux_input` | 正端多路复用器输入（Positive Multiplexer Input）。 |
| `enum comp_mcux_acmp_mux_input` | `negative_mux_input` | 负端多路复用器输入（Negative Multiplexer Input）。 |
| `enum comp_mcux_acmp_port_input` | `positive_port_input` | 正端口输入（Positive Port Input）。 |
| `enum comp_mcux_acmp_port_input` | `negative_port_input` | 负端口输入（Negative Port Input）。 |

## 12.2\_对应设置函数

以下为使用该配置结构的函数声明。

```c
int comp_mcux_acmp_set_input_config(const struct device *dev,
                                    const struct comp_mcux_acmp_input_config *config);
```

函数接收设备指针`dev`和只读配置指针`config`。原结构体页没有定义该函数的返回约定；声明与相关枚举见[MCUX模拟比较器扩展参考](P003_MCUX模拟比较器扩展头文件参考.md)，完整结构体定义见[源码页](P004_MCUX模拟比较器扩展头文件源码.md)。

---

[上一章：MCUX比较器滤波配置结构](P011_MCUX比较器滤波配置结构.md) · [下一章：MCUX比较器工作模式配置结构](P013_MCUX比较器工作模式配置结构.md) · [返回大纲](大纲.md)
