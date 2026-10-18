---
id: learning.zephyr-docs.api-file-runtime-reference.page-35
title: zephyr__drivers__flash__mchp_nvmctrl_g3.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g3_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_zephyr\_\_drivers\_\_flash\_\_mchp\_nvmctrl\_g3.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g3_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

支持Microchip flash-controller G3驱动ex_op扩展操作的头文件。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <stdbool.h>
```

查看此文件的源码。

支持 Microchip G3 闪存控制器驱动（Flash-Controller G3 Driver）扩展操作（`ex_op`）的头文件。本头文件定义 Microchip NVMCTRL G3 闪存控制器特有的附加闪存操作。它通过提供区域锁定／解锁（Region Locking / Unlocking）、清除页缓冲区（Clear Page Buffer）等高级操作，扩展标准闪存 API 的能力。

注意（Note）：只有目标设备采用 NVMCTRL G3 闪存控制器时，才应使用此 API 扩展。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 35.1\_数据结构（Data Structures）

<a id="r_pfm_5Fexop"></a>

```c
struct pfm_exop
```

相关声明：[pfm_exop](../device_power_control_model_reference/P059_pfm_exop_结构体.md)。

程序闪存（Program Flash Memory，PFM）的扩展操作参数。

<a id="r_bfm_5Fexop"></a>

```c
struct bfm_exop
```

相关声明：[bfm_exop](../driver_model_reference/P026_启动闪存BFM扩展操作.md)。

启动闪存（Boot Flash Memory，BFM）扩展操作参数。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 35.2\_枚举（Enumerations）

<a id="r_ga4dae21b9b6e0a90faddfa045b30e19a8"></a>

```c
enum flash_mchp_ex_ops_t { FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_ENABLE , FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_DISABLE , FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_LOCK , FLASH_EX_OP_BFM_WRITE_PROTECT_ENABLE , FLASH_EX_OP_BFM_WRITE_PROTECT_DISABLE , FLASH_EX_OP_BFM_WRITE_PROTECT_LOCK }
```

相关声明：[flash_mchp_ex_ops_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#ga4dae21b9b6e0a90faddfa045b30e19a8)、[FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a30737465e185532f3400725b533ee3a9)、[FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8aa8818fcf993809f03564ab8e15de3d89)、[FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8ae20aba272606df44e4e4c5cd76078675)、[FLASH_EX_OP_BFM_WRITE_PROTECT_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8adf56dd5adcb84bb4a56ea2b112279122)、[FLASH_EX_OP_BFM_WRITE_PROTECT_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a71054144eabce681da9ee95e852211da)、[FLASH_EX_OP_BFM_WRITE_PROTECT_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a8f0b96d19fb3584a24addfc0749b758f)。

本枚举（Enumeration）定义可对闪存执行的扩展操作（Extended Operations），例如擦除或写入用户行（User Row），以及锁定或解锁特定闪存区域（Flash Regions）。

<a id="r_ga68310865b2b4ef28fe8259b0d625bc56"></a>

```c
enum pfm_wp_region { PFM_WP_REGION_0 , PFM_WP_REGION_1 , PFM_WP_REGION_2 , PFM_WP_REGION_3 , PFM_WP_REGION_4 , PFM_WP_REGION_5 , PFM_WP_REGION_6 , PFM_WP_REGION_7 }
```

相关声明：[pfm_wp_region](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#ga68310865b2b4ef28fe8259b0d625bc56)、[PFM_WP_REGION_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga68310865b2b4ef28fe8259b0d625bc56ae5ed65dd074c8ec6fe07086ece6c6c89)、[PFM_WP_REGION_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga68310865b2b4ef28fe8259b0d625bc56a9d007673c8b011e551fd0eaf67ce0a6d)、[PFM_WP_REGION_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga68310865b2b4ef28fe8259b0d625bc56ae71436dcc0d7a89d9d497eb8e21697f9)、[PFM_WP_REGION_3](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga68310865b2b4ef28fe8259b0d625bc56a7f2214b918478b67a9fb986bb13573ee)、[PFM_WP_REGION_4](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga68310865b2b4ef28fe8259b0d625bc56a350b8165b2c0bfc682d8a46ea87593fb)、[PFM_WP_REGION_5](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga68310865b2b4ef28fe8259b0d625bc56a6e913daec2faf0d10082ce1f520ff268)、[PFM_WP_REGION_6](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga68310865b2b4ef28fe8259b0d625bc56a24d6f6c04f0013976549e02f03126b6c)、[PFM_WP_REGION_7](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga68310865b2b4ef28fe8259b0d625bc56a686c824b326a95a54c52c7d2a97ee2e5)。

程序闪存（Program Flash Memory，PFM）的写保护区域（Write Protection Regions）。

<a id="r_gae4ce42c1991f6edf715e4aa2b294234b"></a>

```c
enum boot_flash_bank { BOOT_FLASH_BANK_1 , BOOT_FLASH_BANK_2 }
```

相关声明：[boot_flash_bank](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gae4ce42c1991f6edf715e4aa2b294234b)、[BOOT_FLASH_BANK_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#ggae4ce42c1991f6edf715e4aa2b294234ba2e23c772674e6e52a08fe8519a7f496d)、[BOOT_FLASH_BANK_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#ggae4ce42c1991f6edf715e4aa2b294234bab4d24bb75453d95c963ff5d7a529bbbe)。

引导闪存（Boot Flash Memory，BFM）的存储体选择（Bank Selection）。


## 35.3\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P500_mchp_nvmctrl_g3.h_源码浏览.md)
- [pfm_exop](../device_power_control_model_reference/P059_pfm_exop_结构体.md)
- [bfm_exop](../driver_model_reference/P026_启动闪存BFM扩展操作.md)
- [flash_mchp_ex_ops_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#ga4dae21b9b6e0a90faddfa045b30e19a8)
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

<a id="header-details"></a>

---

[上一章](P034_zephyr__drivers__sensor__max30210.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P036_zephyr__drivers__reset__mchp_rstc_g1.h_文件参考.md)
