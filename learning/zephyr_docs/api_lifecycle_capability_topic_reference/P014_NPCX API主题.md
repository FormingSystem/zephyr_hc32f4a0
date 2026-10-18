---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-14
title: NPCX API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_NPCX API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NPCX 闪存控制器的扩展操作。

<a id="details"></a>

NPCX 闪存控制器的扩展操作。

<a id="header-files"></a>
<a id="files"></a>

## 14.1\_文件（Files）

<a id="r_npcx_5Fflash_5Fapi_5Fex_2Eh"></a>

```c
file npcx_flash_api_ex.h
```

相关声明：[npcx_flash_api_ex.h](../api_file_runtime_reference/P045_zephyr__drivers__flash__npcx_flash_api_ex.h_文件参考.md)。

NPCX闪存扩展操作（Flash Extended Operations）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.2\_数据结构（Data Structures）

<a id="r_npcx_5Fex_5Fops_5Fuma_5Fin"></a>

```c
struct npcx_ex_ops_uma_in
```

相关声明：[npcx_ex_ops_uma_in](../device_power_control_model_reference/P047_npcx_ex_ops_uma_in_结构体.md)。

FLASH_NPCX_EX_OP_EXEC_UMA操作的输入参数。

<a id="r_npcx_5Fex_5Fops_5Fuma_5Fout"></a>

```c
struct npcx_ex_ops_uma_out
```

相关声明：[npcx_ex_ops_uma_out](../device_power_control_model_reference/P048_npcx_ex_ops_uma_out_结构体.md)。

FLASH_NPCX_EX_OP_EXEC_UMA操作的输出参数。

<a id="r_npcx_5Fex_5Fops_5Fqspi_5Foper_5Fin"></a>

```c
struct npcx_ex_ops_qspi_oper_in
```

相关声明：[npcx_ex_ops_qspi_oper_in](../device_power_control_model_reference/P045_npcx_ex_ops_qspi_oper_in_结构体.md)。

FLASH_NPCX_EX_OP_SET_QSPI_OPER操作的输入参数。

<a id="r_npcx_5Fex_5Fops_5Fqspi_5Foper_5Fout"></a>

```c
struct npcx_ex_ops_qspi_oper_out
```

相关声明：[npcx_ex_ops_qspi_oper_out](../device_power_control_model_reference/P046_npcx_ex_ops_qspi_oper_out_结构体.md)。

FLASH_NPCX_EX_OP_GET_QSPI_OPER操作的输出参数。

<a id="r_npcx_5Fex_5Fops_5Fgdma_5Fin"></a>

```c
struct npcx_ex_ops_gdma_in
```

相关声明：[npcx_ex_ops_gdma_in](../device_power_control_model_reference/P044_npcx_ex_ops_gdma_in_结构体.md)。

FLASH_NPCX_EX_OP_EXEC_GDMA操作的输入参数。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 14.3\_枚举（Enumerations）

<a id="r_gad4f93f7272e825355875d0fb05351474"></a>

```c
enum flash_npcx_ex_ops { FLASH_NPCX_EX_OP_EXEC_UMA = FLASH_EX_OP_VENDOR_BASE , FLASH_NPCX_EX_OP_SET_QSPI_OPER , FLASH_NPCX_EX_OP_GET_QSPI_OPER , FLASH_NPCX_EX_OP_EXEC_GDMA }
```

