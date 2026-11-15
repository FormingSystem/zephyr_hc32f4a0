---
id: learning.zephyr-docs.api-source-configuration-reference.page-70
title: pinctrl_soc_bflb_common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__soc__bflb__common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_pinctrl\_soc\_bflb\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__soc__bflb__common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__soc__bflb__common_8h.html)。

## 70.1\_原始可见代码（Source Code）

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
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="adevicetree_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="apinctrl__rcar__common_8h_html_a022eeb1c811e7ef94d3a7a99cbda0e2d"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2021-2025 Gerson Fernando Budke <nandojve@gmail.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_SOC_BFLB_COMMON_H_
#define ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_SOC_BFLB_COMMON_H_

#include <zephyr/devicetree.h>
#include <zephyr/types.h>
#include <zephyr/dt-bindings/pinctrl/bflb-common-pinctrl.h>

/* clang-format off */

#ifdef __cplusplus
extern "C" {
#endif


typedef uint32_t pinctrl_soc_pin_t;

#define Z_PINCTRL_STATE_PIN_INIT(node_id, prop, idx)                                            \
        ((DT_PROP_BY_IDX(node_id, prop, idx))                                                   \
         | (DT_PROP(node_id, bias_pull_up)              << BFLB_PINMUX_PULL_UP_POS)             \
         | (DT_PROP(node_id, bias_pull_down)            << BFLB_PINMUX_PULL_DOWN_POS)           \
         | (DT_PROP(node_id, output_enable)             << BFLB_PINMUX_OE_POS)                  \
         | (DT_PROP(node_id, input_schmitt_enable)      << BFLB_PINMUX_SMT_POS)                 \
         | (DT_ENUM_IDX(node_id, drive_strength)        << BFLB_PINMUX_DRIVER_STRENGTH_POS)     \
        ),

#define Z_PINCTRL_STATE_PINS_INIT(node_id, prop)                               \
        {DT_FOREACH_CHILD_VARGS(DT_PHANDLE(node_id, prop),                     \
                                DT_FOREACH_PROP_ELEM, pinmux,                  \
                                Z_PINCTRL_STATE_PIN_INIT)}


#ifdef __cplusplus
}
#endif

/* clang-format on */

#endif /* ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_SOC_BFLB_COMMON_H_ */
```

## 70.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021-2025 Gerson Fernando Budke <nandojve@gmail.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 19 行

关闭 clang-format 自动排版（clang-format off）。

### 注释 3：原第 82 行

开启 clang-format 自动排版（clang-format on）。

### 注释 4：原第 84 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_SOC_BFLB_COMMON_H_`。

## 70.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__soc__bflb__common_8h.html)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pinctrl_soc_pin_t](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h.html#a022eeb1c811e7ef94d3a7a99cbda0e2d)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)

---

[上一章](P069_pinctrl-zynqmp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P071_device.h_源码浏览.md)
