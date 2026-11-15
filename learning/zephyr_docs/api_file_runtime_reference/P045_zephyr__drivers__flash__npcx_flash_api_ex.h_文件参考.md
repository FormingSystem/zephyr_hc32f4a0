---
id: learning.zephyr-docs.api-file-runtime-reference.page-45
title: zephyr__drivers__flash__npcx_flash_api_ex.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/npcx__flash__api__ex_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_zephyr\_\_drivers\_\_flash\_\_npcx\_flash\_api\_ex.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/npcx__flash__api__ex_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NPCX闪存扩展操作（Flash Extended Operations）的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/flash.h>
```

查看此文件的源码。

NPCX闪存扩展操作（Flash Extended Operations）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 45.1\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 45.2\_宏定义（Macros）

<a id="define-members-0"></a>

### NPCX QSPI 操作控制位（Operation Control Bits）

<a id="r_gabfe13897bc1ad3a19d7cf4f52cc86c7b"></a>

```c
#define NPCX_EX_OP_LOCK_UMA BIT(0)
```

相关声明：[NPCX_EX_OP_LOCK_UMA](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#gabfe13897bc1ad3a19d7cf4f52cc86c7b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

锁定／解锁 UMA 模式（UMA Mode）。

<a id="r_gaf33c593f223dc4ebd2d2b2745cd20951"></a>

```c
#define NPCX_EX_OP_INT_FLASH_WP BIT(1)
```

相关声明：[NPCX_EX_OP_INT_FLASH_WP](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#gaf33c593f223dc4ebd2d2b2745cd20951)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

对内部闪存（Internal Flash）施加写保护（Write Protection）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 45.3\_枚举（Enumerations）

<a id="r_gad4f93f7272e825355875d0fb05351474"></a>

```c
enum flash_npcx_ex_ops { FLASH_NPCX_EX_OP_EXEC_UMA = FLASH_EX_OP_VENDOR_BASE , FLASH_NPCX_EX_OP_SET_QSPI_OPER , FLASH_NPCX_EX_OP_GET_QSPI_OPER , FLASH_NPCX_EX_OP_EXEC_GDMA }
```

相关声明：[flash_npcx_ex_ops](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#gad4f93f7272e825355875d0fb05351474)、[FLASH_NPCX_EX_OP_EXEC_UMA](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474ad1fde767b235165d178a13de61d5f007)、[FLASH_NPCX_EX_OP_SET_QSPI_OPER](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474abbf87cdc7e9c3cdc9e6afde3c0485ec9)、[FLASH_NPCX_EX_OP_GET_QSPI_OPER](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474a46c5fff8b0ffbc480c01fed93ff8fd57)、[FLASH_NPCX_EX_OP_EXEC_GDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474ad675f28e2066d7d97be0ecdc7f3d34b9)。

NPCX 闪存扩展操作（Flash Extended Operations）的枚举（Enumeration）。


## 45.4\_原页交叉引用（Cross References）

- [zephyr/drivers/flash.h](../flash_reference/P010_Flash公共头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P594_npcx_flash_api_ex.h_源码浏览.md)
- [npcx_ex_ops_uma_in](../device_power_control_model_reference/P047_npcx_ex_ops_uma_in_结构体.md)
- [FLASH_NPCX_EX_OP_EXEC_UMA](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474ad1fde767b235165d178a13de61d5f007)
- [npcx_ex_ops_uma_out](../device_power_control_model_reference/P048_npcx_ex_ops_uma_out_结构体.md)
- [npcx_ex_ops_qspi_oper_in](../device_power_control_model_reference/P045_npcx_ex_ops_qspi_oper_in_结构体.md)
- [FLASH_NPCX_EX_OP_SET_QSPI_OPER](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474abbf87cdc7e9c3cdc9e6afde3c0485ec9)
- [npcx_ex_ops_qspi_oper_out](../device_power_control_model_reference/P046_npcx_ex_ops_qspi_oper_out_结构体.md)
- [FLASH_NPCX_EX_OP_GET_QSPI_OPER](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474a46c5fff8b0ffbc480c01fed93ff8fd57)
- [npcx_ex_ops_gdma_in](../device_power_control_model_reference/P044_npcx_ex_ops_gdma_in_结构体.md)
- [FLASH_NPCX_EX_OP_EXEC_GDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474ad675f28e2066d7d97be0ecdc7f3d34b9)
- [NPCX_EX_OP_LOCK_UMA](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#gabfe13897bc1ad3a19d7cf4f52cc86c7b)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [NPCX_EX_OP_INT_FLASH_WP](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#gaf33c593f223dc4ebd2d2b2745cd20951)
- [flash_npcx_ex_ops](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#gad4f93f7272e825355875d0fb05351474)

<a id="header-details"></a>

---

[上一章](P044_zephyr__drivers__mspi_emul.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P046_zephyr__drivers__flash__nrf_qspi_nor.h_文件参考.md)
