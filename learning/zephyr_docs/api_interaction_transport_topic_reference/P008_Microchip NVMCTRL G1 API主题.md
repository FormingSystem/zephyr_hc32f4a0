---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-8
title: Microchip NVMCTRL G1 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_Microchip NVMCTRL G1 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip NVMCTRL G1 闪存控制器的扩展操作。

<a id="details"></a>

Microchip NVMCTRL G1 闪存控制器的扩展操作。

<a id="header-files"></a>
<a id="files"></a>

## 8.1\_文件（Files）

<a id="r_mchp_5Fnvmctrl_5Fg1_2Eh"></a>

```c
file mchp_nvmctrl_g1.h
```

相关声明：[mchp_nvmctrl_g1.h](../api_file_configuration_reference/P049_zephyr__drivers__flash__mchp_nvmctrl_g1.h_文件参考.md)。

Microchip NVMCTRL G1闪存扩展操作（Flash Extended Operations）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.2\_数据结构（Data Structures）

<a id="r_flash_5Fmchp_5Fex_5Fop_5Fuserrow_5Fdata"></a>

```c
struct flash_mchp_ex_op_userrow_data
```

相关声明：[flash_mchp_ex_op_userrow_data](../system_service_model_reference/P032_flash_mchp_ex_op_userrow_data_结构体.md)。

MCHP NVMCTRL G1闪存用户行（User Row）数据操作的参数。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.3\_类型定义（Typedefs）

<a id="r_ga26d417de48ac23416675b9830e3f8ee4"></a>

```c
typedef struct flash_mchp_ex_op_userrow_data flash_mchp_ex_op_userrow_data_t
```

相关声明：[flash_mchp_ex_op_userrow_data](../system_service_model_reference/P032_flash_mchp_ex_op_userrow_data_结构体.md)、[flash_mchp_ex_op_userrow_data_t](#ga26d417de48ac23416675b9830e3f8ee4)。

MCHP NVMCTRL G1闪存用户行（User Row）数据操作的参数。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.4\_枚举（Enumerations）

<a id="r_ga4dae21b9b6e0a90faddfa045b30e19a8"></a>

```c
enum flash_mchp_ex_ops_t { FLASH_EX_OP_USER_ROW_ERASE , FLASH_EX_OP_USER_ROW_WRITE , FLASH_EX_OP_REGION_LOCK , FLASH_EX_OP_REGION_UNLOCK }
```

相关声明：[flash_mchp_ex_ops_t](#ga4dae21b9b6e0a90faddfa045b30e19a8)、[FLASH_EX_OP_USER_ROW_ERASE](#gga4dae21b9b6e0a90faddfa045b30e19a8af25afe42760eb6f7af298f9ef44889af)、[FLASH_EX_OP_USER_ROW_WRITE](#gga4dae21b9b6e0a90faddfa045b30e19a8a1a4c0eddbc371ca9cf9f4fd11f06847d)、[FLASH_EX_OP_REGION_LOCK](#gga4dae21b9b6e0a90faddfa045b30e19a8a28aeedfece9b637e6698a64ad7e036e8)、[FLASH_EX_OP_REGION_UNLOCK](#gga4dae21b9b6e0a90faddfa045b30e19a8a412cbb9c36affa8a61e38c8ec77d22e4)。

MCHP NVMCTRL G1 闪存控制器的扩展操作码（Extended Operation Codes）枚举（Enumeration）。

## 8.5\_详细说明（Detailed Documentation）

<a id="ga26d417de48ac23416675b9830e3f8ee4"></a>

### `flash_mchp_ex_op_userrow_data_t`

```c
typedef struct flash_mchp_ex_op_userrow_data flash_mchp_ex_op_userrow_data_t
```

```c
#include <zephyr/drivers/flash/mchp_nvmctrl_g1.h>
```

MCHP NVMCTRL G1闪存用户行（User Row）数据操作的参数。

作为 `FLASH_EX_OP_USER_ROW_WRITE` 的 `in` 参数，用于指定源数据缓冲区和用户行区域（User Row Region）内的目标位置。

<a id="ga4dae21b9b6e0a90faddfa045b30e19a8"></a>

### `flash_mchp_ex_ops_t`

```c
enum flash_mchp_ex_ops_t
```

```c
#include <zephyr/drivers/flash/mchp_nvmctrl_g1.h>
```

MCHP NVMCTRL G1 闪存控制器的扩展操作码（Extended Operation Codes）枚举（Enumeration）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FLASH_EX_OP_USER_ROW_ERASE` | 擦除闪存中的整个用户行（User Row），从 `SOC_NV_USERROW_BASE_ADDR` 定义的基地址开始擦除用户行区域。**参数（Parameters）：**`in` 不使用；`out` 不使用。 |
| `in` | 不使用（Not Used）。 |
| `out` | 不使用（Not Used）。 |
| `FLASH_EX_OP_USER_ROW_WRITE` | 向闪存的用户行区域（User Row Section）写入数据。偏移量和数据长度必须按用户行写入块大小对齐，即四字（Quad-word），通常为 16 字节。**参数（Parameters）：**`in` 为指向 `flash_mchp_ex_op_userrow_data_t` 的指针，用于指定目标偏移、源数据缓冲区及长度；`out` 不使用。 |
| `in` | 指向 `flash_mchp_ex_op_userrow_data_t` 结构体的指针，用于指定目标偏移、源数据缓冲区及长度。 |
| `out` | 不使用（Not Used）。 |
| `FLASH_EX_OP_REGION_LOCK` | 锁定闪存所有区域。遍历主闪存阵列（Main Flash Array）的所有可锁定区域，逐一发出锁定区域命令（Lock Region，LR）。**参数（Parameters）：**`in` 和 `out` 均不使用。 |
| `in` | 不使用（Not Used）。 |
| `out` | 不使用（Not Used）。 |
| `FLASH_EX_OP_REGION_UNLOCK` | 解锁闪存所有区域。遍历主闪存阵列（Main Flash Array）的所有可锁定区域，逐一发出解锁区域命令（Unlock Region，UR）。**参数（Parameters）：**`in` 和 `out` 均不使用。 |
| `in` | 不使用（Not Used）。 |
| `out` | 不使用（Not Used）。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 不使用（Not Used）。 |
| `out` | 不使用（Not Used）。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 指向 `flash_mchp_ex_op_userrow_data_t` 结构体的指针，用于指定目标偏移、源数据缓冲区及长度。 |
| `out` | 不使用（Not Used）。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 不使用（Not Used）。 |
| `out` | 不使用（Not Used）。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 不使用（Not Used）。 |
| `out` | 不使用（Not Used）。 |


## 8.6\_原页交叉引用（Cross References）

- [mchp_nvmctrl_g1.h](../api_file_configuration_reference/P049_zephyr__drivers__flash__mchp_nvmctrl_g1.h_文件参考.md)
- [flash_mchp_ex_op_userrow_data](../system_service_model_reference/P032_flash_mchp_ex_op_userrow_data_结构体.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8af25afe42760eb6f7af298f9ef44889af"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8a1a4c0eddbc371ca9cf9f4fd11f06847d"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8a28aeedfece9b637e6698a64ad7e036e8"></a>
<a id="gga4dae21b9b6e0a90faddfa045b30e19a8a412cbb9c36affa8a61e38c8ec77d22e4"></a>

---

[上一章](P007_定点到浮点转换（Fixed to Float point conversions）.md) · [返回大纲](大纲.md) · [下一章](P009_MFD AD559X 接口.md)
