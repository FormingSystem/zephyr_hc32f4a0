---
id: learning.zephyr-docs.api-source-reference.page-658
title: pinctrl_rcar_x5h_common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__x5h__common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第658章\_pinctrl\_rcar\_x5h\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__x5h__common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__x5h__common_8h.html)。

## 658.1\_原始可见代码（Source Code）

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
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
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
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00078"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00089"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="adevicetree_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="apinctrl__rcar__common_8h_html_a022eeb1c811e7ef94d3a7a99cbda0e2d"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructpfc__bias__reg_html"></a>
<a id="astructpfc__bias__reg_html_aa096ddd0c55e1874be418e96a5824e48"></a>
<a id="astructpfc__bias__reg_html_ad5b3f9a184e18852279224bc8bd410f1"></a>
<a id="astructpfc__bias__reg_html_af52bea8a971a9d529b88de56a96ba2f6"></a>
<a id="astructpfc__drive__reg_html"></a>
<a id="astructpfc__drive__reg_html_a716001404ab11edd9fe7a1281afc41d3"></a>
<a id="astructpfc__drive__reg_html_a7fdf928c9474496c086cbcebfec6cd15"></a>
<a id="astructpfc__drive__reg_html_aaa4d83e9f4b91295c57e04420c80fddb"></a>
<a id="astructpfc__drive__reg_html_aaf9d7e2d485f6eb0801c31f9749ee096"></a>
<a id="astructpinctrl__soc__pin_html"></a>
<a id="astructpinctrl__soc__pin_html_a0a2ceae237c3321a4ce1a3dd7a031322"></a>
<a id="astructpinctrl__soc__pin_html_aa1e68145488d654ab03e114c3f9949a9"></a>
<a id="astructpinctrl__soc__pin_html_ae23bf05694cea7ddf3ebcafaf9f1c44d"></a>
<a id="astructrcar__pin__func_html"></a>
<a id="astructrcar__pin__func_html_a0e714822c49f80b771652183bd85f25a"></a>
<a id="astructrcar__pin__func_html_a90ca45273500d81009fb245d7e10fd84"></a>
<a id="astructrcar__pin__func_html_aeafc3b430ee3137afdc362027c6b058c"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright (c) 2026 BayLibre, SAS
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_RCAR_X5H_COMMON_H_
#define ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_RCAR_X5H_COMMON_H_


#include <stdint.h>
#include <zephyr/devicetree.h>
#include <zephyr/sys/util_macro.h>

struct rcar_pin_func {
        uint8_t group: 4;
        uint8_t bit: 5;
        uint8_t func: 4;
};

#define RCAR_PIN_FLAGS_PULL_SET BIT(0)
#define RCAR_PIN_FLAGS_PUEN     BIT(1)
#define RCAR_PIN_FLAGS_PUD      BIT(2)
#define RCAR_PIN_FLAGS_FUNC_SET BIT(3)

#define RCAR_PIN_PULL_UP      (RCAR_PIN_FLAGS_PULL_SET | RCAR_PIN_FLAGS_PUEN | RCAR_PIN_FLAGS_PUD)
#define RCAR_PIN_PULL_DOWN    (RCAR_PIN_FLAGS_PULL_SET | RCAR_PIN_FLAGS_PUEN)
#define RCAR_PIN_PULL_DISABLE RCAR_PIN_FLAGS_PULL_SET

typedef struct pinctrl_soc_pin {
        uint16_t pin;
        struct rcar_pin_func func;
        uint8_t flags;
        uint16_t drive_strength_microamp;
} pinctrl_soc_pin_t;

#define RCAR_ALTSEL(node_id) DT_PROP_BY_IDX(node_id, pin, 1)

#define RCAR_HAS_ALTSEL(node_id) DT_PROP_HAS_IDX(node_id, pin, 1)

#define RCAR_PIN_FUNC(node_id) {                 \
        ((RCAR_ALTSEL(node_id) >> 10U) & 0xFU),  \
        ((RCAR_ALTSEL(node_id) >> 14U) & 0x1FU), \
        ((RCAR_ALTSEL(node_id) & 0xFU))}

#define RCAR_PIN_FLAGS(node_id)                                  \
        DT_PROP(node_id, bias_pull_up) * RCAR_PIN_PULL_UP |      \
        DT_PROP(node_id, bias_pull_down) * RCAR_PIN_PULL_DOWN |  \
        DT_PROP(node_id, bias_disable) * RCAR_PIN_PULL_DISABLE | \
        RCAR_HAS_ALTSEL(node_id) * RCAR_PIN_FLAGS_FUNC_SET

