---
id: learning.zephyr-docs.api-source-reference.page-498
title: mchp_nvmctrl_g1.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g1_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第498章\_mchp\_nvmctrl\_g1.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g1_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g1_8h.html)。

## 498.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00025"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="agroup__mchp__nvmctrl__g1__flash__ex__op_html_ga26d417de48ac23416675b9830e3f8ee4"></a>
<a id="agroup__mchp__nvmctrl__g1__flash__ex__op_html_ga4dae21b9b6e0a90faddfa045b30e19a8"></a>
<a id="agroup__mchp__nvmctrl__g1__flash__ex__op_html_gga4dae21b9b6e0a90faddfa045b30e19a8a1a4c0eddbc371ca9cf9f4fd11f06847d"></a>
<a id="agroup__mchp__nvmctrl__g1__flash__ex__op_html_gga4dae21b9b6e0a90faddfa045b30e19a8a28aeedfece9b637e6698a64ad7e036e8"></a>
<a id="agroup__mchp__nvmctrl__g1__flash__ex__op_html_gga4dae21b9b6e0a90faddfa045b30e19a8a412cbb9c36affa8a61e38c8ec77d22e4"></a>
<a id="agroup__mchp__nvmctrl__g1__flash__ex__op_html_gga4dae21b9b6e0a90faddfa045b30e19a8af25afe42760eb6f7af298f9ef44889af"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="astructflash__mchp__ex__op__userrow__data_html"></a>
<a id="astructflash__mchp__ex__op__userrow__data_html_a47930c1edb14b8b15f5800c7f05cf287"></a>
<a id="astructflash__mchp__ex__op__userrow__data_html_ae69ed8df0f2a63ab836df7fe7c35f1df"></a>
<a id="astructflash__mchp__ex__op__userrow__data_html_aeecffa84916b2be1f5118fc405ae5279"></a>

```c
/*
 * Copyright (c) 2025 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FLASH_MCHP_NVMCTRL_G1_H_
#define ZEPHYR_INCLUDE_DRIVERS_FLASH_MCHP_NVMCTRL_G1_H_


typedef enum {
        FLASH_EX_OP_USER_ROW_ERASE,

        FLASH_EX_OP_USER_ROW_WRITE,

        FLASH_EX_OP_REGION_LOCK,

        FLASH_EX_OP_REGION_UNLOCK
} flash_mchp_ex_ops_t;

typedef struct flash_mchp_ex_op_userrow_data {
        const void *data;

        size_t data_len;

        off_t offset;
} flash_mchp_ex_op_userrow_data_t;


#endif /* ZEPHYR_INCLUDE_DRIVERS_FLASH_MCHP_NVMCTRL_G1_H_ */
```

## 498.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 100 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FLASH_MCHP_NVMCTRL_G1_H_`。

## 498.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g1_8h.html)
- [FLASH_EX_OP_USER_ROW_ERASE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#gga4dae21b9b6e0a90faddfa045b30e19a8af25afe42760eb6f7af298f9ef44889af)
- [FLASH_EX_OP_USER_ROW_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#gga4dae21b9b6e0a90faddfa045b30e19a8a1a4c0eddbc371ca9cf9f4fd11f06847d)
- [FLASH_EX_OP_REGION_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#gga4dae21b9b6e0a90faddfa045b30e19a8a28aeedfece9b637e6698a64ad7e036e8)
- [FLASH_EX_OP_REGION_UNLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#gga4dae21b9b6e0a90faddfa045b30e19a8a412cbb9c36affa8a61e38c8ec77d22e4)
- [flash_mchp_ex_ops_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#ga4dae21b9b6e0a90faddfa045b30e19a8)
- [flash_mchp_ex_op_userrow_data](../system_service_model_reference/P032_flash_mchp_ex_op_userrow_data_结构体.md)
- [data](../system_service_model_reference/P032_flash_mchp_ex_op_userrow_data_结构体.md#a47930c1edb14b8b15f5800c7f05cf287)
- [data_len](../system_service_model_reference/P032_flash_mchp_ex_op_userrow_data_结构体.md#ae69ed8df0f2a63ab836df7fe7c35f1df)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [offset](../system_service_model_reference/P032_flash_mchp_ex_op_userrow_data_结构体.md#aeecffa84916b2be1f5118fc405ae5279)
- [flash_mchp_ex_op_userrow_data_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#ga26d417de48ac23416675b9830e3f8ee4)
- [flash_mchp_ex_op_userrow_data::data](../system_service_model_reference/P032_flash_mchp_ex_op_userrow_data_结构体.md#a47930c1edb14b8b15f5800c7f05cf287)
- [flash_mchp_ex_op_userrow_data::data_len](../system_service_model_reference/P032_flash_mchp_ex_op_userrow_data_结构体.md#ae69ed8df0f2a63ab836df7fe7c35f1df)
- [flash_mchp_ex_op_userrow_data::offset](../system_service_model_reference/P032_flash_mchp_ex_op_userrow_data_结构体.md#aeecffa84916b2be1f5118fc405ae5279)

---

[上一章](P497_mchp_flash.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P499_mchp_nvmctrl_g2.h_源码浏览.md)
