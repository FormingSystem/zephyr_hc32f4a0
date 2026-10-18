---
id: learning.zephyr-docs.api-source-configuration-reference.page-69
title: pinctrl-zynqmp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-zynqmp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_pinctrl-zynqmp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-zynqmp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-zynqmp_8h.html)。

## 69.1\_原始可见代码（Source Code）

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
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
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
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>

```c
/*
 * Copyright (c) 2024 Antmicro <www.antmicro.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_PINCTRL_ZYNQMP_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_PINCTRL_ZYNQMP_H_

/*
 * The offset is defined at `pictrl_soc.h` for the ZynqMP platform
 */
#define FUNCTION_OFFSET 8
#define UART_FUNCTION 0x1

/*
 * For functions that can be selected for a subset of MIO pins,
 * specific macro identifiers were generated to avoid complex checking
 * logic at compile time. For more generalized applications existing on
 * every pin (eg. GPIO), a generic macro function to generate a driver-compliant
 * selector value can be used.
 */

#define UART0_RX_2  (2U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_6  (6U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_10 (10U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_14 (14U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_18 (18U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_22 (22U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_26 (26U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_30 (30U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_34 (34U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_38 (38U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_42 (42U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_46 (46U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_50 (50U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_54 (54U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_58 (58U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_62 (62U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_66 (66U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_70 (70U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_RX_74 (74U | (UART_FUNCTION << FUNCTION_OFFSET))

#define UART0_TX_3  (3U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_7  (7U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_11 (11U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_15 (15U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_19 (19U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_23 (23U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_27 (27U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_31 (31U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_35 (35U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_39 (39U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_43 (43U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_47 (47U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_51 (51U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_55 (55U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_59 (59U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_63 (63U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_67 (67U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_71 (71U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART0_TX_75 (75U | (UART_FUNCTION << FUNCTION_OFFSET))

#define UART1_RX_1  (1U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_5  (5U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_9  (9U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_13 (13U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_17 (17U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_21 (21U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_25 (25U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_29 (29U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_33 (33U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_37 (37U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_41 (41U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_45 (45U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_49 (49U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_53 (53U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_57 (57U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_61 (61U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_65 (65U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_69 (69U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_RX_73 (73U | (UART_FUNCTION << FUNCTION_OFFSET))

#define UART1_TX_0  (0U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_4  (4U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_8  (8U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_12 (12U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_16 (16U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_20 (20U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_24 (24U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_28 (28U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_32 (32U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_36 (36U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_40 (40U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_44 (44U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_48 (28U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_52 (52U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_56 (56U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_60 (60U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_64 (64U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_68 (28U | (UART_FUNCTION << FUNCTION_OFFSET))
#define UART1_TX_72 (72U | (UART_FUNCTION << FUNCTION_OFFSET))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_PINCTRL_ZYNQMP_H_ */
```

## 69.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Antmicro <www.antmicro.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

ZynqMP 平台的偏移量定义在 `pictrl_soc.h` 中。

### 注释 3：原第 16 行

对于仅能在部分 MIO 引脚上选择的功能，已生成专用宏标识符，以避免复杂的编译期检查逻辑。对于每个引脚都具有的通用用途，例如 GPIO，可以使用通用宏函数生成符合驱动要求的选择器值。

### 注释 4：原第 104 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_PINCTRL_ZYNQMP_H_`。

## 69.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-zynqmp_8h.html)

---

[上一章](P068_pinctrl-rx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P070_pinctrl_soc_bflb_common.h_源码浏览.md)
