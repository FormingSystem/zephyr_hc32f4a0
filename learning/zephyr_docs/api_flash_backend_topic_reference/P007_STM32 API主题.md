---
id: learning.zephyr-docs.api-flash-backend-topic-reference.page-7
title: STM32 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_STM32 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STM32 闪存控制器的扩展操作。

<a id="details"></a>

STM32 闪存控制器的扩展操作。

<a id="header-files"></a>
<a id="files"></a>

## 7.1\_文件（Files）

<a id="r_stm32_5Fflash_5Fapi_5Fextensions_2Eh"></a>

```c
file stm32_flash_api_extensions.h
```

相关声明：[stm32_flash_api_extensions.h](../api_file_configuration_reference/P072_zephyr__drivers__flash__stm32_flash_api_extensions.h_文件参考.md)。

STM32闪存扩展操作（Flash Extended Operations）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.2\_数据结构（Data Structures）

<a id="r_flash_5Fstm32_5Fex_5Fop_5Fsector_5Fwp_5Fin"></a>

```c
struct flash_stm32_ex_op_sector_wp_in
```

相关声明：[flash_stm32_ex_op_sector_wp_in](../system_service_model_reference/P035_flash_stm32_ex_op_sector_wp_in_结构体.md)。

FLASH_STM32_EX_OP_SECTOR_WP操作的输入结构。

<a id="r_flash_5Fstm32_5Fex_5Fop_5Fsector_5Fwp_5Fout"></a>

```c
struct flash_stm32_ex_op_sector_wp_out
```

相关声明：[flash_stm32_ex_op_sector_wp_out](../system_service_model_reference/P036_flash_stm32_ex_op_sector_wp_out_结构体.md)。

FLASH_STM32_EX_OP_SECTOR_WP操作的输出结构。

<a id="r_flash_5Fstm32_5Fex_5Fop_5Frdp"></a>

```c
struct flash_stm32_ex_op_rdp
```

相关声明：[flash_stm32_ex_op_rdp](../system_service_model_reference/P034_flash_stm32_ex_op_rdp_结构体.md)。

FLASH_STM32_EX_OP_RDP操作的输入结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.3\_枚举（Enumerations）

<a id="r_ga95b012159eb95cd62859a6d5c4d862b8"></a>

```c
enum stm32_ex_ops { FLASH_STM32_EX_OP_SECTOR_WP = FLASH_EX_OP_VENDOR_BASE , FLASH_STM32_EX_OP_RDP , FLASH_STM32_EX_OP_BLOCK_OPTION_REG , FLASH_STM32_EX_OP_BLOCK_CONTROL_REG , FLASH_STM32_EX_OP_OPTB_READ , FLASH_STM32_EX_OP_OPTB_WRITE }
```

