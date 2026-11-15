---
id: learning.zephyr-docs.api-source-supplement-reference.page-161
title: renesas-rztn-gpio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas-rztn-gpio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第161章\_renesas-rztn-gpio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rztn-gpio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rztn-gpio_8h.html)。

## 161.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>

```c
/*
 * Copyright (c) 2025-2026 Renesas Electronics Corporation
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_RENESAS_RZTN_GPIO_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_RENESAS_RZTN_GPIO_H_


#define RZTN_GPIO_SAFETY      0U
#define RZTN_GPIO_NONSAFETY   BIT(14)



/* GPIO DRCTL register */
#define RZTN_GPIO_DRCTL_SHIFT        8U
#define RZTN_GPIO_SCHMITT_TRIG_SHIFT 4U
#define RZTN_GPIO_SLEW_RATE_SHIFT    5U

#define RZTN_GPIO_DRCTL_SET(drive_ability, schmitt_trig, slew_rate)                                \
        (((drive_ability) | ((schmitt_trig) << RZTN_GPIO_SCHMITT_TRIG_SHIFT) |                     \
          ((slew_rate) << RZTN_GPIO_SLEW_RATE_SHIFT))                                              \
         << RZTN_GPIO_DRCTL_SHIFT)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_RENESAS_RZTN_GPIO_H_ */
```

## 161.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025-2026 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 62 行

GPIO 的 `DRCTL` 寄存器。

### 注释 3：原第 75 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_RENESAS_RZTN_GPIO_H_`。

## 161.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rztn-gpio_8h.html)

---

[上一章](P160_renesas-ra-gpio-ioport.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P162_renesas_rza2m_clock.h_源码浏览.md)
