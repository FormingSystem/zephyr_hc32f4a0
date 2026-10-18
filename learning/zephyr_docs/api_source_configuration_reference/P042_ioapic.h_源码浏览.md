---
id: learning.zephyr-docs.api-source-configuration-reference.page-42
title: ioapic.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ioapic_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_ioapic.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ioapic_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ioapic_8h.html)。

## 42.1\_原始可见代码（Source Code）

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
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/* ioapic.h - public IOAPIC APIs */

/*
 * Copyright (c) 2012-2015 Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_IOAPIC_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_IOAPIC_H_

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Redirection table entry bits: lower 32 bit
 * Used as flags argument in ioapic_irq_set
 */

#define IOAPIC_INT_MASK 0x00010000
#define IOAPIC_TRIGGER_MASK 0x00008000
#define IOAPIC_LEVEL 0x00008000
#define IOAPIC_EDGE 0x00000000
#define IOAPIC_REMOTE 0x00004000
#define IOAPIC_POLARITY_MASK 0x00002000
#define IOAPIC_LOW 0x00002000
#define IOAPIC_HIGH 0x00000000
#define IOAPIC_LOGICAL 0x00000800
#define IOAPIC_PHYSICAL 0x00000000
#define IOAPIC_DELIVERY_MODE_MASK 0x00000700
#define IOAPIC_FIXED 0x00000000
#define IOAPIC_LOWEST 0x00000100
#define IOAPIC_SMI 0x00000200
#define IOAPIC_NMI 0x00000400
#define IOAPIC_INIT 0x00000500
#define IOAPIC_EXTINT 0x00000700

#ifndef _ASMLANGUAGE
uint32_t z_ioapic_num_rtes(void);
void z_ioapic_irq_enable(unsigned int irq);
void z_ioapic_irq_disable(unsigned int irq);
void z_ioapic_int_vec_set(unsigned int irq, unsigned int vector);
void z_ioapic_irq_set(unsigned int irq, unsigned int vector, uint32_t flags);
#endif /* _ASMLANGUAGE */

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_IOAPIC_H_ */
```

## 42.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`ioapic.h`：公共 I/O 高级可编程中断控制器（IOAPIC）API。

### 注释 2：原第 3 行

版权（Copyright）：© 2012-2015 Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 16 行

重定向表项（Redirection table entry）的低 32 位，作为 `ioapic_irq_set` 的 `flags` 参数使用。

### 注释 4：原第 45 行

条件编译标记：`_ASMLANGUAGE`。

### 注释 5：原第 51 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_IOAPIC_H_`。

## 42.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ioapic_8h.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

---

[上一章](P041_intel_socfpga_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P043_it51xxx_pwm.h_源码浏览.md)
