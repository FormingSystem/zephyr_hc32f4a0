---
id: learning.zephyr-docs.api-source-supplement-reference.page-92
title: imx_spc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/imx__spc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第92章\_imx\_spc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/imx__spc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/imx__spc_8h.html)。

## 92.1\_原始可见代码（Source Code）

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
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>

```c
/*
 * Copyright (c) 2021, NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


/*
 * Setpoint definitions for IMX Set point controller. The SPC uses a series
 * of set points to determine the clock speeds and states of cores, as well
 * as which peripherals to gate clocks to. Higher values correspond to more
 * power saving. See your SOC's datasheet for specifics of what peripherals
 * have their clocks gated at each set point.
 *
 * Set point control is implemented at the soc level (see pm_state_set())
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_POWER_IMX_SPC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_POWER_IMX_SPC_H_

#define IMX_GPC_RUN             0x0
#define IMX_GPC_WAIT    0x1
#define IMX_GPC_STOP    0x2
#define IMX_GPC_SUSPEND 0x3


#define IMX_SPC_MASK 0xF0
#define IMX_SPC_SHIFT 4
#define IMX_GPC_MODE_MASK 0xF

#define IMX_SPC(x) ((x & IMX_SPC_MASK) >> IMX_SPC_SHIFT)
#define IMX_GPC_MODE(x) (x & IMX_GPC_MODE_MASK)

#define IMX_SPC_0       0x00
#define IMX_SPC_1       0x10
#define IMX_SPC_2       0x20
#define IMX_SPC_3       0x30
#define IMX_SPC_4       0x40
#define IMX_SPC_5       0x50
#define IMX_SPC_6       0x60
#define IMX_SPC_7       0x70
#define IMX_SPC_8       0x80
#define IMX_SPC_9       0x90
#define IMX_SPC_10      0xA0
#define IMX_SPC_11      0xB0
#define IMX_SPC_12      0xC0
#define IMX_SPC_13      0xD0
#define IMX_SPC_14      0xE0
#define IMX_SPC_15      0xF0


#define IMX_SPC_SET_POINT_0_RUN                 (IMX_SPC_0 | IMX_GPC_RUN)
#define IMX_SPC_SET_POINT_0_WAIT                (IMX_SPC_0 | IMX_GPC_WAIT)
#define IMX_SPC_SET_POINT_0_STOP                (IMX_SPC_0 | IMX_GPC_STOP)
#define IMX_SPC_SET_POINT_0_SUSPEND             (IMX_SPC_0 | IMX_GPC_SUSPEND)
#define IMX_SPC_SET_POINT_1_RUN                 (IMX_SPC_1 | IMX_GPC_RUN)
#define IMX_SPC_SET_POINT_1_WAIT                (IMX_SPC_1 | IMX_GPC_WAIT)
#define IMX_SPC_SET_POINT_1_STOP                (IMX_SPC_1 | IMX_GPC_STOP)
#define IMX_SPC_SET_POINT_1_SUSPEND             (IMX_SPC_1 | IMX_GPC_SUSPEND)
#define IMX_SPC_SET_POINT_2_RUN                 (IMX_SPC_2 | IMX_GPC_RUN)
#define IMX_SPC_SET_POINT_2_WAIT                (IMX_SPC_2 | IMX_GPC_WAIT)
#define IMX_SPC_SET_POINT_2_STOP                (IMX_SPC_2 | IMX_GPC_STOP)
#define IMX_SPC_SET_POINT_2_SUSPEND             (IMX_SPC_2 | IMX_GPC_SUSPEND)
#define IMX_SPC_SET_POINT_3_RUN                 (IMX_SPC_3 | IMX_GPC_RUN)
#define IMX_SPC_SET_POINT_3_WAIT                (IMX_SPC_3 | IMX_GPC_WAIT)
#define IMX_SPC_SET_POINT_3_STOP                (IMX_SPC_3 | IMX_GPC_STOP)
#define IMX_SPC_SET_POINT_3_SUSPEND             (IMX_SPC_3 | IMX_GPC_SUSPEND)
#define IMX_SPC_SET_POINT_4_RUN                 (IMX_SPC_4 | IMX_GPC_RUN)
#define IMX_SPC_SET_POINT_4_WAIT                (IMX_SPC_4 | IMX_GPC_WAIT)
#define IMX_SPC_SET_POINT_4_STOP                (IMX_SPC_4 | IMX_GPC_STOP)
#define IMX_SPC_SET_POINT_4_SUSPEND             (IMX_SPC_4 | IMX_GPC_SUSPEND)
#define IMX_SPC_SET_POINT_5_RUN                 (IMX_SPC_5 | IMX_GPC_RUN)
#define IMX_SPC_SET_POINT_5_WAIT                (IMX_SPC_5 | IMX_GPC_WAIT)
#define IMX_SPC_SET_POINT_5_STOP                (IMX_SPC_5 | IMX_GPC_STOP)
#define IMX_SPC_SET_POINT_5_SUSPEND             (IMX_SPC_5 | IMX_GPC_SUSPEND)
#define IMX_SPC_SET_POINT_6_RUN                 (IMX_SPC_6 | IMX_GPC_RUN)
#define IMX_SPC_SET_POINT_6_WAIT                (IMX_SPC_6 | IMX_GPC_WAIT)
#define IMX_SPC_SET_POINT_6_STOP                (IMX_SPC_6 | IMX_GPC_STOP)
#define IMX_SPC_SET_POINT_6_SUSPEND             (IMX_SPC_6 | IMX_GPC_SUSPEND)
#define IMX_SPC_SET_POINT_7_RUN                 (IMX_SPC_7 | IMX_GPC_RUN)
#define IMX_SPC_SET_POINT_7_WAIT                (IMX_SPC_7 | IMX_GPC_WAIT)
#define IMX_SPC_SET_POINT_7_STOP                (IMX_SPC_7 | IMX_GPC_STOP)
#define IMX_SPC_SET_POINT_7_SUSPEND             (IMX_SPC_7 | IMX_GPC_SUSPEND)
#define IMX_SPC_SET_POINT_8_RUN                 (IMX_SPC_8 | IMX_GPC_RUN)
#define IMX_SPC_SET_POINT_8_WAIT                (IMX_SPC_8 | IMX_GPC_WAIT)
#define IMX_SPC_SET_POINT_8_STOP                (IMX_SPC_8 | IMX_GPC_STOP)
#define IMX_SPC_SET_POINT_8_SUSPEND             (IMX_SPC_8 | IMX_GPC_SUSPEND)
#define IMX_SPC_SET_POINT_9_RUN                 (IMX_SPC_9 | IMX_GPC_RUN)
#define IMX_SPC_SET_POINT_9_WAIT                (IMX_SPC_9 | IMX_GPC_WAIT)
#define IMX_SPC_SET_POINT_9_STOP                (IMX_SPC_9 | IMX_GPC_STOP)
#define IMX_SPC_SET_POINT_9_SUSPEND             (IMX_SPC_9 | IMX_GPC_SUSPEND)
#define IMX_SPC_SET_POINT_10_RUN                (IMX_SPC_10 | IMX_GPC_RUN)
#define IMX_SPC_SET_POINT_10_WAIT               (IMX_SPC_10 | IMX_GPC_WAIT)
#define IMX_SPC_SET_POINT_10_STOP               (IMX_SPC_10 | IMX_GPC_STOP)
#define IMX_SPC_SET_POINT_10_SUSPEND    (IMX_SPC_10 | IMX_GPC_SUSPEND)
#define IMX_SPC_SET_POINT_11_RUN                (IMX_SPC_11 | IMX_GPC_RUN)
#define IMX_SPC_SET_POINT_11_WAIT               (IMX_SPC_11 | IMX_GPC_WAIT)
#define IMX_SPC_SET_POINT_11_STOP               (IMX_SPC_11 | IMX_GPC_STOP)
#define IMX_SPC_SET_POINT_11_SUSPEND    (IMX_SPC_11 | IMX_GPC_SUSPEND)
#define IMX_SPC_SET_POINT_12_RUN                (IMX_SPC_12 | IMX_GPC_RUN)
#define IMX_SPC_SET_POINT_12_WAIT               (IMX_SPC_12 | IMX_GPC_WAIT)
#define IMX_SPC_SET_POINT_12_STOP               (IMX_SPC_12 | IMX_GPC_STOP)
#define IMX_SPC_SET_POINT_12_SUSPEND    (IMX_SPC_12 | IMX_GPC_SUSPEND)
#define IMX_SPC_SET_POINT_13_RUN                (IMX_SPC_13 | IMX_GPC_RUN)
#define IMX_SPC_SET_POINT_13_WAIT               (IMX_SPC_13 | IMX_GPC_WAIT)
#define IMX_SPC_SET_POINT_13_STOP               (IMX_SPC_13 | IMX_GPC_STOP)
#define IMX_SPC_SET_POINT_13_SUSPEND    (IMX_SPC_13 | IMX_GPC_SUSPEND)
#define IMX_SPC_SET_POINT_14_RUN                (IMX_SPC_14 | IMX_GPC_RUN)
#define IMX_SPC_SET_POINT_14_WAIT               (IMX_SPC_14 | IMX_GPC_WAIT)
#define IMX_SPC_SET_POINT_14_STOP               (IMX_SPC_14 | IMX_GPC_STOP)
#define IMX_SPC_SET_POINT_14_SUSPEND    (IMX_SPC_14 | IMX_GPC_SUSPEND)
#define IMX_SPC_SET_POINT_15_RUN                (IMX_SPC_15 | IMX_GPC_RUN)
#define IMX_SPC_SET_POINT_15_WAIT               (IMX_SPC_15 | IMX_GPC_WAIT)
#define IMX_SPC_SET_POINT_15_STOP               (IMX_SPC_15 | IMX_GPC_STOP)
#define IMX_SPC_SET_POINT_15_SUSPEND    (IMX_SPC_15 | IMX_GPC_SUSPEND)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_POWER_IMX_SPC_H_ */
```

## 92.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021, NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 8 行

IMX 设定点控制器（Set point controller）的设定点定义。SPC 使用一系列设定点确定各处理器核的时钟速度和状态，以及对哪些外设执行时钟门控（Clock gating）。值越高，对应的节能程度越高。各个设定点下具体哪些外设被门控，请查阅对应 SoC 的数据手册。

设定点控制在 SoC 层实现，参见 `pm_state_set()`。

### 注释 3：原第 118 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_POWER_IMX_SPC_H_`。

## 92.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/imx__spc_8h.html)

---

[上一章](P091_img_mgmt_callbacks.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P093_time.h_源码浏览.md)
