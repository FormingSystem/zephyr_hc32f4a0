---
id: learning.zephyr-docs.api-source-reference.page-499
title: mchp_nvmctrl_g2.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g2_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第499章\_mchp\_nvmctrl\_g2.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g2_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g2_8h.html)。

## 499.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00033"></a>
<a id="foldopen00039"></a>
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
<a id="l00053"></a>
<a id="l00054"></a>
<a id="agroup__mchp__flash__interface_html_gga4dae21b9b6e0a90faddfa045b30e19a8a5b1b658937299999761f59173a16b93e"></a>
<a id="agroup__mchp__flash__interface_html_gga4dae21b9b6e0a90faddfa045b30e19a8a6525dc6f8c6b289b1d2f6402f57ad312"></a>
<a id="agroup__mchp__flash__interface_html_gga4dae21b9b6e0a90faddfa045b30e19a8a7f180551fd905e7ca4d217932087787a"></a>
<a id="agroup__mchp__flash__interface_html_gga4dae21b9b6e0a90faddfa045b30e19a8a953190cedd6519ce991793a07b990cc1"></a>
<a id="agroup__mchp__flash__interface_html_gga4dae21b9b6e0a90faddfa045b30e19a8acdbe7b8985bb07f8fb0faadee3072dcb"></a>
<a id="agroup__mchp__flash__interface_html_gga4dae21b9b6e0a90faddfa045b30e19a8aefa3c18a91556306795f51a14fba9f4b"></a>
<a id="agroup__mchp__nvmctrl__g1__flash__ex__op_html_ga4dae21b9b6e0a90faddfa045b30e19a8"></a>
<a id="agroup__mchp__nvmctrl__g1__flash__ex__op_html_gga4dae21b9b6e0a90faddfa045b30e19a8a28aeedfece9b637e6698a64ad7e036e8"></a>
<a id="agroup__mchp__nvmctrl__g1__flash__ex__op_html_gga4dae21b9b6e0a90faddfa045b30e19a8a412cbb9c36affa8a61e38c8ec77d22e4"></a>

```c
/*
 * Copyright (c) 2026 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef INCLUDE_ZEPHYR_DRIVERS_FLASH_MCHP_NVMCTRL_G2_H_
#define INCLUDE_ZEPHYR_DRIVERS_FLASH_MCHP_NVMCTRL_G2_H_


typedef enum {
        FLASH_EX_OP_REGION_LOCK,
        FLASH_EX_OP_REGION_UNLOCK,
        FLASH_EX_OP_SET_PWR_REDUCTION_MODE,
        FLASH_EX_OP_CLR_PWR_REDUCTION_MODE,
        FLASH_EX_OP_CLR_PAGE_BUFFER,
        FLASH_EX_OP_SET_SECURITY_BIT,
        FLASH_EX_OP_INVALIDATE_CACHE_LINES,
        FLASH_EX_OP_SET_CHIP_ERASE_HARDLOCK,
} flash_mchp_ex_ops_t;


#endif /* INCLUDE_ZEPHYR_DRIVERS_FLASH_MCHP_NVMCTRL_G2_H_ */
```

## 499.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 54 行

头文件保护宏（Header guard）标记：`INCLUDE_ZEPHYR_DRIVERS_FLASH_MCHP_NVMCTRL_G2_H_`。

## 499.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g2_8h.html)
- [FLASH_EX_OP_REGION_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#gga4dae21b9b6e0a90faddfa045b30e19a8a28aeedfece9b637e6698a64ad7e036e8)
- [FLASH_EX_OP_REGION_UNLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#gga4dae21b9b6e0a90faddfa045b30e19a8a412cbb9c36affa8a61e38c8ec77d22e4)
- [FLASH_EX_OP_SET_PWR_REDUCTION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a7f180551fd905e7ca4d217932087787a)
- [FLASH_EX_OP_CLR_PWR_REDUCTION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a5b1b658937299999761f59173a16b93e)
- [FLASH_EX_OP_CLR_PAGE_BUFFER](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a953190cedd6519ce991793a07b990cc1)
- [FLASH_EX_OP_SET_SECURITY_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8aefa3c18a91556306795f51a14fba9f4b)
- [FLASH_EX_OP_INVALIDATE_CACHE_LINES](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8acdbe7b8985bb07f8fb0faadee3072dcb)
- [FLASH_EX_OP_SET_CHIP_ERASE_HARDLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a6525dc6f8c6b289b1d2f6402f57ad312)
- [flash_mchp_ex_ops_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#ga4dae21b9b6e0a90faddfa045b30e19a8)

---

[上一章](P498_mchp_nvmctrl_g1.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P500_mchp_nvmctrl_g3.h_源码浏览.md)
