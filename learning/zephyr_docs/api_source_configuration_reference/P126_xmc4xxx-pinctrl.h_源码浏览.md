---
id: learning.zephyr-docs.api-source-configuration-reference.page-126
title: xmc4xxx-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/xmc4xxx-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第126章\_xmc4xxx-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/xmc4xxx-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/xmc4xxx-pinctrl_8h.html)。

## 126.1\_原始可见代码（Source Code）

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
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00050"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>

```c
/*
 * Copyright (c) 2022 Schlumberger
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_XMC4XXX_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_XMC4XXX_PINCTRL_H_

/* Bit Masks */

#define XMC4XXX_PORT_POS        0
#define XMC4XXX_PORT_MASK       0xf

#define XMC4XXX_PIN_POS         4
#define XMC4XXX_PIN_MASK        0xf

#define XMC4XXX_ALT_POS         8
#define XMC4XXX_ALT_MASK        0xf

#define XMC4XXX_PULL_DOWN_POS   12
#define XMC4XXX_PULL_DOWN_MASK  0x1

#define XMC4XXX_PULL_UP_POS     13
#define XMC4XXX_PULL_UP_MASK    0x1

#define XMC4XXX_PUSH_PULL_POS   14
#define XMC4XXX_PUSH_PULL_MASK  0x1

#define XMC4XXX_OPEN_DRAIN_POS  15
#define XMC4XXX_OPEN_DRAIN_MASK 0x1

#define XMC4XXX_OUT_HIGH_POS    16
#define XMC4XXX_OUT_HIGH_MASK   0x1

#define XMC4XXX_OUT_LOW_POS     17
#define XMC4XXX_OUT_LOW_MASK    0x1

#define XMC4XXX_INV_INPUT_POS   18
#define XMC4XXX_INV_INPUT_MASK  0x1

#define XMC4XXX_DRIVE_POS       19
#define XMC4XXX_DRIVE_MASK      0x7

#define XMC4XXX_HWCTRL_POS      22
#define XMC4XXX_HWCTRL_MASK     0x3

/* Setters and getters */

#define XMC4XXX_PINMUX_SET(port, pin, alt_fun)                                                     \
        ((port) << XMC4XXX_PORT_POS | (pin) << XMC4XXX_PIN_POS | (alt_fun) << XMC4XXX_ALT_POS)

#define XMC4XXX_PINMUX_GET_PORT(mx)           ((mx >> XMC4XXX_PORT_POS)       & XMC4XXX_PORT_MASK)
#define XMC4XXX_PINMUX_GET_PIN(mx)            ((mx >> XMC4XXX_PIN_POS)        & XMC4XXX_PIN_MASK)
#define XMC4XXX_PINMUX_GET_ALT(mx)            ((mx >> XMC4XXX_ALT_POS)        & XMC4XXX_ALT_MASK)
#define XMC4XXX_PINMUX_GET_PULL_DOWN(mx)  ((mx >> XMC4XXX_PULL_DOWN_POS)  & XMC4XXX_PULL_DOWN_MASK)
#define XMC4XXX_PINMUX_GET_PULL_UP(mx)    ((mx >> XMC4XXX_PULL_UP_POS)    & XMC4XXX_PULL_UP_MASK)
#define XMC4XXX_PINMUX_GET_PUSH_PULL(mx)  ((mx >> XMC4XXX_PUSH_PULL_POS)  & XMC4XXX_PUSH_PULL_MASK)
#define XMC4XXX_PINMUX_GET_OPEN_DRAIN(mx) ((mx >> XMC4XXX_OPEN_DRAIN_POS) & XMC4XXX_OPEN_DRAIN_MASK)
#define XMC4XXX_PINMUX_GET_OUT_HIGH(mx)   ((mx >> XMC4XXX_OUT_HIGH_POS)   & XMC4XXX_OUT_HIGH_MASK)
#define XMC4XXX_PINMUX_GET_OUT_LOW(mx)    ((mx >> XMC4XXX_OUT_LOW_POS)    & XMC4XXX_OUT_LOW_MASK)
#define XMC4XXX_PINMUX_GET_INV_INPUT(mx)  ((mx >> XMC4XXX_INV_INPUT_POS)  & XMC4XXX_INV_INPUT_MASK)
#define XMC4XXX_PINMUX_GET_DRIVE(mx)      ((mx >> XMC4XXX_DRIVE_POS)      & XMC4XXX_DRIVE_MASK)
#define XMC4XXX_PINMUX_GET_HWCTRL(mx)     ((mx >> XMC4XXX_HWCTRL_POS)     & XMC4XXX_HWCTRL_MASK)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_XMC4XXX_PINCTRL_H_ */
```

## 126.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Schlumberger。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

位掩码（Bit Masks）。

### 注释 3：原第 48 行

设置与获取函数（Setters and getters）。

### 注释 4：原第 66 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_XMC4XXX_PINCTRL_H_`。

## 126.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/xmc4xxx-pinctrl_8h.html)

---

[上一章](P125_xlnx_gem.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P127_ztest.h_源码浏览.md)
