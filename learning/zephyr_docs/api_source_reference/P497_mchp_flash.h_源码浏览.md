---
id: learning.zephyr-docs.api-source-reference.page-497
title: mchp_flash.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__flash_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第497章\_mchp\_flash.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__flash_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__flash_8h.html)。

## 497.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="amchp__nvmctrl__g1_8h_html"></a>
<a id="amchp__nvmctrl__g2_8h_html"></a>
<a id="amchp__nvmctrl__g3_8h_html"></a>

```c
/*
 * Copyright (c) 2025-2026 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FLASH_MCHP_FLASH_H_
#define ZEPHYR_INCLUDE_DRIVERS_FLASH_MCHP_FLASH_H_

#ifdef CONFIG_FLASH_MCHP_NVMCTRL_G1
#include "mchp_nvmctrl_g1.h"
#endif /* CONFIG_FLASH_MCHP_NVMCTRL_G1 */
#ifdef CONFIG_FLASH_MCHP_NVMCTRL_G2
#include "mchp_nvmctrl_g2.h"
#endif /* CONFIG_FLASH_MCHP_NVMCTRL_G2 */
#ifdef CONFIG_FLASH_MCHP_NVMCTRL_G3
#include "mchp_nvmctrl_g3.h"
#endif /* CONFIG_FLASH_MCHP_NVMCTRL_G3 */

#endif /* ZEPHYR_INCLUDE_DRIVERS_FLASH_MCHP_FLASH_H_ */
```

## 497.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025-2026 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 25 行

条件编译配置（Configuration）标记：`CONFIG_FLASH_MCHP_NVMCTRL_G1`。

### 注释 3：原第 28 行

条件编译配置（Configuration）标记：`CONFIG_FLASH_MCHP_NVMCTRL_G2`。

### 注释 4：原第 31 行

条件编译配置（Configuration）标记：`CONFIG_FLASH_MCHP_NVMCTRL_G3`。

### 注释 5：原第 33 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FLASH_MCHP_FLASH_H_`。

## 497.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__flash_8h.html)
- [mchp_nvmctrl_g1.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g1_8h.html)
- [mchp_nvmctrl_g2.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g2_8h.html)
- [mchp_nvmctrl_g3.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g3_8h.html)

---

[上一章](P496_mchp_clock_sam_d5x_e5x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P498_mchp_nvmctrl_g1.h_源码浏览.md)
