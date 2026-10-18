---
id: learning.zephyr-docs.api-source-reference.page-599
title: nrf_comp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第599章\_nrf\_comp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html)。

## 599.1\_原始可见代码（Source Code）

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
<a id="foldopen00018"></a>
<a id="l00018"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="acomparator_8h_html"></a>
<a id="anrf-comp_8h_html"></a>
<a id="anrf__comp_8h_html_a63ca5bf56504df5c9d0904609c433e11"></a>
<a id="anrf__comp_8h_html_a661d2e37c4acd5551b77e5bf2437b553"></a>
<a id="anrf__comp_8h_html_a661d2e37c4acd5551b77e5bf2437b553a0e8f3057261749e3a15333d42e49512f"></a>
<a id="anrf__comp_8h_html_a661d2e37c4acd5551b77e5bf2437b553a3670bac3f83f144ca1373a4ea6c0107c"></a>
<a id="anrf__comp_8h_html_a661d2e37c4acd5551b77e5bf2437b553a87eba8036aea56146b734ee47a9cd6ca"></a>
<a id="anrf__comp_8h_html_a661d2e37c4acd5551b77e5bf2437b553ab0ae8de9e72cf723645691166e9fbb2e"></a>
<a id="anrf__comp_8h_html_a661d2e37c4acd5551b77e5bf2437b553abf7088360f68099140b06de7d3f4b4e7"></a>
<a id="anrf__comp_8h_html_a661d2e37c4acd5551b77e5bf2437b553abfa40254064295fec8c5882402f7f0d2"></a>
<a id="anrf__comp_8h_html_a74444aeafb5a2bf633ffd706cc6b9010"></a>
<a id="anrf__comp_8h_html_a74444aeafb5a2bf633ffd706cc6b9010a16df414be65b65763e5938bc37bb392f"></a>
<a id="anrf__comp_8h_html_a74444aeafb5a2bf633ffd706cc6b9010a1890799d7f32b44f1a870ed67a8707a0"></a>
<a id="anrf__comp_8h_html_a74444aeafb5a2bf633ffd706cc6b9010a3d47ebd769b9d4b9668d7c6502294043"></a>
<a id="anrf__comp_8h_html_a74444aeafb5a2bf633ffd706cc6b9010ab413c10f12cbfb5b2e550f8fa07992c2"></a>
<a id="anrf__comp_8h_html_aca8ca4ea25fbfbe962f754ef79bcb356"></a>
<a id="anrf__comp_8h_html_ad13baf7c262d5fb2321ea5140180b3b1"></a>
<a id="anrf__comp_8h_html_ad13baf7c262d5fb2321ea5140180b3b1a108433aa9b89eeca9a706e67d5eb8826"></a>
<a id="anrf__comp_8h_html_ad13baf7c262d5fb2321ea5140180b3b1a1fb59dd0aa818e279c5e4d15b620fac5"></a>
<a id="anrf__comp_8h_html_ad13baf7c262d5fb2321ea5140180b3b1aeb3aad272a4b6cd1269180306357bd98"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructcomp__nrf__comp__diff__config_html"></a>
<a id="astructcomp__nrf__comp__diff__config_html_a32e78a6a82b1baba4d77c2737c2db069"></a>
<a id="astructcomp__nrf__comp__diff__config_html_a9a9b95f993a1a193292eb940c0550e1f"></a>
<a id="astructcomp__nrf__comp__diff__config_html_ac1aada8c9bceab130cd6ffdf294ce52f"></a>
<a id="astructcomp__nrf__comp__diff__config_html_ac80eeeca2f685ddb2f2a97af18f9515b"></a>
<a id="astructcomp__nrf__comp__diff__config_html_ae597d46f83c77923541e73cf254bc4ee"></a>
<a id="astructcomp__nrf__comp__se__config_html"></a>
<a id="astructcomp__nrf__comp__se__config_html_a3a7c4e624cb7e34624732dbe4b5ab4f8"></a>
<a id="astructcomp__nrf__comp__se__config_html_a3ffb95afd621727dedbc617e3072cfd9"></a>
<a id="astructcomp__nrf__comp__se__config_html_a484cc2b4c38c7b5a8c05e87e560c7b5e"></a>
<a id="astructcomp__nrf__comp__se__config_html_a486c261d0d13cc1feb4a2a60c5ea54f5"></a>
<a id="astructcomp__nrf__comp__se__config_html_a72dcaac8a0508b8859397b7926238112"></a>
<a id="astructcomp__nrf__comp__se__config_html_a7faaf85605587ce3b3d1b9a7a3d062d6"></a>
<a id="astructcomp__nrf__comp__se__config_html_ad4c0e1711565c3bd05c08a6eaf593aad"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_COMP_NRF_COMP_H_
#define ZEPHYR_INCLUDE_DRIVERS_COMP_NRF_COMP_H_

