---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-1
title: Andes QSPI-NOR 原地执行（XIP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_Andes QSPI-NOR 原地执行（XIP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Andes QSPI-NOR 就地执行（Execute In Place，XIP）闪存的扩展操作。

<a id="details"></a>

Andes QSPI-NOR 就地执行（Execute In Place，XIP）闪存的扩展操作。

<a id="header-files"></a>
<a id="files"></a>

## 1.1\_文件（Files）

<a id="r_andes_5Fflash_5Fxip_5Fapi_5Fex_2Eh"></a>

```c
file andes_flash_xip_api_ex.h
```

相关声明：[andes_flash_xip_api_ex.h](../api_file_configuration_reference/P005_zephyr__drivers__flash__andes_flash_xip_api_ex.h_文件参考.md)。

Andes QSPI-NOR就地执行（XIP）闪存扩展操作的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.2\_数据结构（Data Structures）

<a id="r_andes_5Fxip_5Fex_5Fops_5Fget_5Fout"></a>

```c
struct andes_xip_ex_ops_get_out
```

相关声明：[andes_xip_ex_ops_get_out](../driver_model_reference/P009_Andes原位执行读取参数.md)。

`FLASH_ANDES_XIP_EX_OP_GET_STATUS_REGS` 操作的输出参数。

<a id="r_andes_5Fxip_5Fex_5Fops_5Fset_5Fin"></a>

```c
struct andes_xip_ex_ops_set_in
```

相关声明：[andes_xip_ex_ops_set_in](../driver_model_reference/P013_Andes原位执行设置参数.md)。

`FLASH_ANDES_XIP_EX_OP_SET_STATUS_REGS` 操作的输入参数。

<a id="r_andes_5Fxip_5Fex_5Fops_5Flock_5Fin"></a>

```c
struct andes_xip_ex_ops_lock_in
```

相关声明：[andes_xip_ex_ops_lock_in](../driver_model_reference/P010_Andes原位执行锁定参数.md)。

`FLASH_ANDES_XIP_EX_OP_LOCK` 操作的输入参数。

<a id="r_andes_5Fxip_5Fex_5Fops_5Flock_5Fstate_5Fout"></a>

```c
struct andes_xip_ex_ops_lock_state_out
```

相关声明：[andes_xip_ex_ops_lock_state_out](../driver_model_reference/P011_Andes原位执行锁状态.md)。

`FLASH_ANDES_XIP_EX_OP_LOCK_STATE` 操作的输出参数。

<a id="r_andes_5Fxip_5Fex_5Fops_5Fmem_5Fread_5Fcmd_5Fin"></a>

```c
struct andes_xip_ex_ops_mem_read_cmd_in
```

相关声明：[andes_xip_ex_ops_mem_read_cmd_in](../driver_model_reference/P012_Andes原位执行存储器读命令.md)。

`FLASH_ANDES_XIP_EX_OP_MEM_READ_CMD` 操作的输入参数。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.3\_枚举（Enumerations）

<a id="r_ga4b46df3b8254c20bf81be3957f9a0d1e"></a>

```c
enum flash_andes_xip_ex_ops { FLASH_ANDES_XIP_EX_OP_GET_STATUS_REGS = FLASH_EX_OP_VENDOR_BASE , FLASH_ANDES_XIP_EX_OP_SET_STATUS_REGS , FLASH_ANDES_XIP_EX_OP_LOCK , FLASH_ANDES_XIP_EX_OP_LOCK_STATE , FLASH_ANDES_XIP_EX_OP_MEM_READ_CMD }
```

