---
id: learning.zephyr-docs.api-source-reference.page-832
title: stm32_flash_api_extensions.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32__flash__api__extensions_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第832章\_stm32\_flash\_api\_extensions.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32__flash__api__extensions_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32__flash__api__extensions_8h.html)。

## 832.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00045"></a>
<a id="l00055"></a>
<a id="l00063"></a>
<a id="l00071"></a>
<a id="l00077"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00098"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="foldopen00111"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="foldopen00121"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="foldopen00129"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="aflash_8h_html"></a>
<a id="agroup__flash__interface_html_ga67418b2d5cbbec83463dce3d426162e3"></a>
<a id="agroup__stm32__flash__ex__op_html_ga95b012159eb95cd62859a6d5c4d862b8"></a>
<a id="agroup__stm32__flash__ex__op_html_gaac68791eaf037279ae1a51a0058ed4b6"></a>
<a id="agroup__stm32__flash__ex__op_html_gga95b012159eb95cd62859a6d5c4d862b8a40f2e65d83c8ef8144c2ba3072cb4a85"></a>
<a id="agroup__stm32__flash__ex__op_html_gga95b012159eb95cd62859a6d5c4d862b8a59b3b9a3b0eaee9cd4435f452855b903"></a>
<a id="agroup__stm32__flash__ex__op_html_gga95b012159eb95cd62859a6d5c4d862b8a778e98df945314508cb9c2c266e6f02a"></a>
<a id="agroup__stm32__flash__ex__op_html_gga95b012159eb95cd62859a6d5c4d862b8a7bde6043879f1a6139da11679b4455fe"></a>
<a id="agroup__stm32__flash__ex__op_html_gga95b012159eb95cd62859a6d5c4d862b8aab8109cdf28181ef0dbb9d1e3b93b096"></a>
<a id="agroup__stm32__flash__ex__op_html_gga95b012159eb95cd62859a6d5c4d862b8ae1b013a96c3a64b0d3e677b4bce954a0"></a>
<a id="agroup__stm32__flash__ex__op_html_ggaac68791eaf037279ae1a51a0058ed4b6a092676857a6a2ba1f33486cf50cf20ef"></a>
<a id="agroup__stm32__flash__ex__op_html_ggaac68791eaf037279ae1a51a0058ed4b6a70307ddcc9bdb96f3e5f3796d2bd442e"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructflash__stm32__ex__op__rdp_html"></a>
<a id="astructflash__stm32__ex__op__rdp_html_a45454dfb14c59310c2549aca1e7b31b2"></a>
<a id="astructflash__stm32__ex__op__rdp_html_aab59e61f810e1e33bd96261fb7f9668b"></a>
<a id="astructflash__stm32__ex__op__sector__wp__in_html"></a>
<a id="astructflash__stm32__ex__op__sector__wp__in_html_a85ce4a4eb0ce48c326dbb203795d641a"></a>
<a id="astructflash__stm32__ex__op__sector__wp__in_html_af6bd2a9a30f17eeb073483e1d3714961"></a>
<a id="astructflash__stm32__ex__op__sector__wp__out_html"></a>
<a id="astructflash__stm32__ex__op__sector__wp__out_html_a5260c9c8f92f88563845e863365b4ae2"></a>

```c
/*
 * Copyright (c) 2023 Google Inc
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FLASH_STM32_FLASH_API_EXTENSIONS_H_
#define ZEPHYR_INCLUDE_DRIVERS_FLASH_STM32_FLASH_API_EXTENSIONS_H_


#include <zephyr/drivers/flash.h>

enum stm32_ex_ops {
        FLASH_STM32_EX_OP_SECTOR_WP = FLASH_EX_OP_VENDOR_BASE,
        FLASH_STM32_EX_OP_RDP,
        FLASH_STM32_EX_OP_BLOCK_OPTION_REG,
        FLASH_STM32_EX_OP_BLOCK_CONTROL_REG,
        FLASH_STM32_EX_OP_OPTB_READ,
        FLASH_STM32_EX_OP_OPTB_WRITE,
};

enum stm32_qspi_ex_ops {
        FLASH_STM32_QSPI_EX_OP_GENERIC_READ,
        FLASH_STM32_QSPI_EX_OP_GENERIC_WRITE,
};

struct flash_stm32_ex_op_sector_wp_in {
        uint64_t enable_mask;
        uint64_t disable_mask;
};

struct flash_stm32_ex_op_sector_wp_out {
        uint64_t protected_mask;
};

struct flash_stm32_ex_op_rdp {
        bool enable;
        bool permanent;
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_FLASH_STM32_FLASH_API_EXTENSIONS_H_ */
```

