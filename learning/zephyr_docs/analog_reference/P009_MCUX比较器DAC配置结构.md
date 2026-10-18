---
id: learning.zephyr-docs.analog_reference.analogheader-9
title: MCUX比较器DAC配置结构
kind: reference
status: maintained
domains: [zephyr, analog_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcomp__mcux__acmp__dac__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第9章\_MCUX比较器DAC配置结构

原文：[structcomp__mcux__acmp__dac__config](https://docs.zephyrproject.org/latest/doxygen/html/structcomp__mcux__acmp__dac__config.html)。读取日期：2026-10-13，`latest`。

结构体`comp_mcux_acmp_dac_config`保存MCUX模拟比较器（Analog Comparator，ACMP）的数模转换器（Digital-to-Analog Converter，DAC）配置。官方结构体页列出字段声明，未附加字段说明；下表的中文含义为依据名称补充的译注，不代表额外的默认值、取值范围或时序保证。

## 9.1\_头文件与字段

该结构体来自以下头文件，字段类型和顺序全部保留。

```c
#include <zephyr/drivers/comparator/mcux_acmp.h>
```

| 类型 | 字段 | 中文名称释义 |
| --- | --- | --- |
| `enum comp_mcux_acmp_dac_vref_source` | `vref_source` | 参考电压源（Reference Voltage Source）。 |
| `uint8_t` | `value` | DAC设置值（Value）。原页未给出位宽内的有效范围或换算公式。 |
| `bool` | `enable_output` | 使能输出（Enable Output）。 |
| `bool` | `enable_high_speed_mode` | 使能高速模式（Enable High-Speed Mode）。 |

## 9.2\_对应设置函数

以下为使用该配置结构的函数声明。

```c
int comp_mcux_acmp_set_dac_config(const struct device *dev,
                                  const struct comp_mcux_acmp_dac_config *config);
```

函数接收设备指针`dev`和只读配置指针`config`。原结构体页没有定义该函数的返回约定；声明与相关枚举见[MCUX模拟比较器扩展参考](P003_MCUX模拟比较器扩展头文件参考.md)，完整结构体定义见[源码页](P004_MCUX模拟比较器扩展头文件源码.md)。

---

[上一章：运算放大器公共头文件源码](P008_运算放大器公共头文件源码.md) · [下一章：MCUX比较器DM模式配置结构](P010_MCUX比较器DM模式配置结构.md) · [返回大纲](大纲.md)
