---
id: learning.zephyr-docs.api-source-supplement-reference.page-95
title: intc_infineon_aurix.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第95章\_intc\_infineon\_aurix.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h.html)。

## 95.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="adevice_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aintc__infineon__aurix_8h_html_a0b02c47eb40443d9cceec818a1b7bb93"></a>
<a id="aintc__infineon__aurix_8h_html_a1d7882c67c41d5106e60c9ac2d34da59"></a>
<a id="aintc__infineon__aurix_8h_html_a3ba347e14b314f2afdfb87deddf79d1d"></a>
<a id="aintc__infineon__aurix_8h_html_a431de8a889dcd8691221a2ec3f7cda89"></a>
<a id="aintc__infineon__aurix_8h_html_a50e9bab548376d645b0a6f72e84a29a1"></a>
<a id="aintc__infineon__aurix_8h_html_a6c512b4b26dfda0b434b10332f6b5373"></a>
<a id="aintc__infineon__aurix_8h_html_a6e85af7d5a690b0470ba750359ec008c"></a>
<a id="aintc__infineon__aurix_8h_html_ac58092370a3f7087417edc786a804b60"></a>
<a id="aintc__infineon__aurix_8h_html_afd28b85ed701604b62abba1f7b6839cf"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2024 Infineon Technologies AG,
 * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
 * SPDX-FileCopyrightText: Copyright (c) 2026 Linumiz
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_DRIVERS_INTERRUPT_CONTROLLER_INTC_AURIX_IR_H_
#define ZEPHYR_DRIVERS_INTERRUPT_CONTROLLER_INTC_AURIX_IR_H_

#define IR_BASE DT_REG_ADDR_BY_IDX(DT_INST(0, infineon_aurix_ir), 0)

#define SRC_BASE DT_REG_ADDR_BY_IDX(DT_INST(0, infineon_aurix_ir), 1)

#ifndef _ASMLANGUAGE

#include <zephyr/types.h>
#include <zephyr/device.h>

void intc_aurix_ir_irq_config(unsigned int irq, unsigned int priority, unsigned int flags);

void intc_aurix_ir_irq_enable(unsigned int irq);

void intc_aurix_ir_irq_disable(unsigned int irq);

bool intc_aurix_ir_irq_is_enabled(unsigned int irq);

bool intc_aurix_ir_irq_is_pending(unsigned int irq);

void intc_aurix_ir_irq_clear_pending(unsigned int irq);

void intc_aurix_ir_irq_raise(unsigned int irq);

unsigned int intc_aurix_ir_get_active(void);

void intc_aurix_ir_src_raise(uintptr_t src);

#endif /* !_ASMLANGUAGE */

#endif /* ZEPHYR_DRIVERS_INTERRUPT_CONTROLLER_INTC_AURIX_IR_H_ */
```

## 95.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2024 Infineon Technologies AG,。

SPDX 文件版权声明（FileCopyrightText）：or an affiliate of Infineon Technologies AG. All rights reserved.。

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Linumiz。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 131 行

条件编译表达式：`!_ASMLANGUAGE`。

### 注释 3：原第 133 行

头文件保护宏（Header guard）标记：`ZEPHYR_DRIVERS_INTERRUPT_CONTROLLER_INTC_AURIX_IR_H_`。

## 95.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [intc_aurix_ir_irq_config](https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h.html#a3ba347e14b314f2afdfb87deddf79d1d)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [intc_aurix_ir_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h.html#a1d7882c67c41d5106e60c9ac2d34da59)
- [intc_aurix_ir_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h.html#afd28b85ed701604b62abba1f7b6839cf)
- [intc_aurix_ir_irq_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h.html#a50e9bab548376d645b0a6f72e84a29a1)
- [intc_aurix_ir_irq_is_pending](https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h.html#ac58092370a3f7087417edc786a804b60)
- [intc_aurix_ir_irq_clear_pending](https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h.html#a6e85af7d5a690b0470ba750359ec008c)
- [intc_aurix_ir_irq_raise](https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h.html#a431de8a889dcd8691221a2ec3f7cda89)
- [intc_aurix_ir_get_active](https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h.html#a6c512b4b26dfda0b434b10332f6b5373)
- [intc_aurix_ir_src_raise](https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h.html#a0b02c47eb40443d9cceec818a1b7bb93)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)

---

[上一章](P094_types.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P096_intel_socfpga_clock.h_源码浏览.md)
