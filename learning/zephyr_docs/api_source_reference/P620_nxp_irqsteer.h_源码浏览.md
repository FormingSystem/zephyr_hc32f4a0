---
id: learning.zephyr-docs.api-source-reference.page-620
title: nxp_irqsteer.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__irqsteer_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第620章\_nxp\_irqsteer.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nxp__irqsteer_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nxp__irqsteer_8h.html)。

## 620.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="anxp__irqsteer_8h_html_a4fda601d90bcf144c9671f0ef23db22a"></a>
<a id="anxp__irqsteer_8h_html_a804052418d11f36a4070ea82be29d9cc"></a>
<a id="anxp__irqsteer_8h_html_a965f25329c0731f6932eeee7d3ee292c"></a>
<a id="anxp__irqsteer_8h_html_a9906ded93b7efe994d60b3b66c443352"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_NXP_IRQSTEER_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_NXP_IRQSTEER_H_

#include <zephyr/types.h>

void nxp_irqstr_irq_enable(uint32_t irq);

void nxp_irqstr_irq_disable(uint32_t irq);

int nxp_irqstr_irq_is_enabled(unsigned int irq);

void nxp_irqstr_irq_priority_set(unsigned int irq, unsigned int prio, unsigned int flags);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_NXP_IRQSTEER_H_ */
```

## 620.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 48 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_NXP_IRQSTEER_H_`。

## 620.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nxp__irqsteer_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [nxp_irqstr_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/nxp__irqsteer_8h.html#a804052418d11f36a4070ea82be29d9cc)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [nxp_irqstr_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/nxp__irqsteer_8h.html#a965f25329c0731f6932eeee7d3ee292c)
- [nxp_irqstr_irq_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/nxp__irqsteer_8h.html#a4fda601d90bcf144c9671f0ef23db22a)
- [nxp_irqstr_irq_priority_set](https://docs.zephyrproject.org/latest/doxygen/html/nxp__irqsteer_8h.html#a9906ded93b7efe994d60b3b66c443352)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)

---

[上一章](P619_nxp_flexio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P621_nxp_lp_flexcomm.h_源码浏览.md)
