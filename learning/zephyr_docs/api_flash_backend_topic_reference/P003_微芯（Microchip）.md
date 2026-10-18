---
id: learning.zephyr-docs.api-flash-backend-topic-reference.page-3
title: 微芯（Microchip）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_微芯（Microchip）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip G3 闪存控制器的扩展操作。

<a id="details"></a>

Microchip G3 闪存控制器（Flash Memory Controllers）的扩展操作（Extended Operations）。自 4.5 起提供，版本 0.1.0。

<a id="header-files"></a>
<a id="files"></a>

## 3.1\_文件（Files）

<a id="r_mchp_5Fnvmctrl_5Fg2_2Eh"></a>

```c
file mchp_nvmctrl_g2.h
```

相关声明：[mchp_nvmctrl_g2.h](../api_file_configuration_reference/P050_zephyr__drivers__flash__mchp_nvmctrl_g2.h_文件参考.md)。

支持Microchip flash-controller G2驱动ex_op扩展操作的头文件。

<a id="r_mchp_5Fnvmctrl_5Fg3_2Eh"></a>

```c
file mchp_nvmctrl_g3.h
```

相关声明：[mchp_nvmctrl_g3.h](../api_file_runtime_reference/P035_zephyr__drivers__flash__mchp_nvmctrl_g3.h_文件参考.md)。

支持Microchip flash-controller G3驱动ex_op扩展操作的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.2\_数据结构（Data Structures）

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

## 3.3\_枚举（Enumerations）

<a id="r_ga4dae21b9b6e0a90faddfa045b30e19a8"></a>

```c
enum flash_mchp_ex_ops_t { FLASH_EX_OP_REGION_LOCK , FLASH_EX_OP_REGION_UNLOCK , FLASH_EX_OP_SET_PWR_REDUCTION_MODE , FLASH_EX_OP_CLR_PWR_REDUCTION_MODE , FLASH_EX_OP_CLR_PAGE_BUFFER , FLASH_EX_OP_SET_SECURITY_BIT , FLASH_EX_OP_INVALIDATE_CACHE_LINES , FLASH_EX_OP_SET_CHIP_ERASE_HARDLOCK }
```

