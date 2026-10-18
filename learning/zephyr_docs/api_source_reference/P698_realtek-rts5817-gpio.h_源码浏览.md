---
id: learning.zephyr-docs.api-source-reference.page-698
title: realtek-rts5817-gpio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/realtek-rts5817-gpio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第698章\_realtek-rts5817-gpio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/realtek-rts5817-gpio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/realtek-rts5817-gpio_8h.html)。

## 698.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
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
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>

```c
/*
 * Copyright (c) 2026 Realtek Semiconductor, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_RTS5817_GPIO_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_RTS5817_GPIO_H_


#define GPIO_CACHE_CS2  0
#define GPIO_SSI_M_MISO 4
#define GPIO_SSI_M_MOSI 5
#define GPIO_SSI_M_CS   6
#define GPIO_SSI_M_SCK  7
#define GPIO_SCL0       8
#define GPIO_SDA0       9
#define GPIO_SCL2       10
#define GPIO_SDA2       11
#define GPIO_SCL1       12
#define GPIO_SDA1       13
#define GPIO_SSI_S_MISO 14
#define GPIO_SSI_S_MOSI 15
#define GPIO_SSI_S_CS   16
#define GPIO_SSI_S_SCK  17
#define GPIO_GPIO14     18
#define GPIO_GPIO15     19
#define GPIO_AL0        20
#define GPIO_AL1        21
#define GPIO_AL2        22
#define GPIO_SNR_RST    23
#define GPIO_SNR_CS     24
#define GPIO_SNR_GPIO   25
#define GPI_WAKE1       26
#define GPI_WAKE2       27



#define GPIO_POWER_3V3 BIT(8)
#define GPIO_POWER_1V8 BIT(9)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_RTS5817_GPIO_H_ */
```

## 698.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Realtek Semiconductor, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 73 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_RTS5817_GPIO_H_`。

## 698.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/realtek-rts5817-gpio_8h.html)

---

[上一章](P697_realtek-bee-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P699_regions.h_源码浏览.md)
