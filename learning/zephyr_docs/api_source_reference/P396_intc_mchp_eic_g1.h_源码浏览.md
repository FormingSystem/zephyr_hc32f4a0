---
id: learning.zephyr-docs.api-source-reference.page-396
title: intc_mchp_eic_g1.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第396章\_intc\_mchp\_eic\_g1.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html)。

## 396.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="foldopen00109"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aintc__mchp__eic__g1_8h_html_a3a92a102ec5b77cf35016dae7cacf41f"></a>
<a id="aintc__mchp__eic__g1_8h_html_a3a92a102ec5b77cf35016dae7cacf41fa0043919874fba56cfecf81b6af88c511"></a>
<a id="aintc__mchp__eic__g1_8h_html_a3a92a102ec5b77cf35016dae7cacf41fa76c21794771849ca27bfeae560393442"></a>
<a id="aintc__mchp__eic__g1_8h_html_a3a92a102ec5b77cf35016dae7cacf41fa871bfb5c942a54250d8b03c0c5c9ed02"></a>
<a id="aintc__mchp__eic__g1_8h_html_a3a92a102ec5b77cf35016dae7cacf41fa93d49c3438952c6d76d2cbb61477f496"></a>
<a id="aintc__mchp__eic__g1_8h_html_a3a92a102ec5b77cf35016dae7cacf41face8d3c3419e2ea54cd9b6ba9aa83bbf8"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913f"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913fa13a8e7a14cbb3eb0a29e4adb153fddf1"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913fa1b09c3dcf5e1e6bb4383d59d8d59139e"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913fa2480037d5320d82b51ef791602e86744"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913fa2a19ee62bd2238ed0b230128460eea0e"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913fa3e3128f973a6b4e3c6c9ebff72214c27"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913fa455d858d964458f84acd4710e0792f0b"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913fa478a0b1c6ea938e962c5b9847472dd51"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913fa4a4e98221146268888edd655465222c5"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913fa61d79f894d2a9099f0a1926d22e6dd29"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913fa9f26cc1a0ba03a5dc234704ca1009331"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913faa755a252e4d1b2c4aff1824dece02377"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913fab0aa7cf6c7e4544caeed49f8f1370465"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913fab2da776e2843f1b4de58bb365e661baa"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913fab447e3383e4b1bc48c53265c74b00d33"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913fab634c21298a333b2461b66f0169ec3bd"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913fab7107f342e53d5064cfcee8d791fbed8"></a>
<a id="aintc__mchp__eic__g1_8h_html_a43ecd6415e664dc6bda9c3374f86913fadcef4e5bb50e89389a7a543bbab4c7fe"></a>
<a id="aintc__mchp__eic__g1_8h_html_a710e45791e99d5f4e511923ea3d116fc"></a>
<a id="aintc__mchp__eic__g1_8h_html_a9055a4d254b3d4c8cf2124b0459e8272"></a>
<a id="aintc__mchp__eic__g1_8h_html_aec15300a23f1397ed93625d5418d3cc4"></a>
<a id="aintc__mchp__eic__g1_8h_html_aec15300a23f1397ed93625d5418d3cc4a1053c0ce57a811b634c24e4f1342689f"></a>
<a id="aintc__mchp__eic__g1_8h_html_aec15300a23f1397ed93625d5418d3cc4aa7a9d95ee540de2dfbec299e0b7fddec"></a>
<a id="aintc__mchp__eic__g1_8h_html_aec15300a23f1397ed93625d5418d3cc4aab13ef018cd24524b971a61baacf25f3"></a>
<a id="aintc__mchp__eic__g1_8h_html_aec15300a23f1397ed93625d5418d3cc4abb7842e8dbb3a8a2e60d978172ca8fa8"></a>
<a id="aintc__mchp__eic__g1_8h_html_aec15300a23f1397ed93625d5418d3cc4af49402c39ba9da1b0e0f7da49474c7a7"></a>
<a id="aintc__mchp__eic__g1_8h_html_af05976a876021ebc3900a52209a49c00"></a>
<a id="aintc__mchp__eic__g1_8h_html_af2698011a2a1dfee017645dda7b72d0d"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructeic__config__params_html"></a>
<a id="astructeic__config__params_html_a29d70eaee32a2835f5514e7ce168ec14"></a>
<a id="astructeic__config__params_html_a44492d0b42ea6ccd0545726467ca82aa"></a>
<a id="astructeic__config__params_html_a95858dedfde317eb8f70d15567a75ee6"></a>
<a id="astructeic__config__params_html_a9de61236e03ae6fff8a111dcd1a30497"></a>
<a id="astructeic__config__params_html_a9f5b10cb7dc39d11c263e7e88e583ac6"></a>
<a id="astructeic__config__params_html_ab7422775ca216017cbb74444bd1df6a4"></a>
<a id="astructeic__config__params_html_add7f563e55292364350b66cbb47f1f21"></a>