#define RCAR_DT_PIN(node_id) {                                                  \
        .pin = DT_PROP_BY_IDX(node_id, pin, 0),                                 \
        .func = COND_CODE_1(RCAR_HAS_ALTSEL(node_id),                           \
                            (RCAR_PIN_FUNC(node_id)), ({0})),                   \
        .flags = RCAR_PIN_FLAGS(node_id),                                       \
        .drive_strength_microamp =                                              \
                COND_CODE_1(DT_NODE_HAS_PROP(node_id, drive_strength_microamp), \
                            (DT_PROP(node_id, drive_strength_microamp)), (0))},

#define Z_PINCTRL_STATE_PIN_INIT(node_id, state_prop, idx) \
        RCAR_DT_PIN(DT_PROP_BY_IDX(node_id, state_prop, idx))

#define Z_PINCTRL_STATE_PINS_INIT(node_id, prop) \
        {DT_FOREACH_PROP_ELEM(node_id, prop, Z_PINCTRL_STATE_PIN_INIT)}

struct pfc_drive_reg {
        uint32_t drvctrl0;
        uint32_t drvctrl1;
        uint32_t drvctrl2;
        const uint16_t pins[32];
};

struct pfc_bias_reg {
        uint32_t puen;
        uint32_t pud;
        const uint16_t pins[32];
};

#endif /* ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_RCAR_X5H_COMMON_H_ */
```

## 658.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 BayLibre, SAS。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 132 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_RCAR_X5H_COMMON_H_`。

## 658.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__x5h__common_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [rcar_pin_func](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [group](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md#a90ca45273500d81009fb245d7e10fd84)
- [bit](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md#a0e714822c49f80b771652183bd85f25a)
- [func](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md#aeafc3b430ee3137afdc362027c6b058c)
- [pinctrl_soc_pin](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [pin](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md#a0a2ceae237c3321a4ce1a3dd7a031322)
- [func](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md#aa1e68145488d654ab03e114c3f9949a9)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [drive_strength_microamp](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md#ae23bf05694cea7ddf3ebcafaf9f1c44d)
- [pinctrl_soc_pin_t](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h.html#a022eeb1c811e7ef94d3a7a99cbda0e2d)
- [pfc_drive_reg](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [drvctrl0](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md#aaf9d7e2d485f6eb0801c31f9749ee096)
- [drvctrl1](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md#a7fdf928c9474496c086cbcebfec6cd15)
- [drvctrl2](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md#a716001404ab11edd9fe7a1281afc41d3)
- [pins](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md#aaa4d83e9f4b91295c57e04420c80fddb)
- [pfc_bias_reg](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md)
- [puen](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md#af52bea8a971a9d529b88de56a96ba2f6)
- [pud](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md#ad5b3f9a184e18852279224bc8bd410f1)
- [pins](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md#aa096ddd0c55e1874be418e96a5824e48)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [pfc_bias_reg::pins](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md#aa096ddd0c55e1874be418e96a5824e48)
- [pfc_bias_reg::pud](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md#ad5b3f9a184e18852279224bc8bd410f1)
- [pfc_bias_reg::puen](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md#af52bea8a971a9d529b88de56a96ba2f6)
- [pfc_drive_reg::drvctrl2](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md#a716001404ab11edd9fe7a1281afc41d3)
- [pfc_drive_reg::drvctrl1](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md#a7fdf928c9474496c086cbcebfec6cd15)
- [pfc_drive_reg::pins](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md#aaa4d83e9f4b91295c57e04420c80fddb)
- [pfc_drive_reg::drvctrl0](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md#aaf9d7e2d485f6eb0801c31f9749ee096)
- [pinctrl_soc_pin::pin](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md#a0a2ceae237c3321a4ce1a3dd7a031322)
- [pinctrl_soc_pin::func](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md#aa1e68145488d654ab03e114c3f9949a9)
- [pinctrl_soc_pin::drive_strength_microamp](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md#ae23bf05694cea7ddf3ebcafaf9f1c44d)
- [rcar_pin_func::bit](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md#a0e714822c49f80b771652183bd85f25a)
- [rcar_pin_func::group](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md#a90ca45273500d81009fb245d7e10fd84)
- [rcar_pin_func::func](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md#aeafc3b430ee3137afdc362027c6b058c)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P657_pinctrl_nxp_siul2_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P659_pinctrl_soc_sam_common.h_源码浏览.md)
