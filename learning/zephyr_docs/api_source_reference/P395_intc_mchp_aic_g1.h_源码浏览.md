---
id: learning.zephyr-docs.api-source-reference.page-395
title: intc_mchp_aic_g1.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__aic__g1_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第395章\_intc\_mchp\_aic\_g1.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__aic__g1_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__aic__g1_8h.html)。

## 395.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>

```c
/*
 * Copyright (C) 2025-2026 Microchip Technology Inc. and its subsidiaries
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_MCHP_AIC_G1_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_MCHP_AIC_G1_H_

unsigned int z_aic_irq_get_active(void);

void z_aic_irq_eoi(unsigned int irq);

void z_aic_irq_init(void);

void z_aic_irq_priority_set(unsigned int irq, unsigned int prio, unsigned int flags);

void z_aic_irq_enable(unsigned int irq);

void z_aic_irq_disable(unsigned int irq);

int z_aic_irq_is_enabled(unsigned int irq);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_MCHP_AIC_G1_H_ */
```

## 395.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：(C) 2025-2026 Microchip Technology Inc. and its subsidiaries。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 67 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_MCHP_AIC_G1_H_`。

## 395.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__aic__g1_8h.html)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

---

[上一章](P394_intc_max32_rv32.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P396_intc_mchp_eic_g1.h_源码浏览.md)
