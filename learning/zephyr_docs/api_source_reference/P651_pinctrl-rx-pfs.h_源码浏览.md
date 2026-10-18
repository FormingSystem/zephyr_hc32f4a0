---
id: learning.zephyr-docs.api-source-reference.page-651
title: pinctrl-rx-pfs.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rx-pfs_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第651章\_pinctrl-rx-pfs.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rx-pfs_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rx-pfs_8h.html)。

## 651.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>

```c
/*
 * Copyright (c) 2026 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RX_H__
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RX_H__

#define RX_PORT_NUM_POS  0
#define RX_PORT_NUM_MASK 0xf

#define RX_PIN_NUM_POS  5
#define RX_PIN_NUM_MASK 0xf

#define RX_PSEL_HIZ_JTAG_SWD 0x0
#define RX_PSEL_SCI_0        0xA
#define RX_PSEL_SCI_2        0xA
#define RX_PSEL_SCI_4        0xA
#define RX_PSEL_SCI_6        0xA
#define RX_PSEL_SCI_8        0xA
#define RX_PSEL_SCI_10       0xA
#define RX_PSEL_SCI_12       0xA
#define RX_PSEL_SCI_1        0xD
#define RX_PSEL_SCI_3        0xD
#define RX_PSEL_SCI_5        0xD
#define RX_PSEL_SCI_7        0xD
#define RX_PSEL_SCI_9        0xD
#define RX_PSEL_SCI_11       0xD

#define RX_PSEL_POS  9
#define RX_PSEL_MASK 0x1f

#define RX_MODE_POS  16
#define RX_MODE_MASK 0x1

#define RX_PSEL(psel, port_num, pin_num)                                                           \
        (1 << RX_MODE_POS | psel << RX_PSEL_POS | port_num << RX_PORT_NUM_POS |                    \
         pin_num << RX_PIN_NUM_POS)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RX_H__ */
```

## 651.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 79 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RX_H__`。

## 651.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rx-pfs_8h.html)

---

[上一章](P650_pinctrl-ra.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P652_pinctrl-rza3m.h_源码浏览.md)
