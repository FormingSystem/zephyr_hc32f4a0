---
id: learning.zephyr-docs.api-source-runtime-reference.page-31
title: ifx_cat1-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ifx__cat1-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_ifx\_cat1-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ifx__cat1-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ifx__cat1-pinctrl_8h.html)。

## 31.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00011"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
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
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="foldopen00069"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
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
<a id="foldopen00118"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>

```c
/* Copyright 2022 Cypress Semiconductor Corporation (an Infineon company) or
 * an affiliate of Cypress Semiconductor Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_IFX_CAT1_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_IFX_CAT1_PINCTRL_H_

#define SOC_PINMUX_PORT_POS                                (0)
#define SOC_PINMUX_PORT_MASK                               (0xFFul << SOC_PINMUX_PORT_POS)
#define SOC_PINMUX_PIN_POS                                 (8)
#define SOC_PINMUX_PIN_MASK                                (0xFFul << SOC_PINMUX_PIN_POS)
#define SOC_PINMUX_HSIOM_FUNC_POS                          (16)
#define SOC_PINMUX_HSIOM_MASK                              (0xFFul << SOC_PINMUX_HSIOM_FUNC_POS)
#define SOC_PINMUX_SIGNAL_POS                              (24)
#define SOC_PINMUX_SIGNAL_MASK                             (0xFFul << SOC_PINMUX_SIGNAL_POS)

#define HSIOM_SEL_GPIO                                     (0)
#define HSIOM_SEL_GPIO_DSI                                 (1)
#define HSIOM_SEL_DSI_DSI                                  (2)
#define HSIOM_SEL_DSI_GPIO                                 (3)
#define HSIOM_SEL_AMUXA                                    (4)
#define HSIOM_SEL_AMUXB                                    (5)
#define HSIOM_SEL_AMUXA_DSI                                (6)
#define HSIOM_SEL_AMUXB_DSI                                (7)
#define HSIOM_SEL_ACT_0                                    (8)
#define HSIOM_SEL_ACT_1                                    (9)
#define HSIOM_SEL_ACT_2                                    (10)
#define HSIOM_SEL_ACT_3                                    (11)
#define HSIOM_SEL_DS_0                                     (12)
#define HSIOM_SEL_DS_1                                     (13)
#define HSIOM_SEL_DS_2                                     (14)
#define HSIOM_SEL_DS_3                                     (15)
#define HSIOM_SEL_ACT_4                                    (16)
#define HSIOM_SEL_ACT_5                                    (17)
#define HSIOM_SEL_ACT_6                                    (18)
#define HSIOM_SEL_ACT_7                                    (19)
#define HSIOM_SEL_ACT_8                                    (20)
#define HSIOM_SEL_ACT_9                                    (21)
#define HSIOM_SEL_ACT_10                                   (22)
#define HSIOM_SEL_ACT_11                                   (23)
#define HSIOM_SEL_ACT_12                                   (24)
#define HSIOM_SEL_ACT_13                                   (25)
#define HSIOM_SEL_ACT_14                                   (26)
#define HSIOM_SEL_ACT_15                                   (27)
#define HSIOM_SEL_DS_4                                     (28)
#define HSIOM_SEL_DS_5                                     (29)
#define HSIOM_SEL_DS_6                                     (30)
#define HSIOM_SEL_DS_7                                     (31)

#define DT_CAT1_DRIVE_MODE_INFO(peripheral_signal) \
        CAT1_PIN_MAP_DRIVE_MODE_##peripheral_signal

#define DT_CAT1_PINMUX(port, pin, hsiom) \
        ((port << SOC_PINMUX_PORT_POS) | \
         (pin << SOC_PINMUX_PIN_POS) |   \
         (hsiom << SOC_PINMUX_HSIOM_FUNC_POS))

#define IFX_SMIF0_PORT0               (22)
#define IFX_SMIF0_PORT1               (23)
#define IFX_SMIF0_PORT2               (24)
#define IFX_SMIF1_PORT0               (25)
#define IFX_SMIF1_PORT1               (26)
#define IFX_SMIF1_PORT2               (27)

/* Redefine DT GPIO label (Px) to CYHAL port macros (CYHAL_PORT_x) */
#define P0  CYHAL_PORT_0
#define P1  CYHAL_PORT_1
#define P2  CYHAL_PORT_2
#define P3  CYHAL_PORT_3
#define P4  CYHAL_PORT_4
#define P5  CYHAL_PORT_5
#define P6  CYHAL_PORT_6
#define P7  CYHAL_PORT_7
#define P8  CYHAL_PORT_8
#define P9  CYHAL_PORT_9
#define P10 CYHAL_PORT_10
#define P11 CYHAL_PORT_11
#define P12 CYHAL_PORT_12
#define P13 CYHAL_PORT_13
#define P14 CYHAL_PORT_14
#define P15 CYHAL_PORT_15
#define P16 CYHAL_PORT_16
#define P17 CYHAL_PORT_17
#define P18 CYHAL_PORT_18
#define P19 CYHAL_PORT_19
#define P20 CYHAL_PORT_20

/* Returns CYHAL GPIO from Board device tree GPIO configuration
 * CYHAL_GET_GPIO(port_number, pin_number),
 * port_number = ((REG ADDR of node) - (REG ADDR of gpio_prt0)) / (REG SIZE of gpio_prt0)
 * pin_number  = DT_PHA_BY_IDX(node, gpios_prop, 0, pin)
 */
#define DT_GET_CYHAL_GPIO_FROM_DT_GPIOS(node, gpios_prop)                          \
        CYHAL_GET_GPIO(                                                            \
                (DT_REG_ADDR_BY_IDX(DT_GPIO_CTLR_BY_IDX(node, gpios_prop, 0), 0) - \
                 DT_REG_ADDR_BY_IDX(DT_NODELABEL(gpio_prt0), 0)) /                 \
                DT_REG_ADDR_BY_IDX(DT_NODELABEL(gpio_prt0), 1),                    \
                DT_PHA_BY_IDX(node, gpios_prop, 0, pin)                            \
                )

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_IFX_CAT1_PINCTRL_H_ */
```

## 31.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022 Cypress Semiconductor Corporation（Infineon 旗下公司）或 Cypress Semiconductor Corporation 的关联公司。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 90 行

将设备树（DT）GPIO 标签 `Px` 重新定义为 CYHAL 端口宏 `CYHAL_PORT_x`。

### 注释 3：原第 113 行

根据开发板设备树中的 GPIO 配置返回 CYHAL GPIO：

```text
CYHAL_GET_GPIO(port_number, pin_number),
port_number = ((REG ADDR of node) - (REG ADDR of gpio_prt0)) / (REG SIZE of gpio_prt0)
pin_number  = DT_PHA_BY_IDX(node, gpios_prop, 0, pin)
```

其中 `REG ADDR` 表示寄存器地址，`REG SIZE` 表示寄存器区域大小。

### 注释 4：原第 126 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_IFX_CAT1_PINCTRL_H_`。

## 31.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ifx__cat1-pinctrl_8h.html)

---

[上一章](P030_hl78xx_apis.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P032_ifx_clock_source_psoc4xx.h_源码浏览.md)
