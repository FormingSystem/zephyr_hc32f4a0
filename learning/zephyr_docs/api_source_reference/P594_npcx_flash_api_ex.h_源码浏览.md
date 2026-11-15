---
id: learning.zephyr-docs.api-source-reference.page-594
title: npcx_flash_api_ex.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/npcx__flash__api__ex_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第594章\_npcx\_flash\_api\_ex.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/npcx__flash__api__ex_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/npcx__flash__api__ex_8h.html)。

## 594.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00046"></a>
<a id="l00057"></a>
<a id="l00066"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00116"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="foldopen00125"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="aflash_8h_html"></a>
<a id="agroup__flash__interface_html_ga67418b2d5cbbec83463dce3d426162e3"></a>
<a id="agroup__npcx__flash__ex__op_html_gad4f93f7272e825355875d0fb05351474"></a>
<a id="agroup__npcx__flash__ex__op_html_ggad4f93f7272e825355875d0fb05351474a46c5fff8b0ffbc480c01fed93ff8fd57"></a>
<a id="agroup__npcx__flash__ex__op_html_ggad4f93f7272e825355875d0fb05351474abbf87cdc7e9c3cdc9e6afde3c0485ec9"></a>
<a id="agroup__npcx__flash__ex__op_html_ggad4f93f7272e825355875d0fb05351474ad1fde767b235165d178a13de61d5f007"></a>
<a id="agroup__npcx__flash__ex__op_html_ggad4f93f7272e825355875d0fb05351474ad675f28e2066d7d97be0ecdc7f3d34b9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructnpcx__ex__ops__gdma__in_html"></a>
<a id="astructnpcx__ex__ops__gdma__in_html_a14eaa0c83b6f1234218e6d350405dbf3"></a>
<a id="astructnpcx__ex__ops__gdma__in_html_a2c7b04d7918257a0e4523822d4ccf07e"></a>
<a id="astructnpcx__ex__ops__gdma__in_html_a806cb6bab93a437093914cbffac07c62"></a>
<a id="astructnpcx__ex__ops__qspi__oper__in_html"></a>
<a id="astructnpcx__ex__ops__qspi__oper__in_html_a0b9c9407bb320396d73f30ae4a8b55f1"></a>
<a id="astructnpcx__ex__ops__qspi__oper__in_html_afc12bebd886ba71fc9431cedf0765c24"></a>
<a id="astructnpcx__ex__ops__qspi__oper__out_html"></a>
<a id="astructnpcx__ex__ops__qspi__oper__out_html_aa77f1bdcc00e1f3cc7a66cc150ab5686"></a>
<a id="astructnpcx__ex__ops__uma__in_html"></a>
<a id="astructnpcx__ex__ops__uma__in_html_a3c950c4208da78e2908a116ea3eedd5f"></a>
<a id="astructnpcx__ex__ops__uma__in_html_a4fe44cf0e3b09193700a72b62b78f544"></a>
<a id="astructnpcx__ex__ops__uma__in_html_a67c765977abd17095e4589604dfe43b0"></a>
<a id="astructnpcx__ex__ops__uma__in_html_a7c36c34ffe3f6c69e9229efdc41da87c"></a>
<a id="astructnpcx__ex__ops__uma__in_html_a891172574f487bcfbcbbed20cd340998"></a>
<a id="astructnpcx__ex__ops__uma__in_html_add76f25d7adf905d4d4ba3b6f4b977e6"></a>
<a id="astructnpcx__ex__ops__uma__out_html"></a>
<a id="astructnpcx__ex__ops__uma__out_html_a9be2364b1328eedc07e0123d774dbba7"></a>