相关声明：[flash_npcx_ex_ops](#gad4f93f7272e825355875d0fb05351474)、[FLASH_NPCX_EX_OP_EXEC_UMA](#ggad4f93f7272e825355875d0fb05351474ad1fde767b235165d178a13de61d5f007)、[FLASH_NPCX_EX_OP_SET_QSPI_OPER](#ggad4f93f7272e825355875d0fb05351474abbf87cdc7e9c3cdc9e6afde3c0485ec9)、[FLASH_NPCX_EX_OP_GET_QSPI_OPER](#ggad4f93f7272e825355875d0fb05351474a46c5fff8b0ffbc480c01fed93ff8fd57)、[FLASH_NPCX_EX_OP_EXEC_GDMA](#ggad4f93f7272e825355875d0fb05351474ad675f28e2066d7d97be0ecdc7f3d34b9)。

NPCX 闪存扩展操作（Flash Extended Operations）的枚举（Enumeration）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 14.4\_NPCX QSPI 操作控制位（Operation Control Bits）

<a id="r_gabfe13897bc1ad3a19d7cf4f52cc86c7b"></a>

```c
#define NPCX_EX_OP_LOCK_UMA BIT(0)
```

相关声明：[NPCX_EX_OP_LOCK_UMA](#gabfe13897bc1ad3a19d7cf4f52cc86c7b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

锁定／解锁 UMA 模式（UMA Mode）。

<a id="r_gaf33c593f223dc4ebd2d2b2745cd20951"></a>

```c
#define NPCX_EX_OP_INT_FLASH_WP BIT(1)
```

相关声明：[NPCX_EX_OP_INT_FLASH_WP](#gaf33c593f223dc4ebd2d2b2745cd20951)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

对内部闪存（Internal Flash）施加写保护（Write Protection）。

## 14.5\_详细说明（Detailed Documentation）

<a id="gaf33c593f223dc4ebd2d2b2745cd20951"></a>

### `NPCX_EX_OP_INT_FLASH_WP`

```c
#define NPCX_EX_OP_INT_FLASH_WP BIT(1)
```

```c
#include <zephyr/drivers/flash/npcx_flash_api_ex.h>
```

对内部闪存（Internal Flash）施加写保护（Write Protection）。

<a id="gabfe13897bc1ad3a19d7cf4f52cc86c7b"></a>

### `NPCX_EX_OP_LOCK_UMA`

```c
#define NPCX_EX_OP_LOCK_UMA BIT(0)
```

```c
#include <zephyr/drivers/flash/npcx_flash_api_ex.h>
```

锁定／解锁 UMA 模式（UMA Mode）。

<a id="gad4f93f7272e825355875d0fb05351474"></a>

### `flash_npcx_ex_ops`

```c
enum flash_npcx_ex_ops
```

```c
#include <zephyr/drivers/flash/npcx_flash_api_ex.h>
```

NPCX 闪存扩展操作（Flash Extended Operations）的枚举（Enumeration）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FLASH_NPCX_EX_OP_EXEC_UMA` | 用户模式访问（User Mode Access，UMA）模式执行：通过 UMA 模式执行 SPI 事务。用户可执行自定义事务，以读写设备配置，例如 NOR 闪存状态寄存器、电源开关等。**参数（Parameters）：**`in` 指向指定 UMA 事务的 `npcx_ex_ops_uma_in` 结构体；`out` 指向存储 UMA 事务结果的 `npcx_ex_ops_uma_out` 结构体。 |
| `in` | 指向指定 UMA 事务（Transaction）的 `npcx_ex_ops_uma_in` 结构体的指针。 |
| `out` | 指向存储 UMA 事务（Transaction）结果的 `npcx_ex_ops_uma_out` 结构体的指针。 |
| `FLASH_NPCX_EX_OP_SET_QSPI_OPER` | 配置 Quad-SPI NOR 闪存的特定操作（Specific Operation），例如锁定或解锁 UMA 模式、设置内部闪存写保护引脚等。**参数（Parameters）：**`in` 指向指定要设置操作的 `npcx_ex_ops_qspi_oper_in` 结构体。 |
| `in` | 指向指定要设置操作（Operation）的 `npcx_ex_ops_qspi_oper_in` 结构体的指针。 |
| `FLASH_NPCX_EX_OP_GET_QSPI_OPER` | 获取 Quad-SPI NOR 闪存的特定操作（Specific Operation），返回当前操作。**参数（Parameters）：**`out` 指向用于存储操作结果的 `npcx_ex_ops_qspi_oper_out` 结构体。 |
| `out` | 指向用于存储操作结果（Operation Result）的 `npcx_ex_ops_qspi_oper_out` 结构体的指针。 |
| `FLASH_NPCX_EX_OP_EXEC_GDMA` | NPCX 通用 DMA（General DMA，GDMA）模式执行：通过 GDMA 模块执行内存传输。**参数（Parameters）：**`in` 指向指定 GDMA 事务的 `npcx_ex_ops_gdma_in` 结构体。 |
| `in` | 指向指定 GDMA 事务（Transaction）的 `npcx_ex_ops_gdma_in` 结构体的指针。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 指向指定 UMA 事务（Transaction）的 `npcx_ex_ops_uma_in` 结构体的指针。 |
| `out` | 指向存储 UMA 事务（Transaction）结果的 `npcx_ex_ops_uma_out` 结构体的指针。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 指向指定要设置操作（Operation）的 `npcx_ex_ops_qspi_oper_in` 结构体的指针。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `out` | 指向用于存储操作结果（Operation Result）的 `npcx_ex_ops_qspi_oper_out` 结构体的指针。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 指向指定 GDMA 事务（Transaction）的 `npcx_ex_ops_gdma_in` 结构体的指针。 |


## 14.6\_原页交叉引用（Cross References）

- [npcx_flash_api_ex.h](../api_file_runtime_reference/P045_zephyr__drivers__flash__npcx_flash_api_ex.h_文件参考.md)
- [npcx_ex_ops_uma_in](../device_power_control_model_reference/P047_npcx_ex_ops_uma_in_结构体.md)
- [npcx_ex_ops_uma_out](../device_power_control_model_reference/P048_npcx_ex_ops_uma_out_结构体.md)
- [npcx_ex_ops_qspi_oper_in](../device_power_control_model_reference/P045_npcx_ex_ops_qspi_oper_in_结构体.md)
- [npcx_ex_ops_qspi_oper_out](../device_power_control_model_reference/P046_npcx_ex_ops_qspi_oper_out_结构体.md)
- [npcx_ex_ops_gdma_in](../device_power_control_model_reference/P044_npcx_ex_ops_gdma_in_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggad4f93f7272e825355875d0fb05351474ad1fde767b235165d178a13de61d5f007"></a>
<a id="ggad4f93f7272e825355875d0fb05351474abbf87cdc7e9c3cdc9e6afde3c0485ec9"></a>
<a id="ggad4f93f7272e825355875d0fb05351474a46c5fff8b0ffbc480c01fed93ff8fd57"></a>
<a id="ggad4f93f7272e825355875d0fb05351474ad675f28e2066d7d97be0ecdc7f3d34b9"></a>

---

[上一章](P013_变换元素（Transforms）.md) · [返回大纲](大纲.md) · [下一章](P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md)
