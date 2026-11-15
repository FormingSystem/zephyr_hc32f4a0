---
id: learning.zephyr-docs.api-source-reference.page-774
title: sf32lb-common-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-common-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第774章\_sf32lb-common-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-common-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-common-pinctrl_8h.html)。

## 774.1\_原始可见代码（Source Code）

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
<a id="foldopen00037"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00054"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>

```c
/*
 * Copyright (c) 2025 Core Devices LLC
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SF32LB_COMMON_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SF32LB_COMMON_PINCTRL_H_

#define SF32LB_FSEL_POS        0U
#define SF32LB_FSEL_MSK        0x0000000FU
#define SF32LB_PORT_POS        12U
#define SF32LB_PORT_MSK        0x00003000U
#define SF32LB_PAD_POS         14U
#define SF32LB_PAD_MSK         0x003FC000U
#define SF32LB_PINR_FIELD_POS  22U
#define SF32LB_PINR_FIELD_MSK  0x00C00000U
#define SF32LB_PINR_OFFSET_POS 24U
#define SF32LB_PINR_OFFSET_MSK 0xFF000000U

#define SF32LB_PINMUX(port, pad, fsel, pinr_offset, pinr_field)                                    \
        ((((pinr_offset) << SF32LB_PINR_OFFSET_POS) & SF32LB_PINR_OFFSET_MSK) |                    \
         (((pinr_field) << SF32LB_PINR_FIELD_POS) & SF32LB_PINR_FIELD_MSK) |                       \
         (((SF32LB_PORT_##port) << SF32LB_PORT_POS) & SF32LB_PORT_MSK) |                           \
         (((pad) << SF32LB_PAD_POS) & SF32LB_PAD_MSK) |                                            \
         (((fsel) << SF32LB_FSEL_POS) & SF32LB_FSEL_MSK))


#define SF32LB_PINMUX_ANALOG(port, pad)                                                            \
        ((((SF32LB_PORT_##port) << SF32LB_PORT_POS) & SF32LB_PORT_MSK) |                           \
         (((pad) << SF32LB_PAD_POS) & SF32LB_PAD_MSK) |                                            \
         ((15U << SF32LB_FSEL_POS) & SF32LB_FSEL_MSK))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SF32LB_COMMON_PINCTRL_H_ */
```

## 774.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Core Devices LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 60 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SF32LB_COMMON_PINCTRL_H_`。

## 774.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-common-pinctrl_8h.html)

---

[上一章](P773_sf32lb-clocks-common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P775_sf32lb-dma-config.h_源码浏览.md)
