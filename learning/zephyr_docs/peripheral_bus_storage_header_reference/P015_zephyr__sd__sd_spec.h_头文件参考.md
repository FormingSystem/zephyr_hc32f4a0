---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-15
title: zephyr__sd__sd_spec.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_sd\_\_sd\_spec.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

<a id="r_sd_5Fswitch_5Fcaps"></a>

```c
struct sd_switch_caps
```

相关声明：[sd_switch_caps](../peripheral_bus_storage_model_reference/P078_sd_switch_caps_结构体.md)。

SD切换能力（Switch Capabilities）。

<a id="r_sd_5Fcid"></a>

```c
struct sd_cid
```

相关声明：[sd_cid](../peripheral_bus_storage_model_reference/P075_sd_cid_结构体.md)。

SD卡标识寄存器（Card Identification Register）。

<a id="r_sd_5Fcsd"></a>

```c
struct sd_csd
```

相关声明：[sd_csd](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md)。

SD卡专用数据寄存器（Card Specific Data Register）。

<a id="r_mmc_5Fdevice_5Ftype"></a>

```c
struct mmc_device_type
```

相关声明：[mmc_device_type](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md)。

多媒体卡（MMC）的设备类型。

<a id="r_mmc_5Fext_5Fcsd"></a>

```c
struct mmc_ext_csd
```

相关声明：[mmc_ext_csd](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md)。

多媒体卡（MMC）的扩展卡专用数据寄存器（Extended CSD）。

<a id="r_sd_5Fscr"></a>

```c
struct sd_scr
```

相关声明：[sd_scr](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md)。

SD卡配置寄存器（Card Configuration Register）。

<a id="r_sdio_5Fcis"></a>

```c
struct sdio_cis
```

相关声明：[sdio_cis](../peripheral_bus_storage_model_reference/P085_sdio_cis_结构体.md)。

SDIO通用卡信息结构（CIS）元组的属性。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.2\_宏定义（Macros）

<a id="r_ac104a7c39f61829092eaffd98663045b"></a>

```c
#define SD_R1_CURRENT_STATE(x)
```

