---
id: learning.zephyr-docs.api-source-device-reference.page-30
title: pinctrl_rcar_common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_pinctrl\_rcar\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h.html)。

## 30.1\_原始可见代码（Source Code）

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
<a id="foldopen00016"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00038"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="foldopen00070"></a>
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
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00104"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="foldopen00115"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="adevicetree_8h_html"></a>
<a id="apinctrl-rcar-common_8h_html"></a>
<a id="apinctrl__rcar__common_8h_html_a022eeb1c811e7ef94d3a7a99cbda0e2d"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructpfc__bias__reg_html"></a>
<a id="astructpfc__bias__reg_html_aa096ddd0c55e1874be418e96a5824e48"></a>
<a id="astructpfc__bias__reg_html_ad5b3f9a184e18852279224bc8bd410f1"></a>
<a id="astructpfc__bias__reg_html_af52bea8a971a9d529b88de56a96ba2f6"></a>
<a id="astructpfc__drive__reg__field_html"></a>
<a id="astructpfc__drive__reg__field_html_a39e89d41227063647a0bbdc881a49b30"></a>
<a id="astructpfc__drive__reg__field_html_a7d65f9710f1ca64d162e50fc63cbd45c"></a>
<a id="astructpfc__drive__reg__field_html_a8cfedc171cbedd9c8dd24930e800c2c1"></a>
<a id="astructpfc__drive__reg_html"></a>
<a id="astructpfc__drive__reg_html_a92e5c3d645c3a1278f6e0b1afed677f4"></a>
<a id="astructpfc__drive__reg_html_ab9ae8bee56ea46c08ede93f67d1c520c"></a>
<a id="astructpinctrl__soc__pin_html"></a>
<a id="astructpinctrl__soc__pin_html_a0784ff8fd0192c54997ab5841153c82b"></a>
<a id="astructpinctrl__soc__pin_html_a0a2ceae237c3321a4ce1a3dd7a031322"></a>
<a id="astructpinctrl__soc__pin_html_a37e11e6cc80fdd3cedbbbee555e062ae"></a>
<a id="astructpinctrl__soc__pin_html_a8e7c595f1e24e227da45a2b5d5fad501"></a>
<a id="astructpinctrl__soc__pin_html_aa1e68145488d654ab03e114c3f9949a9"></a>
<a id="astructrcar__pin__func_html"></a>
<a id="astructrcar__pin__func_html_abc0b9a433a3b0e00da4a5fe733c31c7d"></a>
<a id="astructrcar__pin__func_html_acf66a4904ab66054f9f8c0f680157481"></a>
<a id="astructrcar__pin__func_html_aeafc3b430ee3137afdc362027c6b058c"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright (c) 2023 IoT.bzh
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_RCAR_COMMON_H_
#define ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_RCAR_COMMON_H_

#include <zephyr/devicetree.h>
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rcar-common.h>
#include <stdint.h>
#include <zephyr/sys/util_macro.h>

struct rcar_pin_func {
        uint8_t bank:5;      /* bank number 0 - 18 */
        uint8_t shift:5;     /* bit shift 0 - 28 */
        uint8_t func:4;      /* choice from 0x0 to 0xF */
};

#define RCAR_PIN_FLAGS_PULL_SET BIT(0)
#define RCAR_PIN_FLAGS_PUEN     BIT(1)
#define RCAR_PIN_FLAGS_PUD      BIT(2)
#define RCAR_PIN_FLAGS_FUNC_SET BIT(3)
#define RCAR_PIN_FLAGS_FUNC_DUMMY BIT(4)

#define RCAR_PIN_PULL_UP      (RCAR_PIN_FLAGS_PULL_SET | RCAR_PIN_FLAGS_PUEN | RCAR_PIN_FLAGS_PUD)
#define RCAR_PIN_PULL_DOWN    (RCAR_PIN_FLAGS_PULL_SET | RCAR_PIN_FLAGS_PUEN)
#define RCAR_PIN_PULL_DISABLE  RCAR_PIN_FLAGS_PULL_SET

typedef struct pinctrl_soc_pin {
        uint16_t pin;
        struct rcar_pin_func func;
        uint8_t flags;
        uint8_t drive_strength;
        uint8_t voltage;
} pinctrl_soc_pin_t;