```c
/*
 * Copyright (c) 2025-2026 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_MCHP_EIC_G1_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_MCHP_EIC_G1_H_

#include <soc.h>
#include <zephyr/types.h>
#include <zephyr/drivers/gpio.h>

typedef void (*mchp_eic_callback_t)(uint32_t pins, void *data);

enum mchp_eic_trigger {
        MCHP_EIC_RISING = 1,
        MCHP_EIC_FALLING,
        MCHP_EIC_BOTH,
        MCHP_EIC_HIGH,
        MCHP_EIC_LOW,
};

enum mchp_gpio_port_id {
        MCHP_PORT_ID0 = 0,
        MCHP_PORT_ID1,
        MCHP_PORT_ID2,
        MCHP_PORT_ID3,
        MCHP_PORT_ID_MAX,
};

enum mchp_eic_line {
        EIC_LINE_0 = 0,
        EIC_LINE_1,
        EIC_LINE_2,
        EIC_LINE_3,
        EIC_LINE_4,
        EIC_LINE_5,
        EIC_LINE_6,
        EIC_LINE_7,
        EIC_LINE_8,
        EIC_LINE_9,
        EIC_LINE_10,
        EIC_LINE_11,
        EIC_LINE_12,
        EIC_LINE_13,
        EIC_LINE_14,
        EIC_LINE_15,
        EIC_LINE_MAX,
};

struct eic_config_params {
        enum mchp_eic_trigger trig_type;

        uint8_t pin_num;

        uint8_t port_id;

        bool debounce;

        void *gpio_data;

        port_group_registers_t *port_addr;

        mchp_eic_callback_t eic_line_callback;
};

int eic_mchp_config_interrupt(struct eic_config_params *eic_pin_config);

uint32_t eic_mchp_interrupt_pending(uint8_t port_id);

int eic_mchp_disable_interrupt(struct eic_config_params *eic_pin_config);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_MCHP_EIC_G1_H_ */
```

## 396.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025-2026 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 174 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_MCHP_EIC_G1_H_`。

