---
id: learning.zephyr-docs.api-source-reference.page-659
title: pinctrl_soc_sam_common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__soc__sam__common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第659章\_pinctrl\_soc\_sam\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__soc__sam__common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__soc__sam__common_8h.html)。

## 659.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00032"></a>
<a id="l00033"></a>
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
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
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
<a id="l00098"></a>
<a id="foldopen00105"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="foldopen00108"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="adevicetree_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="apinctrl__rcar__common_8h_html_a022eeb1c811e7ef94d3a7a99cbda0e2d"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2022, Gerson Fernando Budke <nandojve@gmail.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_SOC_SAM_COMMON_H_
#define ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_SOC_SAM_COMMON_H_

#include <zephyr/devicetree.h>
#include <zephyr/types.h>
#include <dt-bindings/pinctrl/atmel_sam_pinctrl.h>

#ifdef __cplusplus
extern "C" {
#endif


typedef uint32_t pinctrl_soc_pin_t;

#if defined(CONFIG_SOC_FAMILY_ATMEL_SAM)
#define Z_PINCTRL_STATE_PIN_INIT(node_id, prop, idx)                            \
        ((DT_PROP_BY_IDX(node_id, prop, idx)   << SAM_PINCTRL_PINMUX_POS)       \
         | (DT_PROP(node_id, bias_pull_up)     << SAM_PINCTRL_PULLUP_POS)       \
         | (DT_PROP(node_id, bias_pull_down)   << SAM_PINCTRL_PULLDOWN_POS)     \
         | (DT_PROP(node_id, drive_open_drain) << SAM_PINCTRL_OPENDRAIN_POS)    \
        ),
#else /* CONFIG_SOC_FAMILY_ATMEL_SAM0 */
#define Z_PINCTRL_STATE_PIN_INIT(node_id, prop, idx)                              \
        ((DT_PROP_BY_IDX(node_id, prop, idx)     << SAM_PINCTRL_PINMUX_POS)       \
         | (DT_PROP(node_id, bias_pull_up)       << SAM_PINCTRL_PULLUP_POS)       \
         | (DT_PROP(node_id, bias_pull_down)     << SAM_PINCTRL_PULLDOWN_POS)     \
         | (DT_PROP(node_id, input_enable)       << SAM_PINCTRL_INPUTENABLE_POS)  \
         | (DT_PROP(node_id, output_enable)      << SAM_PINCTRL_OUTPUTENABLE_POS) \
         | (DT_ENUM_IDX(node_id, drive_strength) << SAM_PINCTRL_DRIVESTRENGTH_POS)\
        ),
#endif

#define Z_PINCTRL_STATE_PINS_INIT(node_id, prop)                                \
        {DT_FOREACH_CHILD_VARGS(DT_PHANDLE(node_id, prop),                      \
                                DT_FOREACH_PROP_ELEM, pinmux,                   \
                                Z_PINCTRL_STATE_PIN_INIT)}




#define SAM_PINCTRL_FLAGS_DEFAULT       (0U)
#define SAM_PINCTRL_FLAGS_POS           (0U)
#define SAM_PINCTRL_FLAGS_MASK          (0x3F << SAM_PINCTRL_FLAGS_POS)
#define SAM_PINCTRL_FLAG_MASK           (1U)
#define SAM_PINCTRL_PULLUP_POS          (SAM_PINCTRL_FLAGS_POS)
#define SAM_PINCTRL_PULLUP              (1U << SAM_PINCTRL_PULLUP_POS)
#define SAM_PINCTRL_PULLDOWN_POS        (SAM_PINCTRL_PULLUP_POS + 1U)
#define SAM_PINCTRL_PULLDOWN            (1U << SAM_PINCTRL_PULLDOWN_POS)
#define SAM_PINCTRL_OPENDRAIN_POS       (SAM_PINCTRL_PULLDOWN_POS + 1U)
#define SAM_PINCTRL_OPENDRAIN           (1U << SAM_PINCTRL_OPENDRAIN_POS)
#define SAM_PINCTRL_INPUTENABLE_POS     (SAM_PINCTRL_OPENDRAIN_POS + 1U)
#define SAM_PINCTRL_INPUTENABLE         (1U << SAM_PINCTRL_INPUTENABLE_POS)
#define SAM_PINCTRL_OUTPUTENABLE_POS    (SAM_PINCTRL_INPUTENABLE_POS + 1U)
#define SAM_PINCTRL_OUTPUTENABLE        (1U << SAM_PINCTRL_OUTPUTENABLE_POS)
#define SAM_PINCTRL_DRIVESTRENGTH_POS   (SAM_PINCTRL_OUTPUTENABLE_POS + 1U)
#define SAM_PINCTRL_DRIVESTRENGTH       (1U << SAM_PINCTRL_DRIVESTRENGTH_POS)


#define SAM_PINCTRL_FLAG_GET(pincfg, pos) \
        (((pincfg) >> pos) & SAM_PINCTRL_FLAG_MASK)

#define SAM_PINCTRL_FLAGS_GET(pincfg) \
        (((pincfg) >> SAM_PINCTRL_FLAGS_POS) & SAM_PINCTRL_FLAGS_MASK)

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_SOC_SAM_COMMON_H_ */
```

## 659.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022, Gerson Fernando Budke <nandojve@gmail.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 48 行

条件编译配置（Configuration）标记：`CONFIG_SOC_FAMILY_ATMEL_SAM0`。

### 注释 3：原第 115 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_SOC_SAM_COMMON_H_`。

## 659.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__soc__sam__common_8h.html)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pinctrl_soc_pin_t](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h.html#a022eeb1c811e7ef94d3a7a99cbda0e2d)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)

---

[上一章](P658_pinctrl_rcar_x5h_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P660_pio_rpi_pico.h_源码浏览.md)
