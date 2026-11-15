---
id: learning.zephyr-docs.api-source-network-reference.page-19
title: stm32-pinctrl-common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32-pinctrl-common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_stm32-pinctrl-common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32-pinctrl-common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_configuration_reference/P071_zephyr__dt-bindings__pinctrl__stm32-pinctrl-common.h_文件参考.md)。

## 19.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>

```c
/*
 * Copyright (c) 2017 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_STM32_PINCTRL_COMMON_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_STM32_PINCTRL_COMMON_H_


#define STM32_PORTA 0   /* IO port A */
#define STM32_PORTB 1   /* .. */
#define STM32_PORTC 2
#define STM32_PORTD 3
#define STM32_PORTE 4
#define STM32_PORTF 5
#define STM32_PORTG 6
#define STM32_PORTH 7
#define STM32_PORTI 8
#define STM32_PORTJ 9
#define STM32_PORTK 10  /* IO port K */
#define STM32_PORTM 12  /* IO port M (0xC) */
#define STM32_PORTN 13
#define STM32_PORTO 14
#define STM32_PORTP 15  /* IO port P (0xF) */
#define STM32_PORTQ 16  /* IO port Q (0x10) */
#define STM32_PORTZ 25  /* IO port Z (0x19) */

#ifndef STM32_PORTS_MAX
#define STM32_PORTS_MAX (STM32_PORTZ + 1)
#endif

#define STM32PIN(_port, _pin) \
        (_port << 4 | _pin)

#endif  /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_STM32_PINCTRL_COMMON_H_ */
```

## 19.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 14 行

输入/输出端口（I/O port）A。

### 注释 3：原第 15 行

省略号。

### 注释 4：原第 24 行

输入/输出端口（I/O port）K。

### 注释 5：原第 25 行

输入/输出端口（I/O port）M（`0xC`）。

### 注释 6：原第 28 行

输入/输出端口（I/O port）P（`0xF`）。

### 注释 7：原第 29 行

输入/输出端口（I/O port）Q（`0x10`）。

### 注释 8：原第 30 行

输入/输出端口（I/O port）Z（`0x19`）。

### 注释 9：原第 42 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_STM32_PINCTRL_COMMON_H_`。

## 19.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_configuration_reference/P071_zephyr__dt-bindings__pinctrl__stm32-pinctrl-common.h_文件参考.md)

---

[上一章](P018_rts5912_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P020_stm32h7_clock.h_源码浏览.md)
