---
id: learning.zephyr-docs.api-source-reference.page-657
title: pinctrl_nxp_siul2_common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__nxp__siul2__common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第657章\_pinctrl\_nxp\_siul2\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__nxp__siul2__common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__nxp__siul2__common_8h.html)。

## 657.1\_原始可见代码（Source Code）

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
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="adevicetree_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="apinctrl__rcar__common_8h_html_a022eeb1c811e7ef94d3a7a99cbda0e2d"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>

```c
/*
 * Copyright 2022-2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_NXP_SIUL2_COMMON_H_
#define ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_NXP_SIUL2_COMMON_H_

#include <zephyr/devicetree.h>
#include <zephyr/types.h>


struct pinctrl_soc_reg {
        uint8_t inst;
        uint16_t idx;
        uint32_t val;
};

typedef struct {
        struct pinctrl_soc_reg mscr;
        struct pinctrl_soc_reg imcr;
} pinctrl_soc_pin_t;

#define Z_PINCTRL_STATE_PIN_INIT(group, prop, idx)                                                 \
        {NXP_SIUL2_PINMUX_INIT(group, DT_PROP_BY_IDX(group, prop, idx))},

#define Z_PINCTRL_STATE_PINS_INIT(node_id, prop)                                                   \
        {                                                                                          \
                DT_FOREACH_CHILD_VARGS(DT_PHANDLE(node_id, prop), DT_FOREACH_PROP_ELEM, pinmux,    \
                                       Z_PINCTRL_STATE_PIN_INIT)                                   \
        }


#endif /* ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_NXP_SIUL2_COMMON_H_ */
```

## 657.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022-2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 52 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_NXP_SIUL2_COMMON_H_`。

## 657.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__nxp__siul2__common_8h.html)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pinctrl_soc_pin_t](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h.html#a022eeb1c811e7ef94d3a7a99cbda0e2d)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)

---

[上一章](P656_pinctrl_esp32_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P658_pinctrl_rcar_x5h_common.h_源码浏览.md)