相关声明：[stm32_ex_ops](#ga95b012159eb95cd62859a6d5c4d862b8)、[FLASH_STM32_EX_OP_SECTOR_WP](#gga95b012159eb95cd62859a6d5c4d862b8a7bde6043879f1a6139da11679b4455fe)、[FLASH_STM32_EX_OP_RDP](#gga95b012159eb95cd62859a6d5c4d862b8ae1b013a96c3a64b0d3e677b4bce954a0)、[FLASH_STM32_EX_OP_BLOCK_OPTION_REG](#gga95b012159eb95cd62859a6d5c4d862b8a59b3b9a3b0eaee9cd4435f452855b903)、[FLASH_STM32_EX_OP_BLOCK_CONTROL_REG](#gga95b012159eb95cd62859a6d5c4d862b8aab8109cdf28181ef0dbb9d1e3b93b096)、[FLASH_STM32_EX_OP_OPTB_READ](#gga95b012159eb95cd62859a6d5c4d862b8a778e98df945314508cb9c2c266e6f02a)、[FLASH_STM32_EX_OP_OPTB_WRITE](#gga95b012159eb95cd62859a6d5c4d862b8a40f2e65d83c8ef8144c2ba3072cb4a85)。

STM32 闪存扩展操作（Flash Extended Operations）的枚举（Enumeration）。

<a id="r_gaac68791eaf037279ae1a51a0058ed4b6"></a>

```c
enum stm32_qspi_ex_ops { FLASH_STM32_QSPI_EX_OP_GENERIC_READ , FLASH_STM32_QSPI_EX_OP_GENERIC_WRITE }
```

相关声明：[stm32_qspi_ex_ops](#gaac68791eaf037279ae1a51a0058ed4b6)、[FLASH_STM32_QSPI_EX_OP_GENERIC_READ](#ggaac68791eaf037279ae1a51a0058ed4b6a70307ddcc9bdb96f3e5f3796d2bd442e)、[FLASH_STM32_QSPI_EX_OP_GENERIC_WRITE](#ggaac68791eaf037279ae1a51a0058ed4b6a092676857a6a2ba1f33486cf50cf20ef)。

STM32 四线串行外设接口扩展操作（QSPI Extended Operations）的枚举（Enumeration）。

## 7.4\_详细说明（Detailed Documentation）

<a id="ga95b012159eb95cd62859a6d5c4d862b8"></a>

### `stm32_ex_ops`

```c
enum stm32_ex_ops
```

```c
#include <zephyr/drivers/flash/stm32_flash_api_extensions.h>
```

STM32 闪存扩展操作（Flash Extended Operations）的枚举（Enumeration）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FLASH_STM32_EX_OP_SECTOR_WP` | STM32 扇区写保护控制（Sector Write Protection Control）。注意：仅在启用 Kconfig 选项 `CONFIG_FLASH_STM32_WRITE_PROTECT` 时可用。输入为 `flash_stm32_ex_op_sector_wp_in`，包含两个扇区掩码：第一个使能保护，第二个禁用保护。若两个掩码均为 0，保护状态保持不变；若同一扇区同时出现在两个掩码中，则使能保护。输出为已使能保护的扇区掩码。若只需查询受保护扇区，输入可为 `NULL`；不需要输出时，输出可为 `NULL`。 |
| `FLASH_STM32_EX_OP_RDP` | STM32 扇区读出保护控制（Sector Readout Protection Control）。注意：仅在启用 Kconfig 选项 `CONFIG_FLASH_STM32_READOUT_PROTECTION` 时可用。输入为 `flash_stm32_ex_op_rdp`，包含所需读出保护（RDP）状态的信息；输出为应用更改后的状态。 |
| `FLASH_STM32_EX_OP_BLOCK_OPTION_REG` | STM32 锁定选项寄存器（Block Option Register）。此操作锁定选项寄存器，直到下次启动；调用后无法更改选项字节（Option Bytes），包括写保护（WP）、读出保护（RDP）和用户字节。 |
| `FLASH_STM32_EX_OP_BLOCK_CONTROL_REG` | STM32 锁定控制寄存器（Block Control Register）。此操作锁定控制寄存器，直到下次启动；调用后无法执行擦除或写入等基本操作。 |
| `FLASH_STM32_EX_OP_OPTB_READ` | STM32 选项字节读取（Option Bytes Read）。读取选项字节内容；`out` 接收一个 `uint32_t` 指针，不使用 `in`。 |
| `FLASH_STM32_EX_OP_OPTB_WRITE` | STM32 选项字节写入（Option Bytes Write）。写入选项字节内容；`in` 接收新值，不使用 `out`。新值仅在设备重启后生效。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_FLASH_STM32_WRITE_PROTECT` 时可用。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_FLASH_STM32_READOUT_PROTECTION` 时可用。

<a id="gaac68791eaf037279ae1a51a0058ed4b6"></a>

### `stm32_qspi_ex_ops`

```c
enum stm32_qspi_ex_ops
```

```c
#include <zephyr/drivers/flash/stm32_flash_api_extensions.h>
```

STM32 四线串行外设接口扩展操作（QSPI Extended Operations）的枚举（Enumeration）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FLASH_STM32_QSPI_EX_OP_GENERIC_READ` | 四线 SPI（QSPI）通用读取命令（Generic Read Command）。发送自定义命令，并将读取结果写入用户提供的缓冲区。 |
| `FLASH_STM32_QSPI_EX_OP_GENERIC_WRITE` | 四线 SPI（QSPI）通用写入命令（Generic Write Command）。发送自定义命令，然后写入从用户提供缓冲区取出的数据。 |


## 7.5\_原页交叉引用（Cross References）

- [stm32_flash_api_extensions.h](../api_file_configuration_reference/P072_zephyr__drivers__flash__stm32_flash_api_extensions.h_文件参考.md)
- [flash_stm32_ex_op_sector_wp_in](../system_service_model_reference/P035_flash_stm32_ex_op_sector_wp_in_结构体.md)
- [flash_stm32_ex_op_sector_wp_out](../system_service_model_reference/P036_flash_stm32_ex_op_sector_wp_out_结构体.md)
- [flash_stm32_ex_op_rdp](../system_service_model_reference/P034_flash_stm32_ex_op_rdp_结构体.md)
- [CONFIG_FLASH_STM32_WRITE_PROTECT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_STM32_WRITE_PROTECT)
- [CONFIG_FLASH_STM32_READOUT_PROTECTION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_STM32_READOUT_PROTECTION)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga95b012159eb95cd62859a6d5c4d862b8a7bde6043879f1a6139da11679b4455fe"></a>
<a id="gga95b012159eb95cd62859a6d5c4d862b8ae1b013a96c3a64b0d3e677b4bce954a0"></a>
<a id="gga95b012159eb95cd62859a6d5c4d862b8a59b3b9a3b0eaee9cd4435f452855b903"></a>
<a id="gga95b012159eb95cd62859a6d5c4d862b8aab8109cdf28181ef0dbb9d1e3b93b096"></a>
<a id="gga95b012159eb95cd62859a6d5c4d862b8a778e98df945314508cb9c2c266e6f02a"></a>
<a id="gga95b012159eb95cd62859a6d5c4d862b8a40f2e65d83c8ef8144c2ba3072cb4a85"></a>
<a id="ggaac68791eaf037279ae1a51a0058ed4b6a70307ddcc9bdb96f3e5f3796d2bd442e"></a>
<a id="ggaac68791eaf037279ae1a51a0058ed4b6a092676857a6a2ba1f33486cf50cf20ef"></a>

---

[上一章](P006_时钟协议（Clock Protocol）.md) · [返回大纲](大纲.md)
