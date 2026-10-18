---
id: learning.zephyr-docs.api-source-reference.page-403
title: intc_thejas32.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__thejas32_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第403章\_intc\_thejas32.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__thejas32_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__thejas32_8h.html)。

## 403.1\_原始可见代码（Source Code）

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
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="aintc__thejas32_8h_html_a0a4623b59f2f106493c9046da20f7799"></a>
<a id="aintc__thejas32_8h_html_a21f7b9f44b60ee4b83afa3cb7c03ce1e"></a>
<a id="aintc__thejas32_8h_html_ae81206dbe469ac478fb89330e4a2cb05"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2026 Anuj Deshpande
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_THEJAS32_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_THEJAS32_H_

#include <stdint.h>

void thejas32_intc_irq_enable(uint32_t irq);

void thejas32_intc_irq_disable(uint32_t irq);

int thejas32_intc_irq_is_enabled(uint32_t irq);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_THEJAS32_H_ */
```

## 403.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Anuj Deshpande。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 39 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_THEJAS32_H_`。

## 403.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__thejas32_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [thejas32_intc_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/intc__thejas32_8h.html#a21f7b9f44b60ee4b83afa3cb7c03ce1e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [thejas32_intc_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/intc__thejas32_8h.html#ae81206dbe469ac478fb89330e4a2cb05)
- [thejas32_intc_irq_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/intc__thejas32_8h.html#a0a4623b59f2f106493c9046da20f7799)

---

[上一章](P402_intc_rz_tint.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P404_intc_wkpu_nxp_s32.h_源码浏览.md)
