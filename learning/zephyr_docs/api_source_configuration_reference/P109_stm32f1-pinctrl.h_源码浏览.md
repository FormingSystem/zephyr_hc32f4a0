---
id: learning.zephyr-docs.api-source-configuration-reference.page-109
title: stm32f1-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32f1-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第109章\_stm32f1-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32f1-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32f1-pinctrl_8h.html)。

## 109.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
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
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="astm32-pinctrl-common_8h_html"></a>
<a id="astm32f1-afio_8h_html"></a>

```c
/*
 * Copyright (c) 2017 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_STM32F1_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_STM32F1_PINCTRL_H_

#include <zephyr/dt-bindings/pinctrl/stm32-pinctrl-common.h>
#include <zephyr/dt-bindings/pinctrl/stm32f1-afio.h>



#define STM32_MODE_SHIFT  0U
#define STM32_MODE_MASK   0x3U
#define STM32_LINE_SHIFT  2U
#define STM32_LINE_MASK   0xFU
#define STM32_PORT_SHIFT  6U
#define STM32_PORT_MASK   0xFU
#define STM32_REMAP_SHIFT 10U
#define STM32_REMAP_MASK  0x3FFU

#define STM32F1_PINMUX(port, line, mode, remap)                                \
                (((((port) - 'A') & STM32_PORT_MASK) << STM32_PORT_SHIFT) |    \
                (((line) & STM32_LINE_MASK) << STM32_LINE_SHIFT) |             \
                (((mode) & STM32_MODE_MASK) << STM32_MODE_SHIFT) |             \
                (((remap) & STM32_REMAP_MASK) << STM32_REMAP_SHIFT))


#define ALTERNATE       0x0  /* Alternate function output */
#define GPIO_IN         0x1  /* Input */
#define ANALOG          0x2  /* Analog */
#define GPIO_OUT        0x3  /* Output */

#endif  /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_STM32F1_PINCTRL_H_ */
```

## 109.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 61 行

复用功能输出（Alternate function output）。

### 注释 3：原第 62 行

`input`（输入）。

### 注释 4：原第 63 行

模拟模式（Analog）。

### 注释 5：原第 64 行

`output`（输出）。

### 注释 6：原第 66 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_STM32F1_PINCTRL_H_`。

## 109.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32f1-pinctrl_8h.html)
- [zephyr/dt-bindings/pinctrl/stm32-pinctrl-common.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32-pinctrl-common_8h.html)
- [zephyr/dt-bindings/pinctrl/stm32f1-afio.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32f1-afio_8h.html)
- [stm32-pinctrl-common.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32-pinctrl-common_8h.html)
- [stm32f1-afio.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32f1-afio_8h.html)

---

[上一章](P108_stm32f1-afio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P110_stm32f37x_clock.h_源码浏览.md)
