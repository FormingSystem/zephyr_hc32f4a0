---
id: learning.zephyr-docs.api-source-supplement-reference.page-72
title: focaltech_ft9001_pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_focaltech\_ft9001\_pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__pinctrl_8h.html)。

## 72.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00020"></a>
<a id="l00047"></a>
<a id="l00049"></a>
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
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00132"></a>

```c
/*
 * Copyright (c) 2025, FocalTech Systems CO.,Ltd
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_FOCALTECH_FT9001_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_FOCALTECH_FT9001_PINCTRL_H_




/*
 * Pinmux encoding:
 *   bit[0:0]   - VALUE (0 = default, 1 = alternate)
 *   bit[5:1]   - BIT position in register
 *   bit[25:6]  - Register offset
 */

#define FOCALTECH_IOCTRL_BASE 0x40000000U

#define FOCALTECH_PINCTRL_VALUE_POS 0U
#define FOCALTECH_PINCTRL_BIT_POS   1U
#define FOCALTECH_PINCTRL_REG_POS   6U

#define FOCALTECH_PINCTRL_VALUE_MASK 0x1U
#define FOCALTECH_PINCTRL_BIT_MASK   0x1FU
#define FOCALTECH_PINCTRL_REG_MASK   0xFFFFFU

#define FOCALTECH_PINCTRL_REG_GET(pinmux)                                                          \
        ((((pinmux) >> FOCALTECH_PINCTRL_REG_POS) & FOCALTECH_PINCTRL_REG_MASK) |                  \
         FOCALTECH_IOCTRL_BASE)

#define FOCALTECH_PINCTRL_BIT_GET(pinmux)                                                          \
        (((pinmux) >> FOCALTECH_PINCTRL_BIT_POS) & FOCALTECH_PINCTRL_BIT_MASK)

#define FOCALTECH_PINCTRL_VALUE_GET(pinmux)                                                        \
        (((pinmux) >> FOCALTECH_PINCTRL_VALUE_POS) & FOCALTECH_PINCTRL_VALUE_MASK)


#define FOCALTECH_PINMUX(reg, bit, value)                                                          \
        (((reg) << FOCALTECH_PINCTRL_REG_POS) | ((bit) << FOCALTECH_PINCTRL_BIT_POS) |             \
         ((value) << FOCALTECH_PINCTRL_VALUE_POS))


#define FOCALTECH_IOCTRL_SPICR_OFFSET    0x00000U
#define FOCALTECH_IOCTRL_I2CCR_OFFSET    0x00008U
#define FOCALTECH_IOCTRL_SCICR_OFFSET    0x0000CU
#define FOCALTECH_IOCTRL_SWAPCR_OFFSET   0x0001CU
#define FOCALTECH_IOCTRL_CLKRSTCR_OFFSET 0x00044U
#define FOCALTECH_IOCTRL_EPORT2CR_OFFSET 0x00054U
#define FOCALTECH_IOCTRL_EPORT3CR_OFFSET 0x00058U
#define FOCALTECH_IOCTRL_EPORT4CR_OFFSET 0x0005CU
#define FOCALTECH_IOCTRL_EPORT5CR_OFFSET 0x00060U
#define FOCALTECH_IOCTRL_EPORT6CR_OFFSET 0x00064U
#define FOCALTECH_IOCTRL_EPORT7CR_OFFSET 0x00068U
#define FOCALTECH_IOCTRL_SWAPCR2_OFFSET  0x0006CU
#define FOCALTECH_IOCTRL_SWAPCR3_OFFSET  0x00070U
#define FOCALTECH_IOCTRL_SWAPCR4_OFFSET  0x00074U
#define FOCALTECH_IOCTRL_SWAPCR5_OFFSET  0x00078U



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_FOCALTECH_FT9001_PINCTRL_H_ */
```

## 72.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025, FocalTech Systems CO.,Ltd。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 50 行

引脚复用编码（Pinmux encoding）：

- `bit[0:0]`：VALUE，0 表示默认功能，1 表示备用功能。
- `bit[5:1]`：在寄存器中的位位置（BIT）。
- `bit[25:6]`：寄存器偏移量。

### 注释 3：原第 132 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_FOCALTECH_FT9001_PINCTRL_H_`。

## 72.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__pinctrl_8h.html)

---

[上一章](P071_fff_extensions.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P073_formats.h_源码浏览.md)