#include <zephyr/dt-bindings/comparator/nrf-comp.h>
#include <zephyr/drivers/comparator.h>

#ifdef __cplusplus
extern "C" {
#endif

enum comp_nrf_comp_refsel {
        COMP_NRF_COMP_REFSEL_INT_1V2,
        COMP_NRF_COMP_REFSEL_INT_1V8,
        COMP_NRF_COMP_REFSEL_INT_2V4,
        COMP_NRF_COMP_REFSEL_AVDDAO1V8,
        COMP_NRF_COMP_REFSEL_VDD,
        COMP_NRF_COMP_REFSEL_AREF,
};

enum comp_nrf_comp_sp_mode {
        COMP_NRF_COMP_SP_MODE_LOW,
        COMP_NRF_COMP_SP_MODE_NORMAL,
        COMP_NRF_COMP_SP_MODE_HIGH,
};

enum comp_nrf_comp_isource {
        COMP_NRF_COMP_ISOURCE_DISABLED,
        COMP_NRF_COMP_ISOURCE_2UA5,
        COMP_NRF_COMP_ISOURCE_5UA,
        COMP_NRF_COMP_ISOURCE_10UA,
};

struct comp_nrf_comp_se_config {
        uint8_t psel;
        enum comp_nrf_comp_sp_mode sp_mode;
        enum comp_nrf_comp_isource isource;
        uint8_t extrefsel;
        enum comp_nrf_comp_refsel refsel;
        uint8_t th_down;
        uint8_t th_up;
};

int comp_nrf_comp_configure_se(const struct device *dev,
                               const struct comp_nrf_comp_se_config *config);

struct comp_nrf_comp_diff_config {
        uint8_t psel;
        enum comp_nrf_comp_sp_mode sp_mode;
        enum comp_nrf_comp_isource isource;
        uint8_t extrefsel;
        bool enable_hyst;
};

int comp_nrf_comp_configure_diff(const struct device *dev,
                                 const struct comp_nrf_comp_diff_config *config);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_COMP_NRF_COMP_H_ */
```

## 599.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 121 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_COMP_NRF_COMP_H_`。

## 599.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html)
- [zephyr/dt-bindings/comparator/nrf-comp.h](https://docs.zephyrproject.org/latest/doxygen/html/nrf-comp_8h.html)
- [zephyr/drivers/comparator.h](../analog_reference/P001_比较器公共头文件参考.md)
- [comp_nrf_comp_refsel](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a661d2e37c4acd5551b77e5bf2437b553)
- [COMP_NRF_COMP_REFSEL_INT_1V2](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a661d2e37c4acd5551b77e5bf2437b553abfa40254064295fec8c5882402f7f0d2)
- [COMP_NRF_COMP_REFSEL_INT_1V8](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a661d2e37c4acd5551b77e5bf2437b553abf7088360f68099140b06de7d3f4b4e7)
- [COMP_NRF_COMP_REFSEL_INT_2V4](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a661d2e37c4acd5551b77e5bf2437b553a3670bac3f83f144ca1373a4ea6c0107c)
- [COMP_NRF_COMP_REFSEL_AVDDAO1V8](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a661d2e37c4acd5551b77e5bf2437b553a87eba8036aea56146b734ee47a9cd6ca)
- [COMP_NRF_COMP_REFSEL_VDD](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a661d2e37c4acd5551b77e5bf2437b553a0e8f3057261749e3a15333d42e49512f)
- [COMP_NRF_COMP_REFSEL_AREF](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a661d2e37c4acd5551b77e5bf2437b553ab0ae8de9e72cf723645691166e9fbb2e)
- [comp_nrf_comp_sp_mode](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#ad13baf7c262d5fb2321ea5140180b3b1)
- [COMP_NRF_COMP_SP_MODE_LOW](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#ad13baf7c262d5fb2321ea5140180b3b1a108433aa9b89eeca9a706e67d5eb8826)
- [COMP_NRF_COMP_SP_MODE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#ad13baf7c262d5fb2321ea5140180b3b1a1fb59dd0aa818e279c5e4d15b620fac5)
- [COMP_NRF_COMP_SP_MODE_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#ad13baf7c262d5fb2321ea5140180b3b1aeb3aad272a4b6cd1269180306357bd98)
- [comp_nrf_comp_isource](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a74444aeafb5a2bf633ffd706cc6b9010)
- [COMP_NRF_COMP_ISOURCE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a74444aeafb5a2bf633ffd706cc6b9010a3d47ebd769b9d4b9668d7c6502294043)
- [COMP_NRF_COMP_ISOURCE_2UA5](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a74444aeafb5a2bf633ffd706cc6b9010ab413c10f12cbfb5b2e550f8fa07992c2)
- [COMP_NRF_COMP_ISOURCE_5UA](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a74444aeafb5a2bf633ffd706cc6b9010a1890799d7f32b44f1a870ed67a8707a0)
- [COMP_NRF_COMP_ISOURCE_10UA](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a74444aeafb5a2bf633ffd706cc6b9010a16df414be65b65763e5938bc37bb392f)
- [comp_nrf_comp_se_config](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [psel](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md#a7faaf85605587ce3b3d1b9a7a3d062d6)
- [sp_mode](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md#a484cc2b4c38c7b5a8c05e87e560c7b5e)
- [isource](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md#a3ffb95afd621727dedbc617e3072cfd9)
- [extrefsel](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md#a486c261d0d13cc1feb4a2a60c5ea54f5)
- [refsel](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md#a3a7c4e624cb7e34624732dbe4b5ab4f8)
- [th_down](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md#ad4c0e1711565c3bd05c08a6eaf593aad)
- [th_up](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md#a72dcaac8a0508b8859397b7926238112)
- [comp_nrf_comp_configure_se](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#aca8ca4ea25fbfbe962f754ef79bcb356)
- [device](../device_reference/P002_设备对象结构.md)
- [comp_nrf_comp_diff_config](../device_power_control_model_reference/P003_comp_nrf_comp_diff_config_结构体.md)
- [psel](../device_power_control_model_reference/P003_comp_nrf_comp_diff_config_结构体.md#a32e78a6a82b1baba4d77c2737c2db069)
- [sp_mode](../device_power_control_model_reference/P003_comp_nrf_comp_diff_config_结构体.md#a9a9b95f993a1a193292eb940c0550e1f)
- [isource](../device_power_control_model_reference/P003_comp_nrf_comp_diff_config_结构体.md#ac1aada8c9bceab130cd6ffdf294ce52f)
- [extrefsel](../device_power_control_model_reference/P003_comp_nrf_comp_diff_config_结构体.md#ac80eeeca2f685ddb2f2a97af18f9515b)
- [enable_hyst](../device_power_control_model_reference/P003_comp_nrf_comp_diff_config_结构体.md#ae597d46f83c77923541e73cf254bc4ee)
- [comp_nrf_comp_configure_diff](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html#a63ca5bf56504df5c9d0904609c433e11)
- [comparator.h](../analog_reference/P001_比较器公共头文件参考.md)
- [nrf-comp.h](https://docs.zephyrproject.org/latest/doxygen/html/nrf-comp_8h.html)
- [comp_nrf_comp_diff_config::psel](../device_power_control_model_reference/P003_comp_nrf_comp_diff_config_结构体.md#a32e78a6a82b1baba4d77c2737c2db069)
- [comp_nrf_comp_diff_config::sp_mode](../device_power_control_model_reference/P003_comp_nrf_comp_diff_config_结构体.md#a9a9b95f993a1a193292eb940c0550e1f)
- [comp_nrf_comp_diff_config::isource](../device_power_control_model_reference/P003_comp_nrf_comp_diff_config_结构体.md#ac1aada8c9bceab130cd6ffdf294ce52f)
- [comp_nrf_comp_diff_config::extrefsel](../device_power_control_model_reference/P003_comp_nrf_comp_diff_config_结构体.md#ac80eeeca2f685ddb2f2a97af18f9515b)
- [comp_nrf_comp_diff_config::enable_hyst](../device_power_control_model_reference/P003_comp_nrf_comp_diff_config_结构体.md#ae597d46f83c77923541e73cf254bc4ee)
- [comp_nrf_comp_se_config::refsel](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md#a3a7c4e624cb7e34624732dbe4b5ab4f8)
- [comp_nrf_comp_se_config::isource](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md#a3ffb95afd621727dedbc617e3072cfd9)
- [comp_nrf_comp_se_config::sp_mode](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md#a484cc2b4c38c7b5a8c05e87e560c7b5e)
- [comp_nrf_comp_se_config::extrefsel](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md#a486c261d0d13cc1feb4a2a60c5ea54f5)
- [comp_nrf_comp_se_config::th_up](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md#a72dcaac8a0508b8859397b7926238112)
- [comp_nrf_comp_se_config::psel](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md#a7faaf85605587ce3b3d1b9a7a3d062d6)
- [comp_nrf_comp_se_config::th_down](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md#ad4c0e1711565c3bd05c08a6eaf593aad)

---

[上一章](P598_nrf5x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P600_nrf_lpcomp.h_源码浏览.md)