## 832.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Google Inc。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 140 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FLASH_STM32_FLASH_API_EXTENSIONS_H_`。

## 832.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32__flash__api__extensions_8h.html)
- [zephyr/drivers/flash.h](../flash_reference/P009_Flash公共头文件参考.md)
- [stm32_ex_ops](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#ga95b012159eb95cd62859a6d5c4d862b8)
- [FLASH_STM32_EX_OP_SECTOR_WP](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8a7bde6043879f1a6139da11679b4455fe)
- [FLASH_EX_OP_VENDOR_BASE](../flash_reference/P001_Flash公共接口.md#ga67418b2d5cbbec83463dce3d426162e3)
- [FLASH_STM32_EX_OP_RDP](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8ae1b013a96c3a64b0d3e677b4bce954a0)
- [FLASH_STM32_EX_OP_BLOCK_OPTION_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8a59b3b9a3b0eaee9cd4435f452855b903)
- [FLASH_STM32_EX_OP_BLOCK_CONTROL_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8aab8109cdf28181ef0dbb9d1e3b93b096)
- [FLASH_STM32_EX_OP_OPTB_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8a778e98df945314508cb9c2c266e6f02a)
- [FLASH_STM32_EX_OP_OPTB_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8a40f2e65d83c8ef8144c2ba3072cb4a85)
- [stm32_qspi_ex_ops](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gaac68791eaf037279ae1a51a0058ed4b6)
- [FLASH_STM32_QSPI_EX_OP_GENERIC_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#ggaac68791eaf037279ae1a51a0058ed4b6a70307ddcc9bdb96f3e5f3796d2bd442e)
- [FLASH_STM32_QSPI_EX_OP_GENERIC_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#ggaac68791eaf037279ae1a51a0058ed4b6a092676857a6a2ba1f33486cf50cf20ef)
- [flash_stm32_ex_op_sector_wp_in](../system_service_model_reference/P035_flash_stm32_ex_op_sector_wp_in_结构体.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [enable_mask](../system_service_model_reference/P035_flash_stm32_ex_op_sector_wp_in_结构体.md#af6bd2a9a30f17eeb073483e1d3714961)
- [disable_mask](../system_service_model_reference/P035_flash_stm32_ex_op_sector_wp_in_结构体.md#a85ce4a4eb0ce48c326dbb203795d641a)
- [flash_stm32_ex_op_sector_wp_out](../system_service_model_reference/P036_flash_stm32_ex_op_sector_wp_out_结构体.md)
- [protected_mask](../system_service_model_reference/P036_flash_stm32_ex_op_sector_wp_out_结构体.md#a5260c9c8f92f88563845e863365b4ae2)
- [flash_stm32_ex_op_rdp](../system_service_model_reference/P034_flash_stm32_ex_op_rdp_结构体.md)
- [enable](../system_service_model_reference/P034_flash_stm32_ex_op_rdp_结构体.md#a45454dfb14c59310c2549aca1e7b31b2)
- [permanent](../system_service_model_reference/P034_flash_stm32_ex_op_rdp_结构体.md#aab59e61f810e1e33bd96261fb7f9668b)
- [flash.h](../flash_reference/P009_Flash公共头文件参考.md)
- [flash_stm32_ex_op_rdp::enable](../system_service_model_reference/P034_flash_stm32_ex_op_rdp_结构体.md#a45454dfb14c59310c2549aca1e7b31b2)
- [flash_stm32_ex_op_rdp::permanent](../system_service_model_reference/P034_flash_stm32_ex_op_rdp_结构体.md#aab59e61f810e1e33bd96261fb7f9668b)
- [flash_stm32_ex_op_sector_wp_in::disable_mask](../system_service_model_reference/P035_flash_stm32_ex_op_sector_wp_in_结构体.md#a85ce4a4eb0ce48c326dbb203795d641a)
- [flash_stm32_ex_op_sector_wp_in::enable_mask](../system_service_model_reference/P035_flash_stm32_ex_op_sector_wp_in_结构体.md#af6bd2a9a30f17eeb073483e1d3714961)
- [flash_stm32_ex_op_sector_wp_out::protected_mask](../system_service_model_reference/P036_flash_stm32_ex_op_sector_wp_out_结构体.md#a5260c9c8f92f88563845e863365b4ae2)

---

[上一章](P831_stm32_dcmi.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P833_stm32_pwm.h_源码浏览.md)
