---
id: learning.zephyr-docs.api-source-reference.page-512
title: memc_stm32.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/memc__stm32_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第512章\_memc\_stm32.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/memc__stm32_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/memc__stm32_8h.html)。

## 512.1\_原始可见代码（Source Code）

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
<a id="amemc__stm32_8h_html_a3ff474a6a2a4e6b4683adf21c8806a67"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2025 Georgij Cernysiov <geo.cgv@gmail.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_MEMC_STM32_H_
#define ZEPHYR_INCLUDE_MEMC_STM32_H_

int memc_stm32_fmc_clock_rate(uint32_t *rate);

#endif /* ZEPHYR_INCLUDE_MEMC_STM32_H_ */
```

## 512.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Georgij Cernysiov <geo.cgv@gmail.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 12 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MEMC_STM32_H_`。

## 512.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/memc__stm32_8h.html)
- [memc_stm32_fmc_clock_rate](https://docs.zephyrproject.org/latest/doxygen/html/memc__stm32_8h.html#a3ff474a6a2a4e6b4683adf21c8806a67)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

---

[上一章](P511_mcux_lpcmp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P513_memory.h_源码浏览.md)
