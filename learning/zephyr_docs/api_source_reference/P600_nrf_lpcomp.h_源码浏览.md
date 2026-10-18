---
id: learning.zephyr-docs.api-source-reference.page-600
title: nrf_lpcomp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第600章\_nrf\_lpcomp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html)。

## 600.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="acomparator_8h_html"></a>
<a id="anrf-comp_8h_html"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04a25c009efcddd2e84417d115b5f4e346e"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04a295352a4ecb28f6288efe33fd0c49526"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04a2b1cd929103b9af8ef372472078efb76"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04a3b3760b0298de0fcb94812f98433ba16"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04a3c10840415f3aed4d0b8414a6decf56d"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04a624b842d3ef6e8fa172412fc3a06dd1a"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04a848e512c3223a019f6ec59612616fe33"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04a930ce822163d6654cda439e43fbbaab1"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04a94a97a641eaa3dc25b09d00dda8fb137"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04a98def2c5d100c1c51c697203606b66dd"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04a9913bfd70d57767e295ced6e7287a7bb"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04a99627f00ae3182014da516333f64705f"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04aa62402dda42b69bd974de3f19aa4a509"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04aade5263dc54bd126f9a761e0188b13f7"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04abf717bfb0610352e60d4f4fc45a370b1"></a>
<a id="anrf__lpcomp_8h_html_ae42326afcd4f5435480f80d382266a04acd4c60e604696b7d24028ad9e98d77f3"></a>
<a id="anrf__lpcomp_8h_html_aff748ac1a1a8c13796b81ef789b4c7f2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructcomp__nrf__lpcomp__config_html"></a>
<a id="astructcomp__nrf__lpcomp__config_html_a21b862cc82704353d269cb81b0c71a42"></a>
<a id="astructcomp__nrf__lpcomp__config_html_a6145079376220c7fc3914e208bee819f"></a>
<a id="astructcomp__nrf__lpcomp__config_html_ac561f00056c9faabb61a4a67b628f963"></a>
<a id="astructcomp__nrf__lpcomp__config_html_ad1022de6c772909a4f8c3d90e0748fe7"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_COMP_NRF_LPCOMP_H_
#define ZEPHYR_INCLUDE_DRIVERS_COMP_NRF_LPCOMP_H_

#include <zephyr/dt-bindings/comparator/nrf-comp.h>
#include <zephyr/drivers/comparator.h>

