---
id: learning.zephyr-docs.api-source-configuration-reference.page-36
title: infineon-xmc4xxx-gpio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-xmc4xxx-gpio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_infineon-xmc4xxx-gpio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/infineon-xmc4xxx-gpio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/infineon-xmc4xxx-gpio_8h.html)。

## 36.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2022 Schlumberger
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_INFINEON_XMC4XXX_GPIO_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_INFINEON_XMC4XXX_GPIO_H_

#define XMC4XXX_GPIO_DS_POS                   9
#define XMC4XXX_GPIO_DS_MASK                  0xf

/* GPIO driver will use XMC_GPIO_OUTPUT_STRENGTH_STRONG_MEDIUM_EDGE if DS is unset */
#define XMC4XXX_GPIO_DS_STRONG_SHARP_EDGE    (0x1 << XMC4XXX_GPIO_DS_POS)
#define XMC4XXX_GPIO_DS_STRONG_MEDIUM_EDGE   (0x2 << XMC4XXX_GPIO_DS_POS)
#define XMC4XXX_GPIO_DS_STRONG_SOFT_EDGE     (0x3 << XMC4XXX_GPIO_DS_POS)
#define XMC4XXX_GPIO_DS_STRONG_SLOW_EDGE     (0x4 << XMC4XXX_GPIO_DS_POS)
#define XMC4XXX_GPIO_DS_MEDIUM               (0x5 << XMC4XXX_GPIO_DS_POS)
/* values 5, 6 not set in xmc4_gpio.h */
#define XMC4XXX_GPIO_DS_WEAK                 (0x8 << XMC4XXX_GPIO_DS_POS)

#define XMC4XXX_GPIO_GET_DS(flags)           ((flags >> XMC4XXX_GPIO_DS_POS) & XMC4XXX_GPIO_DS_MASK)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_INFINEON_XMC4XXX_GPIO_H_ */
```

## 36.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Schlumberger。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 12 行

如果未设置 DS，GPIO 驱动将使用 `XMC_GPIO_OUTPUT_STRENGTH_STRONG_MEDIUM_EDGE`。

### 注释 3：原第 18 行

`xmc4_gpio.h` 中未设置值 5、6。

### 注释 4：原第 23 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_INFINEON_XMC4XXX_GPIO_H_`。

## 36.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/infineon-xmc4xxx-gpio_8h.html)

---

[上一章](P035_settings.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P037_input_kbd_matrix.h_源码浏览.md)