相关声明：[flash_andes_xip_ex_ops](#ga4b46df3b8254c20bf81be3957f9a0d1e)、[FLASH_ANDES_XIP_EX_OP_GET_STATUS_REGS](#gga4b46df3b8254c20bf81be3957f9a0d1ead7dc137a0bc5b2511b85d194f27bd6c7)、[FLASH_ANDES_XIP_EX_OP_SET_STATUS_REGS](#gga4b46df3b8254c20bf81be3957f9a0d1ea90ae34480ccec850be7ac347f64fbb8f)、[FLASH_ANDES_XIP_EX_OP_LOCK](#gga4b46df3b8254c20bf81be3957f9a0d1eae40ae84ea8da6a831c1ed37ea40d37c0)、[FLASH_ANDES_XIP_EX_OP_LOCK_STATE](#gga4b46df3b8254c20bf81be3957f9a0d1eadb8562975bd289b303b26e0227ac853f)、[FLASH_ANDES_XIP_EX_OP_MEM_READ_CMD](#gga4b46df3b8254c20bf81be3957f9a0d1ea06bff51aaa30f75f7fd26154c512d6fc)。

Andes 闪存扩展操作（Flash Extended Operations）的枚举（Enumeration）。

<a id="r_gabb24a40e5fd9462fe0cd06f426e0583f"></a>

```c
enum flash_andes_xip_mem_rd_cmd { FLASH_ANDES_XIP_MEM_RD_CMD_03 = 0 , FLASH_ANDES_XIP_MEM_RD_CMD_0B = 1 , FLASH_ANDES_XIP_MEM_RD_CMD_3B = 2 , FLASH_ANDES_XIP_MEM_RD_CMD_6B = 3 , FLASH_ANDES_XIP_MEM_RD_CMD_BB = 4 , FLASH_ANDES_XIP_MEM_RD_CMD_EB = 5 , FLASH_ANDES_XIP_MEM_RD_CMD_13 = 8 , FLASH_ANDES_XIP_MEM_RD_CMD_0C = 9 , FLASH_ANDES_XIP_MEM_RD_CMD_3C = 10 , FLASH_ANDES_XIP_MEM_RD_CMD_6C = 11 , FLASH_ANDES_XIP_MEM_RD_CMD_BC = 12 , FLASH_ANDES_XIP_MEM_RD_CMD_EC = 13 }
```

相关声明：[flash_andes_xip_mem_rd_cmd](#gabb24a40e5fd9462fe0cd06f426e0583f)、[FLASH_ANDES_XIP_MEM_RD_CMD_03](#ggabb24a40e5fd9462fe0cd06f426e0583fa8a3b5bbe3ec17ce470a9636934dd2bce)、[FLASH_ANDES_XIP_MEM_RD_CMD_0B](#ggabb24a40e5fd9462fe0cd06f426e0583fa2dcf42c1425ed5483e3db48733f2eefc)、[FLASH_ANDES_XIP_MEM_RD_CMD_3B](#ggabb24a40e5fd9462fe0cd06f426e0583facd50bfc16ae83b41ffcac3d0941a5c00)、[FLASH_ANDES_XIP_MEM_RD_CMD_6B](#ggabb24a40e5fd9462fe0cd06f426e0583fa6c0d9468075b962602fa0cc652a92bc3)、[FLASH_ANDES_XIP_MEM_RD_CMD_BB](#ggabb24a40e5fd9462fe0cd06f426e0583fad48e3482a04cb3aff0bb6afca65cf36b)、[FLASH_ANDES_XIP_MEM_RD_CMD_EB](#ggabb24a40e5fd9462fe0cd06f426e0583fa7e7321429e68649e18743a3d697cf999)、[FLASH_ANDES_XIP_MEM_RD_CMD_13](#ggabb24a40e5fd9462fe0cd06f426e0583fa2bfc829bb2e088af96ad309e0ff924c8)、[FLASH_ANDES_XIP_MEM_RD_CMD_0C](#ggabb24a40e5fd9462fe0cd06f426e0583faf12149f961944dea851ccc7e494ba190)、[FLASH_ANDES_XIP_MEM_RD_CMD_3C](#ggabb24a40e5fd9462fe0cd06f426e0583fa5464912c8f396f13e00bb4e7342185a8)、[FLASH_ANDES_XIP_MEM_RD_CMD_6C](#ggabb24a40e5fd9462fe0cd06f426e0583fa7e8f108992e34d0cca57cfddde68bd6a)、[FLASH_ANDES_XIP_MEM_RD_CMD_BC](#ggabb24a40e5fd9462fe0cd06f426e0583fa65afd15579c86eb3d60aae8d4b6dee19)、[FLASH_ANDES_XIP_MEM_RD_CMD_EC](#ggabb24a40e5fd9462fe0cd06f426e0583fa6211518baeefc2eeeb000757e500c8d3)。

用于内存映射读取模式（Memory-Mapped Read Mode）的 SPI 命令（Commands）。

## 1.4\_详细说明（Detailed Documentation）

<a id="ga4b46df3b8254c20bf81be3957f9a0d1e"></a>

### `flash_andes_xip_ex_ops`

```c
enum flash_andes_xip_ex_ops
```

```c
#include <zephyr/drivers/flash/andes_flash_xip_api_ex.h>
```

Andes 闪存扩展操作（Flash Extended Operations）的枚举（Enumeration）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FLASH_ANDES_XIP_EX_OP_GET_STATUS_REGS` | 获取三个状态寄存器（Status Registers，SR1、SR2、SR3）。此操作从闪存设备读取三个状态寄存器的内容。 参数（Parameters）：out：指向 andes_xip_ex_ops_get_out 结构体的指针，用于存放寄存器值。 |
| `out` | 指向 andes_xip_ex_ops_get_out 结构体的指针，用于存放寄存器值。 |
| `FLASH_ANDES_XIP_EX_OP_SET_STATUS_REGS` | 设置三个状态寄存器（Status Registers，SR1、SR2、SR3）。此操作向状态寄存器写入新值，通过掩码仅修改特定位。操作受到软件锁（Software Lock）保护，可通过 FLASH_ANDES_XIP_EX_OP_LOCK 控制该锁。 参数（Parameters）：in：指向 andes_xip_ex_ops_set_in 结构体的指针，其中包含要写入的值和掩码（Masks）。 |
| `in` | 指向 andes_xip_ex_ops_set_in 结构体的指针，其中包含要写入的值和掩码（Masks）。 |
| `FLASH_ANDES_XIP_EX_OP_LOCK` | 设置软件锁（Software Lock），防止修改状态寄存器。此操作启用或禁用软件锁，以阻止 FLASH_ANDES_XIP_EX_OP_SET_STATUS_REGS 操作执行。 参数（Parameters）：in：指向 andes_xip_ex_ops_lock_in 结构体的指针，指定启用还是禁用锁。 |
| `in` | 指向 andes_xip_ex_ops_lock_in 结构体的指针，指定启用还是禁用锁。 |
| `FLASH_ANDES_XIP_EX_OP_LOCK_STATE` | 获取状态寄存器软件锁（Software Status Register Lock）的当前状态。 参数（Parameters）：out：指向 andes_xip_ex_ops_lock_state_out 结构体的指针，用于存放当前锁状态。 |
| `out` | 指向 andes_xip_ex_ops_lock_state_out 结构体的指针，用于存放当前锁状态。 |
| `FLASH_ANDES_XIP_EX_OP_MEM_READ_CMD` | 设置内存映射读取模式（Memory-mapped Read Mode）的 SPI 命令。此操作配置硬件用于原地执行（Execute-In-Place，XIP）或内存映射读取的命令。 参数（Parameters）：in：指向 andes_xip_ex_ops_mem_read_cmd_in 结构体的指针，指定要使用的读取命令。 |
| `in` | 指向 andes_xip_ex_ops_mem_read_cmd_in 结构体的指针，指定要使用的读取命令。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `out` | 指向 andes_xip_ex_ops_get_out 结构体的指针，用于存放寄存器值。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 指向 andes_xip_ex_ops_set_in 结构体的指针，其中包含要写入的值和掩码（Masks）。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 指向 andes_xip_ex_ops_lock_in 结构体的指针，指定启用还是禁用锁。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `out` | 指向 andes_xip_ex_ops_lock_state_out 结构体的指针，用于存放当前锁状态。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 指向 andes_xip_ex_ops_mem_read_cmd_in 结构体的指针，指定要使用的读取命令。 |

<a id="gabb24a40e5fd9462fe0cd06f426e0583f"></a>

### `flash_andes_xip_mem_rd_cmd`

```c
enum flash_andes_xip_mem_rd_cmd
```

```c
#include <zephyr/drivers/flash/andes_flash_xip_api_ex.h>
```

用于内存映射读取模式（Memory-Mapped Read Mode）的 SPI 命令（Commands）。

这些值表示可通过 FLASH_ANDES_XIP_EX_OP_MEM_READ_CMD 操作为内存映射访问（Memory-mapped Access）配置的不同 SPI 读取命令。命令码对应标准 SPI 闪存读取命令操作码（Opcodes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FLASH_ANDES_XIP_MEM_RD_CMD_03` | 普通读取（Normal Read，0x03）。 |
| `FLASH_ANDES_XIP_MEM_RD_CMD_0B` | 快速读取（Fast Read，0x0B）。 |
| `FLASH_ANDES_XIP_MEM_RD_CMD_3B` | 双线 I/O 快速读取（Dual I/O Fast Read，0x3B）。 |
| `FLASH_ANDES_XIP_MEM_RD_CMD_6B` | 四线 I/O 快速读取（Quad I/O Fast Read，0x6B）。 |
| `FLASH_ANDES_XIP_MEM_RD_CMD_BB` | 双线输出快速读取（Dual Output Fast Read，0xBB）。 |
| `FLASH_ANDES_XIP_MEM_RD_CMD_EB` | 四线输出快速读取（Quad Output Fast Read，0xEB）。 |
| `FLASH_ANDES_XIP_MEM_RD_CMD_13` | 使用 4 字节地址的普通读取（Normal Read，0x13）。 |
| `FLASH_ANDES_XIP_MEM_RD_CMD_0C` | 使用 4 字节地址的快速读取（Fast Read，0x0C）。 |
| `FLASH_ANDES_XIP_MEM_RD_CMD_3C` | 使用 4 字节地址的双线 I/O 快速读取（Dual I/O Fast Read，0x3C）。 |
| `FLASH_ANDES_XIP_MEM_RD_CMD_6C` | 使用 4 字节地址的四线 I/O 快速读取（Quad I/O Fast Read，0x6C）。 |
| `FLASH_ANDES_XIP_MEM_RD_CMD_BC` | 使用 4 字节地址的双线输出快速读取（Dual Output Fast Read，0xBC）。 |
| `FLASH_ANDES_XIP_MEM_RD_CMD_EC` | 使用 4 字节地址的四线输出快速读取（Quad Output Fast Read，0xEC）。 |


## 1.5\_原页交叉引用（Cross References）

- [andes_flash_xip_api_ex.h](../api_file_configuration_reference/P005_zephyr__drivers__flash__andes_flash_xip_api_ex.h_文件参考.md)
- [andes_xip_ex_ops_get_out](../driver_model_reference/P009_Andes原位执行读取参数.md)
- [andes_xip_ex_ops_set_in](../driver_model_reference/P013_Andes原位执行设置参数.md)
- [andes_xip_ex_ops_lock_in](../driver_model_reference/P010_Andes原位执行锁定参数.md)
- [andes_xip_ex_ops_lock_state_out](../driver_model_reference/P011_Andes原位执行锁状态.md)
- [andes_xip_ex_ops_mem_read_cmd_in](../driver_model_reference/P012_Andes原位执行存储器读命令.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga4b46df3b8254c20bf81be3957f9a0d1ead7dc137a0bc5b2511b85d194f27bd6c7"></a>
<a id="gga4b46df3b8254c20bf81be3957f9a0d1ea90ae34480ccec850be7ac347f64fbb8f"></a>
<a id="gga4b46df3b8254c20bf81be3957f9a0d1eae40ae84ea8da6a831c1ed37ea40d37c0"></a>
<a id="gga4b46df3b8254c20bf81be3957f9a0d1eadb8562975bd289b303b26e0227ac853f"></a>
<a id="gga4b46df3b8254c20bf81be3957f9a0d1ea06bff51aaa30f75f7fd26154c512d6fc"></a>
<a id="ggabb24a40e5fd9462fe0cd06f426e0583fa8a3b5bbe3ec17ce470a9636934dd2bce"></a>
<a id="ggabb24a40e5fd9462fe0cd06f426e0583fa2dcf42c1425ed5483e3db48733f2eefc"></a>
<a id="ggabb24a40e5fd9462fe0cd06f426e0583facd50bfc16ae83b41ffcac3d0941a5c00"></a>
<a id="ggabb24a40e5fd9462fe0cd06f426e0583fa6c0d9468075b962602fa0cc652a92bc3"></a>
<a id="ggabb24a40e5fd9462fe0cd06f426e0583fad48e3482a04cb3aff0bb6afca65cf36b"></a>
<a id="ggabb24a40e5fd9462fe0cd06f426e0583fa7e7321429e68649e18743a3d697cf999"></a>
<a id="ggabb24a40e5fd9462fe0cd06f426e0583fa2bfc829bb2e088af96ad309e0ff924c8"></a>
<a id="ggabb24a40e5fd9462fe0cd06f426e0583faf12149f961944dea851ccc7e494ba190"></a>
<a id="ggabb24a40e5fd9462fe0cd06f426e0583fa5464912c8f396f13e00bb4e7342185a8"></a>
<a id="ggabb24a40e5fd9462fe0cd06f426e0583fa7e8f108992e34d0cca57cfddde68bd6a"></a>
<a id="ggabb24a40e5fd9462fe0cd06f426e0583fa65afd15579c86eb3d60aae8d4b6dee19"></a>
<a id="ggabb24a40e5fd9462fe0cd06f426e0583fa6211518baeefc2eeeb000757e500c8d3"></a>

---

[返回大纲](大纲.md) · [下一章](P002_CCP 呼叫控制客户端 API.md)
