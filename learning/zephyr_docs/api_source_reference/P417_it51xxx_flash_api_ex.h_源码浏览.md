---
id: learning.zephyr-docs.api-source-reference.page-417
title: it51xxx_flash_api_ex.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/it51xxx__flash__api__ex_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第417章\_it51xxx\_flash\_api\_ex.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/it51xxx__flash__api__ex_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/it51xxx__flash__api__ex_8h.html)。

## 417.1\_原始可见代码（Source Code）

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
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00054"></a>
<a id="l00061"></a>
<a id="l00068"></a>
<a id="l00075"></a>
<a id="l00082"></a>
<a id="l00086"></a>
<a id="l00090"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="foldopen00100"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00114"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="aflash_8h_html"></a>
<a id="agroup__it51xxx__flash__ex__op_html_ga202c4883f6d1108844399f52f7f8a650"></a>
<a id="agroup__it51xxx__flash__ex__op_html_gga202c4883f6d1108844399f52f7f8a650a1e6bb921cb7ef22edeb2e6a241a98526"></a>
<a id="agroup__it51xxx__flash__ex__op_html_gga202c4883f6d1108844399f52f7f8a650a2eaa44cde3aea200ab0cf3e09d92b492"></a>
<a id="agroup__it51xxx__flash__ex__op_html_gga202c4883f6d1108844399f52f7f8a650a3aac745c29f6fe7def99e2bfb1f92150"></a>
<a id="agroup__it51xxx__flash__ex__op_html_gga202c4883f6d1108844399f52f7f8a650a47a857da09d2086cbcec1b87cfcfab83"></a>
<a id="agroup__it51xxx__flash__ex__op_html_gga202c4883f6d1108844399f52f7f8a650aaf3619f6f55e8b4ecc11bce418ed042e"></a>
<a id="agroup__it51xxx__flash__ex__op_html_gga202c4883f6d1108844399f52f7f8a650abceab43c2f5880c68d1307ba3b4a640d"></a>
<a id="agroup__it51xxx__flash__ex__op_html_gga202c4883f6d1108844399f52f7f8a650ae447c52cb768677fe02af6fc51e90e3c"></a>
<a id="agroup__it51xxx__flash__ex__op_html_gga202c4883f6d1108844399f52f7f8a650ae732fbd6292ab7dc340c15510a5e5cc4"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructflash__it51xxx__ex__op__addr__protection_html"></a>
<a id="astructflash__it51xxx__ex__op__addr__protection_html_a05615f4f616b2d03d8218311faf9b57c"></a>
<a id="astructflash__it51xxx__ex__op__addr__protection_html_ac74e0e265856f6da0c8c76cae1e195aa"></a>
<a id="astructflash__it51xxx__ex__op__addr__protection_html_aeb261e12e2276ab42fe76d4a7803a3bb"></a>
<a id="astructflash__it51xxx__ex__op__addr__protection_html_af5f3e6d03547d30e1f0b922319803b06"></a>
<a id="astructflash__it51xxx__ex__op__wr__protect__lock_html"></a>
<a id="astructflash__it51xxx__ex__op__wr__protect__lock_html_a1702b7b51516aeb5cc0195ea2db1689e"></a>
<a id="astructflash__it51xxx__ex__op__wr__protect__lock_html_a9e3607562530d062a8ac22f6b1b1cc72"></a>

```c
/*
 * Copyright (c) 2025 ITE Corporation. All Rights Reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FLASH_IT51XXX_FLASH_API_EX_H_
#define ZEPHYR_INCLUDE_DRIVERS_FLASH_IT51XXX_FLASH_API_EX_H_


#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/drivers/flash.h>

#define IT51XXX_PROTECT_PATH_COUNT 3
#define PROTECT_PATH_EC            BIT(0)
#define PROTECT_PATH_HOST          BIT(1)
#define PROTECT_PATH_DBGR          BIT(2)
#define PROTECT_PATH_ALL           (PROTECT_PATH_EC | PROTECT_PATH_HOST | PROTECT_PATH_DBGR)

enum flash_it51xxx_ex_op {
        FLASH_IT51XXX_INTERNAL,
        FLASH_IT51XXX_EXTERNAL_FSPI_CS0,
        FLASH_IT51XXX_EXTERNAL_FSPI_CS1,
        FLASH_IT51XXX_ADDR_3B,
        FLASH_IT51XXX_ADDR_4B,
        FLASH_IT51XXX_WRITE_PROTECT,
        FLASH_IT51XXX_READ_PROTECT,
        FLASH_IT51XXX_WR_PROTECT_LOCK,
};

struct flash_it51xxx_ex_op_addr_protection {
        uint32_t addr;
        size_t size;
        uint8_t path;
        bool is_protected;
};

struct flash_it51xxx_ex_op_wr_protect_lock {
        uint8_t path;
        bool is_locked;
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_FLASH_IT51XXX_FLASH_API_EX_H_ */
```

