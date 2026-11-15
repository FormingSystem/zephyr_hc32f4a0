---
id: learning.zephyr-docs.api-source-reference.page-21
title: alif-clocks-common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_alif-clocks-common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html)。

## 21.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00023"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00137"></a>

```c
/*
 * Copyright (c) 2025 Alif Semiconductor
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ALIF_CLOCKS_COMMON_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ALIF_CLOCKS_COMMON_H_



#define ALIF_CLOCK_MODULE_MASK         0x7U
#define ALIF_CLOCK_MODULE_SHIFT        0U
#define ALIF_CLOCK_REG_MASK            0xFFU
#define ALIF_CLOCK_REG_SHIFT           3U
#define ALIF_CLOCK_EN_BIT_POS_MASK     0x1FU
#define ALIF_CLOCK_EN_BIT_POS_SHIFT    11U
#define ALIF_CLOCK_EN_MASK_SHIFT       16U
#define ALIF_CLOCK_SRC_VAL_MASK            0x3U
#define ALIF_CLOCK_SRC_VAL_SHIFT           17U
#define ALIF_CLOCK_SRC_FIELD_WIDTH_MASK    0x3U
#define ALIF_CLOCK_SRC_FIELD_WIDTH_SHIFT   19U
#define ALIF_CLOCK_SRC_FIELD_POS_MASK      0x1FU
#define ALIF_CLOCK_SRC_FIELD_POS_SHIFT     21U
#define ALIF_CLOCK_PARENT_CLK_MASK     0x1FU
#define ALIF_CLOCK_PARENT_CLK_SHIFT    26U


#define ALIF_CLK_CFG(module, reg, en_bit, en_mask, src_val,                                        \
                             src_field_width, src_field_pos, parent_clk)                           \
        ((((ALIF_##module##_MODULE) & ALIF_CLOCK_MODULE_MASK) << ALIF_CLOCK_MODULE_SHIFT) |        \
         (((ALIF_##reg##_REG) & ALIF_CLOCK_REG_MASK) << ALIF_CLOCK_REG_SHIFT) |                    \
         (((en_bit) & ALIF_CLOCK_EN_BIT_POS_MASK) << ALIF_CLOCK_EN_BIT_POS_SHIFT) |                \
         (((en_mask) & 0x1U) << ALIF_CLOCK_EN_MASK_SHIFT) |                                        \
         (((src_val) & ALIF_CLOCK_SRC_VAL_MASK) << ALIF_CLOCK_SRC_VAL_SHIFT) |                     \
         (((src_field_width) & ALIF_CLOCK_SRC_FIELD_WIDTH_MASK) <<                                 \
          ALIF_CLOCK_SRC_FIELD_WIDTH_SHIFT) |                                                      \
         (((src_field_pos) & ALIF_CLOCK_SRC_FIELD_POS_MASK) << ALIF_CLOCK_SRC_FIELD_POS_SHIFT) |   \
         (((parent_clk) & ALIF_CLOCK_PARENT_CLK_MASK) << ALIF_CLOCK_PARENT_CLK_SHIFT))


#define ALIF_PARENT_CLK_SYST_ACLK   0x0U
#define ALIF_PARENT_CLK_SYST_HCLK   0x1U
#define ALIF_PARENT_CLK_SYST_PCLK   0x2U
#define ALIF_PARENT_CLK_S32K        0x3U
#define ALIF_PARENT_CLK_128K        0x4U



#define ALIF_CGU_MODULE                 0x0U
#define ALIF_CLKCTL_PER_MST_MODULE      0x1U
#define ALIF_CLKCTL_PER_SLV_MODULE      0x2U
#define ALIF_AON_MODULE                 0x3U
#define ALIF_VBAT_MODULE                0x4U
#define ALIF_M55HE_CFG_MODULE           0x5U
#define ALIF_M55HP_CFG_MODULE           0x6U


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ALIF_CLOCKS_COMMON_H_ */
```

## 21.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Alif Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 137 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_ALIF_CLOCKS_COMMON_H_`。

## 21.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html)

---

[上一章](P020_alif-balletto-clocks.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P022_alif-ensemble-clocks.h_源码浏览.md)
