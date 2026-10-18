---
id: learning.zephyr-docs.api-source-reference.page-827
title: stm32-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第827章\_stm32-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32-pinctrl_8h.html)。

## 827.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
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
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00069"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="astm32-pinctrl-common_8h_html"></a>

```c
/*
 * Copyright (c) 2017 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_STM32_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_STM32_PINCTRL_H_

#include <zephyr/dt-bindings/pinctrl/stm32-pinctrl-common.h>



#define STM32_AF0     0x0
#define STM32_AF1     0x1
#define STM32_AF2     0x2
#define STM32_AF3     0x3
#define STM32_AF4     0x4
#define STM32_AF5     0x5
#define STM32_AF6     0x6
#define STM32_AF7     0x7
#define STM32_AF8     0x8
#define STM32_AF9     0x9
#define STM32_AF10    0xa
#define STM32_AF11    0xb
#define STM32_AF12    0xc
#define STM32_AF13    0xd
#define STM32_AF14    0xe
#define STM32_AF15    0xf
#define STM32_ANALOG  0x10
#define STM32_GPIO    0x11


#define STM32_MODE_SHIFT 0U
#define STM32_MODE_MASK  0x1FU
#define STM32_LINE_SHIFT 5U
#define STM32_LINE_MASK  0xFU
#define STM32_PORT_SHIFT 9U
#define STM32_PORT_MASK  0x1FU

#define STM32_PINMUX(port, line, mode)                                         \
                (((((port) - 'A') & STM32_PORT_MASK) << STM32_PORT_SHIFT) |    \
                (((line) & STM32_LINE_MASK) << STM32_LINE_SHIFT) |             \
                (((STM32_ ## mode) & STM32_MODE_MASK) << STM32_MODE_SHIFT))

#endif  /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_STM32_PINCTRL_H_ */
```

## 827.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 74 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_STM32_PINCTRL_H_`。

## 827.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32-pinctrl_8h.html)
- [zephyr/dt-bindings/pinctrl/stm32-pinctrl-common.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32-pinctrl-common_8h.html)
- [stm32-pinctrl-common.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32-pinctrl-common_8h.html)

---

[上一章](P826_stm32-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P828_stm32-tsc-defines.h_源码浏览.md)
