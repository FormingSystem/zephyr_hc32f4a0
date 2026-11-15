---
id: learning.zephyr-docs.api-source-reference.page-718
title: riscv_clic.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/riscv__clic_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第718章\_riscv\_clic.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/riscv__clic_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/riscv__clic_8h.html)。

## 718.1\_原始可见代码（Source Code）

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
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="ariscv__clic_8h_html_a58034939d55cac9197e0494ef40f0276"></a>
<a id="ariscv__clic_8h_html_a97a6fb5c16f1542d7c3010212a5efa05"></a>
<a id="ariscv__clic_8h_html_aabf4e38a154115fb4ee112b0c04af71f"></a>
<a id="ariscv__clic_8h_html_ac46870266793fabffd76b29c06834b35"></a>
<a id="ariscv__clic_8h_html_aefcfc1008aba2e0f98f24b26113b776e"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2022 Carlo Caione <ccaione@baylibre.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_RISCV_CLIC_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_RISCV_CLIC_H_

void riscv_clic_irq_enable(uint32_t irq);

void riscv_clic_irq_disable(uint32_t irq);

int riscv_clic_irq_is_enabled(uint32_t irq);

void riscv_clic_irq_priority_set(uint32_t irq, uint32_t prio, uint32_t flags);

void riscv_clic_irq_vector_set(uint32_t irq);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_RISCV_CLIC_H_ */
```

## 718.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Carlo Caione <ccaione@baylibre.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 53 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_RISCV_CLIC_H_`。

## 718.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/riscv__clic_8h.html)
- [riscv_clic_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/riscv__clic_8h.html#a97a6fb5c16f1542d7c3010212a5efa05)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [riscv_clic_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/riscv__clic_8h.html#ac46870266793fabffd76b29c06834b35)
- [riscv_clic_irq_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/riscv__clic_8h.html#aabf4e38a154115fb4ee112b0c04af71f)
- [riscv_clic_irq_priority_set](https://docs.zephyrproject.org/latest/doxygen/html/riscv__clic_8h.html#a58034939d55cac9197e0494ef40f0276)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [riscv_clic_irq_vector_set](https://docs.zephyrproject.org/latest/doxygen/html/riscv__clic_8h.html#aefcfc1008aba2e0f98f24b26113b776e)

---

[上一章](P717_riscv_aplic_direct.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P719_riscv_plic.h_源码浏览.md)
