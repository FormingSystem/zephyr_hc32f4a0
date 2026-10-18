---
id: learning.zephyr-docs.api-file-configuration-reference.page-72
title: zephyr__drivers__flash__stm32_flash_api_extensions.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32__flash__api__extensions_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_zephyr\_\_drivers\_\_flash\_\_stm32\_flash\_api\_extensions.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stm32__flash__api__extensions_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STM32闪存扩展操作（Flash Extended Operations）的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/flash.h>
```

查看此文件的源码。

STM32闪存扩展操作（Flash Extended Operations）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 72.1\_数据结构（Data Structures）

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

## 72.2\_枚举（Enumerations）

<a id="r_ga95b012159eb95cd62859a6d5c4d862b8"></a>

```c
enum stm32_ex_ops { FLASH_STM32_EX_OP_SECTOR_WP = FLASH_EX_OP_VENDOR_BASE , FLASH_STM32_EX_OP_RDP , FLASH_STM32_EX_OP_BLOCK_OPTION_REG , FLASH_STM32_EX_OP_BLOCK_CONTROL_REG , FLASH_STM32_EX_OP_OPTB_READ , FLASH_STM32_EX_OP_OPTB_WRITE }
```

相关声明：[stm32_ex_ops](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#ga95b012159eb95cd62859a6d5c4d862b8)、[FLASH_STM32_EX_OP_SECTOR_WP](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8a7bde6043879f1a6139da11679b4455fe)、[FLASH_STM32_EX_OP_RDP](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8ae1b013a96c3a64b0d3e677b4bce954a0)、[FLASH_STM32_EX_OP_BLOCK_OPTION_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8a59b3b9a3b0eaee9cd4435f452855b903)、[FLASH_STM32_EX_OP_BLOCK_CONTROL_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8aab8109cdf28181ef0dbb9d1e3b93b096)、[FLASH_STM32_EX_OP_OPTB_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8a778e98df945314508cb9c2c266e6f02a)、[FLASH_STM32_EX_OP_OPTB_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8a40f2e65d83c8ef8144c2ba3072cb4a85)。

STM32 闪存扩展操作（Flash Extended Operations）的枚举（Enumeration）。

<a id="r_gaac68791eaf037279ae1a51a0058ed4b6"></a>

```c
enum stm32_qspi_ex_ops { FLASH_STM32_QSPI_EX_OP_GENERIC_READ , FLASH_STM32_QSPI_EX_OP_GENERIC_WRITE }
```

相关声明：[stm32_qspi_ex_ops](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gaac68791eaf037279ae1a51a0058ed4b6)、[FLASH_STM32_QSPI_EX_OP_GENERIC_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#ggaac68791eaf037279ae1a51a0058ed4b6a70307ddcc9bdb96f3e5f3796d2bd442e)、[FLASH_STM32_QSPI_EX_OP_GENERIC_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#ggaac68791eaf037279ae1a51a0058ed4b6a092676857a6a2ba1f33486cf50cf20ef)。

STM32 四线串行外设接口扩展操作（QSPI Extended Operations）的枚举（Enumeration）。


## 72.3\_原页交叉引用（Cross References）

- [zephyr/drivers/flash.h](../flash_reference/P010_Flash公共头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P832_stm32_flash_api_extensions.h_源码浏览.md)
- [flash_stm32_ex_op_sector_wp_in](../system_service_model_reference/P035_flash_stm32_ex_op_sector_wp_in_结构体.md)
- [FLASH_STM32_EX_OP_SECTOR_WP](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8a7bde6043879f1a6139da11679b4455fe)
- [flash_stm32_ex_op_sector_wp_out](../system_service_model_reference/P036_flash_stm32_ex_op_sector_wp_out_结构体.md)
- [flash_stm32_ex_op_rdp](../system_service_model_reference/P034_flash_stm32_ex_op_rdp_结构体.md)
- [FLASH_STM32_EX_OP_RDP](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8ae1b013a96c3a64b0d3e677b4bce954a0)
- [stm32_ex_ops](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#ga95b012159eb95cd62859a6d5c4d862b8)
- [FLASH_STM32_EX_OP_BLOCK_OPTION_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8a59b3b9a3b0eaee9cd4435f452855b903)
- [FLASH_STM32_EX_OP_BLOCK_CONTROL_REG](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8aab8109cdf28181ef0dbb9d1e3b93b096)
- [FLASH_STM32_EX_OP_OPTB_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8a778e98df945314508cb9c2c266e6f02a)
- [FLASH_STM32_EX_OP_OPTB_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gga95b012159eb95cd62859a6d5c4d862b8a40f2e65d83c8ef8144c2ba3072cb4a85)
- [stm32_qspi_ex_ops](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#gaac68791eaf037279ae1a51a0058ed4b6)
- [FLASH_STM32_QSPI_EX_OP_GENERIC_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#ggaac68791eaf037279ae1a51a0058ed4b6a70307ddcc9bdb96f3e5f3796d2bd442e)
- [FLASH_STM32_QSPI_EX_OP_GENERIC_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__flash__ex__op.html#ggaac68791eaf037279ae1a51a0058ed4b6a092676857a6a2ba1f33486cf50cf20ef)

<a id="header-details"></a>

---

[上一章](P071_zephyr__dt-bindings__pinctrl__stm32-pinctrl-common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P073_zephyr__debug__symtab.h_文件参考.md)
