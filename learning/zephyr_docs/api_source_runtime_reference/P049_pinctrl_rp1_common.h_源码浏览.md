---
id: learning.zephyr-docs.api-source-runtime-reference.page-49
title: pinctrl_rp1_common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rp1__common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_pinctrl\_rp1\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rp1__common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rp1__common_8h.html)。

## 49.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00033"></a>
<a id="l00034"></a>
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
<a id="l00098"></a>
<a id="l00099"></a>
<a id="arp1-pinctrl_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2025 TOKITA Hiroshi
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_RP1_COMMON_H_
#define ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_RP1_COMMON_H_


#include <stdint.h>
#include <zephyr/dt-bindings/pinctrl/rp1-pinctrl.h>

#define RP1_GET_PIN_NUM(pinctrl)  (((pinctrl) >> RP1_PIN_NUM_POS) & RP1_PIN_NUM_MASK)

#define RP1_GET_ALT_FUNC(pinctrl) (((pinctrl) >> RP1_ALT_FUNC_POS) & RP1_ALT_FUNC_MASK)


/* Initialize one RP1 pinctrl entry from a devicetree property item. */
#define RASPBERRYPI_RP1_PINCTRL_STATE_PIN_INIT(node_id, prop, idx)                                 \
        {                                                                                          \
                .pin_num = RP1_GET_PIN_NUM(DT_PROP_BY_IDX(node_id, prop, idx)),                    \
                .alt_func = RP1_GET_ALT_FUNC(DT_PROP_BY_IDX(node_id, prop, idx)),                  \
                .f_m = DT_PROP(node_id, raspberrypi_f_m),                                          \
                .oe_override = DT_PROP(node_id, raspberrypi_oe_override),                          \
                .out_override = DT_PROP(node_id, raspberrypi_out_override),                        \
                .in_override = DT_PROP(node_id, raspberrypi_in_override),                          \
                .irqmask_edge_low = DT_PROP(node_id, raspberrypi_irqmask_edge_low),                \
                .irqmask_edge_high = DT_PROP(node_id, raspberrypi_irqmask_edge_high),              \
                .irqmask_level_low = DT_PROP(node_id, raspberrypi_irqmask_level_low),              \
                .irqmask_level_high = DT_PROP(node_id, raspberrypi_irqmask_level_high),            \
                .irqmask_f_edge_low = DT_PROP(node_id, raspberrypi_irqmask_f_edge_low),            \
                .irqmask_f_edge_high = DT_PROP(node_id, raspberrypi_irqmask_f_edge_high),          \
                .irqmask_db_level_low = DT_PROP(node_id, raspberrypi_irqmask_db_level_low),        \
                .irqmask_db_level_high = DT_PROP(node_id, raspberrypi_irqmask_db_level_high),      \
                .irq_override = DT_PROP(node_id, raspberrypi_irq_override),                        \
                .slew_rate = DT_ENUM_IDX(node_id, slew_rate),                                      \
                .schmitt_enable = DT_PROP(node_id, input_schmitt_enable),                          \
                .pulldown = DT_PROP(node_id, bias_pull_down),                                      \
                .pullup = DT_PROP(node_id, bias_pull_up),                                          \
                .drive_strength = DT_ENUM_IDX(node_id, drive_strength),                            \
                .input_enable = DT_PROP(node_id, input_enable),                                    \
                .output_disable = DT_PROP(node_id, output_disable),                                \
        }

/* Per-pin RP1 pinctrl settings expanded from devicetree properties. */
struct raspberrypi_rp1_pinctrl_pinconfig {
        uint32_t pin_num: 5;
        uint32_t alt_func: 5;
        uint32_t f_m: 7;
        uint32_t oe_override: 2;
        uint32_t out_override: 2;
        uint32_t in_override: 2;
        uint32_t irqmask_edge_low: 1;
        uint32_t irqmask_edge_high: 1;
        uint32_t irqmask_level_low: 1;
        uint32_t irqmask_level_high: 1;
        uint32_t irqmask_f_edge_low: 1;
        uint32_t irqmask_f_edge_high: 1;
        uint32_t irqmask_db_level_low: 1;
        uint32_t irqmask_db_level_high: 1;
        uint32_t irq_override: 2;
        uint32_t slew_rate: 1;
        uint32_t schmitt_enable: 1;
        uint32_t pulldown: 1;
        uint32_t pullup: 1;
        uint32_t drive_strength: 2;
        uint32_t input_enable: 1;
        uint32_t output_disable: 1;
};

/* Apply one RP1 pin configuration entry. */
int raspberrypi_rp1_pinctrl_configure_pin(const struct raspberrypi_rp1_pinctrl_pinconfig *pin);


#endif /* ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_RP1_COMMON_H_ */
```

## 49.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 TOKITA Hiroshi。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 39 行

根据一个设备树属性项初始化一个 RP1 引脚控制（Pinctrl）条目。

### 注释 3：原第 66 行

从设备树属性展开得到的逐引脚 RP1 引脚控制设置。

### 注释 4：原第 92 行

应用一个 RP1 引脚配置条目。

### 注释 5：原第 99 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_RP1_COMMON_H_`。

## 49.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rp1__common_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/dt-bindings/pinctrl/rp1-pinctrl.h](https://docs.zephyrproject.org/latest/doxygen/html/rp1-pinctrl_8h.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [rp1-pinctrl.h](https://docs.zephyrproject.org/latest/doxygen/html/rp1-pinctrl_8h.html)

---

[上一章](P048_pinctrl_bcm2712_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P050_sched.h_源码浏览.md)
