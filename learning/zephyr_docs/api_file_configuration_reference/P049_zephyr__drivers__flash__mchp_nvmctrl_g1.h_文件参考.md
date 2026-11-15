---
id: learning.zephyr-docs.api-file-configuration-reference.page-49
title: zephyr__drivers__flash__mchp_nvmctrl_g1.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g1_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_zephyr\_\_drivers\_\_flash\_\_mchp\_nvmctrl\_g1.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g1_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip NVMCTRL G1闪存扩展操作（Flash Extended Operations）的头文件。

查看此文件的源码。

<a id="details"></a>

Microchip 非易失性存储器控制器 G1（NVMCTRL G1）闪存扩展操作（Flash Extended Operations）的头文件。

注意（Note）：只有目标设备采用 NVMCTRL G1 闪存控制器时，才应包含本文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 49.1\_数据结构（Data Structures）

<a id="r_flash_5Fmchp_5Fex_5Fop_5Fuserrow_5Fdata"></a>

```c
struct flash_mchp_ex_op_userrow_data
```

相关声明：[flash_mchp_ex_op_userrow_data](../system_service_model_reference/P032_flash_mchp_ex_op_userrow_data_结构体.md)。

MCHP NVMCTRL G1闪存用户行（User Row）数据操作的参数。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 49.2\_类型定义（Typedefs）

<a id="r_ga26d417de48ac23416675b9830e3f8ee4"></a>

```c
typedef struct flash_mchp_ex_op_userrow_data flash_mchp_ex_op_userrow_data_t
```

相关声明：[flash_mchp_ex_op_userrow_data](../system_service_model_reference/P032_flash_mchp_ex_op_userrow_data_结构体.md)、[flash_mchp_ex_op_userrow_data_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#ga26d417de48ac23416675b9830e3f8ee4)。

MCHP NVMCTRL G1闪存用户行（User Row）数据操作的参数。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 49.3\_枚举（Enumerations）

<a id="r_ga4dae21b9b6e0a90faddfa045b30e19a8"></a>

```c
enum flash_mchp_ex_ops_t { FLASH_EX_OP_USER_ROW_ERASE , FLASH_EX_OP_USER_ROW_WRITE , FLASH_EX_OP_REGION_LOCK , FLASH_EX_OP_REGION_UNLOCK }
```

相关声明：[flash_mchp_ex_ops_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#ga4dae21b9b6e0a90faddfa045b30e19a8)、[FLASH_EX_OP_USER_ROW_ERASE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#gga4dae21b9b6e0a90faddfa045b30e19a8af25afe42760eb6f7af298f9ef44889af)、[FLASH_EX_OP_USER_ROW_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#gga4dae21b9b6e0a90faddfa045b30e19a8a1a4c0eddbc371ca9cf9f4fd11f06847d)、[FLASH_EX_OP_REGION_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#gga4dae21b9b6e0a90faddfa045b30e19a8a28aeedfece9b637e6698a64ad7e036e8)、[FLASH_EX_OP_REGION_UNLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#gga4dae21b9b6e0a90faddfa045b30e19a8a412cbb9c36affa8a61e38c8ec77d22e4)。

MCHP NVMCTRL G1 闪存控制器的扩展操作码（Extended Operation Codes）枚举（Enumeration）。


## 49.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P498_mchp_nvmctrl_g1.h_源码浏览.md)
- [flash_mchp_ex_op_userrow_data](../system_service_model_reference/P032_flash_mchp_ex_op_userrow_data_结构体.md)
- [flash_mchp_ex_op_userrow_data_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#ga26d417de48ac23416675b9830e3f8ee4)
- [flash_mchp_ex_ops_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#ga4dae21b9b6e0a90faddfa045b30e19a8)
- [FLASH_EX_OP_USER_ROW_ERASE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#gga4dae21b9b6e0a90faddfa045b30e19a8af25afe42760eb6f7af298f9ef44889af)
- [FLASH_EX_OP_USER_ROW_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#gga4dae21b9b6e0a90faddfa045b30e19a8a1a4c0eddbc371ca9cf9f4fd11f06847d)
- [FLASH_EX_OP_REGION_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#gga4dae21b9b6e0a90faddfa045b30e19a8a28aeedfece9b637e6698a64ad7e036e8)
- [FLASH_EX_OP_REGION_UNLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#gga4dae21b9b6e0a90faddfa045b30e19a8a412cbb9c36affa8a61e38c8ec77d22e4)

<a id="header-details"></a>

---

[上一章](P048_zephyr__dt-bindings__dma__mchp-xec-dmac.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P050_zephyr__drivers__flash__mchp_nvmctrl_g2.h_文件参考.md)