#ifdef __cplusplus
extern "C" {
#endif

enum comp_nrf_lpcomp_refsel {
        COMP_NRF_LPCOMP_REFSEL_VDD_1_8,
        COMP_NRF_LPCOMP_REFSEL_VDD_2_8,
        COMP_NRF_LPCOMP_REFSEL_VDD_3_8,
        COMP_NRF_LPCOMP_REFSEL_VDD_4_8,
        COMP_NRF_LPCOMP_REFSEL_VDD_5_8,
        COMP_NRF_LPCOMP_REFSEL_VDD_6_8,
        COMP_NRF_LPCOMP_REFSEL_VDD_7_8,
        COMP_NRF_LPCOMP_REFSEL_VDD_1_16,
        COMP_NRF_LPCOMP_REFSEL_VDD_3_16,
        COMP_NRF_LPCOMP_REFSEL_VDD_5_16,
        COMP_NRF_LPCOMP_REFSEL_VDD_7_16,
        COMP_NRF_LPCOMP_REFSEL_VDD_9_16,
        COMP_NRF_LPCOMP_REFSEL_VDD_11_16,
        COMP_NRF_LPCOMP_REFSEL_VDD_13_16,
        COMP_NRF_LPCOMP_REFSEL_VDD_15_16,
        COMP_NRF_LPCOMP_REFSEL_AREF,
};

struct comp_nrf_lpcomp_config {
        uint8_t psel;
        uint8_t extrefsel;
        enum comp_nrf_lpcomp_refsel refsel;
        bool enable_hyst;
};

int comp_nrf_lpcomp_configure(const struct device *dev,
                              const struct comp_nrf_lpcomp_config *config);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_COMP_NRF_LPCOMP_H_ */
```

## 600.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 85 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_COMP_NRF_LPCOMP_H_`。

## 600.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html)
- [zephyr/dt-bindings/comparator/nrf-comp.h](https://docs.zephyrproject.org/latest/doxygen/html/nrf-comp_8h.html)
- [zephyr/drivers/comparator.h](../analog_reference/P001_比较器公共头文件参考.md)
- [comp_nrf_lpcomp_refsel](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04)
- [COMP_NRF_LPCOMP_REFSEL_VDD_1_8](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04a99627f00ae3182014da516333f64705f)
- [COMP_NRF_LPCOMP_REFSEL_VDD_2_8](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04a3c10840415f3aed4d0b8414a6decf56d)
- [COMP_NRF_LPCOMP_REFSEL_VDD_3_8](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04a25c009efcddd2e84417d115b5f4e346e)
- [COMP_NRF_LPCOMP_REFSEL_VDD_4_8](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04a848e512c3223a019f6ec59612616fe33)
- [COMP_NRF_LPCOMP_REFSEL_VDD_5_8](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04a295352a4ecb28f6288efe33fd0c49526)
- [COMP_NRF_LPCOMP_REFSEL_VDD_6_8](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04a624b842d3ef6e8fa172412fc3a06dd1a)
- [COMP_NRF_LPCOMP_REFSEL_VDD_7_8](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04a2b1cd929103b9af8ef372472078efb76)
- [COMP_NRF_LPCOMP_REFSEL_VDD_1_16](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04acd4c60e604696b7d24028ad9e98d77f3)
- [COMP_NRF_LPCOMP_REFSEL_VDD_3_16](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04a3b3760b0298de0fcb94812f98433ba16)
- [COMP_NRF_LPCOMP_REFSEL_VDD_5_16](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04a94a97a641eaa3dc25b09d00dda8fb137)
- [COMP_NRF_LPCOMP_REFSEL_VDD_7_16](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04a98def2c5d100c1c51c697203606b66dd)
- [COMP_NRF_LPCOMP_REFSEL_VDD_9_16](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04aa62402dda42b69bd974de3f19aa4a509)
- [COMP_NRF_LPCOMP_REFSEL_VDD_11_16](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04a9913bfd70d57767e295ced6e7287a7bb)
- [COMP_NRF_LPCOMP_REFSEL_VDD_13_16](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04a930ce822163d6654cda439e43fbbaab1)
- [COMP_NRF_LPCOMP_REFSEL_VDD_15_16](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04aade5263dc54bd126f9a761e0188b13f7)
- [COMP_NRF_LPCOMP_REFSEL_AREF](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#ae42326afcd4f5435480f80d382266a04abf717bfb0610352e60d4f4fc45a370b1)
- [comp_nrf_lpcomp_config](../device_power_control_model_reference/P005_comp_nrf_lpcomp_config_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [psel](../device_power_control_model_reference/P005_comp_nrf_lpcomp_config_结构体.md#a6145079376220c7fc3914e208bee819f)
- [extrefsel](../device_power_control_model_reference/P005_comp_nrf_lpcomp_config_结构体.md#a21b862cc82704353d269cb81b0c71a42)
- [refsel](../device_power_control_model_reference/P005_comp_nrf_lpcomp_config_结构体.md#ad1022de6c772909a4f8c3d90e0748fe7)
- [enable_hyst](../device_power_control_model_reference/P005_comp_nrf_lpcomp_config_结构体.md#ac561f00056c9faabb61a4a67b628f963)
- [comp_nrf_lpcomp_configure](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html#aff748ac1a1a8c13796b81ef789b4c7f2)
- [device](../device_reference/P002_设备对象结构.md)
- [comparator.h](../analog_reference/P001_比较器公共头文件参考.md)
- [nrf-comp.h](https://docs.zephyrproject.org/latest/doxygen/html/nrf-comp_8h.html)
- [comp_nrf_lpcomp_config::extrefsel](../device_power_control_model_reference/P005_comp_nrf_lpcomp_config_结构体.md#a21b862cc82704353d269cb81b0c71a42)
- [comp_nrf_lpcomp_config::psel](../device_power_control_model_reference/P005_comp_nrf_lpcomp_config_结构体.md#a6145079376220c7fc3914e208bee819f)
- [comp_nrf_lpcomp_config::enable_hyst](../device_power_control_model_reference/P005_comp_nrf_lpcomp_config_结构体.md#ac561f00056c9faabb61a4a67b628f963)
- [comp_nrf_lpcomp_config::refsel](../device_power_control_model_reference/P005_comp_nrf_lpcomp_config_结构体.md#ad1022de6c772909a4f8c3d90e0748fe7)

---

[上一章](P599_nrf_comp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P601_nrf_qspi_nor.h_源码浏览.md)