相关声明：[SD_R1_CURRENT_STATE](#ac104a7c39f61829092eaffd98663045b)。

<a id="r_aa841b78f5937f8499918cc977a36e90f"></a>

```c
#define SD_SPI_CMD_SIZE 6
```

相关声明：[SD_SPI_CMD_SIZE](#aa841b78f5937f8499918cc977a36e90f)。

<a id="r_a85e46f60c0ae5f21a4386009bbfaf0a3"></a>

```c
#define SD_SPI_CMD_BODY_SIZE (SD_SPI_CMD_SIZE - 1)
```

相关声明：[SD_SPI_CMD_BODY_SIZE](#a85e46f60c0ae5f21a4386009bbfaf0a3)、[SD_SPI_CMD_SIZE](#aa841b78f5937f8499918cc977a36e90f)。

<a id="r_aed67a9adbb001dad73eec4054ef6cbc1"></a>

```c
#define SD_SPI_CRC16_SIZE 2
```

相关声明：[SD_SPI_CRC16_SIZE](#aed67a9adbb001dad73eec4054ef6cbc1)。

<a id="r_a7da6535d451c1062f8d0c92f5688e178"></a>

```c
#define SD_SPI_START 0x80
```

相关声明：[SD_SPI_START](#a7da6535d451c1062f8d0c92f5688e178)。

<a id="r_a2283409131ac9ede90773b256094b74c"></a>

```c
#define SD_SPI_TX 0x40
```

相关声明：[SD_SPI_TX](#a2283409131ac9ede90773b256094b74c)。

<a id="r_a2d1dee775c3849a92dac9d179bd50a6c"></a>

```c
#define SD_SPI_CMD 0x3F
```

相关声明：[SD_SPI_CMD](#a2d1dee775c3849a92dac9d179bd50a6c)。

<a id="r_a7cd4fbf7d5ce2e8eba8c795a675486bb"></a>

```c
#define SD_SPI_TOKEN_SINGLE 0xFE
```

相关声明：[SD_SPI_TOKEN_SINGLE](#a7cd4fbf7d5ce2e8eba8c795a675486bb)。

<a id="r_ae34cf95537f2c0963ade18f1ba5d6e20"></a>

```c
#define SD_SPI_TOKEN_MULTI_WRITE 0xFC
```

相关声明：[SD_SPI_TOKEN_MULTI_WRITE](#ae34cf95537f2c0963ade18f1ba5d6e20)。

<a id="r_a9d4f357ff29ee3b5483505404ba3c956"></a>

```c
#define SD_SPI_TOKEN_STOP_TRAN 0xFD
```

相关声明：[SD_SPI_TOKEN_STOP_TRAN](#a9d4f357ff29ee3b5483505404ba3c956)。

<a id="r_a5d36df2e0d1bd88aadc3673cdf12aea7"></a>

```c
#define SD_SPI_RESPONSE_ACCEPTED 0x05
```

相关声明：[SD_SPI_RESPONSE_ACCEPTED](#a5d36df2e0d1bd88aadc3673cdf12aea7)。

<a id="r_a3a206f684b2c878f59a394b06abd9814"></a>

```c
#define SD_SPI_RESPONSE_CRC_ERR 0x0B
```

相关声明：[SD_SPI_RESPONSE_CRC_ERR](#a3a206f684b2c878f59a394b06abd9814)。

<a id="r_a498f76218e054dff0e524a83ac90ccd1"></a>

```c
#define SD_SPI_RESPONSE_WRITE_ERR 0x0C
```

相关声明：[SD_SPI_RESPONSE_WRITE_ERR](#a498f76218e054dff0e524a83ac90ccd1)。

<a id="r_a0d10fc7ae53b5bfb6d7f448844820799"></a>

```c
#define SD_IF_COND_VHS_MASK (0x0F << 8)
```

相关声明：[SD_IF_COND_VHS_MASK](#a0d10fc7ae53b5bfb6d7f448844820799)。

<a id="r_a38157545a4a10dd4757ad1eb80487c60"></a>

```c
#define SD_IF_COND_VHS_3V3 BIT(8)
```

相关声明：[SD_IF_COND_VHS_3V3](#a38157545a4a10dd4757ad1eb80487c60)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aed6aacadb061a42993c59d8d69a2f2ab"></a>

```c
#define SD_IF_COND_CHECK 0xAA
```

相关声明：[SD_IF_COND_CHECK](#aed6aacadb061a42993c59d8d69a2f2ab)。

<a id="r_a23690672048afbc75ce2c2f4d9a74144"></a>

```c
#define SDIO_OCR_IO_NUMBER_SHIFT 28
```

相关声明：[SDIO_OCR_IO_NUMBER_SHIFT](#a23690672048afbc75ce2c2f4d9a74144)。

<a id="r_a0d98fd7cd6f67b28981c6e01f8805a01"></a>

```c
#define SDIO_IO_OCR_MASK 0xFFFFFF
```

相关声明：[SDIO_IO_OCR_MASK](#a0d98fd7cd6f67b28981c6e01f8805a01)。

<a id="r_a947520a05fc99c25449fab98d0d02b1e"></a>

```c
#define SD_PRODUCT_NAME_BYTES 5
```

相关声明：[SD_PRODUCT_NAME_BYTES](#a947520a05fc99c25449fab98d0d02b1e)。

<a id="r_a523a28eeec3d0a71f0d7ca49ab397960"></a>

```c
#define SDMMC_DEFAULT_BLOCK_SIZE 512
```

相关声明：[SDMMC_DEFAULT_BLOCK_SIZE](#a523a28eeec3d0a71f0d7ca49ab397960)。

<a id="r_ade9a798f584d431c86e172266394f41e"></a>

```c
#define MMC_EXT_CSD_BYTES 512
```

相关声明：[MMC_EXT_CSD_BYTES](#ade9a798f584d431c86e172266394f41e)。

<a id="r_a960ade30c404ebb08769c5870ac21b37"></a>

```c
#define SDIO_CMD_ARG_RW_SHIFT 31
```

相关声明：[SDIO_CMD_ARG_RW_SHIFT](#a960ade30c404ebb08769c5870ac21b37)。

读写标志的移位量（Shift）。

<a id="r_acd6e41030a8d16419cc22adf9f0a5509"></a>

```c
#define SDIO_CMD_ARG_FUNC_NUM_SHIFT 28
```

相关声明：[SDIO_CMD_ARG_FUNC_NUM_SHIFT](#acd6e41030a8d16419cc22adf9f0a5509)。

功能编号的移位量。

<a id="r_afadddcc143b78325505a40544c04e3b0"></a>

```c
#define SDIO_DIRECT_CMD_ARG_RAW_SHIFT 27
```

相关声明：[SDIO_DIRECT_CMD_ARG_RAW_SHIFT](#afadddcc143b78325505a40544c04e3b0)。

直接访问的 RAW 标志移位量。

<a id="r_aa74dbe588f1f5ca248cf0f5a2e8e8c81"></a>

```c
#define SDIO_CMD_ARG_REG_ADDR_SHIFT 9
```

相关声明：[SDIO_CMD_ARG_REG_ADDR_SHIFT](#aa74dbe588f1f5ca248cf0f5a2e8e8c81)。

直接访问的寄存器地址移位量。

<a id="r_a338e9606baa6937e0887e7a9b9372c23"></a>

```c
#define SDIO_CMD_ARG_REG_ADDR_MASK 0x1FFFF
```

相关声明：[SDIO_CMD_ARG_REG_ADDR_MASK](#a338e9606baa6937e0887e7a9b9372c23)。

直接访问的寄存器地址掩码（Mask）。

<a id="r_a5ab9e1e0c96e7166b1ff7a208f90001d"></a>

```c
#define SDIO_DIRECT_CMD_DATA_MASK 0xFF
```

相关声明：[SDIO_DIRECT_CMD_DATA_MASK](#a5ab9e1e0c96e7166b1ff7a208f90001d)。

数据掩码。

<a id="r_ac6c49ad6118debe7a9e64f412e597f22"></a>

```c
#define SDIO_EXTEND_CMD_ARG_BLK_SHIFT 27
```

相关声明：[SDIO_EXTEND_CMD_ARG_BLK_SHIFT](#ac6c49ad6118debe7a9e64f412e597f22)。

扩展写入的块模式（Block mode）。

<a id="r_a73ca83a4884f13fa5de8500f69252bef"></a>

```c
#define SDIO_EXTEND_CMD_ARG_OP_CODE_SHIFT 26
```

相关声明：[SDIO_EXTEND_CMD_ARG_OP_CODE_SHIFT](#a73ca83a4884f13fa5de8500f69252bef)。

操作码：地址递增（Increment address）。

<a id="r_ae211fa0bfa6809273b5f7267c95ce681"></a>

```c
#define SDIO_CCCR_CCCR 0x00
```

相关声明：[SDIO_CCCR_CCCR](#ae211fa0bfa6809273b5f7267c95ce681)。

卡公共控制寄存器（Card Common Control Register，CCCR）定义。

<a id="r_accf473b0fcdc9e1e03329f91e588de1a"></a>

```c
#define SDIO_CCCR_CCCR_REV_MASK 0x0F
```

相关声明：[SDIO_CCCR_CCCR_REV_MASK](#accf473b0fcdc9e1e03329f91e588de1a)。

<a id="r_af5db599ebd0748528e8369653a5e3929"></a>

```c
#define SDIO_CCCR_CCCR_REV_SHIFT 0x0
```

相关声明：[SDIO_CCCR_CCCR_REV_SHIFT](#af5db599ebd0748528e8369653a5e3929)。

<a id="r_ab240215a68f23ec69e901c0666b0dfe0"></a>

```c
#define SDIO_CCCR_CCCR_REV_1_00 0x0
```

相关声明：[SDIO_CCCR_CCCR_REV_1_00](#ab240215a68f23ec69e901c0666b0dfe0)。

CCCR/功能基本寄存器（FBR）版本 1.00。

<a id="r_aace4672360d77085bec93b52e3ac05d9"></a>

```c
#define SDIO_CCCR_CCCR_REV_1_10 0x1
```

相关声明：[SDIO_CCCR_CCCR_REV_1_10](#aace4672360d77085bec93b52e3ac05d9)。

CCCR/FBR 版本 1.10。

<a id="r_a566200e9322e8e4c9b3edd21a2ced93c"></a>

```c
#define SDIO_CCCR_CCCR_REV_2_00 0x2
```

相关声明：[SDIO_CCCR_CCCR_REV_2_00](#a566200e9322e8e4c9b3edd21a2ced93c)。

CCCR/FBR 版本 2.00。

<a id="r_aa90600f74ff69315e38ed1c10a3cde7c"></a>

```c
#define SDIO_CCCR_CCCR_REV_3_00 0x3
```

相关声明：[SDIO_CCCR_CCCR_REV_3_00](#aa90600f74ff69315e38ed1c10a3cde7c)。

CCCR/FBR 版本 3.00。

<a id="r_aafc2b0c434dff4a0903e4910181f9e81"></a>

```c
#define SDIO_CCCR_SD 0x01
```

相关声明：[SDIO_CCCR_SD](#aafc2b0c434dff4a0903e4910181f9e81)。

SD 规范版本寄存器。

<a id="r_aa425236b097f44a9721e7aedd203ff90"></a>

```c
#define SDIO_CCCR_SD_SPEC_MASK 0x0F
```

相关声明：[SDIO_CCCR_SD_SPEC_MASK](#aa425236b097f44a9721e7aedd203ff90)。

<a id="r_a223defa20d223655d215065b222a6767"></a>

```c
#define SDIO_CCCR_SD_SPEC_SHIFT 0x0
```

相关声明：[SDIO_CCCR_SD_SPEC_SHIFT](#a223defa20d223655d215065b222a6767)。

<a id="r_a0b2103011690e1d3f1daef4e45a11986"></a>

```c
#define SDIO_CCCR_IO_EN 0x02
```

相关声明：[SDIO_CCCR_IO_EN](#a0b2103011690e1d3f1daef4e45a11986)。

SDIO I/O 使能寄存器（IO Enable register）。

<a id="r_a6cfa2671e574650e6f35a65828cd459c"></a>

```c
#define SDIO_CCCR_IO_RD 0x03
```

相关声明：[SDIO_CCCR_IO_RD](#a6cfa2671e574650e6f35a65828cd459c)。

SDIO I/O 就绪寄存器（IO Ready register）。

<a id="r_a15caca2936186b54c330b4a9050c9795"></a>

```c
#define SDIO_CCCR_INT_EN 0x04
```

相关声明：[SDIO_CCCR_INT_EN](#a15caca2936186b54c330b4a9050c9795)。

SDIO 中断使能寄存器（Interrupt enable register）。

<a id="r_a81b7523a76a1826a14c2cc1c242a49a9"></a>

```c
#define SDIO_CCCR_INT_P 0x05
```

相关声明：[SDIO_CCCR_INT_P](#a81b7523a76a1826a14c2cc1c242a49a9)。

SDIO 中断挂起寄存器（Interrupt pending register）。

<a id="r_a7e061818bc8f923d5342c38721a1a501"></a>

```c
#define SDIO_CCCR_ABORT 0x06
```

相关声明：[SDIO_CCCR_ABORT](#a7e061818bc8f923d5342c38721a1a501)。

SDIO I/O 中止寄存器（IO abort register）。

<a id="r_a283f2b2f2c28b3c8208f3d6aca3ca3d2"></a>

```c
#define SDIO_CCCR_BUS_IF 0x07
```

相关声明：[SDIO_CCCR_BUS_IF](#a283f2b2f2c28b3c8208f3d6aca3ca3d2)。

SDIO 总线接口控制寄存器（Bus interface control register）。

<a id="r_a6c04dc28d7f39fda7cd0181421a13ea0"></a>

```c
#define SDIO_CCCR_BUS_IF_WIDTH_MASK 0x3
```

相关声明：[SDIO_CCCR_BUS_IF_WIDTH_MASK](#a6c04dc28d7f39fda7cd0181421a13ea0)。

SDIO 总线宽度设置掩码。

<a id="r_aec58e3fcda2f792266fbd8ab1b75f98c"></a>

```c
#define SDIO_CCCR_BUS_IF_WIDTH_1_BIT 0x00
```

相关声明：[SDIO_CCCR_BUS_IF_WIDTH_1_BIT](#aec58e3fcda2f792266fbd8ab1b75f98c)。

1 位 SDIO 总线设置。

<a id="r_aeb23fa771a16f69fcb9d97b156f25ade"></a>

```c
#define SDIO_CCCR_BUS_IF_WIDTH_4_BIT 0x02
```

相关声明：[SDIO_CCCR_BUS_IF_WIDTH_4_BIT](#aeb23fa771a16f69fcb9d97b156f25ade)。

4 位 SDIO 总线设置。

<a id="r_ade7a14837ee90c8ce24959926d81eaee"></a>

```c
#define SDIO_CCCR_BUS_IF_WIDTH_8_BIT 0x03
```

相关声明：[SDIO_CCCR_BUS_IF_WIDTH_8_BIT](#ade7a14837ee90c8ce24959926d81eaee)。

8 位 SDIO 总线设置。

<a id="r_a0b878d7e794d3edd127c3f08633efbbc"></a>

```c
#define SDIO_CCCR_CAPS 0x08
```

相关声明：[SDIO_CCCR_CAPS](#a0b878d7e794d3edd127c3f08633efbbc)。

SDIO 卡能力（Card capabilities）。

<a id="r_affb9533b340f5424c1f42445c6f1002f"></a>

```c
#define SDIO_CCCR_CAPS_SDC BIT(0)
```

相关声明：[SDIO_CCCR_CAPS_SDC](#affb9533b340f5424c1f42445c6f1002f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持在数据传输期间执行 `CMD52`。

<a id="r_aaaf8d335a8d025b998feeb93c0899a99"></a>

```c
#define SDIO_CCCR_CAPS_SMB BIT(1)
```

相关声明：[SDIO_CCCR_CAPS_SMB](#aaaf8d335a8d025b998feeb93c0899a99)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持多块传输（Multiple block transfer）。

<a id="r_a8011927f7b565304ec31a7e61d403d6e"></a>

```c
#define SDIO_CCCR_CAPS_SRW BIT(2)
```

相关声明：[SDIO_CCCR_CAPS_SRW](#a8011927f7b565304ec31a7e61d403d6e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持读取等待控制（Read wait control）。

<a id="r_a7550fe8aab011fc87baeb575463e27d9"></a>

```c
#define SDIO_CCCR_CAPS_SBS BIT(3)
```

相关声明：[SDIO_CCCR_CAPS_SBS](#a7550fe8aab011fc87baeb575463e27d9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持总线控制。

<a id="r_a74082cfafdd9e8bfa37e92624ff75e80"></a>

```c
#define SDIO_CCCR_CAPS_S4MI BIT(4)
```

相关声明：[SDIO_CCCR_CAPS_S4MI](#a74082cfafdd9e8bfa37e92624ff75e80)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持块间隙中断（Block gap interrupt）。

<a id="r_aa8281a65d0865fba8b85d91d00b90091"></a>

```c
#define SDIO_CCCR_CAPS_E4MI BIT(5)
```

相关声明：[SDIO_CCCR_CAPS_E4MI](#aa8281a65d0865fba8b85d91d00b90091)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

启用块间隙中断。

<a id="r_aee93278e3c0ec4cbf0e3065d6a58f516"></a>

```c
#define SDIO_CCCR_CAPS_LSC BIT(6)
```

相关声明：[SDIO_CCCR_CAPS_LSC](#aee93278e3c0ec4cbf0e3065d6a58f516)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

低速卡（Low speed card）。

<a id="r_a7ba2dcf801f81ab53b418e59441000ae"></a>

```c
#define SDIO_CCCR_CAPS_BLS BIT(7)
```

相关声明：[SDIO_CCCR_CAPS_BLS](#a7ba2dcf801f81ab53b418e59441000ae)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持 4 位总线的低速卡。

<a id="r_a8f97c16c091bd19b545bbe452581dfff"></a>

```c
#define SDIO_CCCR_CIS 0x09
```

相关声明：[SDIO_CCCR_CIS](#a8f97c16c091bd19b545bbe452581dfff)。

SDIO 卡信息结构（CIS）元组指针。

<a id="r_a05edbcb4a98831cbeac509f26e881de8"></a>

```c
#define SDIO_CCCR_SPEED 0x13
```

相关声明：[SDIO_CCCR_SPEED](#a05edbcb4a98831cbeac509f26e881de8)。

SDIO 总线速度选择（Bus speed select）。

<a id="r_a964759dc76bd2a9f9f9dce5c21dc2cb4"></a>

```c
#define SDIO_CCCR_SPEED_SHS BIT(0)
```

相关声明：[SDIO_CCCR_SPEED_SHS](#a964759dc76bd2a9f9f9dce5c21dc2cb4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

是否支持高速模式（High speed）。

<a id="r_a1a1817554f886a999484e2663432cd8b"></a>

```c
#define SDIO_CCCR_SPEED_MASK 0xE
```

相关声明：[SDIO_CCCR_SPEED_MASK](#a1a1817554f886a999484e2663432cd8b)。

总线速度选择掩码。

<a id="r_a38d57134d99e2dfc5760fcf7312b6cd5"></a>

```c
#define SDIO_CCCR_SPEED_SHIFT 0x1
```

相关声明：[SDIO_CCCR_SPEED_SHIFT](#a38d57134d99e2dfc5760fcf7312b6cd5)。

总线速度选择字段的移位量。

<a id="r_a9ee7aec8589aceb8555917971ab9afd3"></a>

```c
#define SDIO_CCCR_SPEED_SDR12 0x0
```

相关声明：[SDIO_CCCR_SPEED_SDR12](#a9ee7aec8589aceb8555917971ab9afd3)。

选择 SDR12。

<a id="r_acb3bdd73bace425a94a357a2f0bff4ef"></a>

```c
#define SDIO_CCCR_SPEED_HS 0x1
```

相关声明：[SDIO_CCCR_SPEED_HS](#acb3bdd73bace425a94a357a2f0bff4ef)。

选择高速模式（High speed mode）。

<a id="r_afabf4bb10bed3295d1d051c113e61545"></a>

```c
#define SDIO_CCCR_SPEED_SDR25 0x1
```

相关声明：[SDIO_CCCR_SPEED_SDR25](#afabf4bb10bed3295d1d051c113e61545)。

选择 SDR25。

<a id="r_a81bc96279a19618c9212674757abd141"></a>

```c
#define SDIO_CCCR_SPEED_SDR50 0x2
```

相关声明：[SDIO_CCCR_SPEED_SDR50](#a81bc96279a19618c9212674757abd141)。

选择 SDR50。

<a id="r_a0d51f98d56303dd55177245785748158"></a>

```c
#define SDIO_CCCR_SPEED_SDR104 0x3
```

相关声明：[SDIO_CCCR_SPEED_SDR104](#a0d51f98d56303dd55177245785748158)。

选择 SDR104。

<a id="r_ad3dc3009d2d78a6306c3247ab85ef48d"></a>

```c
#define SDIO_CCCR_SPEED_DDR50 0x4
```

相关声明：[SDIO_CCCR_SPEED_DDR50](#ad3dc3009d2d78a6306c3247ab85ef48d)。

选择 DDR50。

<a id="r_afb72ff0aa5b90446db296af16bf9bb02"></a>

```c
#define SDIO_CCCR_UHS 0x14
```

相关声明：[SDIO_CCCR_UHS](#afb72ff0aa5b90446db296af16bf9bb02)。

SDIO 超高速（UHS）支持。

<a id="r_a9965d399115bca8574a9beaeac9b9f31"></a>

```c
#define SDIO_CCCR_UHS_SDR50 BIT(0)
```

相关声明：[SDIO_CCCR_UHS_SDR50](#a9965d399115bca8574a9beaeac9b9f31)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

是否支持 SDR50。

<a id="r_aca4fee68fdf3480ec8cf7de7b46a8d4e"></a>

```c
#define SDIO_CCCR_UHS_SDR104 BIT(1)
```

相关声明：[SDIO_CCCR_UHS_SDR104](#aca4fee68fdf3480ec8cf7de7b46a8d4e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

是否支持 SDR104。

<a id="r_a2678ede1ac974a9670fdcaa393682aa6"></a>

```c
#define SDIO_CCCR_UHS_DDR50 BIT(2)
```

相关声明：[SDIO_CCCR_UHS_DDR50](#a2678ede1ac974a9670fdcaa393682aa6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

是否支持 DDR50。

<a id="r_a3a5d01e688b18109ad2f19bc5d017f26"></a>

```c
#define SDIO_CCCR_DRIVE_STRENGTH 0x15
```

相关声明：[SDIO_CCCR_DRIVE_STRENGTH](#a3a5d01e688b18109ad2f19bc5d017f26)。

SDIO 驱动强度（Drive strength）。

<a id="r_a759a9dddc3aa08d0f11114637c5b69ff"></a>

```c
#define SDIO_CCCR_DRIVE_STRENGTH_A BIT(0)
```

相关声明：[SDIO_CCCR_DRIVE_STRENGTH_A](#a759a9dddc3aa08d0f11114637c5b69ff)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

A 型驱动（Drive type A）。

<a id="r_a8487f5a0a97e5f1f72500cf44cec89dc"></a>

```c
#define SDIO_CCCR_DRIVE_STRENGTH_C BIT(1)
```

相关声明：[SDIO_CCCR_DRIVE_STRENGTH_C](#a8487f5a0a97e5f1f72500cf44cec89dc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

C 型驱动（Drive type C）。

<a id="r_abc1ed41094d9cdd300b1b3712bb082b2"></a>

```c
#define SDIO_CCCR_DRIVE_STRENGTH_D BIT(2)
```

相关声明：[SDIO_CCCR_DRIVE_STRENGTH_D](#abc1ed41094d9cdd300b1b3712bb082b2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

D 型驱动（Drive type D）。

<a id="r_a2ff95d19f7f60ce33b17b69e2672e7e5"></a>

```c
#define SDIO_FBR_BASE(n)
```

相关声明：[SDIO_FBR_BASE](#a2ff95d19f7f60ce33b17b69e2672e7e5)。

获取功能基本寄存器（Function Basic Register）的地址。

<a id="r_aea0ed052a9d94d2e2b96931752975858"></a>

```c
#define SDIO_FBR_CIS 0x09
```

相关声明：[SDIO_FBR_CIS](#aea0ed052a9d94d2e2b96931752975858)。

SDIO 功能基本寄存器中的 CIS 指针。

<a id="r_a28fb27484353eb075d501b1ad7a76112"></a>

```c
#define SDIO_FBR_CSA 0x0C
```

相关声明：[SDIO_FBR_CSA](#a28fb27484353eb075d501b1ad7a76112)。

SDIO 功能基本寄存器中的代码存储区（CSA）指针。

<a id="r_af1885023615980d5cbb930538cc201a6"></a>

```c
#define SDIO_FBR_BLK_SIZE 0x10
```

相关声明：[SDIO_FBR_BLK_SIZE](#af1885023615980d5cbb930538cc201a6)。

SDIO 功能基本寄存器中的块大小。

<a id="r_a845866f4f88c280f8414b727e0d77edf"></a>

```c
#define SDIO_MAX_IO_NUMS 7
```

相关声明：[SDIO_MAX_IO_NUMS](#a845866f4f88c280f8414b727e0d77edf)。

SDIO 的最大 I/O 功能数。

<a id="r_afadae8a1db38d93b909b3f2c5b0e0110"></a>

```c
#define SDIO_TPL_CODE_NULL 0x00
```

相关声明：[SDIO_TPL_CODE_NULL](#afadae8a1db38d93b909b3f2c5b0e0110)。

空（NULL）CIS 元组代码。

<a id="r_af1983253320b45a2a1a2aab28c09e08f"></a>

```c
#define SDIO_TPL_CODE_MANIFID 0x20
```

相关声明：[SDIO_TPL_CODE_MANIFID](#af1983253320b45a2a1a2aab28c09e08f)。

制造商 ID 的 CIS 元组代码。

<a id="r_aae6f9377eccdbd5866f1a393e083c5e4"></a>

```c
#define SDIO_TPL_CODE_FUNCID 0x21
```

相关声明：[SDIO_TPL_CODE_FUNCID](#aae6f9377eccdbd5866f1a393e083c5e4)。

功能 ID 的 CIS 元组代码。

<a id="r_ac263bf61bcc750880bae34dde62d61e4"></a>

```c
#define SDIO_TPL_CODE_FUNCE 0x22
```

相关声明：[SDIO_TPL_CODE_FUNCE](#ac263bf61bcc750880bae34dde62d61e4)。

功能扩展（Function extension）的 CIS 元组代码。

<a id="r_a21e0771f38a22f93c9f4167d8b36f608"></a>

```c
#define SDIO_TPL_CODE_END 0xFF
```

相关声明：[SDIO_TPL_CODE_END](#a21e0771f38a22f93c9f4167d8b36f608)。

结束（End）CIS 元组代码。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 15.3\_枚举（Enumerations）

<a id="r_a072705601a34c697515f74acb0474c99"></a>

```c
enum sd_opcode { SD_GO_IDLE_STATE = 0 , MMC_SEND_OP_COND = 1 , SD_ALL_SEND_CID = 2 , SD_SEND_RELATIVE_ADDR = 3 , MMC_SEND_RELATIVE_ADDR = 3 , SDIO_SEND_OP_COND = 5 , SD_SWITCH = 6 , SD_SELECT_CARD = 7 , SD_SEND_IF_COND = 8 , MMC_SEND_EXT_CSD = 8 , SD_SEND_CSD = 9 , SD_SEND_CID = 10 , SD_VOL_SWITCH = 11 , SD_STOP_TRANSMISSION = 12 , SD_SEND_STATUS = 13 , MMC_CHECK_BUS_TEST = 14 , SD_GO_INACTIVE_STATE = 15 , SD_SET_BLOCK_SIZE = 16 , SD_READ_SINGLE_BLOCK = 17 , SD_READ_MULTIPLE_BLOCK = 18 , SD_SEND_TUNING_BLOCK = 19 , MMC_SEND_BUS_TEST = 19 , MMC_SEND_TUNING_BLOCK = 21 , SD_SET_BLOCK_COUNT = 23 , SD_WRITE_SINGLE_BLOCK = 24 , SD_WRITE_MULTIPLE_BLOCK = 25 , SD_ERASE_BLOCK_START = 32 , SD_ERASE_BLOCK_END = 33 , SD_ERASE_BLOCK_OPERATION = 38 , SDIO_RW_DIRECT = 52 , SDIO_RW_EXTENDED = 53 , SD_APP_CMD = 55 , SD_SPI_READ_OCR = 58 , SD_SPI_CRC_ON_OFF = 59 }
```

相关声明：[sd_opcode](#a072705601a34c697515f74acb0474c99)、[SD_GO_IDLE_STATE](#a072705601a34c697515f74acb0474c99a9dcb2e5fb6a5a53c6cb02422fd1fef3c)、[MMC_SEND_OP_COND](#a072705601a34c697515f74acb0474c99a54546b311e446754738a9b6f1e3eaea4)、[SD_ALL_SEND_CID](#a072705601a34c697515f74acb0474c99affcc3d18f6bda30fb3fd34916d8f61fe)、[SD_SEND_RELATIVE_ADDR](#a072705601a34c697515f74acb0474c99a35c39a93dfcc239fcb80db70449af99e)、[MMC_SEND_RELATIVE_ADDR](#a072705601a34c697515f74acb0474c99a56c94068ecb32eb9ced47d4a3bf95481)、[SDIO_SEND_OP_COND](#a072705601a34c697515f74acb0474c99af48c850f0aa9e9f9dbce8fc8855f6a2a)、[SD_SWITCH](#a072705601a34c697515f74acb0474c99a400dc3acd2ae8320f130dbea80c81969)、[SD_SELECT_CARD](#a072705601a34c697515f74acb0474c99afa15c17b4fb95747b444616b085b4905)、[SD_SEND_IF_COND](#a072705601a34c697515f74acb0474c99a0da09225692b10e51140d4f15ba1dd0a)、[MMC_SEND_EXT_CSD](#a072705601a34c697515f74acb0474c99a7c9bfc788861214fae86e22443e9484a)、[SD_SEND_CSD](#a072705601a34c697515f74acb0474c99adc7e589c9352cddf856b2e868f93a097)、[SD_SEND_CID](#a072705601a34c697515f74acb0474c99a8c3edf14ca3a6e04c1949a40cd3fb135)、[SD_VOL_SWITCH](#a072705601a34c697515f74acb0474c99ad6d6f1ccdabc2970ac2ab6c7a853b37e)、[SD_STOP_TRANSMISSION](#a072705601a34c697515f74acb0474c99aa5f2d8c27d0b7ae780734cb4bedbf8a4)、[SD_SEND_STATUS](#a072705601a34c697515f74acb0474c99ad822462692847b4e8433157cd75eef70)、[MMC_CHECK_BUS_TEST](#a072705601a34c697515f74acb0474c99a45bc2d4b117d144ef5191719f9b6c297)、[SD_GO_INACTIVE_STATE](#a072705601a34c697515f74acb0474c99a5c85e3208bb686d8ded9ae0fe7bd9d53)、[SD_SET_BLOCK_SIZE](#a072705601a34c697515f74acb0474c99abd97c835c80320637579c692d6f57878)、[SD_READ_SINGLE_BLOCK](#a072705601a34c697515f74acb0474c99a99c20a704cce28fee37b9b0f14b2ff15)、[SD_READ_MULTIPLE_BLOCK](#a072705601a34c697515f74acb0474c99aa58b1d9f75b639dc1b28163988bc8aa3)、[SD_SEND_TUNING_BLOCK](#a072705601a34c697515f74acb0474c99af48292861388f111b0afad64f0352664)、[MMC_SEND_BUS_TEST](#a072705601a34c697515f74acb0474c99a35b942802a4238882440f2e470f2555f)、[MMC_SEND_TUNING_BLOCK](#a072705601a34c697515f74acb0474c99a0378338c2747ba8947d8ffcb18f77d51)、[SD_SET_BLOCK_COUNT](#a072705601a34c697515f74acb0474c99a7e34ea8ce2a215c2a76f4184b84a06f2)、[SD_WRITE_SINGLE_BLOCK](#a072705601a34c697515f74acb0474c99adca664fbf5ff0b4d174ca21641e01004)、[SD_WRITE_MULTIPLE_BLOCK](#a072705601a34c697515f74acb0474c99a9cd6e9c88c3989531a71015147496895)、[SD_ERASE_BLOCK_START](#a072705601a34c697515f74acb0474c99aa7c628982851eba38074d02e9e335b57)、[SD_ERASE_BLOCK_END](#a072705601a34c697515f74acb0474c99a753b0fc3e44a4376998e5887ed2c5901)、[SD_ERASE_BLOCK_OPERATION](#a072705601a34c697515f74acb0474c99a4aa36f7d8ceaa3cdab300915453b64b5)、[SDIO_RW_DIRECT](#a072705601a34c697515f74acb0474c99a7ef64e231154de2e461005af29918b86)、[SDIO_RW_EXTENDED](#a072705601a34c697515f74acb0474c99a7ccf37711e67b58534689997ac1375df)、[SD_APP_CMD](#a072705601a34c697515f74acb0474c99aef4ee3246cd66cd7d48f1dabf3fcd7ef)、[SD_SPI_READ_OCR](#a072705601a34c697515f74acb0474c99aa3183436decfa0e42ac0461629258ba3)、[SD_SPI_CRC_ON_OFF](#a072705601a34c697515f74acb0474c99ab590e9d9b3213f31a2399ef379d066aa)。

SD 规范命令操作码（Command opcodes）。

<a id="r_a1c77191f9cb8c50e8e2a03cda2984dbc"></a>

```c
enum sd_app_cmd { SD_APP_SET_BUS_WIDTH = 6 , SD_APP_SEND_STATUS = 13 , SD_APP_SEND_NUM_WRITTEN_BLK = 22 , SD_APP_SET_WRITE_BLK_ERASE_CNT = 23 , SD_APP_SEND_OP_COND = 41 , SD_APP_CLEAR_CARD_DETECT = 42 , SD_APP_SEND_SCR = 51 }
```

相关声明：[sd_app_cmd](#a1c77191f9cb8c50e8e2a03cda2984dbc)、[SD_APP_SET_BUS_WIDTH](#a1c77191f9cb8c50e8e2a03cda2984dbcaca51b75cde3505fd672391b9d7a7997a)、[SD_APP_SEND_STATUS](#a1c77191f9cb8c50e8e2a03cda2984dbca36f78cdbd8fcc962c2247d7fc1f33f9b)、[SD_APP_SEND_NUM_WRITTEN_BLK](#a1c77191f9cb8c50e8e2a03cda2984dbca03fc81eeed7047ad914ce6590511dfa3)、[SD_APP_SET_WRITE_BLK_ERASE_CNT](#a1c77191f9cb8c50e8e2a03cda2984dbcacf330302cc8ef7f55d76c2cace40649e)、[SD_APP_SEND_OP_COND](#a1c77191f9cb8c50e8e2a03cda2984dbca2a4278c079a227145f63f5f2d860146a)、[SD_APP_CLEAR_CARD_DETECT](#a1c77191f9cb8c50e8e2a03cda2984dbcaa4a44bb015be3cbcf180f34a39ba8e05)、[SD_APP_SEND_SCR](#a1c77191f9cb8c50e8e2a03cda2984dbca305b2fb720b5191c762b77b886152ca8)。

SD 应用命令操作码（Application command opcodes）。

<a id="r_ad38162e32b87d3c01f1ae46d3423155a"></a>

```c
enum sd_r1_status { SD_R1_AUTH_ERR = BIT(3) , SD_R1_APP_CMD = BIT(5) , SD_R1_FX_EVENT = BIT(6) , SD_R1_RDY_DATA = BIT(8) , SD_R1_CUR_STATE = (0xFU << 9) , SD_R1_ERASE_RESET = BIT(13) , SD_R1_ECC_DISABLED = BIT(14) , SD_R1_ERASE_SKIP = BIT(15) , SD_R1_CSD_OVERWRITE = BIT(16) , SD_R1_ERR = BIT(19) , SD_R1_CC_ERR = BIT(20) , SD_R1_ECC_FAIL = BIT(21) , SD_R1_ILLEGAL_CMD = BIT(22) , SD_R1_CRC_ERR = BIT(23) , SD_R1_UNLOCK_FAIL = BIT(24) , SD_R1_CARD_LOCKED = BIT(25) , SD_R1_WP_VIOLATION = BIT(26) , SD_R1_ERASE_PARAM = BIT(27) , SD_R1_ERASE_SEQ_ERR = BIT(28) , SD_R1_BLOCK_LEN_ERR = BIT(29) , SD_R1_ADDR_ERR = BIT(30) , SD_R1_OUT_OF_RANGE = BIT(31) , SD_R1_ERR_FLAGS , SD_R1ERR_NONE = 0 }
```

相关声明：[sd_r1_status](#ad38162e32b87d3c01f1ae46d3423155a)、[SD_R1_AUTH_ERR](#ad38162e32b87d3c01f1ae46d3423155aaa33240a72b4aeff90e48d8dd3b9419c5)、[SD_R1_APP_CMD](#ad38162e32b87d3c01f1ae46d3423155aa72c5d7592912c25f0440fa38664dfc13)、[SD_R1_FX_EVENT](#ad38162e32b87d3c01f1ae46d3423155aab852db2cfe8d7581e1ad7a1c2aee5406)、[SD_R1_RDY_DATA](#ad38162e32b87d3c01f1ae46d3423155aac99e88e470b5ecb04885b0289a96a2c8)、[SD_R1_CUR_STATE](#ad38162e32b87d3c01f1ae46d3423155aa0815a9749fc47ea398752e886e222b65)、[SD_R1_ERASE_RESET](#ad38162e32b87d3c01f1ae46d3423155aa3c9f8c1239694b9bda4aca0d7f40a929)、[SD_R1_ECC_DISABLED](#ad38162e32b87d3c01f1ae46d3423155aa4cf46d638fd781b73edd03b61dd5d1a2)、[SD_R1_ERASE_SKIP](#ad38162e32b87d3c01f1ae46d3423155aa1388a4a737946b04de90dcec9c719837)、[SD_R1_CSD_OVERWRITE](#ad38162e32b87d3c01f1ae46d3423155aa0b9e2ded1a4aa629d698f3ba5584bcc2)、[SD_R1_ERR](#ad38162e32b87d3c01f1ae46d3423155aac6c818a2d7443a820c3f027e2d799ad2)、[SD_R1_CC_ERR](#ad38162e32b87d3c01f1ae46d3423155aaac890f2e8917f249f729e273f4180c8d)、[SD_R1_ECC_FAIL](#ad38162e32b87d3c01f1ae46d3423155aafe9dd6c272ec4d1c04efdfa4d7e12870)、[SD_R1_ILLEGAL_CMD](#ad38162e32b87d3c01f1ae46d3423155aa6e3c05c3b4a44c9ec63f89554850abbc)、[SD_R1_CRC_ERR](#ad38162e32b87d3c01f1ae46d3423155aac5fb430e08cbab9b2cbf2015202641e2)、[SD_R1_UNLOCK_FAIL](#ad38162e32b87d3c01f1ae46d3423155aa51199d1fa7c1cda33fde647843394d65)、[SD_R1_CARD_LOCKED](#ad38162e32b87d3c01f1ae46d3423155aa02d458f5c51dfb7554e17bad1acb591a)、[SD_R1_WP_VIOLATION](#ad38162e32b87d3c01f1ae46d3423155aa3ac808a14aa22446db1101fe5f2cbfab)、[SD_R1_ERASE_PARAM](#ad38162e32b87d3c01f1ae46d3423155aa4ad410b3a28df509ab875d26ae431e21)、[SD_R1_ERASE_SEQ_ERR](#ad38162e32b87d3c01f1ae46d3423155aa94c0a61d8f8aeb5ed7a13846eb81dfae)、[SD_R1_BLOCK_LEN_ERR](#ad38162e32b87d3c01f1ae46d3423155aabb622edfda732a5fd3fec2b042951254)、[SD_R1_ADDR_ERR](#ad38162e32b87d3c01f1ae46d3423155aa153195025c02879f23af882b6a4d7af4)、[SD_R1_OUT_OF_RANGE](#ad38162e32b87d3c01f1ae46d3423155aac7cb6855c33427bdf0a4e7d344281aaf)、[SD_R1_ERR_FLAGS](#ad38162e32b87d3c01f1ae46d3423155aab6413ec799d46c7341e48f0b5146f400)、[SD_R1ERR_NONE](#ad38162e32b87d3c01f1ae46d3423155aab8635ae93d3d927f662e88c9e55305eb)。

原生 SD 模式（Native SD mode）的 R1 响应状态标志。

<a id="r_aa0686c333989b0551d3af5eb01de4065"></a>

```c
enum sd_r1_current_state { SDMMC_R1_IDLE = 0U , SDMMC_R1_READY = 1U , SDMMC_R1_IDENTIFY = 2U , SDMMC_R1_STANDBY = 3U , SDMMC_R1_TRANSFER = 4U , SDMMC_R1_SEND_DATA = 5U , SDMMC_R1_RECIVE_DATA = 6U , SDMMC_R1_PROGRAM = 7U , SDMMC_R1_DISCONNECT = 8U }
```

相关声明：[sd_r1_current_state](#aa0686c333989b0551d3af5eb01de4065)、[SDMMC_R1_IDLE](#aa0686c333989b0551d3af5eb01de4065a081f03ba34d8cd168ab5d4172d3c8d6a)、[SDMMC_R1_READY](#aa0686c333989b0551d3af5eb01de4065a135f072a7d9ee5967a49f7a164816854)、[SDMMC_R1_IDENTIFY](#aa0686c333989b0551d3af5eb01de4065a1ddcc2a60e6f83538151fc93ad434ddf)、[SDMMC_R1_STANDBY](#aa0686c333989b0551d3af5eb01de4065ac906ebc564bfc63a7f4ce0350db6667b)、[SDMMC_R1_TRANSFER](#aa0686c333989b0551d3af5eb01de4065a59ead4a70e76c9b2d6c817f4e2847998)、[SDMMC_R1_SEND_DATA](#aa0686c333989b0551d3af5eb01de4065a5d6d02968e18dd84af3583d282179e64)、[SDMMC_R1_RECIVE_DATA](#aa0686c333989b0551d3af5eb01de4065a3feb7a1594dc32703d2fbf6e43e77c0c)、[SDMMC_R1_PROGRAM](#aa0686c333989b0551d3af5eb01de4065acccc283c3dc4a36992e76ea0b6f4d68b)、[SDMMC_R1_DISCONNECT](#aa0686c333989b0551d3af5eb01de4065abebe32c9b1e107c729f4e6ecf501ee1e)。

SD 当前状态值。

<a id="r_aaf06bb2dcb6e359e08bae37d2f36bbc3"></a>

```c
enum sd_spi_r1_error_flag { SD_SPI_R1PARAMETER_ERR = BIT(6) , SD_SPI_R1ADDRESS_ERR = BIT(5) , SD_SPI_R1ERASE_SEQ_ERR = BIT(4) , SD_SPI_R1CMD_CRC_ERR = BIT(3) , SD_SPI_R1ILLEGAL_CMD_ERR = BIT(2) , SD_SPI_R1ERASE_RESET = BIT(1) , SD_SPI_R1IDLE_STATE = BIT(0) }
```

相关声明：[sd_spi_r1_error_flag](#aaf06bb2dcb6e359e08bae37d2f36bbc3)、[SD_SPI_R1PARAMETER_ERR](#aaf06bb2dcb6e359e08bae37d2f36bbc3aae5e5c58313c1216448474da513ca2b6)、[SD_SPI_R1ADDRESS_ERR](#aaf06bb2dcb6e359e08bae37d2f36bbc3ae50961a0eb0f59776a156facf51e4620)、[SD_SPI_R1ERASE_SEQ_ERR](#aaf06bb2dcb6e359e08bae37d2f36bbc3aa07d3031debe394b369d93fde728d406)、[SD_SPI_R1CMD_CRC_ERR](#aaf06bb2dcb6e359e08bae37d2f36bbc3ae4785671c3a4dca332c10c9bc0a72fba)、[SD_SPI_R1ILLEGAL_CMD_ERR](#aaf06bb2dcb6e359e08bae37d2f36bbc3a0a59356a4db1abd3f72a8c9778b04e66)、[SD_SPI_R1ERASE_RESET](#aaf06bb2dcb6e359e08bae37d2f36bbc3a4eb47f187f4aee8228b09a37d4669a4f)、[SD_SPI_R1IDLE_STATE](#aaf06bb2dcb6e359e08bae37d2f36bbc3a9c77ef6b4da1f8ac56ebe8be03504b69)。

SPI SD 模式的 R1 响应状态标志。

<a id="r_aa1b9e80034c783cc7ff43dc79ac5878f"></a>

```c
enum sd_spi_r2_status { SDHC_SPI_R2_CARD_LOCKED = BIT(8) , SDHC_SPI_R2_UNLOCK_FAIL = BIT(9) , SDHC_SPI_R2_ERR = BIT(10) , SDHC_SPI_R2_CC_ERR = BIT(11) , SDHC_SPI_R2_ECC_FAIL = BIT(12) , SDHC_SPI_R2_WP_VIOLATION = BIT(13) , SDHC_SPI_R2_ERASE_PARAM = BIT(14) , SDHC_SPI_R2_OUT_OF_RANGE = BIT(15) }
```

相关声明：[sd_spi_r2_status](#aa1b9e80034c783cc7ff43dc79ac5878f)、[SDHC_SPI_R2_CARD_LOCKED](#aa1b9e80034c783cc7ff43dc79ac5878fa8f693e2ff4acfb3d652106fc25f8758f)、[SDHC_SPI_R2_UNLOCK_FAIL](#aa1b9e80034c783cc7ff43dc79ac5878fa3f8fde9c17c04f4500f5a86cf4d9e7df)、[SDHC_SPI_R2_ERR](#aa1b9e80034c783cc7ff43dc79ac5878faf74a4730cc3507a35179fe09da721a19)、[SDHC_SPI_R2_CC_ERR](#aa1b9e80034c783cc7ff43dc79ac5878fad33e5499a36259f5b881ce524a1f4159)、[SDHC_SPI_R2_ECC_FAIL](#aa1b9e80034c783cc7ff43dc79ac5878fac853010c32e85d30f9f5936851ac4ddb)、[SDHC_SPI_R2_WP_VIOLATION](#aa1b9e80034c783cc7ff43dc79ac5878fa92bcd0ee78ddba8dc551c7917a37a792)、[SDHC_SPI_R2_ERASE_PARAM](#aa1b9e80034c783cc7ff43dc79ac5878fa47bb6389f20ceb840612266fedac0f7a)、[SDHC_SPI_R2_OUT_OF_RANGE](#aa1b9e80034c783cc7ff43dc79ac5878faedbd66fd01bb87a4f55291c299589db7)。

SPI SD 模式的 R2 响应状态标志。

<a id="r_a1cfd2df5ec76eeb915fd3689408a65d6"></a>

```c
enum sd_rsp_type { SD_RSP_TYPE_NONE = 0U , SD_RSP_TYPE_R1 = 1U , SD_RSP_TYPE_R1b = 2U , SD_RSP_TYPE_R2 = 3U , SD_RSP_TYPE_R3 = 4U , SD_RSP_TYPE_R4 = 5U , SD_RSP_TYPE_R5 = 6U , SD_RSP_TYPE_R5b = 7U , SD_RSP_TYPE_R6 = 8U , SD_RSP_TYPE_R7 = 9U , SD_SPI_RSP_TYPE_R1 = (1U << 4) , SD_SPI_RSP_TYPE_R1b = (2U << 4) , SD_SPI_RSP_TYPE_R2 = (3U << 4) , SD_SPI_RSP_TYPE_R3 = (4U << 4) , SD_SPI_RSP_TYPE_R4 = (5U << 4) , SD_SPI_RSP_TYPE_R5 = (6U << 4) , SD_SPI_RSP_TYPE_R7 = (7U << 4) }
```

相关声明：[sd_rsp_type](#a1cfd2df5ec76eeb915fd3689408a65d6)、[SD_RSP_TYPE_NONE](#a1cfd2df5ec76eeb915fd3689408a65d6ad74407536823c1ea3afdf41d4b858b1c)、[SD_RSP_TYPE_R1](#a1cfd2df5ec76eeb915fd3689408a65d6a92718e4bd4bccaa2fe4a8780228004d7)、[SD_RSP_TYPE_R1b](#a1cfd2df5ec76eeb915fd3689408a65d6ae64496ba1520651f8bac35af2531eaf8)、[SD_RSP_TYPE_R2](#a1cfd2df5ec76eeb915fd3689408a65d6a96e26220a32f9b6e9e0bdd8c94d48eaf)、[SD_RSP_TYPE_R3](#a1cfd2df5ec76eeb915fd3689408a65d6af779f08bfb2fd73a717ea3789ccad509)、[SD_RSP_TYPE_R4](#a1cfd2df5ec76eeb915fd3689408a65d6a34b03331e8f7a9ea6b67da6b68c7e0ed)、[SD_RSP_TYPE_R5](#a1cfd2df5ec76eeb915fd3689408a65d6a91e216f8a1753b4719ee91819a926dde)、[SD_RSP_TYPE_R5b](#a1cfd2df5ec76eeb915fd3689408a65d6a5dcd82e4fe5a34646a617a5031fdc638)、[SD_RSP_TYPE_R6](#a1cfd2df5ec76eeb915fd3689408a65d6a3532733bc007df5009801bd6f09e45c9)、[SD_RSP_TYPE_R7](#a1cfd2df5ec76eeb915fd3689408a65d6aa5657942fb906d58ef2b7bed05137f23)、[SD_SPI_RSP_TYPE_R1](#a1cfd2df5ec76eeb915fd3689408a65d6a32b2c65c90d0d5b8df5e4a82e9b95a6d)、[SD_SPI_RSP_TYPE_R1b](#a1cfd2df5ec76eeb915fd3689408a65d6a22413680849a7645c7e8c585b5184203)、[SD_SPI_RSP_TYPE_R2](#a1cfd2df5ec76eeb915fd3689408a65d6a855f8e4399cf3ce0c05c6089f3439ec2)、[SD_SPI_RSP_TYPE_R3](#a1cfd2df5ec76eeb915fd3689408a65d6a7c44711a51e8175ebcaf4be24e2daec3)、[SD_SPI_RSP_TYPE_R4](#a1cfd2df5ec76eeb915fd3689408a65d6a4c35ca3a8db652008204cf0cfc8e2339)、[SD_SPI_RSP_TYPE_R5](#a1cfd2df5ec76eeb915fd3689408a65d6a0d82c7d93c187de5c40c0ff83fe8a478)、[SD_SPI_RSP_TYPE_R7](#a1cfd2df5ec76eeb915fd3689408a65d6a78472618e8523bf73ca65aee6b0a8318)。

SD 响应类型（Response types）。

<a id="r_afeec7c838fcf2d5c01cf653e305c749a"></a>

```c
enum sd_support_flag { SD_HIGH_CAPACITY_FLAG = BIT(1) , SD_4BITS_WIDTH = BIT(2) , SD_SDHC_FLAG = BIT(3) , SD_SDXC_FLAG = BIT(4) , SD_1800MV_FLAG = BIT(5) , SD_3000MV_FLAG = BIT(6) , SD_CMD23_FLAG = BIT(7) , SD_SPEED_CLASS_CONTROL_FLAG = BIT(8) , SD_MEM_PRESENT_FLAG = BIT(9) }
```

相关声明：[sd_support_flag](#afeec7c838fcf2d5c01cf653e305c749a)、[SD_HIGH_CAPACITY_FLAG](#afeec7c838fcf2d5c01cf653e305c749aa104798e5266441d5a2f356f50b01cb35)、[SD_4BITS_WIDTH](#afeec7c838fcf2d5c01cf653e305c749aa2511277c6c4ebe38bc7179312292710b)、[SD_SDHC_FLAG](#afeec7c838fcf2d5c01cf653e305c749aad9777c04b150a28916f894f54417286c)、[SD_SDXC_FLAG](#afeec7c838fcf2d5c01cf653e305c749aa0558ef06a64c10456d220e66a5bc0f8b)、[SD_1800MV_FLAG](#afeec7c838fcf2d5c01cf653e305c749aab78269976cbb673b4e00d6059ec38f80)、[SD_3000MV_FLAG](#afeec7c838fcf2d5c01cf653e305c749aa5458d4988d7076d854bd695307771858)、[SD_CMD23_FLAG](#afeec7c838fcf2d5c01cf653e305c749aac1f502da56d7d50b70898329da1ad21a)、[SD_SPEED_CLASS_CONTROL_FLAG](#afeec7c838fcf2d5c01cf653e305c749aa02b4afca69adad8d7f220b8e4a76db45)、[SD_MEM_PRESENT_FLAG](#afeec7c838fcf2d5c01cf653e305c749aa923c57b4134ad360ed3f6abbabfa87f1)。

SD 支持标志。

<a id="r_a7b20cc85df2d9f5ce6c010907d7d5c61"></a>

```c
enum sd_ocr_flag { SD_OCR_PWR_BUSY_FLAG = BIT(31) , SD_OCR_HOST_CAP_FLAG = BIT(30) , SD_OCR_CARD_CAP_FLAG = SD_OCR_HOST_CAP_FLAG , SD_OCR_SWITCH_18_REQ_FLAG = BIT(24) , SD_OCR_SWITCH_18_ACCEPT_FLAG = SD_OCR_SWITCH_18_REQ_FLAG , SD_OCR_VDD27_28FLAG = BIT(15) , SD_OCR_VDD28_29FLAG = BIT(16) , SD_OCR_VDD29_30FLAG = BIT(17) , SD_OCR_VDD30_31FLAG = BIT(18) , SD_OCR_VDD31_32FLAG = BIT(19) , SD_OCR_VDD32_33FLAG = BIT(20) , SD_OCR_VDD33_34FLAG = BIT(21) , SD_OCR_VDD34_35FLAG = BIT(22) , SD_OCR_VDD35_36FLAG = BIT(23) }
```

相关声明：[sd_ocr_flag](#a7b20cc85df2d9f5ce6c010907d7d5c61)、[SD_OCR_PWR_BUSY_FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a5f680f7a518294d7a706b73bbecbdb73)、[SD_OCR_HOST_CAP_FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61ae344e23bbc73a6f2ed17d10618bf7a5a)、[SD_OCR_CARD_CAP_FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a4cfc3b5856c525eda63b3a8b5fce5ae2)、[SD_OCR_SWITCH_18_REQ_FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a69d58775148ae7daf65598d6cf90488d)、[SD_OCR_SWITCH_18_ACCEPT_FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a541be7abf94851538a38f69c2ecb6b5f)、[SD_OCR_VDD27_28FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61acd85dd4f874ed9088e6d7a2260d7bc50)、[SD_OCR_VDD28_29FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a76356316ead27df98dac310eed775707)、[SD_OCR_VDD29_30FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a624191bea93e1a350073fe2e5d5adaf1)、[SD_OCR_VDD30_31FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a98c205ed0f08df1a2f9e2801f02bbe7f)、[SD_OCR_VDD31_32FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a8ae4a104d50c0bdcae4722de0d5ee605)、[SD_OCR_VDD32_33FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a0c8a74f1b50f574b64184bf1cdc1458f)、[SD_OCR_VDD33_34FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61aca49de7bd24df65fd6448a7e570b04a8)、[SD_OCR_VDD34_35FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61ae5e13b78bf3fdece36190e48136927bf)、[SD_OCR_VDD35_36FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a83a9f603da11b75f200d3bb62528cda4)。

SD 操作条件寄存器（OCR）的位标志。

<a id="r_a0769bcc2f15d43383f4e5a6c845c51aa"></a>

```c
enum mmc_ocr_flag { MMC_OCR_VDD170_195FLAG = BIT(7) , MMC_OCR_VDD20_26FLAG = 0x7F << 8 , MMC_OCR_VDD27_36FLAG = 0x1FF << 15 , MMC_OCR_SECTOR_MODE = BIT(30) , MMC_OCR_PWR_BUSY_FLAG = BIT(31) }
```

相关声明：[mmc_ocr_flag](#a0769bcc2f15d43383f4e5a6c845c51aa)、[MMC_OCR_VDD170_195FLAG](#a0769bcc2f15d43383f4e5a6c845c51aaa01aef2529fc39dc455c0fb8f2e9cc434)、[MMC_OCR_VDD20_26FLAG](#a0769bcc2f15d43383f4e5a6c845c51aaa984a5e7f75a4418ca29141f5c6031d1e)、[MMC_OCR_VDD27_36FLAG](#a0769bcc2f15d43383f4e5a6c845c51aaa239f02ae958dc3e25032825bb4c067e7)、[MMC_OCR_SECTOR_MODE](#a0769bcc2f15d43383f4e5a6c845c51aaa669934175190e5416a0d04c3c94acb4b)、[MMC_OCR_PWR_BUSY_FLAG](#a0769bcc2f15d43383f4e5a6c845c51aaa7127f5d946ea6bb4ec19b96033aafc4b)。

MMC OCR 位标志。

<a id="r_a296cbe236e9e36dc79ca30eb54e6bcc6"></a>

```c
enum sdio_ocr_flag { SDIO_OCR_IO_READY_FLAG = BIT(31) , SDIO_OCR_IO_NUMBER = (7U << 28U) , SDIO_OCR_MEM_PRESENT_FLAG = BIT(27) , SDIO_OCR_180_VOL_FLAG = BIT(24) , SDIO_OCR_VDD20_21FLAG = BIT(8) , SDIO_OCR_VDD21_22FLAG = BIT(9) , SDIO_OCR_VDD22_23FLAG = BIT(10) , SDIO_OCR_VDD23_24FLAG = BIT(11) , SDIO_OCR_VDD24_25FLAG = BIT(12) , SDIO_OCR_VDD25_26FLAG = BIT(13) , SDIO_OCR_VDD26_27FLAG = BIT(14) , SDIO_OCR_VDD27_28FLAG = BIT(15) , SDIO_OCR_VDD28_29FLAG = BIT(16) , SDIO_OCR_VDD29_30FLAG = BIT(17) , SDIO_OCR_VDD30_31FLAG = BIT(18) , SDIO_OCR_VDD31_32FLAG = BIT(19) , SDIO_OCR_VDD32_33FLAG = BIT(20) , SDIO_OCR_VDD33_34FLAG = BIT(21) , SDIO_OCR_VDD34_35FLAG = BIT(22) , SDIO_OCR_VDD35_36FLAG = BIT(23) }
```

相关声明：[sdio_ocr_flag](#a296cbe236e9e36dc79ca30eb54e6bcc6)、[SDIO_OCR_IO_READY_FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6adb3e45e84da812297359d6054baa69ba)、[SDIO_OCR_IO_NUMBER](#a296cbe236e9e36dc79ca30eb54e6bcc6a17007c3d37f047e6db56491a4230e8a8)、[SDIO_OCR_MEM_PRESENT_FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6ae923fdf459570657220ec225cbed7336)、[SDIO_OCR_180_VOL_FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a3f6ebe270ba873bab3407ee7d655b53d)、[SDIO_OCR_VDD20_21FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6aa7a656a21495fbf64666b2b80236e4e4)、[SDIO_OCR_VDD21_22FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6ad75d7d47a3d5fcc39a68c08546e9793b)、[SDIO_OCR_VDD22_23FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a560f91eb371bfea5cf6c5c036cc9c096)、[SDIO_OCR_VDD23_24FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a89c4025349ece0021cd627101f0efdd1)、[SDIO_OCR_VDD24_25FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a6323aa0a8cbfb59f8209a37c8135079c)、[SDIO_OCR_VDD25_26FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6ac0aa0897e1bbf45b0f5f4de73d733477)、[SDIO_OCR_VDD26_27FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a4d32525a631342d78f73b6296e148666)、[SDIO_OCR_VDD27_28FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a1f043936c614ac39b75f3835dc498b94)、[SDIO_OCR_VDD28_29FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a1071312f18c64077e6964e421ef00ead)、[SDIO_OCR_VDD29_30FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a246619651470476238452550068db8a0)、[SDIO_OCR_VDD30_31FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a4cb1cc23687e7a1854d8af0c76876a20)、[SDIO_OCR_VDD31_32FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a018af73c25e22c6e5313e5e3cff57e92)、[SDIO_OCR_VDD32_33FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6ac5613e6858d2c9217165ab4cbb240012)、[SDIO_OCR_VDD33_34FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a6673f837fa5a98b573886c5e6429c644)、[SDIO_OCR_VDD34_35FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a3d791855e6df402d5bfd92ce216a9a4b)、[SDIO_OCR_VDD35_36FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6af0baaa7f71d144c7e5edade4b2445813)。

SDIO OCR 位标志。

<a id="r_a76f7ea4b395028ad5d8cc5eee32656e3"></a>

```c
enum sd_switch_arg { SD_SWITCH_CHECK = 0U , SD_SWITCH_SET = 1U }
```

相关声明：[sd_switch_arg](#a76f7ea4b395028ad5d8cc5eee32656e3)、[SD_SWITCH_CHECK](#a76f7ea4b395028ad5d8cc5eee32656e3ae126f56fd639cbd686321a088d1e05e6)、[SD_SWITCH_SET](#a76f7ea4b395028ad5d8cc5eee32656e3a72c39e3140ddd3990c3cbe7c6c867bb1)。

SD 切换参数（Switch arguments）。

<a id="r_a97f4810585247f5fed41110413e49853"></a>

```c
enum sd_group_num { SD_GRP_TIMING_MODE = 0U , SD_GRP_CMD_SYS_MODE = 1U , SD_GRP_DRIVER_STRENGTH_MODE = 2U , SD_GRP_CURRENT_LIMIT_MODE = 3U }
```

相关声明：[sd_group_num](#a97f4810585247f5fed41110413e49853)、[SD_GRP_TIMING_MODE](#a97f4810585247f5fed41110413e49853a488b1aac4a0658c8b04b94b7556a2c5b)、[SD_GRP_CMD_SYS_MODE](#a97f4810585247f5fed41110413e49853a8c620d198b195d913ad3ff913434d764)、[SD_GRP_DRIVER_STRENGTH_MODE](#a97f4810585247f5fed41110413e49853a5e617dd9de3620481b89e517bd2c3a4b)、[SD_GRP_CURRENT_LIMIT_MODE](#a97f4810585247f5fed41110413e49853aa38ef885442708891b4ddc4a83c6ff66)。

SD 切换功能组编号（Switch group numbers）。

<a id="r_a2093143614e52f69e173289391d7e91c"></a>

```c
enum hs_max_data_rate { HS_UNSUPPORTED = 0 , HS_MAX_DTR = MHZ(50) }
```

相关声明：[hs_max_data_rate](#a2093143614e52f69e173289391d7e91c)、[HS_UNSUPPORTED](#a2093143614e52f69e173289391d7e91cac3e8d67442f59c35b57d19d81b5d0d66)、[HS_MAX_DTR](#a2093143614e52f69e173289391d7e91ca10f805e3f66366474428718cb4569da0)。

<a id="r_a5466ef2e30578d03c61831aa09fd7b9a"></a>

```c
enum uhs_max_data_rate { UHS_UNSUPPORTED = 0 , UHS_SDR12_MAX_DTR = MHZ(25) , UHS_SDR25_MAX_DTR = MHZ(50) , UHS_SDR50_MAX_DTR = MHZ(100) , UHS_SDR104_MAX_DTR = MHZ(208) , UHS_DDR50_MAX_DTR = MHZ(50) }
```

相关声明：[uhs_max_data_rate](#a5466ef2e30578d03c61831aa09fd7b9a)、[UHS_UNSUPPORTED](#a5466ef2e30578d03c61831aa09fd7b9aaad6eabbee29e4ff07bdf93a9162aea6b)、[UHS_SDR12_MAX_DTR](#a5466ef2e30578d03c61831aa09fd7b9aad61b9d180a8de3c01be2e892c45504fb)、[UHS_SDR25_MAX_DTR](#a5466ef2e30578d03c61831aa09fd7b9aa5c5c100c048986ecfed728690d05ac55)、[UHS_SDR50_MAX_DTR](#a5466ef2e30578d03c61831aa09fd7b9aa72e9ad81edf54b7139a758d47fe54dd5)、[UHS_SDR104_MAX_DTR](#a5466ef2e30578d03c61831aa09fd7b9aa106c43d63c3b3c02d3835ccf542f3190)、[UHS_DDR50_MAX_DTR](#a5466ef2e30578d03c61831aa09fd7b9aaff651e04c107beb23e0bd76d03029b26)。

<a id="r_a6b42b86d8f2ba4f29787c7c6f3d97f36"></a>

```c
enum sd_bus_speed { UHS_SDR12_BUS_SPEED = BIT(0) , DEFAULT_BUS_SPEED = BIT(0) , HIGH_SPEED_BUS_SPEED = BIT(1) , UHS_SDR25_BUS_SPEED = BIT(1) , UHS_SDR50_BUS_SPEED = BIT(2) , UHS_SDR104_BUS_SPEED = BIT(3) , UHS_DDR50_BUS_SPEED = BIT(4) }
```

相关声明：[sd_bus_speed](#a6b42b86d8f2ba4f29787c7c6f3d97f36)、[UHS_SDR12_BUS_SPEED](#a6b42b86d8f2ba4f29787c7c6f3d97f36a30f38c9e54bed572ca315fdeb9122103)、[DEFAULT_BUS_SPEED](#a6b42b86d8f2ba4f29787c7c6f3d97f36a90413fe7dfd8568eeac79709ece7a549)、[HIGH_SPEED_BUS_SPEED](#a6b42b86d8f2ba4f29787c7c6f3d97f36a5593992de690adb1022b7926d1508ab3)、[UHS_SDR25_BUS_SPEED](#a6b42b86d8f2ba4f29787c7c6f3d97f36ae07a7ef1ffce64bab52c5f6612a96716)、[UHS_SDR50_BUS_SPEED](#a6b42b86d8f2ba4f29787c7c6f3d97f36a360c72912e023e5b21363f3701deaa50)、[UHS_SDR104_BUS_SPEED](#a6b42b86d8f2ba4f29787c7c6f3d97f36aef2ef100dab4187c8600ea721e8726dd)、[UHS_DDR50_BUS_SPEED](#a6b42b86d8f2ba4f29787c7c6f3d97f36a022acb9d379c5ecf9935150ec6f51ffc)。

SD 总线速度支持位标志。

<a id="r_ae82da8038d71cf36ce2237504b498930"></a>

```c
enum sd_timing_mode { SD_TIMING_DEFAULT = 0U , SD_TIMING_SDR12 = 0U , SD_TIMING_HIGH_SPEED = 1U , SD_TIMING_SDR25 = 1U , SD_TIMING_SDR50 = 2U , SD_TIMING_SDR104 = 3U , SD_TIMING_DDR50 = 4U }
```

相关声明：[sd_timing_mode](#ae82da8038d71cf36ce2237504b498930)、[SD_TIMING_DEFAULT](#ae82da8038d71cf36ce2237504b498930aa858c50e3f53d635857084ab5801a204)、[SD_TIMING_SDR12](#ae82da8038d71cf36ce2237504b498930aea7ebe2a07e1ed7727262d522815355b)、[SD_TIMING_HIGH_SPEED](#ae82da8038d71cf36ce2237504b498930a7b6cef084cb3b83a91c05964951b05a6)、[SD_TIMING_SDR25](#ae82da8038d71cf36ce2237504b498930a433d8a39f77a612dd8104ca49c71a76f)、[SD_TIMING_SDR50](#ae82da8038d71cf36ce2237504b498930a787fb937df1275cb3d169e1dade2fb37)、[SD_TIMING_SDR104](#ae82da8038d71cf36ce2237504b498930aad980a4d433ffcf189a2e77b5d765861)、[SD_TIMING_DDR50](#ae82da8038d71cf36ce2237504b498930a88f373b6ac9335667eb8adab49a04e10)。

SD 时序模式（Timing mode）的功能选择值。

<a id="r_a9660a61775e481ae4093e11ce9336539"></a>

```c
enum sdhc_clock_speed { SDMMC_CLOCK_400KHZ = KHZ(400) , SD_CLOCK_25MHZ = MHZ(25) , SD_CLOCK_50MHZ = MHZ(50) , SD_CLOCK_100MHZ = MHZ(100) , SD_CLOCK_208MHZ = MHZ(208) , MMC_CLOCK_26MHZ = MHZ(26) , MMC_CLOCK_52MHZ = MHZ(52) , MMC_CLOCK_DDR52 = MHZ(52) , MMC_CLOCK_HS200 = MHZ(200) , MMC_CLOCK_HS400 = MHZ(200) }
```

相关声明：[sdhc_clock_speed](#a9660a61775e481ae4093e11ce9336539)、[SDMMC_CLOCK_400KHZ](#a9660a61775e481ae4093e11ce9336539a16c56ed964cc6bbb5cc6f0cb857d4f10)、[SD_CLOCK_25MHZ](#a9660a61775e481ae4093e11ce9336539ad5e9d57ee155e1b919f6cc213b05424f)、[SD_CLOCK_50MHZ](#a9660a61775e481ae4093e11ce9336539a39e410f7f5c51753bf415f727551b9fb)、[SD_CLOCK_100MHZ](#a9660a61775e481ae4093e11ce9336539a66ef44acd4ff3fafc2d49120df4b3c10)、[SD_CLOCK_208MHZ](#a9660a61775e481ae4093e11ce9336539a9570bb04b0181b4fbdc96cace060d187)、[MMC_CLOCK_26MHZ](#a9660a61775e481ae4093e11ce9336539ae9369c1cd7595ab83289fc356e9cc1b6)、[MMC_CLOCK_52MHZ](#a9660a61775e481ae4093e11ce9336539a5c37aeeb3c68d7b3dbe8b9001a00507c)、[MMC_CLOCK_DDR52](#a9660a61775e481ae4093e11ce9336539a66ecc8c1a73181d70e23424cf718728d)、[MMC_CLOCK_HS200](#a9660a61775e481ae4093e11ce9336539a14dec2b314ed13974dbba31f33a5eab9)、[MMC_CLOCK_HS400](#a9660a61775e481ae4093e11ce9336539a788a77f1e7a468c14ef57319ef8938f3)。

SD 主机控制器时钟速度。

<a id="r_a5ac0e70389dc6ccec515530df4eab972"></a>

```c
enum sd_current_setting { SD_SET_CURRENT_200MA = 0 , SD_SET_CURRENT_400MA = 1 , SD_SET_CURRENT_600MA = 2 , SD_SET_CURRENT_800MA = 3 }
```

相关声明：[sd_current_setting](#a5ac0e70389dc6ccec515530df4eab972)、[SD_SET_CURRENT_200MA](#a5ac0e70389dc6ccec515530df4eab972a134ed84475be6f55a0f3d3ae9201cbe9)、[SD_SET_CURRENT_400MA](#a5ac0e70389dc6ccec515530df4eab972ad548c59ebbb5045e437157cb9186de19)、[SD_SET_CURRENT_600MA](#a5ac0e70389dc6ccec515530df4eab972a83f1d375e4c5aa645759cc4e4462f8e0)、[SD_SET_CURRENT_800MA](#a5ac0e70389dc6ccec515530df4eab972af44faa0f33705ecbd37b5f3544105e34)。

SD 电流设置值。

<a id="r_a238de48c0cb55d173b6b874f4930c537"></a>

```c
enum sd_current_limit { SD_MAX_CURRENT_200MA = BIT(0) , SD_MAX_CURRENT_400MA = BIT(1) , SD_MAX_CURRENT_600MA = BIT(2) , SD_MAX_CURRENT_800MA = BIT(3) }
```

相关声明：[sd_current_limit](#a238de48c0cb55d173b6b874f4930c537)、[SD_MAX_CURRENT_200MA](#a238de48c0cb55d173b6b874f4930c537a18b21e5e76bea0263f475ecc228c0301)、[SD_MAX_CURRENT_400MA](#a238de48c0cb55d173b6b874f4930c537ae0605a0d9fc89e094a40b03e96c02339)、[SD_MAX_CURRENT_600MA](#a238de48c0cb55d173b6b874f4930c537af82a5f23e51bf3ac3b7bec137269f540)、[SD_MAX_CURRENT_800MA](#a238de48c0cb55d173b6b874f4930c537a2e3c01bc8d16641d7b500ce1244dbb03)。

SD 电流支持位域。

<a id="r_a314c38b1b0603c003e67b5dec2228d4b"></a>

```c
enum sd_driver_type { SD_DRIVER_TYPE_B = 0x1 , SD_DRIVER_TYPE_A = 0x2 , SD_DRIVER_TYPE_C = 0x4 , SD_DRIVER_TYPE_D = 0x8 }
```

相关声明：[sd_driver_type](#a314c38b1b0603c003e67b5dec2228d4b)、[SD_DRIVER_TYPE_B](#a314c38b1b0603c003e67b5dec2228d4ba32ad0894344bc4980f9206022ed0f877)、[SD_DRIVER_TYPE_A](#a314c38b1b0603c003e67b5dec2228d4ba9eec5ff6f7d4c7512212cb48719dcabf)、[SD_DRIVER_TYPE_C](#a314c38b1b0603c003e67b5dec2228d4ba0cd41f5198ce06ce5925b3f52d48b0a2)、[SD_DRIVER_TYPE_D](#a314c38b1b0603c003e67b5dec2228d4ba435b458d33f1568cb76b77a3ea2e1eb8)。

SD 驱动类型（Driver types）。

<a id="r_a66c69cd7d7818af86b6a91fad68334c2"></a>

```c
enum sd_driver_strength { SD_DRV_STRENGTH_TYPEB = 0U , SD_DRV_STRENGTH_TYPEA = 1U , SD_DRV_STRENGTH_TYPEC = 2U , SD_DRV_STRENGTH_TYPED = 3U }
```

相关声明：[sd_driver_strength](#a66c69cd7d7818af86b6a91fad68334c2)、[SD_DRV_STRENGTH_TYPEB](#a66c69cd7d7818af86b6a91fad68334c2a1b1e411f733ad6c1dc41896744441a48)、[SD_DRV_STRENGTH_TYPEA](#a66c69cd7d7818af86b6a91fad68334c2ad870ea9b9fc07a4af81bce3c82330441)、[SD_DRV_STRENGTH_TYPEC](#a66c69cd7d7818af86b6a91fad68334c2aa3e190aa6edb9f6eb7e29b78fc6f1a8a)、[SD_DRV_STRENGTH_TYPED](#a66c69cd7d7818af86b6a91fad68334c2ad5753bf6fae3f43ef8ce7cb7eb169b61)。

SD 切换驱动类型选择。

<a id="r_a313c45576db4ae219288fb4fbaad4bd8"></a>

```c
enum mmc_csd_freq { MMC_MAXFREQ_100KHZ = 0U << 0U , MMC_MAXFREQ_1MHZ = 1U << 0U , MMC_MAXFREQ_10MHZ = 2U << 0U , MMC_MAXFREQ_100MHZ = 3U << 0U , MMC_MAXFREQ_MULT_10 = 1U << 3U , MMC_MAXFREQ_MULT_12 = 2U << 3U , MMC_MAXFREQ_MULT_13 = 3U << 3U , MMC_MAXFREQ_MULT_15 = 4U << 3U , MMC_MAXFREQ_MULT_20 = 5U << 3U , MMC_MAXFREQ_MULT_26 = 6U << 3U , MMC_MAXFREQ_MULT_30 = 7U << 3U , MMC_MAXFREQ_MULT_35 = 8U << 3U , MMC_MAXFREQ_MULT_40 = 9U << 3U , MMC_MAXFREQ_MULT_45 = 0xAU << 3U , MMC_MAXFREQ_MULT_52 = 0xBU << 3U , MMC_MAXFREQ_MULT_55 = 0xCU << 3U , MMC_MAXFREQ_MULT_60 = 0xDU << 3U , MMC_MAXFREQ_MULT_70 = 0xEU << 3U , MMC_MAXFREQ_MULT_80 = 0xFU << 3u }
```

相关声明：[mmc_csd_freq](#a313c45576db4ae219288fb4fbaad4bd8)、[MMC_MAXFREQ_100KHZ](#a313c45576db4ae219288fb4fbaad4bd8a221dc45c7b73f6f96a63acbeb3e5e121)、[MMC_MAXFREQ_1MHZ](#a313c45576db4ae219288fb4fbaad4bd8a32c9f5017cd49c9ca4b352269de6eeff)、[MMC_MAXFREQ_10MHZ](#a313c45576db4ae219288fb4fbaad4bd8af63af4938d5aad64bac19fac42aedd10)、[MMC_MAXFREQ_100MHZ](#a313c45576db4ae219288fb4fbaad4bd8a13c703d344a1e03c1aa5881a77980085)、[MMC_MAXFREQ_MULT_10](#a313c45576db4ae219288fb4fbaad4bd8a74d01430b854f42ea84dba9d3ce45b16)、[MMC_MAXFREQ_MULT_12](#a313c45576db4ae219288fb4fbaad4bd8a4a3b8dc88c6349fb5f49ed3062a39a17)、[MMC_MAXFREQ_MULT_13](#a313c45576db4ae219288fb4fbaad4bd8a2c639715b63769e9a431a93e636f007e)、[MMC_MAXFREQ_MULT_15](#a313c45576db4ae219288fb4fbaad4bd8ac988a54239b7d9e182f1b2f480567e66)、[MMC_MAXFREQ_MULT_20](#a313c45576db4ae219288fb4fbaad4bd8ac8848c5cdf177737744da3283f7140d5)、[MMC_MAXFREQ_MULT_26](#a313c45576db4ae219288fb4fbaad4bd8ab1ff3da74a0dea49ffe7ac1d945ec4e6)、[MMC_MAXFREQ_MULT_30](#a313c45576db4ae219288fb4fbaad4bd8a69e1d369d668d63071410078a31099a0)、[MMC_MAXFREQ_MULT_35](#a313c45576db4ae219288fb4fbaad4bd8a63c0eee223946b1ae2b187bb585dfde4)、[MMC_MAXFREQ_MULT_40](#a313c45576db4ae219288fb4fbaad4bd8a572d53afafb39341e0cdb80d2d041d2c)、[MMC_MAXFREQ_MULT_45](#a313c45576db4ae219288fb4fbaad4bd8a5bd0506d7efbecdc42eb8fae1427dc37)、[MMC_MAXFREQ_MULT_52](#a313c45576db4ae219288fb4fbaad4bd8a988f18b9f418744721b0fc91f2432449)、[MMC_MAXFREQ_MULT_55](#a313c45576db4ae219288fb4fbaad4bd8abecfcd6d212185c74b57941c3fa58233)、[MMC_MAXFREQ_MULT_60](#a313c45576db4ae219288fb4fbaad4bd8adf578325509923b46e3ff4fbd74889ad)、[MMC_MAXFREQ_MULT_70](#a313c45576db4ae219288fb4fbaad4bd8aee24df1d628479fe2d920839a0bf5012)、[MMC_MAXFREQ_MULT_80](#a313c45576db4ae219288fb4fbaad4bd8a24ea8c9db5531b5404bb667da26ac5d0)。

MMC 最高频率（Maximum Frequency）。

<a id="r_ae1956c4b374e2c8b6a585596e93ac345"></a>

```c
enum mmc_timing_mode { MMC_LEGACY_TIMING = 0U , MMC_HS_TIMING = 1U , MMC_HS200_TIMING = 2U , MMC_HS400_TIMING = 3U }
```

相关声明：[mmc_timing_mode](#ae1956c4b374e2c8b6a585596e93ac345)、[MMC_LEGACY_TIMING](#ae1956c4b374e2c8b6a585596e93ac345ae51a5474387816c03970aa0f8058b002)、[MMC_HS_TIMING](#ae1956c4b374e2c8b6a585596e93ac345a17160707005c580fbd52dbd6b99699dd)、[MMC_HS200_TIMING](#ae1956c4b374e2c8b6a585596e93ac345a39200c50c7e22c096db3ce1dd3fe78d5)、[MMC_HS400_TIMING](#ae1956c4b374e2c8b6a585596e93ac345a4ea17060afbcd026387172c1af57bb43)。

MMC 时序模式（Timing Modes）。

<a id="r_af9783799f316cbaed12e18ce9944b09d"></a>

```c
enum mmc_driver_strengths { mmc_driv_type0 = 0U , mmc_driv_type1 = 1U , mmc_driv_type2 = 2U , mmc_driv_type3 = 3U , mmc_driv_type4 = 4U }
```

相关声明：[mmc_driver_strengths](#af9783799f316cbaed12e18ce9944b09d)、[mmc_driv_type0](#af9783799f316cbaed12e18ce9944b09dabd4f3ffac3f52efe797ce3ee3c31a03f)、[mmc_driv_type1](#af9783799f316cbaed12e18ce9944b09da2cedd0b40bf81afb35792150b2d4964a)、[mmc_driv_type2](#af9783799f316cbaed12e18ce9944b09dafed77d2aed13d59fa6645cb06fc21c43)、[mmc_driv_type3](#af9783799f316cbaed12e18ce9944b09dacf4d28d56a6c4925944ffc99072d46e9)、[mmc_driv_type4](#af9783799f316cbaed12e18ce9944b09daf5448a25c8b5a8411f059469112ef2be)。

MMC 驱动强度（Driver Strengths）。

<a id="r_ac86d8a44f37c771cb666f69a516dff81"></a>

```c
enum mmc_ext_csd_rev { MMC_5_1 = 8U , MMC_5_0 = 7U , MMC_4_5 = 6U , MMC_4_4 = 5U , MMC_4_3 = 3U , MMC_4_2 = 2U , MMC_4_1 = 1U , MMC_4_0 = 0U }
```

相关声明：[mmc_ext_csd_rev](#ac86d8a44f37c771cb666f69a516dff81)、[MMC_5_1](#ac86d8a44f37c771cb666f69a516dff81ad49da8223b68d35a4d95d6b48bb8a3f7)、[MMC_5_0](#ac86d8a44f37c771cb666f69a516dff81a87a4c0efb7e10cccce939af5f60343ad)、[MMC_4_5](#ac86d8a44f37c771cb666f69a516dff81aa0d4721b24d0cd71d6a8fbfc666a6e7c)、[MMC_4_4](#ac86d8a44f37c771cb666f69a516dff81a43b7acda3747eb2233c2f2a433ff71c7)、[MMC_4_3](#ac86d8a44f37c771cb666f69a516dff81a0f4fc7047a7c813b9ada618ed05e09a4)、[MMC_4_2](#ac86d8a44f37c771cb666f69a516dff81a9a960567b8ecbd6feff7e6337fc98567)、[MMC_4_1](#ac86d8a44f37c771cb666f69a516dff81ab84ae4edfcca8ccae2a0df0643d04ca2)、[MMC_4_0](#ac86d8a44f37c771cb666f69a516dff81aba4f3f30eaa7d3368743f78f3c355269)。

CSD 修订版本（Revision）。

<a id="r_a98c4f218acfa21e124aa22e9fe209437"></a>

```c
enum sd_csd_flag { SD_CSD_READ_BLK_PARTIAL_FLAG = BIT(0) , SD_CSD_WRITE_BLK_MISALIGN_FLAG = BIT(1) , SD_CSD_READ_BLK_MISALIGN_FLAG = BIT(2) , SD_CSD_DSR_IMPLEMENTED_FLAG = BIT(3) , SD_CSD_ERASE_BLK_EN_FLAG = BIT(4) , SD_CSD_WRITE_PROTECT_GRP_EN_FLAG = BIT(5) , SD_CSD_WRITE_BLK_PARTIAL_FLAG = BIT(6) , SD_CSD_FILE_FMT_GRP_FLAG = BIT(7) , SD_CSD_COPY_FLAG = BIT(8) , SD_CSD_PERMANENT_WRITE_PROTECT_FLAG = BIT(9) , SD_CSD_TMP_WRITE_PROTECT_FLAG = BIT(10) }
```

相关声明：[sd_csd_flag](#a98c4f218acfa21e124aa22e9fe209437)、[SD_CSD_READ_BLK_PARTIAL_FLAG](#a98c4f218acfa21e124aa22e9fe209437ac353a0c3c1ac62920efdc42879a81cff)、[SD_CSD_WRITE_BLK_MISALIGN_FLAG](#a98c4f218acfa21e124aa22e9fe209437a16d3fd179853f1f15b980d2b82b572be)、[SD_CSD_READ_BLK_MISALIGN_FLAG](#a98c4f218acfa21e124aa22e9fe209437aca7d98319db6a23b30625828807e2143)、[SD_CSD_DSR_IMPLEMENTED_FLAG](#a98c4f218acfa21e124aa22e9fe209437a1258364107909d0c4f8e9b7dba59300c)、[SD_CSD_ERASE_BLK_EN_FLAG](#a98c4f218acfa21e124aa22e9fe209437a0d907c1a9e69435433c5bf19bfacbd73)、[SD_CSD_WRITE_PROTECT_GRP_EN_FLAG](#a98c4f218acfa21e124aa22e9fe209437af85839612e4fcc94eb2bd0986bd1740c)、[SD_CSD_WRITE_BLK_PARTIAL_FLAG](#a98c4f218acfa21e124aa22e9fe209437aa8b8f850196e47799cb9b2cd06650520)、[SD_CSD_FILE_FMT_GRP_FLAG](#a98c4f218acfa21e124aa22e9fe209437a2e75506280c1b4d5866f4dd8f2518be8)、[SD_CSD_COPY_FLAG](#a98c4f218acfa21e124aa22e9fe209437a988758fe0720e6fc33564076e3bc51bf)、[SD_CSD_PERMANENT_WRITE_PROTECT_FLAG](#a98c4f218acfa21e124aa22e9fe209437a7496edd5c7ec694d2d175bf751de1458)、[SD_CSD_TMP_WRITE_PROTECT_FLAG](#a98c4f218acfa21e124aa22e9fe209437aa0c70fee97e29875394efc2a4c2fa274)。

SD 卡专用数据（Card Specific Data）标志。

<a id="r_a476ec98763d90a5cba336cbf22d6d553"></a>

```c
enum sd_scr_flag { SD_SCR_DATA_STATUS_AFTER_ERASE = BIT(0) , SD_SCR_SPEC3 = BIT(1) }
```

相关声明：[sd_scr_flag](#a476ec98763d90a5cba336cbf22d6d553)、[SD_SCR_DATA_STATUS_AFTER_ERASE](#a476ec98763d90a5cba336cbf22d6d553a759c63670d0dd41590fdb940a48ac4dd)、[SD_SCR_SPEC3](#a476ec98763d90a5cba336cbf22d6d553a59fb3a34a7dba6ed1c86bca21cf97871)。

SD卡配置寄存器（Card Configuration Register）。

<a id="r_abf77ec1ad65cc9c99dc930ed7a96301a"></a>

```c
enum sd_spec_version { SD_SPEC_VER1_0 = BIT(0) , SD_SPEC_VER1_1 = BIT(1) , SD_SPEC_VER2_0 = BIT(2) , SD_SPEC_VER3_0 = BIT(3) }
```

相关声明：[sd_spec_version](#abf77ec1ad65cc9c99dc930ed7a96301a)、[SD_SPEC_VER1_0](#abf77ec1ad65cc9c99dc930ed7a96301aa39605b86ccfad6196721ddfbb84b33d6)、[SD_SPEC_VER1_1](#abf77ec1ad65cc9c99dc930ed7a96301aac09ddfacee85353e243d6a8cfe7eeba8)、[SD_SPEC_VER2_0](#abf77ec1ad65cc9c99dc930ed7a96301aa3525ee751a482ae1cd816e2674ac3160)、[SD_SPEC_VER3_0](#abf77ec1ad65cc9c99dc930ed7a96301aa9e3d0d084a7d8ad1b9d08e6b699084e6)。

SD 规范版本。

<a id="r_a3a542344967c5c1912bde216559e7cd6"></a>

```c
enum sdio_func_num { SDIO_FUNC_NUM_0 = 0 , SDIO_FUNC_NUM_1 = 1 , SDIO_FUNC_NUM_2 = 2 , SDIO_FUNC_NUM_3 = 3 , SDIO_FUNC_NUM_4 = 4 , SDIO_FUNC_NUM_5 = 5 , SDIO_FUNC_NUM_6 = 6 , SDIO_FUNC_NUM_7 = 7 , SDIO_FUNC_MEMORY = 8 }
```

相关声明：[sdio_func_num](#a3a542344967c5c1912bde216559e7cd6)、[SDIO_FUNC_NUM_0](#a3a542344967c5c1912bde216559e7cd6ad7a10f97094ddb96f26ab44fc34de12a)、[SDIO_FUNC_NUM_1](#a3a542344967c5c1912bde216559e7cd6a900536b934da03f8e8590de3e3d56296)、[SDIO_FUNC_NUM_2](#a3a542344967c5c1912bde216559e7cd6ac2cc5967daee0a3e9ef61c9c486b3a6c)、[SDIO_FUNC_NUM_3](#a3a542344967c5c1912bde216559e7cd6adef5748e2622dab22da33504bbafa149)、[SDIO_FUNC_NUM_4](#a3a542344967c5c1912bde216559e7cd6a9b69d64108c6564bc313e4fb2b53f61c)、[SDIO_FUNC_NUM_5](#a3a542344967c5c1912bde216559e7cd6ac62397290371f5fb3fdf8d4b52fb3575)、[SDIO_FUNC_NUM_6](#a3a542344967c5c1912bde216559e7cd6a2a9baef178307d6e6006ea88b4da383c)、[SDIO_FUNC_NUM_7](#a3a542344967c5c1912bde216559e7cd6a617d1991d70033df3b39eef7ccb98b48)、[SDIO_FUNC_MEMORY](#a3a542344967c5c1912bde216559e7cd6a075731d15b2f4b7c7448d6d4ee059880)。

SDIO 功能编号（Function number）。

<a id="r_a250ae2ce54e941895a720b565632350e"></a>

```c
enum sdio_io_dir { SDIO_IO_READ = 0 , SDIO_IO_WRITE = 1 }
```

相关声明：[sdio_io_dir](#a250ae2ce54e941895a720b565632350e)、[SDIO_IO_READ](#a250ae2ce54e941895a720b565632350eac1212149d096232e75d1d090abb4974c)、[SDIO_IO_WRITE](#a250ae2ce54e941895a720b565632350eabd26fc6f76267231c78eae8be9ebb885)。

SDIO I/O 方向（Direction）。

<a id="r_ac12657ae7d3b8abc562d4d7929a86b65"></a>

```c
enum sdio_cccr_flags { SDIO_SUPPORT_HS = BIT(0) , SDIO_SUPPORT_SDR50 = BIT(1) , SDIO_SUPPORT_SDR104 = BIT(2) , SDIO_SUPPORT_DDR50 = BIT(3) , SDIO_SUPPORT_4BIT_LS_BUS = BIT(4) , SDIO_SUPPORT_MULTIBLOCK = BIT(5) }
```

相关声明：[sdio_cccr_flags](#ac12657ae7d3b8abc562d4d7929a86b65)、[SDIO_SUPPORT_HS](#ac12657ae7d3b8abc562d4d7929a86b65aa23a07a4fe6f6dd8292215221d97d5e2)、[SDIO_SUPPORT_SDR50](#ac12657ae7d3b8abc562d4d7929a86b65acc46ce7f993b3eb81c6a2a2daad84c34)、[SDIO_SUPPORT_SDR104](#ac12657ae7d3b8abc562d4d7929a86b65a9b12d90cd1590f68fc1031449c4560ec)、[SDIO_SUPPORT_DDR50](#ac12657ae7d3b8abc562d4d7929a86b65a6d2084ba4c729c2cb019582b975f652f)、[SDIO_SUPPORT_4BIT_LS_BUS](#ac12657ae7d3b8abc562d4d7929a86b65a6cd553669599181b3677cea94687f025)、[SDIO_SUPPORT_MULTIBLOCK](#ac12657ae7d3b8abc562d4d7929a86b65a364c7067e73960bae74ed80320adb223)。

卡公共控制寄存器（CCCR）标志。

## 15.4\_详细说明（Detailed Documentation）

<a id="ade9a798f584d431c86e172266394f41e"></a>

### `MMC_EXT_CSD_BYTES`

```c
#define MMC_EXT_CSD_BYTES 512
```

<a id="aed6aacadb061a42993c59d8d69a2f2ab"></a>

### `SD_IF_COND_CHECK`

```c
#define SD_IF_COND_CHECK 0xAA
```

<a id="a38157545a4a10dd4757ad1eb80487c60"></a>

### `SD_IF_COND_VHS_3V3`

```c
#define SD_IF_COND_VHS_3V3 BIT(8)
```

<a id="a0d10fc7ae53b5bfb6d7f448844820799"></a>

### `SD_IF_COND_VHS_MASK`

```c
#define SD_IF_COND_VHS_MASK (0x0F << 8)
```

<a id="a947520a05fc99c25449fab98d0d02b1e"></a>

### `SD_PRODUCT_NAME_BYTES`

```c
#define SD_PRODUCT_NAME_BYTES 5
```

<a id="ac104a7c39f61829092eaffd98663045b"></a>

### `SD_R1_CURRENT_STATE`

```c
#define SD_R1_CURRENT_STATE ( x)
```

展开值（Value）：

```c
(((x) & SD_R1_CUR_STATE) >> 9U)
```

<a id="a2d1dee775c3849a92dac9d179bd50a6c"></a>

### `SD_SPI_CMD`

```c
#define SD_SPI_CMD 0x3F
```

<a id="a85e46f60c0ae5f21a4386009bbfaf0a3"></a>

### `SD_SPI_CMD_BODY_SIZE`

```c
#define SD_SPI_CMD_BODY_SIZE (SD_SPI_CMD_SIZE - 1)
```

<a id="aa841b78f5937f8499918cc977a36e90f"></a>

### `SD_SPI_CMD_SIZE`

```c
#define SD_SPI_CMD_SIZE 6
```

<a id="aed67a9adbb001dad73eec4054ef6cbc1"></a>

### `SD_SPI_CRC16_SIZE`

```c
#define SD_SPI_CRC16_SIZE 2
```

<a id="a5d36df2e0d1bd88aadc3673cdf12aea7"></a>

### `SD_SPI_RESPONSE_ACCEPTED`

```c
#define SD_SPI_RESPONSE_ACCEPTED 0x05
```

<a id="a3a206f684b2c878f59a394b06abd9814"></a>

### `SD_SPI_RESPONSE_CRC_ERR`

```c
#define SD_SPI_RESPONSE_CRC_ERR 0x0B
```

<a id="a498f76218e054dff0e524a83ac90ccd1"></a>

### `SD_SPI_RESPONSE_WRITE_ERR`

```c
#define SD_SPI_RESPONSE_WRITE_ERR 0x0C
```

<a id="a7da6535d451c1062f8d0c92f5688e178"></a>

### `SD_SPI_START`

```c
#define SD_SPI_START 0x80
```

<a id="ae34cf95537f2c0963ade18f1ba5d6e20"></a>

### `SD_SPI_TOKEN_MULTI_WRITE`

```c
#define SD_SPI_TOKEN_MULTI_WRITE 0xFC
```

<a id="a7cd4fbf7d5ce2e8eba8c795a675486bb"></a>

### `SD_SPI_TOKEN_SINGLE`

```c
#define SD_SPI_TOKEN_SINGLE 0xFE
```

<a id="a9d4f357ff29ee3b5483505404ba3c956"></a>

### `SD_SPI_TOKEN_STOP_TRAN`

```c
#define SD_SPI_TOKEN_STOP_TRAN 0xFD
```

<a id="a2283409131ac9ede90773b256094b74c"></a>

### `SD_SPI_TX`

```c
#define SD_SPI_TX 0x40
```

<a id="a7e061818bc8f923d5342c38721a1a501"></a>

### `SDIO_CCCR_ABORT`

```c
#define SDIO_CCCR_ABORT 0x06
```

SDIO I/O 中止寄存器（IO abort register）。

<a id="a283f2b2f2c28b3c8208f3d6aca3ca3d2"></a>

### `SDIO_CCCR_BUS_IF`

```c
#define SDIO_CCCR_BUS_IF 0x07
```

SDIO 总线接口控制寄存器（Bus interface control register）。

<a id="aec58e3fcda2f792266fbd8ab1b75f98c"></a>

### `SDIO_CCCR_BUS_IF_WIDTH_1_BIT`

```c
#define SDIO_CCCR_BUS_IF_WIDTH_1_BIT 0x00
```

1 位 SDIO 总线设置。

<a id="aeb23fa771a16f69fcb9d97b156f25ade"></a>

### `SDIO_CCCR_BUS_IF_WIDTH_4_BIT`

```c
#define SDIO_CCCR_BUS_IF_WIDTH_4_BIT 0x02
```

4 位 SDIO 总线设置。

<a id="ade7a14837ee90c8ce24959926d81eaee"></a>

### `SDIO_CCCR_BUS_IF_WIDTH_8_BIT`

```c
#define SDIO_CCCR_BUS_IF_WIDTH_8_BIT 0x03
```

8 位 SDIO 总线设置。

<a id="a6c04dc28d7f39fda7cd0181421a13ea0"></a>

### `SDIO_CCCR_BUS_IF_WIDTH_MASK`

```c
#define SDIO_CCCR_BUS_IF_WIDTH_MASK 0x3
```

SDIO 总线宽度设置掩码。

<a id="a0b878d7e794d3edd127c3f08633efbbc"></a>

### `SDIO_CCCR_CAPS`

```c
#define SDIO_CCCR_CAPS 0x08
```

SDIO 卡能力（Card capabilities）。

<a id="a7ba2dcf801f81ab53b418e59441000ae"></a>

### `SDIO_CCCR_CAPS_BLS`

```c
#define SDIO_CCCR_CAPS_BLS BIT(7)
```

支持 4 位总线的低速卡。

<a id="aa8281a65d0865fba8b85d91d00b90091"></a>

### `SDIO_CCCR_CAPS_E4MI`

```c
#define SDIO_CCCR_CAPS_E4MI BIT(5)
```

启用块间隙中断。

<a id="aee93278e3c0ec4cbf0e3065d6a58f516"></a>

### `SDIO_CCCR_CAPS_LSC`

```c
#define SDIO_CCCR_CAPS_LSC BIT(6)
```

低速卡（Low speed card）。

<a id="a74082cfafdd9e8bfa37e92624ff75e80"></a>

### `SDIO_CCCR_CAPS_S4MI`

```c
#define SDIO_CCCR_CAPS_S4MI BIT(4)
```

支持块间隙中断（Block gap interrupt）。

<a id="a7550fe8aab011fc87baeb575463e27d9"></a>

### `SDIO_CCCR_CAPS_SBS`

```c
#define SDIO_CCCR_CAPS_SBS BIT(3)
```

支持总线控制。

<a id="affb9533b340f5424c1f42445c6f1002f"></a>

### `SDIO_CCCR_CAPS_SDC`

```c
#define SDIO_CCCR_CAPS_SDC BIT(0)
```

支持在数据传输期间执行 `CMD52`。

<a id="aaaf8d335a8d025b998feeb93c0899a99"></a>

### `SDIO_CCCR_CAPS_SMB`

```c
#define SDIO_CCCR_CAPS_SMB BIT(1)
```

支持多块传输（Multiple block transfer）。

<a id="a8011927f7b565304ec31a7e61d403d6e"></a>

### `SDIO_CCCR_CAPS_SRW`

```c
#define SDIO_CCCR_CAPS_SRW BIT(2)
```

支持读取等待控制（Read wait control）。

<a id="ae211fa0bfa6809273b5f7267c95ce681"></a>

### `SDIO_CCCR_CCCR`

```c
#define SDIO_CCCR_CCCR 0x00
```

卡公共控制寄存器（Card Common Control Register，CCCR）定义。

所有 SDIO 卡都具有卡公共控制寄存器；此处为 SDIO CCCR 修订版本寄存器（Revision register）。

<a id="ab240215a68f23ec69e901c0666b0dfe0"></a>

### `SDIO_CCCR_CCCR_REV_1_00`

```c
#define SDIO_CCCR_CCCR_REV_1_00 0x0
```

CCCR/功能基本寄存器（FBR）版本 1.00。

<a id="aace4672360d77085bec93b52e3ac05d9"></a>

### `SDIO_CCCR_CCCR_REV_1_10`

```c
#define SDIO_CCCR_CCCR_REV_1_10 0x1
```

CCCR/FBR 版本 1.10。

<a id="a566200e9322e8e4c9b3edd21a2ced93c"></a>

### `SDIO_CCCR_CCCR_REV_2_00`

```c
#define SDIO_CCCR_CCCR_REV_2_00 0x2
```

CCCR/FBR 版本 2.00。

<a id="aa90600f74ff69315e38ed1c10a3cde7c"></a>

### `SDIO_CCCR_CCCR_REV_3_00`

```c
#define SDIO_CCCR_CCCR_REV_3_00 0x3
```

CCCR/FBR 版本 3.00。

<a id="accf473b0fcdc9e1e03329f91e588de1a"></a>

### `SDIO_CCCR_CCCR_REV_MASK`

```c
#define SDIO_CCCR_CCCR_REV_MASK 0x0F
```

<a id="af5db599ebd0748528e8369653a5e3929"></a>

### `SDIO_CCCR_CCCR_REV_SHIFT`

```c
#define SDIO_CCCR_CCCR_REV_SHIFT 0x0
```

<a id="a8f97c16c091bd19b545bbe452581dfff"></a>

### `SDIO_CCCR_CIS`

```c
#define SDIO_CCCR_CIS 0x09
```

SDIO 卡信息结构（CIS）元组指针。

<a id="a3a5d01e688b18109ad2f19bc5d017f26"></a>

### `SDIO_CCCR_DRIVE_STRENGTH`

```c
#define SDIO_CCCR_DRIVE_STRENGTH 0x15
```

SDIO 驱动强度（Drive strength）。

<a id="a759a9dddc3aa08d0f11114637c5b69ff"></a>

### `SDIO_CCCR_DRIVE_STRENGTH_A`

```c
#define SDIO_CCCR_DRIVE_STRENGTH_A BIT(0)
```

A 型驱动（Drive type A）。

<a id="a8487f5a0a97e5f1f72500cf44cec89dc"></a>

### `SDIO_CCCR_DRIVE_STRENGTH_C`

```c
#define SDIO_CCCR_DRIVE_STRENGTH_C BIT(1)
```

C 型驱动（Drive type C）。

<a id="abc1ed41094d9cdd300b1b3712bb082b2"></a>

### `SDIO_CCCR_DRIVE_STRENGTH_D`

```c
#define SDIO_CCCR_DRIVE_STRENGTH_D BIT(2)
```

D 型驱动（Drive type D）。

<a id="a15caca2936186b54c330b4a9050c9795"></a>

### `SDIO_CCCR_INT_EN`

```c
#define SDIO_CCCR_INT_EN 0x04
```

SDIO 中断使能寄存器（Interrupt enable register）。

<a id="a81b7523a76a1826a14c2cc1c242a49a9"></a>

### `SDIO_CCCR_INT_P`

```c
#define SDIO_CCCR_INT_P 0x05
```

SDIO 中断挂起寄存器（Interrupt pending register）。

<a id="a0b2103011690e1d3f1daef4e45a11986"></a>

### `SDIO_CCCR_IO_EN`

```c
#define SDIO_CCCR_IO_EN 0x02
```

SDIO I/O 使能寄存器（IO Enable register）。

<a id="a6cfa2671e574650e6f35a65828cd459c"></a>

### `SDIO_CCCR_IO_RD`

```c
#define SDIO_CCCR_IO_RD 0x03
```

SDIO I/O 就绪寄存器（IO Ready register）。

<a id="aafc2b0c434dff4a0903e4910181f9e81"></a>

### `SDIO_CCCR_SD`

```c
#define SDIO_CCCR_SD 0x01
```

SD 规范版本寄存器。

<a id="aa425236b097f44a9721e7aedd203ff90"></a>

### `SDIO_CCCR_SD_SPEC_MASK`

```c
#define SDIO_CCCR_SD_SPEC_MASK 0x0F
```

<a id="a223defa20d223655d215065b222a6767"></a>

### `SDIO_CCCR_SD_SPEC_SHIFT`

```c
#define SDIO_CCCR_SD_SPEC_SHIFT 0x0
```

<a id="a05edbcb4a98831cbeac509f26e881de8"></a>

### `SDIO_CCCR_SPEED`

```c
#define SDIO_CCCR_SPEED 0x13
```

SDIO 总线速度选择（Bus speed select）。

<a id="ad3dc3009d2d78a6306c3247ab85ef48d"></a>

### `SDIO_CCCR_SPEED_DDR50`

```c
#define SDIO_CCCR_SPEED_DDR50 0x4
```

选择 DDR50。

<a id="acb3bdd73bace425a94a357a2f0bff4ef"></a>

### `SDIO_CCCR_SPEED_HS`

```c
#define SDIO_CCCR_SPEED_HS 0x1
```

选择高速模式（High speed mode）。

<a id="a1a1817554f886a999484e2663432cd8b"></a>

### `SDIO_CCCR_SPEED_MASK`

```c
#define SDIO_CCCR_SPEED_MASK 0xE
```

总线速度选择掩码。

<a id="a0d51f98d56303dd55177245785748158"></a>

### `SDIO_CCCR_SPEED_SDR104`

```c
#define SDIO_CCCR_SPEED_SDR104 0x3
```

选择 SDR104。

<a id="a9ee7aec8589aceb8555917971ab9afd3"></a>

### `SDIO_CCCR_SPEED_SDR12`

```c
#define SDIO_CCCR_SPEED_SDR12 0x0
```

选择 SDR12。

<a id="afabf4bb10bed3295d1d051c113e61545"></a>

### `SDIO_CCCR_SPEED_SDR25`

```c
#define SDIO_CCCR_SPEED_SDR25 0x1
```

选择 SDR25。

<a id="a81bc96279a19618c9212674757abd141"></a>

### `SDIO_CCCR_SPEED_SDR50`

```c
#define SDIO_CCCR_SPEED_SDR50 0x2
```

选择 SDR50。

<a id="a38d57134d99e2dfc5760fcf7312b6cd5"></a>

### `SDIO_CCCR_SPEED_SHIFT`

```c
#define SDIO_CCCR_SPEED_SHIFT 0x1
```

总线速度选择字段的移位量。

<a id="a964759dc76bd2a9f9f9dce5c21dc2cb4"></a>

### `SDIO_CCCR_SPEED_SHS`

```c
#define SDIO_CCCR_SPEED_SHS BIT(0)
```

是否支持高速模式（High speed）。

<a id="afb72ff0aa5b90446db296af16bf9bb02"></a>

### `SDIO_CCCR_UHS`

```c
#define SDIO_CCCR_UHS 0x14
```

SDIO 超高速（UHS）支持。

<a id="a2678ede1ac974a9670fdcaa393682aa6"></a>

### `SDIO_CCCR_UHS_DDR50`

```c
#define SDIO_CCCR_UHS_DDR50 BIT(2)
```

是否支持 DDR50。

<a id="aca4fee68fdf3480ec8cf7de7b46a8d4e"></a>

### `SDIO_CCCR_UHS_SDR104`

```c
#define SDIO_CCCR_UHS_SDR104 BIT(1)
```

是否支持 SDR104。

<a id="a9965d399115bca8574a9beaeac9b9f31"></a>

### `SDIO_CCCR_UHS_SDR50`

```c
#define SDIO_CCCR_UHS_SDR50 BIT(0)
```

是否支持 SDR50。

<a id="acd6e41030a8d16419cc22adf9f0a5509"></a>

### `SDIO_CMD_ARG_FUNC_NUM_SHIFT`

```c
#define SDIO_CMD_ARG_FUNC_NUM_SHIFT 28
```

功能编号的移位量。

<a id="a338e9606baa6937e0887e7a9b9372c23"></a>

### `SDIO_CMD_ARG_REG_ADDR_MASK`

```c
#define SDIO_CMD_ARG_REG_ADDR_MASK 0x1FFFF
```

直接访问的寄存器地址掩码（Mask）。

<a id="aa74dbe588f1f5ca248cf0f5a2e8e8c81"></a>

### `SDIO_CMD_ARG_REG_ADDR_SHIFT`

```c
#define SDIO_CMD_ARG_REG_ADDR_SHIFT 9
```

直接访问的寄存器地址移位量。

<a id="a960ade30c404ebb08769c5870ac21b37"></a>

### `SDIO_CMD_ARG_RW_SHIFT`

```c
#define SDIO_CMD_ARG_RW_SHIFT 31
```

读写标志的移位量（Shift）。

<a id="afadddcc143b78325505a40544c04e3b0"></a>

### `SDIO_DIRECT_CMD_ARG_RAW_SHIFT`

```c
#define SDIO_DIRECT_CMD_ARG_RAW_SHIFT 27
```

直接访问的 RAW 标志移位量。

<a id="a5ab9e1e0c96e7166b1ff7a208f90001d"></a>

### `SDIO_DIRECT_CMD_DATA_MASK`

```c
#define SDIO_DIRECT_CMD_DATA_MASK 0xFF
```

数据掩码。

<a id="ac6c49ad6118debe7a9e64f412e597f22"></a>

### `SDIO_EXTEND_CMD_ARG_BLK_SHIFT`

```c
#define SDIO_EXTEND_CMD_ARG_BLK_SHIFT 27
```

扩展写入的块模式（Block mode）。

<a id="a73ca83a4884f13fa5de8500f69252bef"></a>

### `SDIO_EXTEND_CMD_ARG_OP_CODE_SHIFT`

```c
#define SDIO_EXTEND_CMD_ARG_OP_CODE_SHIFT 26
```

操作码：地址递增（Increment address）。

<a id="a2ff95d19f7f60ce33b17b69e2672e7e5"></a>

### `SDIO_FBR_BASE`

```c
#define SDIO_FBR_BASE ( n)
```

展开值（Value）：

```c
((n) * 0x100)
```

获取功能基本寄存器（Function Basic Register）的地址。

<a id="af1885023615980d5cbb930538cc201a6"></a>

### `SDIO_FBR_BLK_SIZE`

```c
#define SDIO_FBR_BLK_SIZE 0x10
```

SDIO 功能基本寄存器中的块大小。

<a id="aea0ed052a9d94d2e2b96931752975858"></a>

### `SDIO_FBR_CIS`

```c
#define SDIO_FBR_CIS 0x09
```

SDIO 功能基本寄存器中的 CIS 指针。

<a id="a28fb27484353eb075d501b1ad7a76112"></a>

### `SDIO_FBR_CSA`

```c
#define SDIO_FBR_CSA 0x0C
```

SDIO 功能基本寄存器中的代码存储区（CSA）指针。

<a id="a0d98fd7cd6f67b28981c6e01f8805a01"></a>

### `SDIO_IO_OCR_MASK`

```c
#define SDIO_IO_OCR_MASK 0xFFFFFF
```

<a id="a845866f4f88c280f8414b727e0d77edf"></a>

### `SDIO_MAX_IO_NUMS`

```c
#define SDIO_MAX_IO_NUMS 7
```

SDIO 的最大 I/O 功能数。

<a id="a23690672048afbc75ce2c2f4d9a74144"></a>

### `SDIO_OCR_IO_NUMBER_SHIFT`

```c
#define SDIO_OCR_IO_NUMBER_SHIFT 28
```

<a id="a21e0771f38a22f93c9f4167d8b36f608"></a>

### `SDIO_TPL_CODE_END`

```c
#define SDIO_TPL_CODE_END 0xFF
```

结束（End）CIS 元组代码。

<a id="ac263bf61bcc750880bae34dde62d61e4"></a>

### `SDIO_TPL_CODE_FUNCE`

```c
#define SDIO_TPL_CODE_FUNCE 0x22
```

功能扩展（Function extension）的 CIS 元组代码。

<a id="aae6f9377eccdbd5866f1a393e083c5e4"></a>

### `SDIO_TPL_CODE_FUNCID`

```c
#define SDIO_TPL_CODE_FUNCID 0x21
```

功能 ID 的 CIS 元组代码。

<a id="af1983253320b45a2a1a2aab28c09e08f"></a>

### `SDIO_TPL_CODE_MANIFID`

```c
#define SDIO_TPL_CODE_MANIFID 0x20
```

制造商 ID 的 CIS 元组代码。

<a id="afadae8a1db38d93b909b3f2c5b0e0110"></a>

### `SDIO_TPL_CODE_NULL`

```c
#define SDIO_TPL_CODE_NULL 0x00
```

空（NULL）CIS 元组代码。

<a id="a523a28eeec3d0a71f0d7ca49ab397960"></a>

### `SDMMC_DEFAULT_BLOCK_SIZE`

```c
#define SDMMC_DEFAULT_BLOCK_SIZE 512
```

<a id="a2093143614e52f69e173289391d7e91c"></a>

### `hs_max_data_rate`

```c
enum hs_max_data_rate
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HS_UNSUPPORTED` |  |
| `HS_MAX_DTR` |  |

<a id="a313c45576db4ae219288fb4fbaad4bd8"></a>

### `mmc_csd_freq`

```c
enum mmc_csd_freq
```

MMC 最高频率（Maximum Frequency）。

MMC CSD 中的最高频率。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MMC_MAXFREQ_100KHZ` |  |
| `MMC_MAXFREQ_1MHZ` |  |
| `MMC_MAXFREQ_10MHZ` |  |
| `MMC_MAXFREQ_100MHZ` |  |
| `MMC_MAXFREQ_MULT_10` |  |
| `MMC_MAXFREQ_MULT_12` |  |
| `MMC_MAXFREQ_MULT_13` |  |
| `MMC_MAXFREQ_MULT_15` |  |
| `MMC_MAXFREQ_MULT_20` |  |
| `MMC_MAXFREQ_MULT_26` |  |
| `MMC_MAXFREQ_MULT_30` |  |
| `MMC_MAXFREQ_MULT_35` |  |
| `MMC_MAXFREQ_MULT_40` |  |
| `MMC_MAXFREQ_MULT_45` |  |
| `MMC_MAXFREQ_MULT_52` |  |
| `MMC_MAXFREQ_MULT_55` |  |
| `MMC_MAXFREQ_MULT_60` |  |
| `MMC_MAXFREQ_MULT_70` |  |
| `MMC_MAXFREQ_MULT_80` |  |

<a id="af9783799f316cbaed12e18ce9944b09d"></a>

### `mmc_driver_strengths`

```c
enum mmc_driver_strengths
```

MMC 驱动强度（Driver Strengths）。

编码在 `EXT_CSD` 中。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `mmc_driv_type0` |  |
| `mmc_driv_type1` |  |
| `mmc_driv_type2` |  |
| `mmc_driv_type3` |  |
| `mmc_driv_type4` |  |

<a id="ac86d8a44f37c771cb666f69a516dff81"></a>

### `mmc_ext_csd_rev`

```c
enum mmc_ext_csd_rev
```

CSD 修订版本（Revision）。

`EXT_CSD` 中的 CSD 修订版本值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MMC_5_1` |  |
| `MMC_5_0` |  |
| `MMC_4_5` |  |
| `MMC_4_4` |  |
| `MMC_4_3` |  |
| `MMC_4_2` |  |
| `MMC_4_1` |  |
| `MMC_4_0` |  |

<a id="a0769bcc2f15d43383f4e5a6c845c51aa"></a>

### `mmc_ocr_flag`

```c
enum mmc_ocr_flag
```

MMC OCR 位标志。

MMC OCR 响应中的位标志，用于确定 MMC 卡的状态及支持的功能。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MMC_OCR_VDD170_195FLAG` |  |
| `MMC_OCR_VDD20_26FLAG` |  |
| `MMC_OCR_VDD27_36FLAG` |  |
| `MMC_OCR_SECTOR_MODE` |  |
| `MMC_OCR_PWR_BUSY_FLAG` |  |

<a id="ae1956c4b374e2c8b6a585596e93ac345"></a>

### `mmc_timing_mode`

```c
enum mmc_timing_mode
```

MMC 时序模式（Timing Modes）。

MMC 时序模式，编码在 `EXT_CSD` 中。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MMC_LEGACY_TIMING` |  |
| `MMC_HS_TIMING` |  |
| `MMC_HS200_TIMING` |  |
| `MMC_HS400_TIMING` |  |

<a id="a1c77191f9cb8c50e8e2a03cda2984dbc"></a>

### `sd_app_cmd`

```c
enum sd_app_cmd
```

SD 应用命令操作码（Application command opcodes）。

所有应用命令操作码之前都必须先发送 `CMD55`，告知 SD 卡下一条命令是应用专用命令。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_APP_SET_BUS_WIDTH` |  |
| `SD_APP_SEND_STATUS` |  |
| `SD_APP_SEND_NUM_WRITTEN_BLK` |  |
| `SD_APP_SET_WRITE_BLK_ERASE_CNT` |  |
| `SD_APP_SEND_OP_COND` |  |
| `SD_APP_CLEAR_CARD_DETECT` |  |
| `SD_APP_SEND_SCR` |  |

<a id="a6b42b86d8f2ba4f29787c7c6f3d97f36"></a>

### `sd_bus_speed`

```c
enum sd_bus_speed
```

SD 总线速度支持位标志。

表示所支持 SD 总线速度的位标志，由卡在 `CMD6` 响应中提供。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UHS_SDR12_BUS_SPEED` |  |
| `DEFAULT_BUS_SPEED` |  |
| `HIGH_SPEED_BUS_SPEED` |  |
| `UHS_SDR25_BUS_SPEED` |  |
| `UHS_SDR50_BUS_SPEED` |  |
| `UHS_SDR104_BUS_SPEED` |  |
| `UHS_DDR50_BUS_SPEED` |  |

<a id="a98c4f218acfa21e124aa22e9fe209437"></a>

### `sd_csd_flag`

```c
enum sd_csd_flag
```

SD 卡专用数据（Card Specific Data）标志。

解码 SD 卡专用数据寄存器时使用的标志。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_CSD_READ_BLK_PARTIAL_FLAG` | 允许读取部分块（Partial blocks for read allowed）`[79:79]`。 |
| `SD_CSD_WRITE_BLK_MISALIGN_FLAG` | 写入块不对齐（Write block misalignment）`[78:78]`。 |
| `SD_CSD_READ_BLK_MISALIGN_FLAG` | 读取块不对齐（Read block misalignment）`[77:77]`。 |
| `SD_CSD_DSR_IMPLEMENTED_FLAG` | 实现了驱动级寄存器（DSR）`[76:76]`。 |
| `SD_CSD_ERASE_BLK_EN_FLAG` | 启用单块擦除（Erase single block enabled）`[46:46]`。 |
| `SD_CSD_WRITE_PROTECT_GRP_EN_FLAG` | 启用写保护组（Write protect group enabled）`[31:31]`。 |
| `SD_CSD_WRITE_BLK_PARTIAL_FLAG` | 允许写入部分块（Partial blocks for write allowed）`[21:21]`。 |
| `SD_CSD_FILE_FMT_GRP_FLAG` | 文件格式组（File format group）`[15:15]`。 |
| `SD_CSD_COPY_FLAG` | 复制标志（Copy flag）`[14:14]`。 |
| `SD_CSD_PERMANENT_WRITE_PROTECT_FLAG` | 永久写保护（Permanent write protection）`[13:13]`。 |
| `SD_CSD_TMP_WRITE_PROTECT_FLAG` | 临时写保护（Temporary write protection）`[12:12]`。 |

<a id="a238de48c0cb55d173b6b874f4930c537"></a>

### `sd_current_limit`

```c
enum sd_current_limit
```

SD 电流支持位域。

与 `CMD6` 配合使用，确定卡将消耗的最大电流。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_MAX_CURRENT_200MA` | 默认电流限制（Current limit）。 |
| `SD_MAX_CURRENT_400MA` | 电流限制为 400 mA。 |
| `SD_MAX_CURRENT_600MA` | 电流限制为 600 mA。 |
| `SD_MAX_CURRENT_800MA` | 电流限制为 800 mA。 |

<a id="a5ac0e70389dc6ccec515530df4eab972"></a>

### `sd_current_setting`

```c
enum sd_current_setting
```

SD 电流设置值。

与 `CMD6` 配合使用，告知卡其最大允许耗流。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_SET_CURRENT_200MA` |  |
| `SD_SET_CURRENT_400MA` |  |
| `SD_SET_CURRENT_600MA` |  |
| `SD_SET_CURRENT_800MA` |  |

<a id="a66c69cd7d7818af86b6a91fad68334c2"></a>

### `sd_driver_strength`

```c
enum sd_driver_strength
```

SD 切换驱动类型选择。

这些值用于选择 SD 卡的首选驱动类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_DRV_STRENGTH_TYPEB` | 默认驱动强度。 |
| `SD_DRV_STRENGTH_TYPEA` | A 型驱动强度（TYPE A）。 |
| `SD_DRV_STRENGTH_TYPEC` | C 型驱动强度（TYPE C）。 |
| `SD_DRV_STRENGTH_TYPED` | D 型驱动强度（TYPE D）。 |

<a id="a314c38b1b0603c003e67b5dec2228d4b"></a>

### `sd_driver_type`

```c
enum sd_driver_type
```

SD 驱动类型（Driver types）。

与 `CMD6` 配合使用，确定卡应使用的驱动类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_DRIVER_TYPE_B` |  |
| `SD_DRIVER_TYPE_A` |  |
| `SD_DRIVER_TYPE_C` |  |
| `SD_DRIVER_TYPE_D` |  |

<a id="a97f4810585247f5fed41110413e49853"></a>

### `sd_group_num`

```c
enum sd_group_num
```

SD 切换功能组编号（Switch group numbers）。

SD `CMD6` 可以检查或设置多个功能组（Function groups）。这些索引用于确定 `CMD6` 要访问的功能组。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_GRP_TIMING_MODE` | 访问模式组（Access mode group）。 |
| `SD_GRP_CMD_SYS_MODE` | 命令系统组（Command system group）。 |
| `SD_GRP_DRIVER_STRENGTH_MODE` | 驱动强度组（Driver strength group）。 |
| `SD_GRP_CURRENT_LIMIT_MODE` | 电流限制组（Current limit group）。 |

<a id="a7b20cc85df2d9f5ce6c010907d7d5c61"></a>

### `sd_ocr_flag`

```c
enum sd_ocr_flag
```

SD 操作条件寄存器（OCR）的位标志。

SD OCR 响应中的位标志，用于确定 SD 卡的状态及支持的功能。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_OCR_PWR_BUSY_FLAG` | 上电忙状态（Power up busy status）。 |
| `SD_OCR_HOST_CAP_FLAG` | 卡容量状态（Card capacity status）。 |
| `SD_OCR_CARD_CAP_FLAG` | 卡容量状态（Card capacity status）。 |
| `SD_OCR_SWITCH_18_REQ_FLAG` | 请求切换至 1.8 V。 |
| `SD_OCR_SWITCH_18_ACCEPT_FLAG` | 已接受切换至 1.8 V 的请求。 |
| `SD_OCR_VDD27_28FLAG` | VDD 电压范围：2.7–2.8 V。 |
| `SD_OCR_VDD28_29FLAG` | VDD 电压范围：2.8–2.9 V。 |
| `SD_OCR_VDD29_30FLAG` | VDD 电压范围：2.9–3.0 V。 |
| `SD_OCR_VDD30_31FLAG` | VDD 电压范围：3.0–3.1 V。 |
| `SD_OCR_VDD31_32FLAG` | VDD 电压范围：3.1–3.2 V。 |
| `SD_OCR_VDD32_33FLAG` | VDD 电压范围：3.2–3.3 V。 |
| `SD_OCR_VDD33_34FLAG` | VDD 电压范围：3.3–3.4 V。 |
| `SD_OCR_VDD34_35FLAG` | VDD 电压范围：3.4–3.5 V。 |
| `SD_OCR_VDD35_36FLAG` | VDD 电压范围：3.5–3.6 V。 |

<a id="a072705601a34c697515f74acb0474c99"></a>

### `sd_opcode`

```c
enum sd_opcode
```

SD 规范命令操作码（Command opcodes）。

SD 规范命令操作码。注意：某些命令操作码仅适用于 SDIO 卡，或仅适用于以 SPI 模式而非原生 SD 模式运行的卡。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_GO_IDLE_STATE` |  |
| `MMC_SEND_OP_COND` |  |
| `SD_ALL_SEND_CID` |  |
| `SD_SEND_RELATIVE_ADDR` |  |
| `MMC_SEND_RELATIVE_ADDR` |  |
| `SDIO_SEND_OP_COND` |  |
| `SD_SWITCH` |  |
| `SD_SELECT_CARD` |  |
| `SD_SEND_IF_COND` |  |
| `MMC_SEND_EXT_CSD` |  |
| `SD_SEND_CSD` |  |
| `SD_SEND_CID` |  |
| `SD_VOL_SWITCH` |  |
| `SD_STOP_TRANSMISSION` |  |
| `SD_SEND_STATUS` |  |
| `MMC_CHECK_BUS_TEST` |  |
| `SD_GO_INACTIVE_STATE` |  |
| `SD_SET_BLOCK_SIZE` |  |
| `SD_READ_SINGLE_BLOCK` |  |
| `SD_READ_MULTIPLE_BLOCK` |  |
| `SD_SEND_TUNING_BLOCK` |  |
| `MMC_SEND_BUS_TEST` |  |
| `MMC_SEND_TUNING_BLOCK` |  |
| `SD_SET_BLOCK_COUNT` |  |
| `SD_WRITE_SINGLE_BLOCK` |  |
| `SD_WRITE_MULTIPLE_BLOCK` |  |
| `SD_ERASE_BLOCK_START` |  |
| `SD_ERASE_BLOCK_END` |  |
| `SD_ERASE_BLOCK_OPERATION` |  |
| `SDIO_RW_DIRECT` |  |
| `SDIO_RW_EXTENDED` |  |
| `SD_APP_CMD` |  |
| `SD_SPI_READ_OCR` |  |
| `SD_SPI_CRC_ON_OFF` |  |

<a id="aa0686c333989b0551d3af5eb01de4065"></a>

### `sd_r1_current_state`

```c
enum sd_r1_current_state
```

SD 当前状态值。

SD 当前状态值，包含在 R1 响应数据中。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SDMMC_R1_IDLE` |  |
| `SDMMC_R1_READY` |  |
| `SDMMC_R1_IDENTIFY` |  |
| `SDMMC_R1_STANDBY` |  |
| `SDMMC_R1_TRANSFER` |  |
| `SDMMC_R1_SEND_DATA` |  |
| `SDMMC_R1_RECIVE_DATA` |  |
| `SDMMC_R1_PROGRAM` |  |
| `SDMMC_R1_DISCONNECT` |  |

<a id="ad38162e32b87d3c01f1ae46d3423155a"></a>

### `sd_r1_status`

```c
enum sd_r1_status
```

原生 SD 模式（Native SD mode）的 R1 响应状态标志。

SD R1 响应的原生响应标志，用于检查命令错误。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_R1_AUTH_ERR` |  |
| `SD_R1_APP_CMD` |  |
| `SD_R1_FX_EVENT` |  |
| `SD_R1_RDY_DATA` |  |
| `SD_R1_CUR_STATE` |  |
| `SD_R1_ERASE_RESET` |  |
| `SD_R1_ECC_DISABLED` |  |
| `SD_R1_ERASE_SKIP` |  |
| `SD_R1_CSD_OVERWRITE` |  |
| `SD_R1_ERR` |  |
| `SD_R1_CC_ERR` |  |
| `SD_R1_ECC_FAIL` |  |
| `SD_R1_ILLEGAL_CMD` |  |
| `SD_R1_CRC_ERR` |  |
| `SD_R1_UNLOCK_FAIL` |  |
| `SD_R1_CARD_LOCKED` |  |
| `SD_R1_WP_VIOLATION` |  |
| `SD_R1_ERASE_PARAM` |  |
| `SD_R1_ERASE_SEQ_ERR` |  |
| `SD_R1_BLOCK_LEN_ERR` |  |
| `SD_R1_ADDR_ERR` |  |
| `SD_R1_OUT_OF_RANGE` |  |
| `SD_R1_ERR_FLAGS` |  |
| `SD_R1ERR_NONE` |  |

<a id="a1cfd2df5ec76eeb915fd3689408a65d6"></a>

### `sd_rsp_type`

```c
enum sd_rsp_type
```

SD 响应类型（Response types）。

SD 响应类型。注意：SPI 模式的响应类型与原生 SD 模式不同。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_RSP_TYPE_NONE` |  |
| `SD_RSP_TYPE_R1` |  |
| `SD_RSP_TYPE_R1b` |  |
| `SD_RSP_TYPE_R2` |  |
| `SD_RSP_TYPE_R3` |  |
| `SD_RSP_TYPE_R4` |  |
| `SD_RSP_TYPE_R5` |  |
| `SD_RSP_TYPE_R5b` |  |
| `SD_RSP_TYPE_R6` |  |
| `SD_RSP_TYPE_R7` |  |
| `SD_SPI_RSP_TYPE_R1` |  |
| `SD_SPI_RSP_TYPE_R1b` |  |
| `SD_SPI_RSP_TYPE_R2` |  |
| `SD_SPI_RSP_TYPE_R3` |  |
| `SD_SPI_RSP_TYPE_R4` |  |
| `SD_SPI_RSP_TYPE_R5` |  |
| `SD_SPI_RSP_TYPE_R7` |  |

<a id="a476ec98763d90a5cba336cbf22d6d553"></a>

### `sd_scr_flag`

```c
enum sd_scr_flag
```

SD卡配置寄存器（Card Configuration Register）。

解码 SD 卡配置寄存器时使用的标志。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_SCR_DATA_STATUS_AFTER_ERASE` | 擦除后的数据状态（Data status after erases）`[55:55]`。 |
| `SD_SCR_SPEC3` | 规范版本为 3.00 或更高 `[47:47]`。 |

<a id="abf77ec1ad65cc9c99dc930ed7a96301a"></a>

### `sd_spec_version`

```c
enum sd_spec_version
```

SD 规范版本。

解码 SD 卡配置寄存器时使用的 SD 规范版本标志。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_SPEC_VER1_0` | SD 卡版本 1.0–1.01。 |
| `SD_SPEC_VER1_1` | SD 卡版本 1.10。 |
| `SD_SPEC_VER2_0` | SD 卡版本 2.00。 |
| `SD_SPEC_VER3_0` | SD 卡版本 3.0。 |

<a id="aaf06bb2dcb6e359e08bae37d2f36bbc3"></a>

### `sd_spi_r1_error_flag`

```c
enum sd_spi_r1_error_flag
```

SPI SD 模式的 R1 响应状态标志。

SPI 模式 R1 响应标志，用于检查 SD SPI 模式命令中的错误。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_SPI_R1PARAMETER_ERR` |  |
| `SD_SPI_R1ADDRESS_ERR` |  |
| `SD_SPI_R1ERASE_SEQ_ERR` |  |
| `SD_SPI_R1CMD_CRC_ERR` |  |
| `SD_SPI_R1ILLEGAL_CMD_ERR` |  |
| `SD_SPI_R1ERASE_RESET` |  |
| `SD_SPI_R1IDLE_STATE` |  |

<a id="aa1b9e80034c783cc7ff43dc79ac5878f"></a>

### `sd_spi_r2_status`

```c
enum sd_spi_r2_status
```

SPI SD 模式的 R2 响应状态标志。

SPI 模式 R2 响应标志，作为 `SEND_STATUS` 命令的响应发送，用于检查 SD 卡状态。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SDHC_SPI_R2_CARD_LOCKED` |  |
| `SDHC_SPI_R2_UNLOCK_FAIL` |  |
| `SDHC_SPI_R2_ERR` |  |
| `SDHC_SPI_R2_CC_ERR` |  |
| `SDHC_SPI_R2_ECC_FAIL` |  |
| `SDHC_SPI_R2_WP_VIOLATION` |  |
| `SDHC_SPI_R2_ERASE_PARAM` |  |
| `SDHC_SPI_R2_OUT_OF_RANGE` |  |

<a id="afeec7c838fcf2d5c01cf653e305c749a"></a>

### `sd_support_flag`

```c
enum sd_support_flag
```

SD 支持标志。

SD 子系统用于确定卡功能支持情况的标志。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_HIGH_CAPACITY_FLAG` |  |
| `SD_4BITS_WIDTH` |  |
| `SD_SDHC_FLAG` |  |
| `SD_SDXC_FLAG` |  |
| `SD_1800MV_FLAG` |  |
| `SD_3000MV_FLAG` |  |
| `SD_CMD23_FLAG` |  |
| `SD_SPEED_CLASS_CONTROL_FLAG` |  |
| `SD_MEM_PRESENT_FLAG` |  |

<a id="a76f7ea4b395028ad5d8cc5eee32656e3"></a>

### `sd_switch_arg`

```c
enum sd_switch_arg
```

SD 切换参数（Switch arguments）。

SD `CMD6` 可以检查或设置功能。检查功能时使用位域表示功能支持情况；设置功能时使用整数值选择该功能。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_SWITCH_CHECK` | SD 切换模式 0：检查功能（Check function）。 |
| `SD_SWITCH_SET` | SD 切换模式 1：设置功能（Set function）。 |

<a id="ae82da8038d71cf36ce2237504b498930"></a>

### `sd_timing_mode`

```c
enum sd_timing_mode
```

SD 时序模式（Timing mode）的功能选择值。

通过 `CMD6` 发送给卡以选择卡速度，同时供 SD 主机控制器识别卡的时序。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_TIMING_DEFAULT` | 默认模式（Default Mode）。 |
| `SD_TIMING_SDR12` | SDR12 模式。 |
| `SD_TIMING_HIGH_SPEED` | 高速模式（High speed mode）。 |
| `SD_TIMING_SDR25` | SDR25 模式。 |
| `SD_TIMING_SDR50` | SDR50 模式。 |
| `SD_TIMING_SDR104` | SDR104 模式。 |
| `SD_TIMING_DDR50` | DDR50 模式。 |

<a id="a9660a61775e481ae4093e11ce9336539"></a>

### `sdhc_clock_speed`

```c
enum sdhc_clock_speed
```

SD 主机控制器时钟速度。

控制 SD 主机控制器在 SD 总线上的时钟速度。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SDMMC_CLOCK_400KHZ` |  |
| `SD_CLOCK_25MHZ` |  |
| `SD_CLOCK_50MHZ` |  |
| `SD_CLOCK_100MHZ` |  |
| `SD_CLOCK_208MHZ` |  |
| `MMC_CLOCK_26MHZ` |  |
| `MMC_CLOCK_52MHZ` |  |
| `MMC_CLOCK_DDR52` |  |
| `MMC_CLOCK_HS200` |  |
| `MMC_CLOCK_HS400` |  |

<a id="ac12657ae7d3b8abc562d4d7929a86b65"></a>

### `sdio_cccr_flags`

```c
enum sdio_cccr_flags
```

卡公共控制寄存器（CCCR）标志。

表示 SDIO 卡所支持能力的标志，从 CCCR 寄存器读取。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SDIO_SUPPORT_HS` |  |
| `SDIO_SUPPORT_SDR50` |  |
| `SDIO_SUPPORT_SDR104` |  |
| `SDIO_SUPPORT_DDR50` |  |
| `SDIO_SUPPORT_4BIT_LS_BUS` |  |
| `SDIO_SUPPORT_MULTIBLOCK` |  |

<a id="a3a542344967c5c1912bde216559e7cd6"></a>

### `sdio_func_num`

```c
enum sdio_func_num
```

SDIO 功能编号（Function number）。

SDIO 功能编号，在对 SDIO 卡执行 I/O 时用于选择功能。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SDIO_FUNC_NUM_0` |  |
| `SDIO_FUNC_NUM_1` |  |
| `SDIO_FUNC_NUM_2` |  |
| `SDIO_FUNC_NUM_3` |  |
| `SDIO_FUNC_NUM_4` |  |
| `SDIO_FUNC_NUM_5` |  |
| `SDIO_FUNC_NUM_6` |  |
| `SDIO_FUNC_NUM_7` |  |
| `SDIO_FUNC_MEMORY` |  |

<a id="a250ae2ce54e941895a720b565632350e"></a>

### `sdio_io_dir`

```c
enum sdio_io_dir
```

SDIO I/O 方向（Direction）。

SDIO I/O 方向：读取或写入。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SDIO_IO_READ` |  |
| `SDIO_IO_WRITE` |  |

<a id="a296cbe236e9e36dc79ca30eb54e6bcc6"></a>

### `sdio_ocr_flag`

```c
enum sdio_ocr_flag
```

SDIO OCR 位标志。

SDIO OCR 响应中的位标志，用于确定 SDIO 卡的状态及支持的功能。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SDIO_OCR_IO_READY_FLAG` |  |
| `SDIO_OCR_IO_NUMBER` | I/O 功能数量。 |
| `SDIO_OCR_MEM_PRESENT_FLAG` | 存在存储器（Memory present）标志。 |
| `SDIO_OCR_180_VOL_FLAG` | 切换至 1.8 V 信号电压。 |
| `SDIO_OCR_VDD20_21FLAG` | VDD 电压范围：2.0–2.1 V。 |
| `SDIO_OCR_VDD21_22FLAG` | VDD 电压范围：2.1–2.2 V。 |
| `SDIO_OCR_VDD22_23FLAG` | VDD 电压范围：2.2–2.3 V。 |
| `SDIO_OCR_VDD23_24FLAG` | VDD 电压范围：2.3–2.4 V。 |
| `SDIO_OCR_VDD24_25FLAG` | VDD 电压范围：2.4–2.5 V。 |
| `SDIO_OCR_VDD25_26FLAG` | VDD 电压范围：2.5–2.6 V。 |
| `SDIO_OCR_VDD26_27FLAG` | VDD 电压范围：2.6–2.7 V。 |
| `SDIO_OCR_VDD27_28FLAG` | VDD 电压范围：2.7–2.8 V。 |
| `SDIO_OCR_VDD28_29FLAG` | VDD 电压范围：2.8–2.9 V。 |
| `SDIO_OCR_VDD29_30FLAG` | VDD 电压范围：2.9–3.0 V。 |
| `SDIO_OCR_VDD30_31FLAG` | VDD 电压范围：2.9–3.0 V。 |
| `SDIO_OCR_VDD31_32FLAG` | VDD 电压范围：3.0–3.1 V。 |
| `SDIO_OCR_VDD32_33FLAG` | VDD 电压范围：3.1–3.2 V。 |
| `SDIO_OCR_VDD33_34FLAG` | VDD 电压范围：3.2–3.3 V。 |
| `SDIO_OCR_VDD34_35FLAG` | VDD 电压范围：3.3–3.4 V。 |
| `SDIO_OCR_VDD35_36FLAG` | VDD 电压范围：3.4–3.5 V。 |

<a id="a5466ef2e30578d03c61831aa09fd7b9a"></a>

### `uhs_max_data_rate`

```c
enum uhs_max_data_rate
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UHS_UNSUPPORTED` |  |
| `UHS_SDR12_MAX_DTR` |  |
| `UHS_SDR25_MAX_DTR` |  |
| `UHS_SDR50_MAX_DTR` |  |
| `UHS_SDR104_MAX_DTR` |  |
| `UHS_DDR50_MAX_DTR` |  |


## 15.5\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h_source.html)
- [sd_switch_caps](../peripheral_bus_storage_model_reference/P078_sd_switch_caps_结构体.md)
- [sd_cid](../peripheral_bus_storage_model_reference/P075_sd_cid_结构体.md)
- [sd_csd](../peripheral_bus_storage_model_reference/P076_sd_csd_结构体.md)
- [mmc_device_type](../peripheral_bus_storage_model_reference/P034_mmc_device_type_结构体.md)
- [mmc_ext_csd](../peripheral_bus_storage_model_reference/P035_mmc_ext_csd_结构体.md)
- [sd_scr](../peripheral_bus_storage_model_reference/P077_sd_scr_结构体.md)
- [sdio_cis](../peripheral_bus_storage_model_reference/P085_sdio_cis_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="asd__spec_8h_html_ad38162e32b87d3c01f1ae46d3423155aa0815a9749fc47ea398752e886e222b65"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a2093143614e52f69e173289391d7e91cac3e8d67442f59c35b57d19d81b5d0d66"></a>
<a id="a2093143614e52f69e173289391d7e91ca10f805e3f66366474428718cb4569da0"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8a221dc45c7b73f6f96a63acbeb3e5e121"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8a32c9f5017cd49c9ca4b352269de6eeff"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8af63af4938d5aad64bac19fac42aedd10"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8a13c703d344a1e03c1aa5881a77980085"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8a74d01430b854f42ea84dba9d3ce45b16"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8a4a3b8dc88c6349fb5f49ed3062a39a17"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8a2c639715b63769e9a431a93e636f007e"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8ac988a54239b7d9e182f1b2f480567e66"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8ac8848c5cdf177737744da3283f7140d5"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8ab1ff3da74a0dea49ffe7ac1d945ec4e6"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8a69e1d369d668d63071410078a31099a0"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8a63c0eee223946b1ae2b187bb585dfde4"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8a572d53afafb39341e0cdb80d2d041d2c"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8a5bd0506d7efbecdc42eb8fae1427dc37"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8a988f18b9f418744721b0fc91f2432449"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8abecfcd6d212185c74b57941c3fa58233"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8adf578325509923b46e3ff4fbd74889ad"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8aee24df1d628479fe2d920839a0bf5012"></a>
<a id="a313c45576db4ae219288fb4fbaad4bd8a24ea8c9db5531b5404bb667da26ac5d0"></a>
<a id="af9783799f316cbaed12e18ce9944b09dabd4f3ffac3f52efe797ce3ee3c31a03f"></a>
<a id="af9783799f316cbaed12e18ce9944b09da2cedd0b40bf81afb35792150b2d4964a"></a>
<a id="af9783799f316cbaed12e18ce9944b09dafed77d2aed13d59fa6645cb06fc21c43"></a>
<a id="af9783799f316cbaed12e18ce9944b09dacf4d28d56a6c4925944ffc99072d46e9"></a>
<a id="af9783799f316cbaed12e18ce9944b09daf5448a25c8b5a8411f059469112ef2be"></a>
<a id="ac86d8a44f37c771cb666f69a516dff81ad49da8223b68d35a4d95d6b48bb8a3f7"></a>
<a id="ac86d8a44f37c771cb666f69a516dff81a87a4c0efb7e10cccce939af5f60343ad"></a>
<a id="ac86d8a44f37c771cb666f69a516dff81aa0d4721b24d0cd71d6a8fbfc666a6e7c"></a>
<a id="ac86d8a44f37c771cb666f69a516dff81a43b7acda3747eb2233c2f2a433ff71c7"></a>
<a id="ac86d8a44f37c771cb666f69a516dff81a0f4fc7047a7c813b9ada618ed05e09a4"></a>
<a id="ac86d8a44f37c771cb666f69a516dff81a9a960567b8ecbd6feff7e6337fc98567"></a>
<a id="ac86d8a44f37c771cb666f69a516dff81ab84ae4edfcca8ccae2a0df0643d04ca2"></a>
<a id="ac86d8a44f37c771cb666f69a516dff81aba4f3f30eaa7d3368743f78f3c355269"></a>
<a id="a0769bcc2f15d43383f4e5a6c845c51aaa01aef2529fc39dc455c0fb8f2e9cc434"></a>
<a id="a0769bcc2f15d43383f4e5a6c845c51aaa984a5e7f75a4418ca29141f5c6031d1e"></a>
<a id="a0769bcc2f15d43383f4e5a6c845c51aaa239f02ae958dc3e25032825bb4c067e7"></a>
<a id="a0769bcc2f15d43383f4e5a6c845c51aaa669934175190e5416a0d04c3c94acb4b"></a>
<a id="a0769bcc2f15d43383f4e5a6c845c51aaa7127f5d946ea6bb4ec19b96033aafc4b"></a>
<a id="ae1956c4b374e2c8b6a585596e93ac345ae51a5474387816c03970aa0f8058b002"></a>
<a id="ae1956c4b374e2c8b6a585596e93ac345a17160707005c580fbd52dbd6b99699dd"></a>
<a id="ae1956c4b374e2c8b6a585596e93ac345a39200c50c7e22c096db3ce1dd3fe78d5"></a>
<a id="ae1956c4b374e2c8b6a585596e93ac345a4ea17060afbcd026387172c1af57bb43"></a>
<a id="a1c77191f9cb8c50e8e2a03cda2984dbcaca51b75cde3505fd672391b9d7a7997a"></a>
<a id="a1c77191f9cb8c50e8e2a03cda2984dbca36f78cdbd8fcc962c2247d7fc1f33f9b"></a>
<a id="a1c77191f9cb8c50e8e2a03cda2984dbca03fc81eeed7047ad914ce6590511dfa3"></a>
<a id="a1c77191f9cb8c50e8e2a03cda2984dbcacf330302cc8ef7f55d76c2cace40649e"></a>
<a id="a1c77191f9cb8c50e8e2a03cda2984dbca2a4278c079a227145f63f5f2d860146a"></a>
<a id="a1c77191f9cb8c50e8e2a03cda2984dbcaa4a44bb015be3cbcf180f34a39ba8e05"></a>
<a id="a1c77191f9cb8c50e8e2a03cda2984dbca305b2fb720b5191c762b77b886152ca8"></a>
<a id="a6b42b86d8f2ba4f29787c7c6f3d97f36a30f38c9e54bed572ca315fdeb9122103"></a>
<a id="a6b42b86d8f2ba4f29787c7c6f3d97f36a90413fe7dfd8568eeac79709ece7a549"></a>
<a id="a6b42b86d8f2ba4f29787c7c6f3d97f36a5593992de690adb1022b7926d1508ab3"></a>
<a id="a6b42b86d8f2ba4f29787c7c6f3d97f36ae07a7ef1ffce64bab52c5f6612a96716"></a>
<a id="a6b42b86d8f2ba4f29787c7c6f3d97f36a360c72912e023e5b21363f3701deaa50"></a>
<a id="a6b42b86d8f2ba4f29787c7c6f3d97f36aef2ef100dab4187c8600ea721e8726dd"></a>
<a id="a6b42b86d8f2ba4f29787c7c6f3d97f36a022acb9d379c5ecf9935150ec6f51ffc"></a>
<a id="a98c4f218acfa21e124aa22e9fe209437ac353a0c3c1ac62920efdc42879a81cff"></a>
<a id="a98c4f218acfa21e124aa22e9fe209437a16d3fd179853f1f15b980d2b82b572be"></a>
<a id="a98c4f218acfa21e124aa22e9fe209437aca7d98319db6a23b30625828807e2143"></a>
<a id="a98c4f218acfa21e124aa22e9fe209437a1258364107909d0c4f8e9b7dba59300c"></a>
<a id="a98c4f218acfa21e124aa22e9fe209437a0d907c1a9e69435433c5bf19bfacbd73"></a>
<a id="a98c4f218acfa21e124aa22e9fe209437af85839612e4fcc94eb2bd0986bd1740c"></a>
<a id="a98c4f218acfa21e124aa22e9fe209437aa8b8f850196e47799cb9b2cd06650520"></a>
<a id="a98c4f218acfa21e124aa22e9fe209437a2e75506280c1b4d5866f4dd8f2518be8"></a>
<a id="a98c4f218acfa21e124aa22e9fe209437a988758fe0720e6fc33564076e3bc51bf"></a>
<a id="a98c4f218acfa21e124aa22e9fe209437a7496edd5c7ec694d2d175bf751de1458"></a>
<a id="a98c4f218acfa21e124aa22e9fe209437aa0c70fee97e29875394efc2a4c2fa274"></a>
<a id="a238de48c0cb55d173b6b874f4930c537a18b21e5e76bea0263f475ecc228c0301"></a>
<a id="a238de48c0cb55d173b6b874f4930c537ae0605a0d9fc89e094a40b03e96c02339"></a>
<a id="a238de48c0cb55d173b6b874f4930c537af82a5f23e51bf3ac3b7bec137269f540"></a>
<a id="a238de48c0cb55d173b6b874f4930c537a2e3c01bc8d16641d7b500ce1244dbb03"></a>
<a id="a5ac0e70389dc6ccec515530df4eab972a134ed84475be6f55a0f3d3ae9201cbe9"></a>
<a id="a5ac0e70389dc6ccec515530df4eab972ad548c59ebbb5045e437157cb9186de19"></a>
<a id="a5ac0e70389dc6ccec515530df4eab972a83f1d375e4c5aa645759cc4e4462f8e0"></a>
<a id="a5ac0e70389dc6ccec515530df4eab972af44faa0f33705ecbd37b5f3544105e34"></a>
<a id="a66c69cd7d7818af86b6a91fad68334c2a1b1e411f733ad6c1dc41896744441a48"></a>
<a id="a66c69cd7d7818af86b6a91fad68334c2ad870ea9b9fc07a4af81bce3c82330441"></a>
<a id="a66c69cd7d7818af86b6a91fad68334c2aa3e190aa6edb9f6eb7e29b78fc6f1a8a"></a>
<a id="a66c69cd7d7818af86b6a91fad68334c2ad5753bf6fae3f43ef8ce7cb7eb169b61"></a>
<a id="a314c38b1b0603c003e67b5dec2228d4ba32ad0894344bc4980f9206022ed0f877"></a>
<a id="a314c38b1b0603c003e67b5dec2228d4ba9eec5ff6f7d4c7512212cb48719dcabf"></a>
<a id="a314c38b1b0603c003e67b5dec2228d4ba0cd41f5198ce06ce5925b3f52d48b0a2"></a>
<a id="a314c38b1b0603c003e67b5dec2228d4ba435b458d33f1568cb76b77a3ea2e1eb8"></a>
<a id="a97f4810585247f5fed41110413e49853a488b1aac4a0658c8b04b94b7556a2c5b"></a>
<a id="a97f4810585247f5fed41110413e49853a8c620d198b195d913ad3ff913434d764"></a>
<a id="a97f4810585247f5fed41110413e49853a5e617dd9de3620481b89e517bd2c3a4b"></a>
<a id="a97f4810585247f5fed41110413e49853aa38ef885442708891b4ddc4a83c6ff66"></a>
<a id="a7b20cc85df2d9f5ce6c010907d7d5c61a5f680f7a518294d7a706b73bbecbdb73"></a>
<a id="a7b20cc85df2d9f5ce6c010907d7d5c61ae344e23bbc73a6f2ed17d10618bf7a5a"></a>
<a id="a7b20cc85df2d9f5ce6c010907d7d5c61a4cfc3b5856c525eda63b3a8b5fce5ae2"></a>
<a id="a7b20cc85df2d9f5ce6c010907d7d5c61a69d58775148ae7daf65598d6cf90488d"></a>
<a id="a7b20cc85df2d9f5ce6c010907d7d5c61a541be7abf94851538a38f69c2ecb6b5f"></a>
<a id="a7b20cc85df2d9f5ce6c010907d7d5c61acd85dd4f874ed9088e6d7a2260d7bc50"></a>
<a id="a7b20cc85df2d9f5ce6c010907d7d5c61a76356316ead27df98dac310eed775707"></a>
<a id="a7b20cc85df2d9f5ce6c010907d7d5c61a624191bea93e1a350073fe2e5d5adaf1"></a>
<a id="a7b20cc85df2d9f5ce6c010907d7d5c61a98c205ed0f08df1a2f9e2801f02bbe7f"></a>
<a id="a7b20cc85df2d9f5ce6c010907d7d5c61a8ae4a104d50c0bdcae4722de0d5ee605"></a>
<a id="a7b20cc85df2d9f5ce6c010907d7d5c61a0c8a74f1b50f574b64184bf1cdc1458f"></a>
<a id="a7b20cc85df2d9f5ce6c010907d7d5c61aca49de7bd24df65fd6448a7e570b04a8"></a>
<a id="a7b20cc85df2d9f5ce6c010907d7d5c61ae5e13b78bf3fdece36190e48136927bf"></a>
<a id="a7b20cc85df2d9f5ce6c010907d7d5c61a83a9f603da11b75f200d3bb62528cda4"></a>
<a id="a072705601a34c697515f74acb0474c99a9dcb2e5fb6a5a53c6cb02422fd1fef3c"></a>
<a id="a072705601a34c697515f74acb0474c99a54546b311e446754738a9b6f1e3eaea4"></a>
<a id="a072705601a34c697515f74acb0474c99affcc3d18f6bda30fb3fd34916d8f61fe"></a>
<a id="a072705601a34c697515f74acb0474c99a35c39a93dfcc239fcb80db70449af99e"></a>
<a id="a072705601a34c697515f74acb0474c99a56c94068ecb32eb9ced47d4a3bf95481"></a>
<a id="a072705601a34c697515f74acb0474c99af48c850f0aa9e9f9dbce8fc8855f6a2a"></a>
<a id="a072705601a34c697515f74acb0474c99a400dc3acd2ae8320f130dbea80c81969"></a>
<a id="a072705601a34c697515f74acb0474c99afa15c17b4fb95747b444616b085b4905"></a>
<a id="a072705601a34c697515f74acb0474c99a0da09225692b10e51140d4f15ba1dd0a"></a>
<a id="a072705601a34c697515f74acb0474c99a7c9bfc788861214fae86e22443e9484a"></a>
<a id="a072705601a34c697515f74acb0474c99adc7e589c9352cddf856b2e868f93a097"></a>
<a id="a072705601a34c697515f74acb0474c99a8c3edf14ca3a6e04c1949a40cd3fb135"></a>
<a id="a072705601a34c697515f74acb0474c99ad6d6f1ccdabc2970ac2ab6c7a853b37e"></a>
<a id="a072705601a34c697515f74acb0474c99aa5f2d8c27d0b7ae780734cb4bedbf8a4"></a>
<a id="a072705601a34c697515f74acb0474c99ad822462692847b4e8433157cd75eef70"></a>
<a id="a072705601a34c697515f74acb0474c99a45bc2d4b117d144ef5191719f9b6c297"></a>
<a id="a072705601a34c697515f74acb0474c99a5c85e3208bb686d8ded9ae0fe7bd9d53"></a>
<a id="a072705601a34c697515f74acb0474c99abd97c835c80320637579c692d6f57878"></a>
<a id="a072705601a34c697515f74acb0474c99a99c20a704cce28fee37b9b0f14b2ff15"></a>
<a id="a072705601a34c697515f74acb0474c99aa58b1d9f75b639dc1b28163988bc8aa3"></a>
<a id="a072705601a34c697515f74acb0474c99af48292861388f111b0afad64f0352664"></a>
<a id="a072705601a34c697515f74acb0474c99a35b942802a4238882440f2e470f2555f"></a>
<a id="a072705601a34c697515f74acb0474c99a0378338c2747ba8947d8ffcb18f77d51"></a>
<a id="a072705601a34c697515f74acb0474c99a7e34ea8ce2a215c2a76f4184b84a06f2"></a>
<a id="a072705601a34c697515f74acb0474c99adca664fbf5ff0b4d174ca21641e01004"></a>
<a id="a072705601a34c697515f74acb0474c99a9cd6e9c88c3989531a71015147496895"></a>
<a id="a072705601a34c697515f74acb0474c99aa7c628982851eba38074d02e9e335b57"></a>
<a id="a072705601a34c697515f74acb0474c99a753b0fc3e44a4376998e5887ed2c5901"></a>
<a id="a072705601a34c697515f74acb0474c99a4aa36f7d8ceaa3cdab300915453b64b5"></a>
<a id="a072705601a34c697515f74acb0474c99a7ef64e231154de2e461005af29918b86"></a>
<a id="a072705601a34c697515f74acb0474c99a7ccf37711e67b58534689997ac1375df"></a>
<a id="a072705601a34c697515f74acb0474c99aef4ee3246cd66cd7d48f1dabf3fcd7ef"></a>
<a id="a072705601a34c697515f74acb0474c99aa3183436decfa0e42ac0461629258ba3"></a>
<a id="a072705601a34c697515f74acb0474c99ab590e9d9b3213f31a2399ef379d066aa"></a>
<a id="aa0686c333989b0551d3af5eb01de4065a081f03ba34d8cd168ab5d4172d3c8d6a"></a>
<a id="aa0686c333989b0551d3af5eb01de4065a135f072a7d9ee5967a49f7a164816854"></a>
<a id="aa0686c333989b0551d3af5eb01de4065a1ddcc2a60e6f83538151fc93ad434ddf"></a>
<a id="aa0686c333989b0551d3af5eb01de4065ac906ebc564bfc63a7f4ce0350db6667b"></a>
<a id="aa0686c333989b0551d3af5eb01de4065a59ead4a70e76c9b2d6c817f4e2847998"></a>
<a id="aa0686c333989b0551d3af5eb01de4065a5d6d02968e18dd84af3583d282179e64"></a>
<a id="aa0686c333989b0551d3af5eb01de4065a3feb7a1594dc32703d2fbf6e43e77c0c"></a>
<a id="aa0686c333989b0551d3af5eb01de4065acccc283c3dc4a36992e76ea0b6f4d68b"></a>
<a id="aa0686c333989b0551d3af5eb01de4065abebe32c9b1e107c729f4e6ecf501ee1e"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aaa33240a72b4aeff90e48d8dd3b9419c5"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aa72c5d7592912c25f0440fa38664dfc13"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aab852db2cfe8d7581e1ad7a1c2aee5406"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aac99e88e470b5ecb04885b0289a96a2c8"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aa0815a9749fc47ea398752e886e222b65"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aa3c9f8c1239694b9bda4aca0d7f40a929"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aa4cf46d638fd781b73edd03b61dd5d1a2"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aa1388a4a737946b04de90dcec9c719837"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aa0b9e2ded1a4aa629d698f3ba5584bcc2"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aac6c818a2d7443a820c3f027e2d799ad2"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aaac890f2e8917f249f729e273f4180c8d"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aafe9dd6c272ec4d1c04efdfa4d7e12870"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aa6e3c05c3b4a44c9ec63f89554850abbc"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aac5fb430e08cbab9b2cbf2015202641e2"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aa51199d1fa7c1cda33fde647843394d65"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aa02d458f5c51dfb7554e17bad1acb591a"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aa3ac808a14aa22446db1101fe5f2cbfab"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aa4ad410b3a28df509ab875d26ae431e21"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aa94c0a61d8f8aeb5ed7a13846eb81dfae"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aabb622edfda732a5fd3fec2b042951254"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aa153195025c02879f23af882b6a4d7af4"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aac7cb6855c33427bdf0a4e7d344281aaf"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aab6413ec799d46c7341e48f0b5146f400"></a>
<a id="ad38162e32b87d3c01f1ae46d3423155aab8635ae93d3d927f662e88c9e55305eb"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6ad74407536823c1ea3afdf41d4b858b1c"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6a92718e4bd4bccaa2fe4a8780228004d7"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6ae64496ba1520651f8bac35af2531eaf8"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6a96e26220a32f9b6e9e0bdd8c94d48eaf"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6af779f08bfb2fd73a717ea3789ccad509"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6a34b03331e8f7a9ea6b67da6b68c7e0ed"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6a91e216f8a1753b4719ee91819a926dde"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6a5dcd82e4fe5a34646a617a5031fdc638"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6a3532733bc007df5009801bd6f09e45c9"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6aa5657942fb906d58ef2b7bed05137f23"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6a32b2c65c90d0d5b8df5e4a82e9b95a6d"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6a22413680849a7645c7e8c585b5184203"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6a855f8e4399cf3ce0c05c6089f3439ec2"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6a7c44711a51e8175ebcaf4be24e2daec3"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6a4c35ca3a8db652008204cf0cfc8e2339"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6a0d82c7d93c187de5c40c0ff83fe8a478"></a>
<a id="a1cfd2df5ec76eeb915fd3689408a65d6a78472618e8523bf73ca65aee6b0a8318"></a>
<a id="a476ec98763d90a5cba336cbf22d6d553a759c63670d0dd41590fdb940a48ac4dd"></a>
<a id="a476ec98763d90a5cba336cbf22d6d553a59fb3a34a7dba6ed1c86bca21cf97871"></a>
<a id="abf77ec1ad65cc9c99dc930ed7a96301aa39605b86ccfad6196721ddfbb84b33d6"></a>
<a id="abf77ec1ad65cc9c99dc930ed7a96301aac09ddfacee85353e243d6a8cfe7eeba8"></a>
<a id="abf77ec1ad65cc9c99dc930ed7a96301aa3525ee751a482ae1cd816e2674ac3160"></a>
<a id="abf77ec1ad65cc9c99dc930ed7a96301aa9e3d0d084a7d8ad1b9d08e6b699084e6"></a>
<a id="aaf06bb2dcb6e359e08bae37d2f36bbc3aae5e5c58313c1216448474da513ca2b6"></a>
<a id="aaf06bb2dcb6e359e08bae37d2f36bbc3ae50961a0eb0f59776a156facf51e4620"></a>
<a id="aaf06bb2dcb6e359e08bae37d2f36bbc3aa07d3031debe394b369d93fde728d406"></a>
<a id="aaf06bb2dcb6e359e08bae37d2f36bbc3ae4785671c3a4dca332c10c9bc0a72fba"></a>
<a id="aaf06bb2dcb6e359e08bae37d2f36bbc3a0a59356a4db1abd3f72a8c9778b04e66"></a>
<a id="aaf06bb2dcb6e359e08bae37d2f36bbc3a4eb47f187f4aee8228b09a37d4669a4f"></a>
<a id="aaf06bb2dcb6e359e08bae37d2f36bbc3a9c77ef6b4da1f8ac56ebe8be03504b69"></a>
<a id="aa1b9e80034c783cc7ff43dc79ac5878fa8f693e2ff4acfb3d652106fc25f8758f"></a>
<a id="aa1b9e80034c783cc7ff43dc79ac5878fa3f8fde9c17c04f4500f5a86cf4d9e7df"></a>
<a id="aa1b9e80034c783cc7ff43dc79ac5878faf74a4730cc3507a35179fe09da721a19"></a>
<a id="aa1b9e80034c783cc7ff43dc79ac5878fad33e5499a36259f5b881ce524a1f4159"></a>
<a id="aa1b9e80034c783cc7ff43dc79ac5878fac853010c32e85d30f9f5936851ac4ddb"></a>
<a id="aa1b9e80034c783cc7ff43dc79ac5878fa92bcd0ee78ddba8dc551c7917a37a792"></a>
<a id="aa1b9e80034c783cc7ff43dc79ac5878fa47bb6389f20ceb840612266fedac0f7a"></a>
<a id="aa1b9e80034c783cc7ff43dc79ac5878faedbd66fd01bb87a4f55291c299589db7"></a>
<a id="afeec7c838fcf2d5c01cf653e305c749aa104798e5266441d5a2f356f50b01cb35"></a>
<a id="afeec7c838fcf2d5c01cf653e305c749aa2511277c6c4ebe38bc7179312292710b"></a>
<a id="afeec7c838fcf2d5c01cf653e305c749aad9777c04b150a28916f894f54417286c"></a>
<a id="afeec7c838fcf2d5c01cf653e305c749aa0558ef06a64c10456d220e66a5bc0f8b"></a>
<a id="afeec7c838fcf2d5c01cf653e305c749aab78269976cbb673b4e00d6059ec38f80"></a>
<a id="afeec7c838fcf2d5c01cf653e305c749aa5458d4988d7076d854bd695307771858"></a>
<a id="afeec7c838fcf2d5c01cf653e305c749aac1f502da56d7d50b70898329da1ad21a"></a>
<a id="afeec7c838fcf2d5c01cf653e305c749aa02b4afca69adad8d7f220b8e4a76db45"></a>
<a id="afeec7c838fcf2d5c01cf653e305c749aa923c57b4134ad360ed3f6abbabfa87f1"></a>
<a id="a76f7ea4b395028ad5d8cc5eee32656e3ae126f56fd639cbd686321a088d1e05e6"></a>
<a id="a76f7ea4b395028ad5d8cc5eee32656e3a72c39e3140ddd3990c3cbe7c6c867bb1"></a>
<a id="ae82da8038d71cf36ce2237504b498930aa858c50e3f53d635857084ab5801a204"></a>
<a id="ae82da8038d71cf36ce2237504b498930aea7ebe2a07e1ed7727262d522815355b"></a>
<a id="ae82da8038d71cf36ce2237504b498930a7b6cef084cb3b83a91c05964951b05a6"></a>
<a id="ae82da8038d71cf36ce2237504b498930a433d8a39f77a612dd8104ca49c71a76f"></a>
<a id="ae82da8038d71cf36ce2237504b498930a787fb937df1275cb3d169e1dade2fb37"></a>
<a id="ae82da8038d71cf36ce2237504b498930aad980a4d433ffcf189a2e77b5d765861"></a>
<a id="ae82da8038d71cf36ce2237504b498930a88f373b6ac9335667eb8adab49a04e10"></a>
<a id="a9660a61775e481ae4093e11ce9336539a16c56ed964cc6bbb5cc6f0cb857d4f10"></a>
<a id="a9660a61775e481ae4093e11ce9336539ad5e9d57ee155e1b919f6cc213b05424f"></a>
<a id="a9660a61775e481ae4093e11ce9336539a39e410f7f5c51753bf415f727551b9fb"></a>
<a id="a9660a61775e481ae4093e11ce9336539a66ef44acd4ff3fafc2d49120df4b3c10"></a>
<a id="a9660a61775e481ae4093e11ce9336539a9570bb04b0181b4fbdc96cace060d187"></a>
<a id="a9660a61775e481ae4093e11ce9336539ae9369c1cd7595ab83289fc356e9cc1b6"></a>
<a id="a9660a61775e481ae4093e11ce9336539a5c37aeeb3c68d7b3dbe8b9001a00507c"></a>
<a id="a9660a61775e481ae4093e11ce9336539a66ecc8c1a73181d70e23424cf718728d"></a>
<a id="a9660a61775e481ae4093e11ce9336539a14dec2b314ed13974dbba31f33a5eab9"></a>
<a id="a9660a61775e481ae4093e11ce9336539a788a77f1e7a468c14ef57319ef8938f3"></a>
<a id="ac12657ae7d3b8abc562d4d7929a86b65aa23a07a4fe6f6dd8292215221d97d5e2"></a>
<a id="ac12657ae7d3b8abc562d4d7929a86b65acc46ce7f993b3eb81c6a2a2daad84c34"></a>
<a id="ac12657ae7d3b8abc562d4d7929a86b65a9b12d90cd1590f68fc1031449c4560ec"></a>
<a id="ac12657ae7d3b8abc562d4d7929a86b65a6d2084ba4c729c2cb019582b975f652f"></a>
<a id="ac12657ae7d3b8abc562d4d7929a86b65a6cd553669599181b3677cea94687f025"></a>
<a id="ac12657ae7d3b8abc562d4d7929a86b65a364c7067e73960bae74ed80320adb223"></a>
<a id="a3a542344967c5c1912bde216559e7cd6ad7a10f97094ddb96f26ab44fc34de12a"></a>
<a id="a3a542344967c5c1912bde216559e7cd6a900536b934da03f8e8590de3e3d56296"></a>
<a id="a3a542344967c5c1912bde216559e7cd6ac2cc5967daee0a3e9ef61c9c486b3a6c"></a>
<a id="a3a542344967c5c1912bde216559e7cd6adef5748e2622dab22da33504bbafa149"></a>
<a id="a3a542344967c5c1912bde216559e7cd6a9b69d64108c6564bc313e4fb2b53f61c"></a>
<a id="a3a542344967c5c1912bde216559e7cd6ac62397290371f5fb3fdf8d4b52fb3575"></a>
<a id="a3a542344967c5c1912bde216559e7cd6a2a9baef178307d6e6006ea88b4da383c"></a>
<a id="a3a542344967c5c1912bde216559e7cd6a617d1991d70033df3b39eef7ccb98b48"></a>
<a id="a3a542344967c5c1912bde216559e7cd6a075731d15b2f4b7c7448d6d4ee059880"></a>
<a id="a250ae2ce54e941895a720b565632350eac1212149d096232e75d1d090abb4974c"></a>
<a id="a250ae2ce54e941895a720b565632350eabd26fc6f76267231c78eae8be9ebb885"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6adb3e45e84da812297359d6054baa69ba"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6a17007c3d37f047e6db56491a4230e8a8"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6ae923fdf459570657220ec225cbed7336"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6a3f6ebe270ba873bab3407ee7d655b53d"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6aa7a656a21495fbf64666b2b80236e4e4"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6ad75d7d47a3d5fcc39a68c08546e9793b"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6a560f91eb371bfea5cf6c5c036cc9c096"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6a89c4025349ece0021cd627101f0efdd1"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6a6323aa0a8cbfb59f8209a37c8135079c"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6ac0aa0897e1bbf45b0f5f4de73d733477"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6a4d32525a631342d78f73b6296e148666"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6a1f043936c614ac39b75f3835dc498b94"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6a1071312f18c64077e6964e421ef00ead"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6a246619651470476238452550068db8a0"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6a4cb1cc23687e7a1854d8af0c76876a20"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6a018af73c25e22c6e5313e5e3cff57e92"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6ac5613e6858d2c9217165ab4cbb240012"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6a6673f837fa5a98b573886c5e6429c644"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6a3d791855e6df402d5bfd92ce216a9a4b"></a>
<a id="a296cbe236e9e36dc79ca30eb54e6bcc6af0baaa7f71d144c7e5edade4b2445813"></a>
<a id="a5466ef2e30578d03c61831aa09fd7b9aaad6eabbee29e4ff07bdf93a9162aea6b"></a>
<a id="a5466ef2e30578d03c61831aa09fd7b9aad61b9d180a8de3c01be2e892c45504fb"></a>
<a id="a5466ef2e30578d03c61831aa09fd7b9aa5c5c100c048986ecfed728690d05ac55"></a>
<a id="a5466ef2e30578d03c61831aa09fd7b9aa72e9ad81edf54b7139a758d47fe54dd5"></a>
<a id="a5466ef2e30578d03c61831aa09fd7b9aa106c43d63c3b3c02d3835ccf542f3190"></a>
<a id="a5466ef2e30578d03c61831aa09fd7b9aaff651e04c107beb23e0bd76d03029b26"></a>

---

[上一章](P014_zephyr__drivers__memc.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__drivers__mspi__mspi_cadence.h_头文件参考.md)