## 396.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [mchp_eic_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a710e45791e99d5f4e511923ea3d116fc)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mchp_eic_trigger](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a3a92a102ec5b77cf35016dae7cacf41f)
- [MCHP_EIC_RISING](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a3a92a102ec5b77cf35016dae7cacf41fa93d49c3438952c6d76d2cbb61477f496)
- [MCHP_EIC_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a3a92a102ec5b77cf35016dae7cacf41face8d3c3419e2ea54cd9b6ba9aa83bbf8)
- [MCHP_EIC_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a3a92a102ec5b77cf35016dae7cacf41fa76c21794771849ca27bfeae560393442)
- [MCHP_EIC_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a3a92a102ec5b77cf35016dae7cacf41fa0043919874fba56cfecf81b6af88c511)
- [MCHP_EIC_LOW](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a3a92a102ec5b77cf35016dae7cacf41fa871bfb5c942a54250d8b03c0c5c9ed02)
- [mchp_gpio_port_id](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#aec15300a23f1397ed93625d5418d3cc4)
- [MCHP_PORT_ID0](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#aec15300a23f1397ed93625d5418d3cc4aab13ef018cd24524b971a61baacf25f3)
- [MCHP_PORT_ID1](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#aec15300a23f1397ed93625d5418d3cc4af49402c39ba9da1b0e0f7da49474c7a7)
- [MCHP_PORT_ID2](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#aec15300a23f1397ed93625d5418d3cc4aa7a9d95ee540de2dfbec299e0b7fddec)
- [MCHP_PORT_ID3](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#aec15300a23f1397ed93625d5418d3cc4abb7842e8dbb3a8a2e60d978172ca8fa8)
- [MCHP_PORT_ID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#aec15300a23f1397ed93625d5418d3cc4a1053c0ce57a811b634c24e4f1342689f)
- [mchp_eic_line](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913f)
- [EIC_LINE_0](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913fab0aa7cf6c7e4544caeed49f8f1370465)
- [EIC_LINE_1](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913fa2a19ee62bd2238ed0b230128460eea0e)
- [EIC_LINE_2](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913fa13a8e7a14cbb3eb0a29e4adb153fddf1)
- [EIC_LINE_3](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913fa2480037d5320d82b51ef791602e86744)
- [EIC_LINE_4](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913fab7107f342e53d5064cfcee8d791fbed8)
- [EIC_LINE_5](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913fa3e3128f973a6b4e3c6c9ebff72214c27)
- [EIC_LINE_6](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913fa478a0b1c6ea938e962c5b9847472dd51)
- [EIC_LINE_7](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913fab447e3383e4b1bc48c53265c74b00d33)
- [EIC_LINE_8](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913fab2da776e2843f1b4de58bb365e661baa)
- [EIC_LINE_9](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913fab634c21298a333b2461b66f0169ec3bd)
- [EIC_LINE_10](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913fa455d858d964458f84acd4710e0792f0b)
- [EIC_LINE_11](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913fa4a4e98221146268888edd655465222c5)
- [EIC_LINE_12](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913faa755a252e4d1b2c4aff1824dece02377)
- [EIC_LINE_13](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913fadcef4e5bb50e89389a7a543bbab4c7fe)
- [EIC_LINE_14](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913fa1b09c3dcf5e1e6bb4383d59d8d59139e)
- [EIC_LINE_15](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913fa61d79f894d2a9099f0a1926d22e6dd29)
- [EIC_LINE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a43ecd6415e664dc6bda9c3374f86913fa9f26cc1a0ba03a5dc234704ca1009331)
- [eic_config_params](../platform_security_model_reference/P005_eic_config_params_结构体.md)
- [trig_type](../platform_security_model_reference/P005_eic_config_params_结构体.md#add7f563e55292364350b66cbb47f1f21)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [pin_num](../platform_security_model_reference/P005_eic_config_params_结构体.md#a44492d0b42ea6ccd0545726467ca82aa)
- [port_id](../platform_security_model_reference/P005_eic_config_params_结构体.md#a29d70eaee32a2835f5514e7ce168ec14)
- [debounce](../platform_security_model_reference/P005_eic_config_params_结构体.md#a9de61236e03ae6fff8a111dcd1a30497)
- [gpio_data](../platform_security_model_reference/P005_eic_config_params_结构体.md#ab7422775ca216017cbb74444bd1df6a4)
- [port_addr](../platform_security_model_reference/P005_eic_config_params_结构体.md#a9f5b10cb7dc39d11c263e7e88e583ac6)
- [eic_line_callback](../platform_security_model_reference/P005_eic_config_params_结构体.md#a95858dedfde317eb8f70d15567a75ee6)
- [eic_mchp_config_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#af05976a876021ebc3900a52209a49c00)
- [eic_mchp_interrupt_pending](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#af2698011a2a1dfee017645dda7b72d0d)
- [eic_mchp_disable_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/intc__mchp__eic__g1_8h.html#a9055a4d254b3d4c8cf2124b0459e8272)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [eic_config_params::port_id](../platform_security_model_reference/P005_eic_config_params_结构体.md#a29d70eaee32a2835f5514e7ce168ec14)
- [eic_config_params::pin_num](../platform_security_model_reference/P005_eic_config_params_结构体.md#a44492d0b42ea6ccd0545726467ca82aa)
- [eic_config_params::eic_line_callback](../platform_security_model_reference/P005_eic_config_params_结构体.md#a95858dedfde317eb8f70d15567a75ee6)
- [eic_config_params::debounce](../platform_security_model_reference/P005_eic_config_params_结构体.md#a9de61236e03ae6fff8a111dcd1a30497)
- [eic_config_params::port_addr](../platform_security_model_reference/P005_eic_config_params_结构体.md#a9f5b10cb7dc39d11c263e7e88e583ac6)
- [eic_config_params::gpio_data](../platform_security_model_reference/P005_eic_config_params_结构体.md#ab7422775ca216017cbb74444bd1df6a4)
- [eic_config_params::trig_type](../platform_security_model_reference/P005_eic_config_params_结构体.md#add7f563e55292364350b66cbb47f1f21)

---

[上一章](P395_intc_mchp_aic_g1.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P397_intc_nxp_gint.h_源码浏览.md)