#define RCAR_HAS_IPSR(node_id) DT_PROP_HAS_IDX(node_id, pin, 1)
#define RCAR_IPSR(node_id) COND_CODE_1(RCAR_HAS_IPSR(node_id), (DT_PROP_BY_IDX(node_id, pin, 1)), \
                                                               (0))

/* Offsets are defined in dt-bindings pinctrl-rcar-common.h */
#define RCAR_PIN_FUNC(node_id)                         \
        {                                              \
                ((RCAR_IPSR(node_id) >> 10U) & 0x1FU), \
                ((RCAR_IPSR(node_id) >> 4U) & 0x1FU),  \
                ((RCAR_IPSR(node_id) & 0xFU))          \
        }

#define RCAR_PIN_IS_FUNC_DUMMY(node_id)                                        \
        ((((RCAR_IPSR(node_id) >> 10U) & 0x1FU) == 0x1F) &&                    \
         (((RCAR_IPSR(node_id) >> 4U) & 0x1FU) == 0x1F) &&                     \
         ((RCAR_IPSR(node_id) & 0xFU) == 0xF))

#define RCAR_PIN_FLAGS(node_id)                                                \
        DT_PROP(node_id, bias_pull_up)   * RCAR_PIN_PULL_UP |                  \
        DT_PROP(node_id, bias_pull_down) * RCAR_PIN_PULL_DOWN |                \
        DT_PROP(node_id, bias_disable)   * RCAR_PIN_PULL_DISABLE |             \
        RCAR_HAS_IPSR(node_id) * RCAR_PIN_FLAGS_FUNC_SET |                     \
        RCAR_PIN_IS_FUNC_DUMMY(node_id) * RCAR_PIN_FLAGS_FUNC_DUMMY

#define RCAR_DT_PIN(node_id)                                                   \
        {                                                                      \
                .pin = DT_PROP_BY_IDX(node_id, pin, 0),                        \
                .func = COND_CODE_1(RCAR_HAS_IPSR(node_id),                    \
                                    (RCAR_PIN_FUNC(node_id)), ({0})),          \
                .flags = RCAR_PIN_FLAGS(node_id),                              \
                .drive_strength =                                              \
                        COND_CODE_1(DT_NODE_HAS_PROP(node_id, drive_strength), \
                                    (DT_PROP(node_id, drive_strength)), (0)),  \
                .voltage = COND_CODE_1(DT_NODE_HAS_PROP(node_id,               \
                                                        power_source),         \
                                       (DT_PROP(node_id, power_source)),       \
                                       (PIN_VOLTAGE_NONE)),                    \
        },

#define Z_PINCTRL_STATE_PIN_INIT(node_id, state_prop, idx) \
        RCAR_DT_PIN(DT_PROP_BY_IDX(node_id, state_prop, idx))

#define Z_PINCTRL_STATE_PINS_INIT(node_id, prop) \
        { DT_FOREACH_PROP_ELEM(node_id, prop, Z_PINCTRL_STATE_PIN_INIT) }

struct pfc_drive_reg_field {
        uint16_t pin;
        uint8_t offset;
        uint8_t size;
};

struct pfc_drive_reg {
        uint32_t reg;
        const struct pfc_drive_reg_field fields[8];
};

struct pfc_bias_reg {
        uint32_t puen;
        uint32_t pud;
        const uint16_t pins[32];
};

#define RCAR_IS_GP_PIN(pin) (pin < PIN_NOGPSR_START)

#endif /* ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_RCAR_COMMON_H_ */
```

## 30.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 IoT.bzh。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 17 行

组编号（Bank Number）：0～18。

### 注释 3：原第 18 行

位移量（Bit Shift）：0～28。

### 注释 4：原第 19 行

选择值（Choice）：0x0～0xF。

### 注释 5：原第 50 行

偏移（Offsets）在设备树绑定（DT Bindings）的 `pinctrl-rcar-common.h` 中定义。

### 注释 6：原第 129 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_RCAR_COMMON_H_`。

