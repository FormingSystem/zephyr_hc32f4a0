---
id: learning.zephyr-docs.api-source-supplement-reference.page-220
title: sysapic.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sysapic_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第220章\_sysapic.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sysapic_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sysapic_8h.html)。

## 220.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
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
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aloapic_8h_html"></a>
<a id="aloapic_8h_html_a5cc8ffe88a717189312314661d489e52"></a>
<a id="aloapic_8h_html_a884390389c9c7cef65801bba00395e4d"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_SYSAPIC_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_SYSAPIC_H_

#include <zephyr/drivers/interrupt_controller/loapic.h>

#define IRQ_TRIGGER_EDGE        IOAPIC_EDGE
#define IRQ_TRIGGER_LEVEL       IOAPIC_LEVEL

#define IRQ_POLARITY_HIGH       IOAPIC_HIGH
#define IRQ_POLARITY_LOW        IOAPIC_LOW

#ifndef _ASMLANGUAGE
#include <zephyr/types.h>

#define LOAPIC_IRQ_COUNT 6  /* Default to LOAPIC_TIMER to LOAPIC_ERROR */

void z_irq_controller_irq_config(unsigned int vector, unsigned int irq,
                                 uint32_t flags);

int z_irq_controller_isr_vector_get(void);

static inline void z_irq_controller_eoi(void)
{
        x86_write_loapic(LOAPIC_EOI, 0);
}

#endif /* _ASMLANGUAGE */

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_SYSAPIC_H_ */
```

## 220.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 21 行

默认范围从 `LOAPIC_TIMER` 到 `LOAPIC_ERROR`。

### 注释 3：原第 33 行

条件编译标记：`_ASMLANGUAGE`。

### 注释 4：原第 35 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_SYSAPIC_H_`。

## 220.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sysapic_8h.html)
- [zephyr/drivers/interrupt_controller/loapic.h](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [x86_write_loapic](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#a884390389c9c7cef65801bba00395e4d)
- [LOAPIC_EOI](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#a5cc8ffe88a717189312314661d489e52)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [loapic.h](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html)

---

[上一章](P219_sy1xx-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P221_system_mm.h_源码浏览.md)