```c
/*
 * Copyright (c) 2023 Nuvoton Technology Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FLASH_NPCX_FLASH_API_EX_H_
#define ZEPHYR_INCLUDE_DRIVERS_FLASH_NPCX_FLASH_API_EX_H_


#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/drivers/flash.h>

enum flash_npcx_ex_ops {
        FLASH_NPCX_EX_OP_EXEC_UMA = FLASH_EX_OP_VENDOR_BASE,
        FLASH_NPCX_EX_OP_SET_QSPI_OPER,
        FLASH_NPCX_EX_OP_GET_QSPI_OPER,
        FLASH_NPCX_EX_OP_EXEC_GDMA,
};

struct npcx_ex_ops_uma_in {
        uint8_t opcode;
        uint8_t *tx_buf;
        size_t tx_count;
        uint32_t addr;
        size_t addr_count;
        size_t rx_count;
};

struct npcx_ex_ops_uma_out {
        uint8_t *rx_buf;
};

struct npcx_ex_ops_qspi_oper_in {
        bool enable;
        uint32_t mask;
};

struct npcx_ex_ops_qspi_oper_out {
        uint32_t oper;
};

struct npcx_ex_ops_gdma_in {
        uint32_t src;
        uint32_t dst;
        uint16_t length;
};

#define NPCX_EX_OP_LOCK_UMA     BIT(0)
#define NPCX_EX_OP_INT_FLASH_WP BIT(1)

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_FLASH_NPCX_FLASH_API_EX_H_ */
```

## 594.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nuvoton Technology Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 147 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FLASH_NPCX_FLASH_API_EX_H_`。