## 30.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h.html)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/dt-bindings/pinctrl/renesas/pinctrl-rcar-common.h](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rcar-common_8h.html)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [rcar_pin_func](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bank](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md#abc0b9a433a3b0e00da4a5fe733c31c7d)
- [shift](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md#acf66a4904ab66054f9f8c0f680157481)
- [func](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md#aeafc3b430ee3137afdc362027c6b058c)
- [pinctrl_soc_pin](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [pin](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md#a0a2ceae237c3321a4ce1a3dd7a031322)
- [func](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md#aa1e68145488d654ab03e114c3f9949a9)
- [flags](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md#a8e7c595f1e24e227da45a2b5d5fad501)
- [drive_strength](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md#a0784ff8fd0192c54997ab5841153c82b)
- [voltage](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md#a37e11e6cc80fdd3cedbbbee555e062ae)
- [pinctrl_soc_pin_t](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h.html#a022eeb1c811e7ef94d3a7a99cbda0e2d)
- [pfc_drive_reg_field](../device_power_control_model_reference/P058_pfc_drive_reg_field_结构体.md)
- [pin](../device_power_control_model_reference/P058_pfc_drive_reg_field_结构体.md#a39e89d41227063647a0bbdc881a49b30)
- [offset](../device_power_control_model_reference/P058_pfc_drive_reg_field_结构体.md#a8cfedc171cbedd9c8dd24930e800c2c1)
- [size](../device_power_control_model_reference/P058_pfc_drive_reg_field_结构体.md#a7d65f9710f1ca64d162e50fc63cbd45c)
- [pfc_drive_reg](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [reg](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md#ab9ae8bee56ea46c08ede93f67d1c520c)
- [fields](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md#a92e5c3d645c3a1278f6e0b1afed677f4)
- [pfc_bias_reg](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md)
- [puen](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md#af52bea8a971a9d529b88de56a96ba2f6)
- [pud](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md#ad5b3f9a184e18852279224bc8bd410f1)
- [pins](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md#aa096ddd0c55e1874be418e96a5824e48)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [pinctrl-rcar-common.h](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rcar-common_8h.html)
- [pfc_bias_reg::pins](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md#aa096ddd0c55e1874be418e96a5824e48)
- [pfc_bias_reg::pud](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md#ad5b3f9a184e18852279224bc8bd410f1)
- [pfc_bias_reg::puen](../device_power_control_model_reference/P056_pfc_bias_reg_结构体.md#af52bea8a971a9d529b88de56a96ba2f6)
- [pfc_drive_reg_field::pin](../device_power_control_model_reference/P058_pfc_drive_reg_field_结构体.md#a39e89d41227063647a0bbdc881a49b30)
- [pfc_drive_reg_field::size](../device_power_control_model_reference/P058_pfc_drive_reg_field_结构体.md#a7d65f9710f1ca64d162e50fc63cbd45c)
- [pfc_drive_reg_field::offset](../device_power_control_model_reference/P058_pfc_drive_reg_field_结构体.md#a8cfedc171cbedd9c8dd24930e800c2c1)
- [pfc_drive_reg::fields](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md#a92e5c3d645c3a1278f6e0b1afed677f4)
- [pfc_drive_reg::reg](../device_power_control_model_reference/P057_pfc_drive_reg_结构体.md#ab9ae8bee56ea46c08ede93f67d1c520c)
- [pinctrl_soc_pin::drive_strength](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md#a0784ff8fd0192c54997ab5841153c82b)
- [pinctrl_soc_pin::pin](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md#a0a2ceae237c3321a4ce1a3dd7a031322)
- [pinctrl_soc_pin::voltage](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md#a37e11e6cc80fdd3cedbbbee555e062ae)
- [pinctrl_soc_pin::flags](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md#a8e7c595f1e24e227da45a2b5d5fad501)
- [pinctrl_soc_pin::func](../device_power_control_model_reference/P060_pinctrl_soc_pin_结构体.md#aa1e68145488d654ab03e114c3f9949a9)
- [rcar_pin_func::bank](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md#abc0b9a433a3b0e00da4a5fe733c31c7d)
- [rcar_pin_func::shift](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md#acf66a4904ab66054f9f8c0f680157481)
- [rcar_pin_func::func](../device_power_control_model_reference/P072_rcar_pin_func_结构体.md#aeafc3b430ee3137afdc362027c6b058c)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P029_nrf_clock_control.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P031_pwd.h_源码浏览.md)
