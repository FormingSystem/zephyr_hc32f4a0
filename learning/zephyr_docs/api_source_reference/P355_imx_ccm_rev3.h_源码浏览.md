---
id: learning.zephyr-docs.api-source-reference.page-355
title: imx_ccm_rev3.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/imx__ccm__rev3_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第355章\_imx\_ccm\_rev3.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/imx__ccm__rev3_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/imx__ccm__rev3_8h.html)。

## 355.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="foldopen00134"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="foldopen00142"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="foldopen00147"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="foldopen00150"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="foldopen00153"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="foldopen00156"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX_CCM_REV3_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX_CCM_REV3_H_


#define IMX_CCM_ID_BITS 16U
#define IMX_CCM_ID_MASK 0xFFFFU

#define IMX_CCM_GATE_SHIFT 0U
#define IMX_CCM_ROOT_SHIFT 16U

#define IMX_CCM_GATE_NONE IMX_CCM_ID_MASK
#define IMX_CCM_ROOT_NONE IMX_CCM_ID_MASK

#define IMX_CCM_CLK(gate, root)                                                                    \
        ((((root) & IMX_CCM_ID_MASK) << IMX_CCM_ROOT_SHIFT) |                                      \
         (((gate) & IMX_CCM_ID_MASK) << IMX_CCM_GATE_SHIFT))

#define IMX_CCM_CLK_GATE(spec) (((spec) >> IMX_CCM_GATE_SHIFT) & IMX_CCM_ID_MASK)
#define IMX_CCM_CLK_ROOT(spec) (((spec) >> IMX_CCM_ROOT_SHIFT) & IMX_CCM_ID_MASK)


#define IMX_CCM_ROOT_CFG_ROOT_SHIFT    0U
#define IMX_CCM_ROOT_CFG_MUX_SHIFT     8U
#define IMX_CCM_ROOT_CFG_DIV_SHIFT     12U
#define IMX_CCM_ROOT_CFG_SND_DIV_SHIFT 20U
#define IMX_CCM_ROOT_CFG_TAG_SHIFT     28U

#define IMX_CCM_ROOT_CFG_ROOT_MASK    0xFFU
#define IMX_CCM_ROOT_CFG_MUX_MASK     0xFU
#define IMX_CCM_ROOT_CFG_DIV_MASK     0xFFU
#define IMX_CCM_ROOT_CFG_SND_DIV_MASK 0xFFU
#define IMX_CCM_ROOT_CFG_TAG_MASK     0xFU

#define IMX_CCM_ROOT_CFG_TAG 0xAU

#define IMX_CCM_ROOT_CFG(root, mux, div, snd_div)                                                  \
        (((IMX_CCM_ROOT_CFG_TAG) << IMX_CCM_ROOT_CFG_TAG_SHIFT) |                                  \
         (((snd_div) & IMX_CCM_ROOT_CFG_SND_DIV_MASK) << IMX_CCM_ROOT_CFG_SND_DIV_SHIFT) |         \
         (((div) & IMX_CCM_ROOT_CFG_DIV_MASK) << IMX_CCM_ROOT_CFG_DIV_SHIFT) |                     \
         (((mux) & IMX_CCM_ROOT_CFG_MUX_MASK) << IMX_CCM_ROOT_CFG_MUX_SHIFT) |                     \
         (((root) & IMX_CCM_ROOT_CFG_ROOT_MASK) << IMX_CCM_ROOT_CFG_ROOT_SHIFT))

#define IMX_CCM_ROOT_CFG_IS(cell)                                                                  \
        ((((cell) >> IMX_CCM_ROOT_CFG_TAG_SHIFT) & IMX_CCM_ROOT_CFG_TAG_MASK) ==                   \
         IMX_CCM_ROOT_CFG_TAG)

#define IMX_CCM_ROOT_CFG_ROOT(cell)                                                                \
        (((cell) >> IMX_CCM_ROOT_CFG_ROOT_SHIFT) & IMX_CCM_ROOT_CFG_ROOT_MASK)

#define IMX_CCM_ROOT_CFG_MUX(cell)                                                                 \
        (((cell) >> IMX_CCM_ROOT_CFG_MUX_SHIFT) & IMX_CCM_ROOT_CFG_MUX_MASK)

#define IMX_CCM_ROOT_CFG_DIV(cell)                                                                 \
        (((cell) >> IMX_CCM_ROOT_CFG_DIV_SHIFT) & IMX_CCM_ROOT_CFG_DIV_MASK)

#define IMX_CCM_ROOT_CFG_SND_DIV(cell)                                                             \
        (((cell) >> IMX_CCM_ROOT_CFG_SND_DIV_SHIFT) & IMX_CCM_ROOT_CFG_SND_DIV_MASK)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX_CCM_REV3_H_ */
```

## 355.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright 2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 161 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX_CCM_REV3_H_`。

## 355.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/imx__ccm__rev3_8h.html)

---

[上一章](P354_imx95_power.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P356_imx_rdc.h_源码浏览.md)