## 417.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 ITE Corporation. All Rights Reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 131 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FLASH_IT51XXX_FLASH_API_EX_H_`。

## 417.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/it51xxx__flash__api__ex_8h.html)
- [zephyr/drivers/flash.h](../flash_reference/P009_Flash公共头文件参考.md)
- [flash_it51xxx_ex_op](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#ga202c4883f6d1108844399f52f7f8a650)
- [FLASH_IT51XXX_INTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650ae732fbd6292ab7dc340c15510a5e5cc4)
- [FLASH_IT51XXX_EXTERNAL_FSPI_CS0](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650a2eaa44cde3aea200ab0cf3e09d92b492)
- [FLASH_IT51XXX_EXTERNAL_FSPI_CS1](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650abceab43c2f5880c68d1307ba3b4a640d)
- [FLASH_IT51XXX_ADDR_3B](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650aaf3619f6f55e8b4ecc11bce418ed042e)
- [FLASH_IT51XXX_ADDR_4B](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650a1e6bb921cb7ef22edeb2e6a241a98526)
- [FLASH_IT51XXX_WRITE_PROTECT](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650a3aac745c29f6fe7def99e2bfb1f92150)
- [FLASH_IT51XXX_READ_PROTECT](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650a47a857da09d2086cbcec1b87cfcfab83)
- [FLASH_IT51XXX_WR_PROTECT_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650ae447c52cb768677fe02af6fc51e90e3c)
- [flash_it51xxx_ex_op_addr_protection](../system_service_model_reference/P030_flash_it51xxx_ex_op_addr_protection_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [addr](../system_service_model_reference/P030_flash_it51xxx_ex_op_addr_protection_结构体.md#a05615f4f616b2d03d8218311faf9b57c)
- [size](../system_service_model_reference/P030_flash_it51xxx_ex_op_addr_protection_结构体.md#aeb261e12e2276ab42fe76d4a7803a3bb)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [path](../system_service_model_reference/P030_flash_it51xxx_ex_op_addr_protection_结构体.md#ac74e0e265856f6da0c8c76cae1e195aa)
- [is_protected](../system_service_model_reference/P030_flash_it51xxx_ex_op_addr_protection_结构体.md#af5f3e6d03547d30e1f0b922319803b06)
- [flash_it51xxx_ex_op_wr_protect_lock](../system_service_model_reference/P031_flash_it51xxx_ex_op_wr_protect_lock_结构体.md)
- [path](../system_service_model_reference/P031_flash_it51xxx_ex_op_wr_protect_lock_结构体.md#a1702b7b51516aeb5cc0195ea2db1689e)
- [is_locked](../system_service_model_reference/P031_flash_it51xxx_ex_op_wr_protect_lock_结构体.md#a9e3607562530d062a8ac22f6b1b1cc72)
- [flash.h](../flash_reference/P009_Flash公共头文件参考.md)
- [flash_it51xxx_ex_op_addr_protection::addr](../system_service_model_reference/P030_flash_it51xxx_ex_op_addr_protection_结构体.md#a05615f4f616b2d03d8218311faf9b57c)
- [flash_it51xxx_ex_op_addr_protection::path](../system_service_model_reference/P030_flash_it51xxx_ex_op_addr_protection_结构体.md#ac74e0e265856f6da0c8c76cae1e195aa)
- [flash_it51xxx_ex_op_addr_protection::size](../system_service_model_reference/P030_flash_it51xxx_ex_op_addr_protection_结构体.md#aeb261e12e2276ab42fe76d4a7803a3bb)
- [flash_it51xxx_ex_op_addr_protection::is_protected](../system_service_model_reference/P030_flash_it51xxx_ex_op_addr_protection_结构体.md#af5f3e6d03547d30e1f0b922319803b06)
- [flash_it51xxx_ex_op_wr_protect_lock::path](../system_service_model_reference/P031_flash_it51xxx_ex_op_wr_protect_lock_结构体.md#a1702b7b51516aeb5cc0195ea2db1689e)
- [flash_it51xxx_ex_op_wr_protect_lock::is_locked](../system_service_model_reference/P031_flash_it51xxx_ex_op_wr_protect_lock_结构体.md#a9e3607562530d062a8ac22f6b1b1cc72)

---

[上一章](P416_it51xxx-vcmp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P418_it51xxx_tach.h_源码浏览.md)
