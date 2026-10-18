---
id: learning.zephyr-docs.api-source-reference.page-500
title: mchp_nvmctrl_g3.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g3_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第500章\_mchp\_nvmctrl\_g3.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g3_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g3_8h.html)。

## 500.1\_原始可见代码（Source Code）

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
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00042"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="foldopen00082"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="foldopen00094"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="foldopen00112"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="agroup__mchp__flash__interface_html_ga68310865b2b4ef28fe8259b0d625bc56"></a>
<a id="agroup__mchp__flash__interface_html_gae4ce42c1991f6edf715e4aa2b294234b"></a>
<a id="agroup__mchp__flash__interface_html_gga4dae21b9b6e0a90faddfa045b30e19a8a30737465e185532f3400725b533ee3a9"></a>
<a id="agroup__mchp__flash__interface_html_gga4dae21b9b6e0a90faddfa045b30e19a8a71054144eabce681da9ee95e852211da"></a>
<a id="agroup__mchp__flash__interface_html_gga4dae21b9b6e0a90faddfa045b30e19a8a8f0b96d19fb3584a24addfc0749b758f"></a>
<a id="agroup__mchp__flash__interface_html_gga4dae21b9b6e0a90faddfa045b30e19a8aa8818fcf993809f03564ab8e15de3d89"></a>
<a id="agroup__mchp__flash__interface_html_gga4dae21b9b6e0a90faddfa045b30e19a8adf56dd5adcb84bb4a56ea2b112279122"></a>
<a id="agroup__mchp__flash__interface_html_gga4dae21b9b6e0a90faddfa045b30e19a8ae20aba272606df44e4e4c5cd76078675"></a>
<a id="agroup__mchp__flash__interface_html_gga68310865b2b4ef28fe8259b0d625bc56a24d6f6c04f0013976549e02f03126b6c"></a>
<a id="agroup__mchp__flash__interface_html_gga68310865b2b4ef28fe8259b0d625bc56a350b8165b2c0bfc682d8a46ea87593fb"></a>
<a id="agroup__mchp__flash__interface_html_gga68310865b2b4ef28fe8259b0d625bc56a686c824b326a95a54c52c7d2a97ee2e5"></a>
<a id="agroup__mchp__flash__interface_html_gga68310865b2b4ef28fe8259b0d625bc56a6e913daec2faf0d10082ce1f520ff268"></a>
<a id="agroup__mchp__flash__interface_html_gga68310865b2b4ef28fe8259b0d625bc56a7f2214b918478b67a9fb986bb13573ee"></a>
<a id="agroup__mchp__flash__interface_html_gga68310865b2b4ef28fe8259b0d625bc56a9d007673c8b011e551fd0eaf67ce0a6d"></a>
<a id="agroup__mchp__flash__interface_html_gga68310865b2b4ef28fe8259b0d625bc56ae5ed65dd074c8ec6fe07086ece6c6c89"></a>
<a id="agroup__mchp__flash__interface_html_gga68310865b2b4ef28fe8259b0d625bc56ae71436dcc0d7a89d9d497eb8e21697f9"></a>
<a id="agroup__mchp__flash__interface_html_ggae4ce42c1991f6edf715e4aa2b294234ba2e23c772674e6e52a08fe8519a7f496d"></a>
<a id="agroup__mchp__flash__interface_html_ggae4ce42c1991f6edf715e4aa2b294234bab4d24bb75453d95c963ff5d7a529bbbe"></a>
<a id="agroup__mchp__nvmctrl__g1__flash__ex__op_html_ga4dae21b9b6e0a90faddfa045b30e19a8"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructbfm__exop_html"></a>
<a id="astructbfm__exop_html_a2b390a2ae33a5690850b95df7b5f8e7d"></a>
<a id="astructbfm__exop_html_a2c16d2c160205b3eaba14b9f0ecb8c37"></a>
<a id="astructpfm__exop_html"></a>
<a id="astructpfm__exop_html_aaf55812dbc58f2f97b97122efc8390dd"></a>
<a id="astructpfm__exop_html_ae724956923f6d97a5c1bc7064dd94de1"></a>
<a id="astructpfm__exop_html_af498df4d30381eb4ee74380e9c2f2639"></a>
<a id="astructpfm__exop_html_af86d62884866a07344bf0a1e11022d06"></a>

```c
/*
 * Copyright (c) 2026 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef INCLUDE_ZEPHYR_DRIVERS_FLASH_MCHP_NVMCTRL_G3_H_
#define INCLUDE_ZEPHYR_DRIVERS_FLASH_MCHP_NVMCTRL_G3_H_


#include <zephyr/types.h>
#include <stdbool.h>

enum flash_mchp_ex_ops_t {
        FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_ENABLE,
        FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_DISABLE,
        FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_LOCK,
        FLASH_EX_OP_BFM_WRITE_PROTECT_ENABLE,
        FLASH_EX_OP_BFM_WRITE_PROTECT_DISABLE,
        FLASH_EX_OP_BFM_WRITE_PROTECT_LOCK,
};

enum pfm_wp_region {
        PFM_WP_REGION_0,
        PFM_WP_REGION_1,
        PFM_WP_REGION_2,
        PFM_WP_REGION_3,
        PFM_WP_REGION_4,
        PFM_WP_REGION_5,
        PFM_WP_REGION_6,
        PFM_WP_REGION_7,
};

enum boot_flash_bank {
        BOOT_FLASH_BANK_1,
        BOOT_FLASH_BANK_2
};

struct pfm_exop {
        enum pfm_wp_region region;
        uint32_t base_addr;
        uint32_t region_size;
        bool mirror_enable;
};

struct bfm_exop {
        enum boot_flash_bank boot_bank;
        uint32_t wp_page;
};


#endif /*INCLUDE_ZEPHYR_DRIVERS_FLASH_MCHP_NVMCTRL_G3_H_*/
```