相关声明：[flash_mchp_ex_ops_t](#ga4dae21b9b6e0a90faddfa045b30e19a8)、[FLASH_EX_OP_REGION_LOCK](#gga4dae21b9b6e0a90faddfa045b30e19a8a28aeedfece9b637e6698a64ad7e036e8)、[FLASH_EX_OP_REGION_UNLOCK](#gga4dae21b9b6e0a90faddfa045b30e19a8a412cbb9c36affa8a61e38c8ec77d22e4)、[FLASH_EX_OP_SET_PWR_REDUCTION_MODE](#gga4dae21b9b6e0a90faddfa045b30e19a8a7f180551fd905e7ca4d217932087787a)、[FLASH_EX_OP_CLR_PWR_REDUCTION_MODE](#gga4dae21b9b6e0a90faddfa045b30e19a8a5b1b658937299999761f59173a16b93e)、[FLASH_EX_OP_CLR_PAGE_BUFFER](#gga4dae21b9b6e0a90faddfa045b30e19a8a953190cedd6519ce991793a07b990cc1)、[FLASH_EX_OP_SET_SECURITY_BIT](#gga4dae21b9b6e0a90faddfa045b30e19a8aefa3c18a91556306795f51a14fba9f4b)、[FLASH_EX_OP_INVALIDATE_CACHE_LINES](#gga4dae21b9b6e0a90faddfa045b30e19a8acdbe7b8985bb07f8fb0faadee3072dcb)、[FLASH_EX_OP_SET_CHIP_ERASE_HARDLOCK](#gga4dae21b9b6e0a90faddfa045b30e19a8a6525dc6f8c6b289b1d2f6402f57ad312)。

本枚举（Enumeration）定义可对闪存执行的扩展操作（Extended Operations），例如擦除或写入用户行（User Row），以及锁定或解锁特定闪存区域（Flash Regions）。

```c
enum flash_mchp_ex_ops_t { FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_ENABLE , FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_DISABLE , FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_LOCK , FLASH_EX_OP_BFM_WRITE_PROTECT_ENABLE , FLASH_EX_OP_BFM_WRITE_PROTECT_DISABLE , FLASH_EX_OP_BFM_WRITE_PROTECT_LOCK }
```

相关声明：[flash_mchp_ex_ops_t](#ga4dae21b9b6e0a90faddfa045b30e19a8)、[FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_ENABLE](#gga4dae21b9b6e0a90faddfa045b30e19a8a30737465e185532f3400725b533ee3a9)、[FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_DISABLE](#gga4dae21b9b6e0a90faddfa045b30e19a8aa8818fcf993809f03564ab8e15de3d89)、[FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_LOCK](#gga4dae21b9b6e0a90faddfa045b30e19a8ae20aba272606df44e4e4c5cd76078675)、[FLASH_EX_OP_BFM_WRITE_PROTECT_ENABLE](#gga4dae21b9b6e0a90faddfa045b30e19a8adf56dd5adcb84bb4a56ea2b112279122)、[FLASH_EX_OP_BFM_WRITE_PROTECT_DISABLE](#gga4dae21b9b6e0a90faddfa045b30e19a8a71054144eabce681da9ee95e852211da)、[FLASH_EX_OP_BFM_WRITE_PROTECT_LOCK](#gga4dae21b9b6e0a90faddfa045b30e19a8a8f0b96d19fb3584a24addfc0749b758f)。

本枚举（Enumeration）定义可对闪存执行的扩展操作（Extended Operations），例如擦除或写入用户行（User Row），以及锁定或解锁特定闪存区域（Flash Regions）。

<a id="r_ga68310865b2b4ef28fe8259b0d625bc56"></a>

```c
enum pfm_wp_region { PFM_WP_REGION_0 , PFM_WP_REGION_1 , PFM_WP_REGION_2 , PFM_WP_REGION_3 , PFM_WP_REGION_4 , PFM_WP_REGION_5 , PFM_WP_REGION_6 , PFM_WP_REGION_7 }
```

相关声明：[pfm_wp_region](#ga68310865b2b4ef28fe8259b0d625bc56)、[PFM_WP_REGION_0](#gga68310865b2b4ef28fe8259b0d625bc56ae5ed65dd074c8ec6fe07086ece6c6c89)、[PFM_WP_REGION_1](#gga68310865b2b4ef28fe8259b0d625bc56a9d007673c8b011e551fd0eaf67ce0a6d)、[PFM_WP_REGION_2](#gga68310865b2b4ef28fe8259b0d625bc56ae71436dcc0d7a89d9d497eb8e21697f9)、[PFM_WP_REGION_3](#gga68310865b2b4ef28fe8259b0d625bc56a7f2214b918478b67a9fb986bb13573ee)、[PFM_WP_REGION_4](#gga68310865b2b4ef28fe8259b0d625bc56a350b8165b2c0bfc682d8a46ea87593fb)、[PFM_WP_REGION_5](#gga68310865b2b4ef28fe8259b0d625bc56a6e913daec2faf0d10082ce1f520ff268)、[PFM_WP_REGION_6](#gga68310865b2b4ef28fe8259b0d625bc56a24d6f6c04f0013976549e02f03126b6c)、[PFM_WP_REGION_7](#gga68310865b2b4ef28fe8259b0d625bc56a686c824b326a95a54c52c7d2a97ee2e5)。

程序闪存（Program Flash Memory，PFM）的写保护区域（Write Protection Regions）。

<a id="r_gae4ce42c1991f6edf715e4aa2b294234b"></a>

```c
enum boot_flash_bank { BOOT_FLASH_BANK_1 , BOOT_FLASH_BANK_2 }
```

相关声明：[boot_flash_bank](#gae4ce42c1991f6edf715e4aa2b294234b)、[BOOT_FLASH_BANK_1](#ggae4ce42c1991f6edf715e4aa2b294234ba2e23c772674e6e52a08fe8519a7f496d)、[BOOT_FLASH_BANK_2](#ggae4ce42c1991f6edf715e4aa2b294234bab4d24bb75453d95c963ff5d7a529bbbe)。

引导闪存（Boot Flash Memory，BFM）的存储体选择（Bank Selection）。

## 3.4\_详细说明（Detailed Documentation）

<a id="gae4ce42c1991f6edf715e4aa2b294234b"></a>

### `boot_flash_bank`

```c
enum boot_flash_bank
```

```c
#include <zephyr/drivers/flash/mchp_nvmctrl_g3.h>
```

引导闪存（Boot Flash Memory，BFM）的存储体选择（Bank Selection）。

此枚举定义可用的启动闪存存储体／分区（Boot Flash Memory Banks/Panels）。启动闪存可组织为多个存储体，以支持冗余（Redundancy）和故障安全启动（Fail-safe Boot）操作。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BOOT_FLASH_BANK_1` | 启动闪存存储体／分区 1（Boot Flash Memory Bank/Panel 1）。 |
| `BOOT_FLASH_BANK_2` | 启动闪存存储体／分区 2（Boot Flash Memory Bank/Panel 2）。 |

<a id="ga4dae21b9b6e0a90faddfa045b30e19a8"></a>

### `flash_mchp_ex_ops_t [1/2]`

```c
enum flash_mchp_ex_ops_t
```

```c
#include <zephyr/drivers/flash/mchp_nvmctrl_g2.h>
```

本枚举（Enumeration）定义可对闪存执行的扩展操作（Extended Operations），例如擦除或写入用户行（User Row），以及锁定或解锁特定闪存区域（Flash Regions）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FLASH_EX_OP_REGION_LOCK` | 锁定指定区域（Region）。 |
| `FLASH_EX_OP_REGION_UNLOCK` | 解锁指定区域（Region）。 |
| `FLASH_EX_OP_SET_PWR_REDUCTION_MODE` | 设置功耗降低模式（Power Reduction Mode）。 |
| `FLASH_EX_OP_CLR_PWR_REDUCTION_MODE` | 清除功耗降低模式（Power Reduction Mode）。 |
| `FLASH_EX_OP_CLR_PAGE_BUFFER` | 清空闪存页缓冲区（Flash Page Buffer）。 |
| `FLASH_EX_OP_SET_SECURITY_BIT` | 设置安全位（Security Bit）。 |
| `FLASH_EX_OP_INVALIDATE_CACHE_LINES` | 使全部缓存行（Cache Lines）失效。 |
| `FLASH_EX_OP_SET_CHIP_ERASE_HARDLOCK` | 设置芯片擦除硬锁（Chip Erase Hard Lock）。 |

### `flash_mchp_ex_ops_t [2/2]`

```c
enum flash_mchp_ex_ops_t
```

```c
#include <zephyr/drivers/flash/mchp_nvmctrl_g3.h>
```

本枚举（Enumeration）定义可对闪存执行的扩展操作（Extended Operations），例如擦除或写入用户行（User Row），以及锁定或解锁特定闪存区域（Flash Regions）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_ENABLE` | 使能程序闪存（PFM）某区域的写保护（Write Protection）。 |
| `FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_DISABLE` | 禁用程序闪存（PFM）某区域的写保护（Write Protection）。 |
| `FLASH_EX_OP_PFM_REGION_WRITE_PROTECT_LOCK` | 锁定程序闪存（PFM）某区域的写保护设置（Write Protection Settings）。 |
| `FLASH_EX_OP_BFM_WRITE_PROTECT_ENABLE` | 使能启动闪存（BFM）的写保护（Write Protection）。 |
| `FLASH_EX_OP_BFM_WRITE_PROTECT_DISABLE` | 禁用启动闪存（BFM）的写保护（Write Protection）。 |
| `FLASH_EX_OP_BFM_WRITE_PROTECT_LOCK` | 锁定启动闪存（BFM）的写保护设置（Write Protection Settings）。 |

<a id="ga68310865b2b4ef28fe8259b0d625bc56"></a>

### `pfm_wp_region`

```c
enum pfm_wp_region
```

```c
#include <zephyr/drivers/flash/mchp_nvmctrl_g3.h>
```

程序闪存（Program Flash Memory，PFM）的写保护区域（Write Protection Regions）。

此枚举定义程序闪存（Program Flash Memory）可用的写保护区域（Write Protection Regions）。各区域可独立配置写保护。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PFM_WP_REGION_0` | 程序闪存（PFM）写保护区域（Write Protection Region）0。 |
| `PFM_WP_REGION_1` | 程序闪存（PFM）写保护区域（Write Protection Region）1。 |
| `PFM_WP_REGION_2` | 程序闪存（PFM）写保护区域（Write Protection Region）2。 |
| `PFM_WP_REGION_3` | 程序闪存（PFM）写保护区域（Write Protection Region）3。 |
| `PFM_WP_REGION_4` | 程序闪存（PFM）写保护区域（Write Protection Region）4。 |
| `PFM_WP_REGION_5` | 程序闪存（PFM）写保护区域（Write Protection Region）5。 |
| `PFM_WP_REGION_6` | 程序闪存（PFM）写保护区域（Write Protection Region）6。 |
| `PFM_WP_REGION_7` | 程序闪存（PFM）写保护区域（Write Protection Region）7。 |


## 3.5\_原页交叉引用（Cross References）

- [mchp_nvmctrl_g2.h](../api_file_configuration_reference/P050_zephyr__drivers__flash__mchp_nvmctrl_g2.h_文件参考.md)
- [mchp_nvmctrl_g3.h](../api_file_runtime_reference/P035_zephyr__drivers__flash__mchp_nvmctrl_g3.h_文件参考.md)
- [pfm_exop](../device_power_control_model_reference/P059_pfm_exop_结构体.md)
- [bfm_exop](../driver_model_reference/P026_启动闪存BFM扩展操作.md)
- [flash_mchp_ex_ops_t](../api_interaction_transport_topic_reference/P008_Microchip NVMCTRL G1 API主题.md#ga4dae21b9b6e0a90faddfa045b30e19a8)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggae4ce42c1991f6edf715e4aa2b294234ba2e23c772674e6e52a08fe8519a7f496d"></a>
<a id="ggae4ce42c1991f6edf715e4aa2b294234bab4d24bb75453d95c963ff5d7a529bbbe"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8a28aeedfece9b637e6698a64ad7e036e8"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8a412cbb9c36affa8a61e38c8ec77d22e4"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8a7f180551fd905e7ca4d217932087787a"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8a5b1b658937299999761f59173a16b93e"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8a953190cedd6519ce991793a07b990cc1"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8aefa3c18a91556306795f51a14fba9f4b"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8acdbe7b8985bb07f8fb0faadee3072dcb"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8a6525dc6f8c6b289b1d2f6402f57ad312"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8a30737465e185532f3400725b533ee3a9"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8aa8818fcf993809f03564ab8e15de3d89"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8ae20aba272606df44e4e4c5cd76078675"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8adf56dd5adcb84bb4a56ea2b112279122"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8a71054144eabce681da9ee95e852211da"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8a8f0b96d19fb3584a24addfc0749b758f"></a>
<a id="gga68310865b2b4ef28fe8259b0d625bc56ae5ed65dd074c8ec6fe07086ece6c6c89"></a>
<a id="gga68310865b2b4ef28fe8259b0d625bc56a9d007673c8b011e551fd0eaf67ce0a6d"></a>
<a id="gga68310865b2b4ef28fe8259b0d625bc56ae71436dcc0d7a89d9d497eb8e21697f9"></a>
<a id="gga68310865b2b4ef28fe8259b0d625bc56a7f2214b918478b67a9fb986bb13573ee"></a>
<a id="gga68310865b2b4ef28fe8259b0d625bc56a350b8165b2c0bfc682d8a46ea87593fb"></a>
<a id="gga68310865b2b4ef28fe8259b0d625bc56a6e913daec2faf0d10082ce1f520ff268"></a>
<a id="gga68310865b2b4ef28fe8259b0d625bc56a24d6f6c04f0013976549e02f03126b6c"></a>
<a id="gga68310865b2b4ef28fe8259b0d625bc56a686c824b326a95a54c52c7d2a97ee2e5"></a>

---

[上一章](P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md) · [返回大纲](大纲.md) · [下一章](P004_以太网过滤条件（Ethernet Filter Conditions）.md)