## 594.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/npcx__flash__api__ex_8h.html)
- [zephyr/drivers/flash.h](../flash_reference/P009_Flash公共头文件参考.md)
- [flash_npcx_ex_ops](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#gad4f93f7272e825355875d0fb05351474)
- [FLASH_NPCX_EX_OP_EXEC_UMA](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474ad1fde767b235165d178a13de61d5f007)
- [FLASH_EX_OP_VENDOR_BASE](../flash_reference/P001_Flash公共接口.md#ga67418b2d5cbbec83463dce3d426162e3)
- [FLASH_NPCX_EX_OP_SET_QSPI_OPER](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474abbf87cdc7e9c3cdc9e6afde3c0485ec9)
- [FLASH_NPCX_EX_OP_GET_QSPI_OPER](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474a46c5fff8b0ffbc480c01fed93ff8fd57)
- [FLASH_NPCX_EX_OP_EXEC_GDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474ad675f28e2066d7d97be0ecdc7f3d34b9)
- [npcx_ex_ops_uma_in](../device_power_control_model_reference/P047_npcx_ex_ops_uma_in_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [opcode](../device_power_control_model_reference/P047_npcx_ex_ops_uma_in_结构体.md#a891172574f487bcfbcbbed20cd340998)
- [tx_buf](../device_power_control_model_reference/P047_npcx_ex_ops_uma_in_结构体.md#a67c765977abd17095e4589604dfe43b0)
- [tx_count](../device_power_control_model_reference/P047_npcx_ex_ops_uma_in_结构体.md#add76f25d7adf905d4d4ba3b6f4b977e6)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [addr](../device_power_control_model_reference/P047_npcx_ex_ops_uma_in_结构体.md#a4fe44cf0e3b09193700a72b62b78f544)
- [addr_count](../device_power_control_model_reference/P047_npcx_ex_ops_uma_in_结构体.md#a3c950c4208da78e2908a116ea3eedd5f)
- [rx_count](../device_power_control_model_reference/P047_npcx_ex_ops_uma_in_结构体.md#a7c36c34ffe3f6c69e9229efdc41da87c)
- [npcx_ex_ops_uma_out](../device_power_control_model_reference/P048_npcx_ex_ops_uma_out_结构体.md)
- [rx_buf](../device_power_control_model_reference/P048_npcx_ex_ops_uma_out_结构体.md#a9be2364b1328eedc07e0123d774dbba7)
- [npcx_ex_ops_qspi_oper_in](../device_power_control_model_reference/P045_npcx_ex_ops_qspi_oper_in_结构体.md)
- [enable](../device_power_control_model_reference/P045_npcx_ex_ops_qspi_oper_in_结构体.md#afc12bebd886ba71fc9431cedf0765c24)
- [mask](../device_power_control_model_reference/P045_npcx_ex_ops_qspi_oper_in_结构体.md#a0b9c9407bb320396d73f30ae4a8b55f1)
- [npcx_ex_ops_qspi_oper_out](../device_power_control_model_reference/P046_npcx_ex_ops_qspi_oper_out_结构体.md)
- [oper](../device_power_control_model_reference/P046_npcx_ex_ops_qspi_oper_out_结构体.md#aa77f1bdcc00e1f3cc7a66cc150ab5686)
- [npcx_ex_ops_gdma_in](../device_power_control_model_reference/P044_npcx_ex_ops_gdma_in_结构体.md)
- [src](../device_power_control_model_reference/P044_npcx_ex_ops_gdma_in_结构体.md#a14eaa0c83b6f1234218e6d350405dbf3)
- [dst](../device_power_control_model_reference/P044_npcx_ex_ops_gdma_in_结构体.md#a806cb6bab93a437093914cbffac07c62)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [length](../device_power_control_model_reference/P044_npcx_ex_ops_gdma_in_结构体.md#a2c7b04d7918257a0e4523822d4ccf07e)
- [flash.h](../flash_reference/P009_Flash公共头文件参考.md)
- [npcx_ex_ops_gdma_in::src](../device_power_control_model_reference/P044_npcx_ex_ops_gdma_in_结构体.md#a14eaa0c83b6f1234218e6d350405dbf3)
- [npcx_ex_ops_gdma_in::length](../device_power_control_model_reference/P044_npcx_ex_ops_gdma_in_结构体.md#a2c7b04d7918257a0e4523822d4ccf07e)
- [npcx_ex_ops_gdma_in::dst](../device_power_control_model_reference/P044_npcx_ex_ops_gdma_in_结构体.md#a806cb6bab93a437093914cbffac07c62)
- [npcx_ex_ops_qspi_oper_in::mask](../device_power_control_model_reference/P045_npcx_ex_ops_qspi_oper_in_结构体.md#a0b9c9407bb320396d73f30ae4a8b55f1)
- [npcx_ex_ops_qspi_oper_in::enable](../device_power_control_model_reference/P045_npcx_ex_ops_qspi_oper_in_结构体.md#afc12bebd886ba71fc9431cedf0765c24)
- [npcx_ex_ops_qspi_oper_out::oper](../device_power_control_model_reference/P046_npcx_ex_ops_qspi_oper_out_结构体.md#aa77f1bdcc00e1f3cc7a66cc150ab5686)
- [npcx_ex_ops_uma_in::addr_count](../device_power_control_model_reference/P047_npcx_ex_ops_uma_in_结构体.md#a3c950c4208da78e2908a116ea3eedd5f)
- [npcx_ex_ops_uma_in::addr](../device_power_control_model_reference/P047_npcx_ex_ops_uma_in_结构体.md#a4fe44cf0e3b09193700a72b62b78f544)
- [npcx_ex_ops_uma_in::tx_buf](../device_power_control_model_reference/P047_npcx_ex_ops_uma_in_结构体.md#a67c765977abd17095e4589604dfe43b0)
- [npcx_ex_ops_uma_in::rx_count](../device_power_control_model_reference/P047_npcx_ex_ops_uma_in_结构体.md#a7c36c34ffe3f6c69e9229efdc41da87c)
- [npcx_ex_ops_uma_in::opcode](../device_power_control_model_reference/P047_npcx_ex_ops_uma_in_结构体.md#a891172574f487bcfbcbbed20cd340998)
- [npcx_ex_ops_uma_in::tx_count](../device_power_control_model_reference/P047_npcx_ex_ops_uma_in_结构体.md#add76f25d7adf905d4d4ba3b6f4b977e6)
- [npcx_ex_ops_uma_out::rx_buf](../device_power_control_model_reference/P048_npcx_ex_ops_uma_out_结构体.md#a9be2364b1328eedc07e0123d774dbba7)

---

[上一章](P593_npcx9_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P595_npcx_tach.h_源码浏览.md)