## 500.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 123 行

头文件保护宏（Header guard）标记：`INCLUDE_ZEPHYR_DRIVERS_FLASH_MCHP_NVMCTRL_G3_H_`。

## 500.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g3_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [flash_mchp_ex_ops_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#ga4dae21b9b6e0a90faddfa045b30e19a8)
- [FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a30737465e185532f3400725b533ee3a9)
- [FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8aa8818fcf993809f03564ab8e15de3d89)
- [FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8ae20aba272606df44e4e4c5cd76078675)
- [FLASH_EX_OP_BFM_WRITE_PROTECT_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8adf56dd5adcb84bb4a56ea2b112279122)
- [FLASH_EX_OP_BFM_WRITE_PROTECT_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a71054144eabce681da9ee95e852211da)
- [FLASH_EX_OP_BFM_WRITE_PROTECT_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a8f0b96d19fb3584a24addfc0749b758f)
- [pfm_wp_region](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#ga68310865b2b4ef28fe8259b0d625bc56)
- [PFM_WP_REGION_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga68310865b2b4ef28fe8259b0d625bc56ae5ed65dd074c8ec6fe07086ece6c6c89)
- [PFM_WP_REGION_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga68310865b2b4ef28fe8259b0d625bc56a9d007673c8b011e551fd0eaf67ce0a6d)
- [PFM_WP_REGION_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga68310865b2b4ef28fe8259b0d625bc56ae71436dcc0d7a89d9d497eb8e21697f9)
- [PFM_WP_REGION_3](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga68310865b2b4ef28fe8259b0d625bc56a7f2214b918478b67a9fb986bb13573ee)
- [PFM_WP_REGION_4](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga68310865b2b4ef28fe8259b0d625bc56a350b8165b2c0bfc682d8a46ea87593fb)
- [PFM_WP_REGION_5](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga68310865b2b4ef28fe8259b0d625bc56a6e913daec2faf0d10082ce1f520ff268)
- [PFM_WP_REGION_6](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga68310865b2b4ef28fe8259b0d625bc56a24d6f6c04f0013976549e02f03126b6c)
- [PFM_WP_REGION_7](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga68310865b2b4ef28fe8259b0d625bc56a686c824b326a95a54c52c7d2a97ee2e5)
- [boot_flash_bank](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gae4ce42c1991f6edf715e4aa2b294234b)
- [BOOT_FLASH_BANK_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#ggae4ce42c1991f6edf715e4aa2b294234ba2e23c772674e6e52a08fe8519a7f496d)
- [BOOT_FLASH_BANK_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#ggae4ce42c1991f6edf715e4aa2b294234bab4d24bb75453d95c963ff5d7a529bbbe)
- [pfm_exop](../device_power_control_model_reference/P059_pfm_exop_结构体.md)
- [region](../device_power_control_model_reference/P059_pfm_exop_结构体.md#ae724956923f6d97a5c1bc7064dd94de1)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [base_addr](../device_power_control_model_reference/P059_pfm_exop_结构体.md#aaf55812dbc58f2f97b97122efc8390dd)
- [region_size](../device_power_control_model_reference/P059_pfm_exop_结构体.md#af86d62884866a07344bf0a1e11022d06)
- [mirror_enable](../device_power_control_model_reference/P059_pfm_exop_结构体.md#af498df4d30381eb4ee74380e9c2f2639)
- [bfm_exop](../driver_model_reference/P026_启动闪存BFM扩展操作.md)
- [boot_bank](../driver_model_reference/P026_启动闪存BFM扩展操作.md#a2c16d2c160205b3eaba14b9f0ecb8c37)
- [wp_page](../driver_model_reference/P026_启动闪存BFM扩展操作.md#a2b390a2ae33a5690850b95df7b5f8e7d)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [bfm_exop::wp_page](../driver_model_reference/P026_启动闪存BFM扩展操作.md#a2b390a2ae33a5690850b95df7b5f8e7d)
- [bfm_exop::boot_bank](../driver_model_reference/P026_启动闪存BFM扩展操作.md#a2c16d2c160205b3eaba14b9f0ecb8c37)
- [pfm_exop::base_addr](../device_power_control_model_reference/P059_pfm_exop_结构体.md#aaf55812dbc58f2f97b97122efc8390dd)
- [pfm_exop::region](../device_power_control_model_reference/P059_pfm_exop_结构体.md#ae724956923f6d97a5c1bc7064dd94de1)
- [pfm_exop::mirror_enable](../device_power_control_model_reference/P059_pfm_exop_结构体.md#af498df4d30381eb4ee74380e9c2f2639)
- [pfm_exop::region_size](../device_power_control_model_reference/P059_pfm_exop_结构体.md#af86d62884866a07344bf0a1e11022d06)

---

[上一章](P499_mchp_nvmctrl_g2.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P501_mchp_pic32ck_sg_gc_clock.h_源码浏览.md)
