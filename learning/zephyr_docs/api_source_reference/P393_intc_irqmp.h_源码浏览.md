---
id: learning.zephyr-docs.api-source-reference.page-393
title: intc_irqmp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__irqmp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第393章\_intc\_irqmp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__irqmp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__irqmp_8h.html)。

## 393.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="aintc__irqmp_8h_html_a6075fec44da0b8a67d90dd61477a8c3b"></a>
<a id="aintc__irqmp_8h_html_a612b61d005749401a85ace84d5052d37"></a>
<a id="aintc__irqmp_8h_html_af4d923ff11d417610c0d786784ef092b"></a>
<a id="aintc__irqmp_8h_html_af8642128f51648d5023d558f9762eafc"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_IRQMP_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_IRQMP_H_

void intc_irqmp_irq_enable(unsigned int source);

void intc_irqmp_irq_disable(unsigned int source);

int intc_irqmp_irq_is_enabled(unsigned int source);

int intc_irqmp_get_source(int irl);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_IRQMP_H_ */
```

## 393.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 49 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_IRQMP_H_`。

## 393.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__irqmp_8h.html)
- [intc_irqmp_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/intc__irqmp_8h.html#af4d923ff11d417610c0d786784ef092b)
- [intc_irqmp_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/intc__irqmp_8h.html#a6075fec44da0b8a67d90dd61477a8c3b)
- [intc_irqmp_irq_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/intc__irqmp_8h.html#af8642128f51648d5023d558f9762eafc)
- [intc_irqmp_get_source](https://docs.zephyrproject.org/latest/doxygen/html/intc__irqmp_8h.html#a612b61d005749401a85ace84d5052d37)

---

[上一章](P392_intc_bcm283x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P394_intc_max32_rv32.h_源码浏览.md)
