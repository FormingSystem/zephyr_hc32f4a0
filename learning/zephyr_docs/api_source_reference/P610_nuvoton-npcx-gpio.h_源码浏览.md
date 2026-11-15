---
id: learning.zephyr-docs.api-source-reference.page-610
title: nuvoton-npcx-gpio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nuvoton-npcx-gpio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第610章\_nuvoton-npcx-gpio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nuvoton-npcx-gpio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nuvoton-npcx-gpio_8h.html)。

## 610.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00017"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>

```c
/*
 * Copyright (c) 2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_NUVOTON_NPCX_GPIO_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_NUVOTON_NPCX_GPIO_H_


#define NPCX_GPIO_VOLTAGE_POS   11
#define NPCX_GPIO_VOLTAGE_MASK  (1U << NPCX_GPIO_VOLTAGE_POS)

#define NPCX_GPIO_VOLTAGE_DEFAULT       (0U << NPCX_GPIO_VOLTAGE_POS)
#define NPCX_GPIO_VOLTAGE_1P8           (1U << NPCX_GPIO_VOLTAGE_POS)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_NUVOTON_NPCX_GPIO_H_ */
```

## 610.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 30 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_NUVOTON_NPCX_GPIO_H_`。

## 610.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nuvoton-npcx-gpio_8h.html)

---

[上一章](P609_nus.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P611_nxp-imx-igpio.h_源码浏览.md)
