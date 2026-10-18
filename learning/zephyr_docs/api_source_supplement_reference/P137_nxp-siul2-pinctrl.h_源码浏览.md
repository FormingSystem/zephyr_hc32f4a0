---
id: learning.zephyr-docs.api-source-supplement-reference.page-137
title: nxp-siul2-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp-siul2-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第137章\_nxp-siul2-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nxp-siul2-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nxp-siul2-pinctrl_8h.html)。

## 137.1\_原始可见代码（Source Code）

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
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00042"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="foldopen00045"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="foldopen00069"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="foldopen00082"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright 2022, 2024-2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_NXP_SIUL2_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_NXP_SIUL2_PINCTRL_H_

#include <zephyr/dt-bindings/dt-util.h>

/*
 * The NXP S32 pinmux configuration is encoded in a 32-bit field value as follows:
 *
 * - 0..2:   Output mux Source Signal Selection (MSCR.SSS)
 * - 3..6:   Input mux Source Signal Selection (IMCR.SSS)
 * - 7..15:  Input Multiplexed Signal Configuration Register (IMCR) index
 * - 16..24: Multiplexed Signal Configuration Register (MSCR) index
 * - 25..27: MSCR SIUL2 instance index (0..7)
 * - 28..30: IMCR SIUL2 instance index (0..7)
 * - 31:     Reserved for future use
 */
#define NXP_SIUL2_MSCR_SSS_SHIFT       0U
#define NXP_SIUL2_MSCR_SSS_MASK        BIT_MASK(3)
#define NXP_SIUL2_IMCR_SSS_SHIFT       3U
#define NXP_SIUL2_IMCR_SSS_MASK        BIT_MASK(4)
#define NXP_SIUL2_IMCR_IDX_SHIFT       7U
#define NXP_SIUL2_IMCR_IDX_MASK        BIT_MASK(9)
#define NXP_SIUL2_MSCR_IDX_SHIFT       16U
#define NXP_SIUL2_MSCR_IDX_MASK        BIT_MASK(9)
#define NXP_SIUL2_MSCR_SIUL2_IDX_SHIFT 25U
#define NXP_SIUL2_MSCR_SIUL2_IDX_MASK  BIT_MASK(3)
#define NXP_SIUL2_IMCR_SIUL2_IDX_SHIFT 28U
#define NXP_SIUL2_IMCR_SIUL2_IDX_MASK  BIT_MASK(3)

#define NXP_SIUL2_PINMUX_MSCR_SSS(cfg)                                                             \
        (((cfg) & NXP_SIUL2_MSCR_SSS_MASK) << NXP_SIUL2_MSCR_SSS_SHIFT)

#define NXP_SIUL2_PINMUX_IMCR_SSS(cfg)                                                             \
        (((cfg) & NXP_SIUL2_IMCR_SSS_MASK) << NXP_SIUL2_IMCR_SSS_SHIFT)

#define NXP_SIUL2_PINMUX_IMCR_IDX(cfg)                                                             \
        (((cfg) & NXP_SIUL2_IMCR_IDX_MASK) << NXP_SIUL2_IMCR_IDX_SHIFT)

#define NXP_SIUL2_PINMUX_MSCR_IDX(cfg)                                                             \
        (((cfg) & NXP_SIUL2_MSCR_IDX_MASK) << NXP_SIUL2_MSCR_IDX_SHIFT)

#define NXP_SIUL2_PINMUX_MSCR_SIUL2_IDX(cfg)                                                       \
        (((cfg) & NXP_SIUL2_MSCR_SIUL2_IDX_MASK) << NXP_SIUL2_MSCR_SIUL2_IDX_SHIFT)

#define NXP_SIUL2_PINMUX_IMCR_SIUL2_IDX(cfg)                                                       \
        (((cfg) & NXP_SIUL2_IMCR_SIUL2_IDX_MASK) << NXP_SIUL2_IMCR_SIUL2_IDX_SHIFT)

#define NXP_SIUL2_PINMUX_GET_MSCR_SSS(cfg)                                                         \
        (((cfg) >> NXP_SIUL2_MSCR_SSS_SHIFT) & NXP_SIUL2_MSCR_SSS_MASK)

#define NXP_SIUL2_PINMUX_GET_IMCR_SSS(cfg)                                                         \
        (((cfg) >> NXP_SIUL2_IMCR_SSS_SHIFT) & NXP_SIUL2_IMCR_SSS_MASK)

#define NXP_SIUL2_PINMUX_GET_IMCR_IDX(cfg)                                                         \
        (((cfg) >> NXP_SIUL2_IMCR_IDX_SHIFT) & NXP_SIUL2_IMCR_IDX_MASK)

#define NXP_SIUL2_PINMUX_GET_MSCR_IDX(cfg)                                                         \
        (((cfg) >> NXP_SIUL2_MSCR_IDX_SHIFT) & NXP_SIUL2_MSCR_IDX_MASK)

#define NXP_SIUL2_PINMUX_GET_MSCR_SIUL2_IDX(cfg)                                                   \
        (((cfg) >> NXP_SIUL2_MSCR_SIUL2_IDX_SHIFT) & NXP_SIUL2_MSCR_SIUL2_IDX_MASK)

#define NXP_SIUL2_PINMUX_GET_IMCR_SIUL2_IDX(cfg)                                                   \
        (((cfg) >> NXP_SIUL2_IMCR_SIUL2_IDX_SHIFT) & NXP_SIUL2_IMCR_SIUL2_IDX_MASK)

#define NXP_SIUL2_PINMUX(mscr_siul2_idx, imcr_siul2_idx, mscr_idx, mscr_sss, imcr_idx, imcr_sss)   \
        (NXP_SIUL2_PINMUX_MSCR_SIUL2_IDX(mscr_siul2_idx) |                                         \
         NXP_SIUL2_PINMUX_IMCR_SIUL2_IDX(imcr_siul2_idx) |                                         \
         NXP_SIUL2_PINMUX_MSCR_IDX(mscr_idx) |                                                     \
         NXP_SIUL2_PINMUX_MSCR_SSS(mscr_sss) |                                                     \
         NXP_SIUL2_PINMUX_IMCR_IDX(imcr_idx) |                                                     \
         NXP_SIUL2_PINMUX_IMCR_SSS(imcr_sss))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_NXP_SIUL2_PINCTRL_H_ */
```

## 137.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022, 2024-2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 12 行

NXP S32 引脚复用配置（Pinmux configuration）编码在一个 32 位字段值中，组织如下：

- `0..2`：输出复用源信号选择（`MSCR.SSS`）。
- `3..6`：输入复用源信号选择（`IMCR.SSS`）。
- `7..15`：输入复用信号配置寄存器（Input Multiplexed Signal Configuration Register，IMCR）索引。
- `16..24`：复用信号配置寄存器（Multiplexed Signal Configuration Register，MSCR）索引。
- `25..27`：MSCR 的 SIUL2 实例索引，范围 0–7。
- `28..30`：IMCR 的 SIUL2 实例索引，范围 0–7。
- `31`：保留供将来使用。

### 注释 3：原第 90 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_NXP_SIUL2_PINCTRL_H_`。

## 137.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nxp-siul2-pinctrl_8h.html)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P136_nxp-s32-xspi.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P138_nxp_nx20p3483.h_源码浏览.md)
