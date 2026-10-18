---
id: learning.zephyr-docs.api-source-reference.page-100
title: clock_control_ifx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ifx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第100章\_clock\_control\_ifx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ifx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ifx_8h.html)。

## 100.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="adevicetree_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructifx__clk__peri_html"></a>
<a id="astructifx__clk__peri_html_a5f6b88b1827ed1fc2a20613475bf82c2"></a>
<a id="astructifx__clk__peri_html_aacbb68c082f9ee6385e0a26436553711"></a>
<a id="astructifx__clk_html"></a>
<a id="astructifx__clk_html_a244fa8efec2792704d70a0c9a2f061bd"></a>
<a id="astructifx__clk_html_afb377cb6f9831a5537e4f4e3272a4809"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 Linumiz
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_IFX_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_IFX_H_

#include <stdint.h>
#include <zephyr/devicetree.h>

#define IFX_CLK_PLL 0

#define IFX_CLK_HF  1

#define IFX_CLK_LF  2

struct ifx_clk {
        uint8_t clk;
        uint8_t clk_id;
};

struct ifx_clk_peri {
        uint32_t div_ord;
        uint8_t rootclk_id;
};

#define IFX_CLK_PERI_DT_SPEC_GET(node_id)                       \
        {                                                       \
                .rootclk_id = DT_PROP(node_id, clk_dst),        \
                .div_ord = DT_DEP_ORD(DT_CLOCKS_CTLR(node_id)), \
        }

#define IFX_CLK_PERI_DT_INST_SPEC_GET(inst)     \
        IFX_CLK_PERI_DT_SPEC_GET(DT_DRV_INST(inst))

#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_IFX_H_ */
```

## 100.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Linumiz。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 57 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_IFX_H_`。

## 100.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ifx_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [ifx_clk](../device_power_control_model_reference/P019_ifx_clk_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [clk](../device_power_control_model_reference/P019_ifx_clk_结构体.md#a244fa8efec2792704d70a0c9a2f061bd)
- [clk_id](../device_power_control_model_reference/P019_ifx_clk_结构体.md#afb377cb6f9831a5537e4f4e3272a4809)
- [ifx_clk_peri](../device_power_control_model_reference/P020_ifx_clk_peri_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [div_ord](../device_power_control_model_reference/P020_ifx_clk_peri_结构体.md#aacbb68c082f9ee6385e0a26436553711)
- [rootclk_id](../device_power_control_model_reference/P020_ifx_clk_peri_结构体.md#a5f6b88b1827ed1fc2a20613475bf82c2)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [ifx_clk_peri::rootclk_id](../device_power_control_model_reference/P020_ifx_clk_peri_结构体.md#a5f6b88b1827ed1fc2a20613475bf82c2)
- [ifx_clk_peri::div_ord](../device_power_control_model_reference/P020_ifx_clk_peri_结构体.md#aacbb68c082f9ee6385e0a26436553711)
- [ifx_clk::clk](../device_power_control_model_reference/P019_ifx_clk_结构体.md#a244fa8efec2792704d70a0c9a2f061bd)
- [ifx_clk::clk_id](../device_power_control_model_reference/P019_ifx_clk_结构体.md#afb377cb6f9831a5537e4f4e3272a4809)

---

[上一章](P099_clock_control_ambiq.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P101_clock_control_numaker.h_源码浏览.md)
