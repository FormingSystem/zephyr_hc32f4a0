---
id: learning.zephyr-docs.api-source-reference.page-608
title: numicro-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/numicro-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第608章\_numicro-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/numicro-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/numicro-pinctrl_8h.html)。

## 608.1\_原始可见代码（Source Code）

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
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00037"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>

```c
/*
 * Copyright (c) 2022 SEAL AG
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_NUMICRO_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_NUMICRO_PINCTRL_H_

#define NUMICRO_MFP_SHIFT 0U
#define NUMICRO_MFP_MASK  0xFU
#define NUMICRO_PIN_SHIFT 4U
#define NUMICRO_PIN_MASK  0xFU
#define NUMICRO_PORT_SHIFT 8U
#define NUMICRO_PORT_MASK  0xFU

#define NUMICRO_PINMUX(port, pin, mfp)                                  \
        (((((port) - 'A') & NUMICRO_PORT_MASK) << NUMICRO_PORT_SHIFT) | \
        (((pin) & NUMICRO_PIN_MASK) << NUMICRO_PIN_SHIFT) |             \
        (((mfp) & NUMICRO_MFP_MASK) << NUMICRO_MFP_SHIFT))

#define NUMICRO_PORT(pinmux) \
        (((pinmux) >> NUMICRO_PORT_SHIFT) & NUMICRO_PORT_MASK)
#define NUMICRO_PIN(pinmux) \
        (((pinmux) >> NUMICRO_PIN_SHIFT) & NUMICRO_PIN_MASK)
#define NUMICRO_MFP(pinmux) \
        (((pinmux) >> NUMICRO_MFP_SHIFT) & NUMICRO_MFP_MASK)

#endif  /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_NUMICRO_PINCTRL_H_ */
```

## 608.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 SEAL AG。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 42 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_NUMICRO_PINCTRL_H_`。

## 608.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/numicro-pinctrl_8h.html)

---

[上一章](P607_numicro-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P609_nus.h_源码浏览.md)
