---
id: learning.zephyr-docs.api-file-audio-test-reference.page-12
title: zephyr__dt-bindings__clock__syna_sr100_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/syna__sr100__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_dt-bindings\_\_clock\_\_syna\_sr100\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/syna__sr100__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

列出Synaptics SR100系列的时钟子系统ID（Clock Subsystem IDs）。

查看此文件的源码。

<a id="details"></a>

列出Synaptics SR100系列的时钟子系统ID（Clock Subsystem IDs）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.1\_宏定义（Macros）

<a id="r_a7690acc7f2717e0bdc4c133181a7aebd"></a>

```c
#define XSPI_CORE_CLK_CTRL 0x30
```

相关声明：[XSPI_CORE_CLK_CTRL](#a7690acc7f2717e0bdc4c133181a7aebd)。

时钟门控辅助宏（Clock Gating Helpers）。

<a id="r_a7011616e937d2c83b03aa0e797de00a0"></a>

```c
#define SD0_CORE_CLK_CTRL 0x38
```

相关声明：[SD0_CORE_CLK_CTRL](#a7011616e937d2c83b03aa0e797de00a0)。

SD0 时钟门控辅助宏（Clock Gating Helper）。

<a id="r_a740a58fa969e22e87cfab92be68edc70"></a>

```c
#define SD1_CORE_CLK_CTRL 0x3c
```

相关声明：[SD1_CORE_CLK_CTRL](#a740a58fa969e22e87cfab92be68edc70)。

SD1 时钟门控辅助宏（Clock Gating Helper）。

<a id="r_ae312e5b78658cb5ae3c7c82879b57619"></a>

```c
#define SPI_MSTR_SSI_CLK_CTRL 0x40
```

相关声明：[SPI_MSTR_SSI_CLK_CTRL](#ae312e5b78658cb5ae3c7c82879b57619)。

SPI 主设备（Master） 时钟门控辅助宏（Clock Gating Helper）。

<a id="r_ac87ea0d1923630c76cc77a3bba96764f"></a>

```c
#define SPI_SLV_SSI_CLK_CTRL 0x44
```

相关声明：[SPI_SLV_SSI_CLK_CTRL](#ac87ea0d1923630c76cc77a3bba96764f)。

SPI 从设备（Slave） 时钟门控辅助宏（Clock Gating Helper）。

<a id="r_a47823afe9b3ba12bc13b995f4d984432"></a>

```c
#define I3C0_CORE_CLK_CTRL 0x48
```

相关声明：[I3C0_CORE_CLK_CTRL](#a47823afe9b3ba12bc13b995f4d984432)。

I3C0 时钟门控辅助宏（Clock Gating Helper）。

<a id="r_a2f57beee7bf6cd8f40c3dba3478ba52f"></a>

```c
#define I3C1_CORE_CLK_CTRL 0x4c
```

相关声明：[I3C1_CORE_CLK_CTRL](#a2f57beee7bf6cd8f40c3dba3478ba52f)。

I3C1 时钟门控辅助宏（Clock Gating Helper）。

<a id="r_a90f5295e630e446572d87aa49d71964c"></a>

```c
#define UART0_CORE_CLK_CTRL 0x50
```

相关声明：[UART0_CORE_CLK_CTRL](#a90f5295e630e446572d87aa49d71964c)。

UART0 时钟门控辅助宏（Clock Gating Helper）。

<a id="r_a5e57580c17d65900d130a580ae850288"></a>

```c
#define UART1_CORE_CLK_CTRL 0x54
```

相关声明：[UART1_CORE_CLK_CTRL](#a5e57580c17d65900d130a580ae850288)。

UART1 时钟门控辅助宏（Clock Gating Helper）。

<a id="r_a07f38be61617bee1db0200ae99e91e5f"></a>

```c
#define I2C0_MSTR_CORE_CLK_CTRL 0x58
```

相关声明：[I2C0_MSTR_CORE_CLK_CTRL](#a07f38be61617bee1db0200ae99e91e5f)。

I2C0 主设备（Master） 时钟门控辅助宏（Clock Gating Helper）。

<a id="r_a6bfb22697cd40cfea2cbc9d9a9201b2c"></a>

```c
#define I2C1_MSTR_CORE_CLK_CTRL 0x5c
```

相关声明：[I2C1_MSTR_CORE_CLK_CTRL](#a6bfb22697cd40cfea2cbc9d9a9201b2c)。

I2C1 主设备（Master） 时钟门控辅助宏（Clock Gating Helper）。

<a id="r_a1778dcfaf18a0eecbd6dbef1873506d4"></a>

```c
#define I2C_SLV_CORE_CLK_CTRL 0x60
```

相关声明：[I2C_SLV_CORE_CLK_CTRL](#a1778dcfaf18a0eecbd6dbef1873506d4)。

I2C 从设备（Slave） 时钟门控辅助宏（Clock Gating Helper）。

<a id="r_afb192359bb0e0839a7b2d76abdc1b48a"></a>

```c
#define USB2_CORE_CLK_CTRL 0x64
```

相关声明：[USB2_CORE_CLK_CTRL](#afb192359bb0e0839a7b2d76abdc1b48a)。

USB 时钟门控辅助宏（Clock Gating Helper）。

<a id="r_a799091b369efb0bc719326768c7fdcee"></a>

```c
#define CGL_REG 16
```

相关声明：[CGL_REG](#a799091b369efb0bc719326768c7fdcee)。

GLOBAL_CLK_ENABLE1/2 寄存器中的位位置（Bit Locations）。

<a id="r_afe8353274febd2f0e89f592443ec70e6"></a>

```c
#define AXI_ID 8
```

相关声明：[AXI_ID](#afe8353274febd2f0e89f592443ec70e6)。

AXI 时钟的位移量（Bit Shift）。

<a id="r_a949b977ada41053d8d02377022f47488"></a>

```c
#define SYNA_IMG_CAM_CLK 0
```

相关声明：[SYNA_IMG_CAM_CLK](#a949b977ada41053d8d02377022f47488)。

设备域时钟选择（Device Domain Clock Selection）。

<a id="r_aa7dc60f7749a562dcb66a0a6422a22a7"></a>

```c
#define SYNA_GPIO_DB_CLK 1
```

相关声明：[SYNA_GPIO_DB_CLK](#aa7dc60f7749a562dcb66a0a6422a22a7)。

GPIO 去抖时钟（Debounce Clock）。

<a id="r_a2a6ef9281468431cf64dbe117389e29e"></a>

```c
#define SYNA_AXI_CLK 2
```

相关声明：[SYNA_AXI_CLK](#a2a6ef9281468431cf64dbe117389e29e)。

AXI 时钟（Clock）。

<a id="r_aa61e4c579e7e1cde51b5f4589af44691"></a>

```c
#define SYNA_NPU_CLK 3
```

相关声明：[SYNA_NPU_CLK](#aa61e4c579e7e1cde51b5f4589af44691)。

NPU 时钟（Clock）。

<a id="r_a7c34f83d663cd37b02b43888287dcb3c"></a>

```c
#define SYNA_DMA0_CLK 4
```

相关声明：[SYNA_DMA0_CLK](#a7c34f83d663cd37b02b43888287dcb3c)。

DMA0 时钟（Clock）。

<a id="r_af9b07d18c40fd6ce7d4d675aa3335036"></a>

```c
#define SYNA_IMG_SYS_CLK 9
```

相关声明：[SYNA_IMG_SYS_CLK](#af9b07d18c40fd6ce7d4d675aa3335036)。

图像处理时钟（Image Processing Clock），sys。

<a id="r_a218df200f4885077220150f11ba4bd54"></a>

```c
#define SYNA_IMG_CFG_CLK 10
```

相关声明：[SYNA_IMG_CFG_CLK](#a218df200f4885077220150f11ba4bd54)。

图像处理时钟（Image Processing Clock），cfg。

<a id="r_a44b3a1ef76cbccdd0db1af502be82bcf"></a>

```c
#define SYNA_IMG_APB_CLK 11
```

相关声明：[SYNA_IMG_APB_CLK](#a44b3a1ef76cbccdd0db1af502be82bcf)。

图像处理时钟（Image Processing Clock），apb。

<a id="r_a3884e7070ac6085f3a17b3c9074eb463"></a>

```c
#define SYNA_DMA1_CLK 12
```

相关声明：[SYNA_DMA1_CLK](#a3884e7070ac6085f3a17b3c9074eb463)。

DMA1 时钟（Clock）。

<a id="r_ada90a0b6a2ca62daea79f110c7fe9ca0"></a>

```c
#define SYNA_PVT_APB_CLK 13
```

相关声明：[SYNA_PVT_APB_CLK](#ada90a0b6a2ca62daea79f110c7fe9ca0)。

工艺、电压与温度时钟（Process, Voltage, and Temperature Clock）。

<a id="r_a1fd4b7fd428ecdb6b77223071b801932"></a>

```c
#define SYNA_XSPI_CLK ((XSPI_CORE_CLK_CTRL << CGL_REG) | (7 << AXI_ID) | 32)
```

相关声明：[SYNA_XSPI_CLK](#a1fd4b7fd428ecdb6b77223071b801932)、[XSPI_CORE_CLK_CTRL](#a7690acc7f2717e0bdc4c133181a7aebd)、[CGL_REG](#a799091b369efb0bc719326768c7fdcee)、[AXI_ID](#afe8353274febd2f0e89f592443ec70e6)。

xSPI 时钟（Clock）。

<a id="r_ac2b015d27000cdc1554bc273a8539071"></a>

```c
#define SYNA_USB_CLK ((USB2_CORE_CLK_CTRL << CGL_REG) | (8 << AXI_ID) | 35)
```

相关声明：[SYNA_USB_CLK](#ac2b015d27000cdc1554bc273a8539071)、[USB2_CORE_CLK_CTRL](#afb192359bb0e0839a7b2d76abdc1b48a)、[CGL_REG](#a799091b369efb0bc719326768c7fdcee)、[AXI_ID](#afe8353274febd2f0e89f592443ec70e6)。

USB 时钟（Clock）。

<a id="r_a97b0ea8d2720b197e9eb8225f6bb8732"></a>

```c
#define SYNA_SD0_CLK ((SD0_CORE_CLK_CTRL << CGL_REG) | (5 << AXI_ID) | 33)
```

相关声明：[SYNA_SD0_CLK](#a97b0ea8d2720b197e9eb8225f6bb8732)、[SD0_CORE_CLK_CTRL](#a7011616e937d2c83b03aa0e797de00a0)、[CGL_REG](#a799091b369efb0bc719326768c7fdcee)、[AXI_ID](#afe8353274febd2f0e89f592443ec70e6)。

SD0 时钟（Clock）。

<a id="r_a5890b5fc369dc9861a31bdb383815705"></a>

```c
#define SYNA_SD1_CLK ((SD1_CORE_CLK_CTRL << CGL_REG) | (6 << AXI_ID) | 34)
```

相关声明：[SYNA_SD1_CLK](#a5890b5fc369dc9861a31bdb383815705)、[SD1_CORE_CLK_CTRL](#a740a58fa969e22e87cfab92be68edc70)、[CGL_REG](#a799091b369efb0bc719326768c7fdcee)、[AXI_ID](#afe8353274febd2f0e89f592443ec70e6)。

SD1 时钟（Clock）。

<a id="r_a59656ee063e2f42b3ebef92757ec5c5a"></a>

```c
#define SYNA_SPI_MSTR_CLK ((SPI_MSTR_SSI_CLK_CTRL << CGL_REG) | 36)
```

相关声明：[SYNA_SPI_MSTR_CLK](#a59656ee063e2f42b3ebef92757ec5c5a)、[SPI_MSTR_SSI_CLK_CTRL](#ae312e5b78658cb5ae3c7c82879b57619)、[CGL_REG](#a799091b369efb0bc719326768c7fdcee)。

SPI 主设备（Master） 时钟（Clock）。

<a id="r_a7046f59a30f98329117d41aa0ba04693"></a>

```c
#define SYNA_SPI_SLV_CLK ((SPI_SLV_SSI_CLK_CTRL << CGL_REG) | 37)
```

相关声明：[SYNA_SPI_SLV_CLK](#a7046f59a30f98329117d41aa0ba04693)、[SPI_SLV_SSI_CLK_CTRL](#ac87ea0d1923630c76cc77a3bba96764f)、[CGL_REG](#a799091b369efb0bc719326768c7fdcee)。

SPI 从设备（Slave） 时钟（Clock）。

<a id="r_ab00ceea69339a2b4a72b7d127adbaa73"></a>

```c
#define SYNA_I3C0_CLK ((I3C0_CORE_CLK_CTRL << CGL_REG) | 38)
```

相关声明：[SYNA_I3C0_CLK](#ab00ceea69339a2b4a72b7d127adbaa73)、[I3C0_CORE_CLK_CTRL](#a47823afe9b3ba12bc13b995f4d984432)、[CGL_REG](#a799091b369efb0bc719326768c7fdcee)。

I3C0 时钟（Clock）。

<a id="r_a121083fe7e0229a49cd8af87f333d378"></a>

```c
#define SYNA_I3C1_CLK ((I3C1_CORE_CLK_CTRL << CGL_REG) | 39)
```

相关声明：[SYNA_I3C1_CLK](#a121083fe7e0229a49cd8af87f333d378)、[I3C1_CORE_CLK_CTRL](#a2f57beee7bf6cd8f40c3dba3478ba52f)、[CGL_REG](#a799091b369efb0bc719326768c7fdcee)。

I3C1 时钟（Clock）。

<a id="r_a76e9f0a802e7799f04ebf3a6f524cf75"></a>

```c
#define SYNA_UART0_CLK ((UART0_CORE_CLK_CTRL << CGL_REG) | 40)
```

相关声明：[SYNA_UART0_CLK](#a76e9f0a802e7799f04ebf3a6f524cf75)、[UART0_CORE_CLK_CTRL](#a90f5295e630e446572d87aa49d71964c)、[CGL_REG](#a799091b369efb0bc719326768c7fdcee)。

UART0 时钟（Clock）。

<a id="r_a8ea942f81b9d7f443e3062c212aa26ad"></a>

```c
#define SYNA_UART1_CLK ((UART1_CORE_CLK_CTRL << CGL_REG) | 41)
```

相关声明：[SYNA_UART1_CLK](#a8ea942f81b9d7f443e3062c212aa26ad)、[UART1_CORE_CLK_CTRL](#a5e57580c17d65900d130a580ae850288)、[CGL_REG](#a799091b369efb0bc719326768c7fdcee)。

UART1 时钟（Clock）。

<a id="r_a992d9347335ca4336e50b2bf262e2756"></a>

```c
#define SYNA_I2C0_MSTR_CLK ((I2C0_MSTR_CORE_CLK_CTRL << CGL_REG) | 42)
```

相关声明：[SYNA_I2C0_MSTR_CLK](#a992d9347335ca4336e50b2bf262e2756)、[I2C0_MSTR_CORE_CLK_CTRL](#a07f38be61617bee1db0200ae99e91e5f)、[CGL_REG](#a799091b369efb0bc719326768c7fdcee)。

I2C0 主设备（Master） 时钟（Clock）。

<a id="r_a4d3edc51cdbb627efc01e98ceecdce97"></a>

```c
#define SYNA_I2C1_MSTR_CLK ((I2C1_MSTR_CORE_CLK_CTRL << CGL_REG) | 43)
```

相关声明：[SYNA_I2C1_MSTR_CLK](#a4d3edc51cdbb627efc01e98ceecdce97)、[I2C1_MSTR_CORE_CLK_CTRL](#a6bfb22697cd40cfea2cbc9d9a9201b2c)、[CGL_REG](#a799091b369efb0bc719326768c7fdcee)。

I2C1 主设备（Master） 时钟（Clock）。

<a id="r_a125f77cf7aace7a3073a7f113beabba5"></a>

```c
#define SYNA_I2C_SLV_CLK ((I2C_SLV_CORE_CLK_CTRL << CGL_REG) | 44)
```

相关声明：[SYNA_I2C_SLV_CLK](#a125f77cf7aace7a3073a7f113beabba5)、[I2C_SLV_CORE_CLK_CTRL](#a1778dcfaf18a0eecbd6dbef1873506d4)、[CGL_REG](#a799091b369efb0bc719326768c7fdcee)。

I2C 从设备（Slave） 时钟（Clock）。

<a id="r_a2e318f0a51debee176e9d6db64d6e6be"></a>

```c
#define SYNA_GPIO_CFG_CLK 45
```

相关声明：[SYNA_GPIO_CFG_CLK](#a2e318f0a51debee176e9d6db64d6e6be)。

GPIO 时钟（Clock）。

<a id="r_adeddb8b169cc7da67d690b33fce59451"></a>

```c
#define SYNA_I2S_CFG_CLK 46
```

相关声明：[SYNA_I2S_CFG_CLK](#adeddb8b169cc7da67d690b33fce59451)。

I2S 时钟（Clock）。

<a id="r_ac7587c7d34c76f200f70b5f865313114"></a>

```c
#define SYNA_I2S_TX0_PCLK 47
```

相关声明：[SYNA_I2S_TX0_PCLK](#ac7587c7d34c76f200f70b5f865313114)。

I2S TX0 时钟（Clock）。

<a id="r_ab0934249511aaa879e62ed4f36bf9e6b"></a>

```c
#define SYNA_I2S_TX1_PCLK 48
```

相关声明：[SYNA_I2S_TX1_PCLK](#ab0934249511aaa879e62ed4f36bf9e6b)。

I2S TX1 时钟（Clock）。

<a id="r_a6b82baf1efde09a3ecb67e359ec05b78"></a>

```c
#define SYNA_I2S_TX2_PCLK 49
```

相关声明：[SYNA_I2S_TX2_PCLK](#a6b82baf1efde09a3ecb67e359ec05b78)。

I2S TX2 时钟（Clock）。

<a id="r_aeec3d29c3298e00a31bdac3225c79327"></a>

```c
#define SYNA_I2S_TX3_PCLK 50
```

相关声明：[SYNA_I2S_TX3_PCLK](#aeec3d29c3298e00a31bdac3225c79327)。

I2S TX3 时钟（Clock）。

<a id="r_af74b5565a0bd8ec887211acc38f98f4b"></a>

```c
#define SYNA_I2S_RX0_PCLK 51
```

相关声明：[SYNA_I2S_RX0_PCLK](#af74b5565a0bd8ec887211acc38f98f4b)。

I2S RX0 时钟（Clock）。

<a id="r_a2bc93185bd315f97cecad9bd63b6ad9e"></a>

```c
#define SYNA_I2S_RX1_PCLK 52
```

相关声明：[SYNA_I2S_RX1_PCLK](#a2bc93185bd315f97cecad9bd63b6ad9e)。

I2S RX1 时钟（Clock）。

<a id="r_a2ffb895b4e84108618f226bd00096bf6"></a>

```c
#define SYNA_I2S_RX2_PCLK 53
```

相关声明：[SYNA_I2S_RX2_PCLK](#a2ffb895b4e84108618f226bd00096bf6)。

I2S RX2 时钟（Clock）。

<a id="r_a59d5945dc7011425a08d195264445276"></a>

```c
#define SYNA_I2S_RX3_PCLK 54
```

相关声明：[SYNA_I2S_RX3_PCLK](#a59d5945dc7011425a08d195264445276)。

I2S RX3 时钟（Clock）。

<a id="r_a311d8c0fa3dec51c6b5a18c026d4ea42"></a>

```c
#define SYNA_I2S_SWIRE_CFG_CLK 55
```

相关声明：[SYNA_I2S_SWIRE_CFG_CLK](#a311d8c0fa3dec51c6b5a18c026d4ea42)。

I2S SWIRE 时钟（Clock）。

## 12.2\_详细说明（Detailed Documentation）

<a id="afe8353274febd2f0e89f592443ec70e6"></a>

### `AXI_ID`

```c
#define AXI_ID 8
```

AXI 时钟的位移量（Bit Shift）。

<a id="a799091b369efb0bc719326768c7fdcee"></a>

### `CGL_REG`

```c
#define CGL_REG 16
```

GLOBAL_CLK_ENABLE1/2 寄存器中的位位置（Bit Locations）。

时钟门控的位移量（Clock Gating Bit Shift）。

<a id="a07f38be61617bee1db0200ae99e91e5f"></a>

### `I2C0_MSTR_CORE_CLK_CTRL`

```c
#define I2C0_MSTR_CORE_CLK_CTRL 0x58
```

I2C0 主设备（Master） 时钟门控辅助宏（Clock Gating Helper）。

<a id="a6bfb22697cd40cfea2cbc9d9a9201b2c"></a>

### `I2C1_MSTR_CORE_CLK_CTRL`

```c
#define I2C1_MSTR_CORE_CLK_CTRL 0x5c
```

I2C1 主设备（Master） 时钟门控辅助宏（Clock Gating Helper）。

<a id="a1778dcfaf18a0eecbd6dbef1873506d4"></a>

### `I2C_SLV_CORE_CLK_CTRL`

```c
#define I2C_SLV_CORE_CLK_CTRL 0x60
```

I2C 从设备（Slave） 时钟门控辅助宏（Clock Gating Helper）。

<a id="a47823afe9b3ba12bc13b995f4d984432"></a>

### `I3C0_CORE_CLK_CTRL`

```c
#define I3C0_CORE_CLK_CTRL 0x48
```

I3C0 时钟门控辅助宏（Clock Gating Helper）。

<a id="a2f57beee7bf6cd8f40c3dba3478ba52f"></a>

### `I3C1_CORE_CLK_CTRL`

```c
#define I3C1_CORE_CLK_CTRL 0x4c
```

I3C1 时钟门控辅助宏（Clock Gating Helper）。

<a id="a7011616e937d2c83b03aa0e797de00a0"></a>

### `SD0_CORE_CLK_CTRL`

```c
#define SD0_CORE_CLK_CTRL 0x38
```

SD0 时钟门控辅助宏（Clock Gating Helper）。

<a id="a740a58fa969e22e87cfab92be68edc70"></a>

### `SD1_CORE_CLK_CTRL`

```c
#define SD1_CORE_CLK_CTRL 0x3c
```

SD1 时钟门控辅助宏（Clock Gating Helper）。

<a id="ae312e5b78658cb5ae3c7c82879b57619"></a>

### `SPI_MSTR_SSI_CLK_CTRL`

```c
#define SPI_MSTR_SSI_CLK_CTRL 0x40
```

SPI 主设备（Master） 时钟门控辅助宏（Clock Gating Helper）。

<a id="ac87ea0d1923630c76cc77a3bba96764f"></a>

### `SPI_SLV_SSI_CLK_CTRL`

```c
#define SPI_SLV_SSI_CLK_CTRL 0x44
```

SPI 从设备（Slave） 时钟门控辅助宏（Clock Gating Helper）。

<a id="a2a6ef9281468431cf64dbe117389e29e"></a>

### `SYNA_AXI_CLK`

```c
#define SYNA_AXI_CLK 2
```

AXI 时钟（Clock）。

<a id="a7c34f83d663cd37b02b43888287dcb3c"></a>

### `SYNA_DMA0_CLK`

```c
#define SYNA_DMA0_CLK 4
```

DMA0 时钟（Clock）。

<a id="a3884e7070ac6085f3a17b3c9074eb463"></a>

### `SYNA_DMA1_CLK`

```c
#define SYNA_DMA1_CLK 12
```

DMA1 时钟（Clock）。

<a id="a2e318f0a51debee176e9d6db64d6e6be"></a>

### `SYNA_GPIO_CFG_CLK`

```c
#define SYNA_GPIO_CFG_CLK 45
```

GPIO 时钟（Clock）。

<a id="aa7dc60f7749a562dcb66a0a6422a22a7"></a>

### `SYNA_GPIO_DB_CLK`

```c
#define SYNA_GPIO_DB_CLK 1
```

GPIO 去抖时钟（Debounce Clock）。

<a id="a992d9347335ca4336e50b2bf262e2756"></a>

### `SYNA_I2C0_MSTR_CLK`

```c
#define SYNA_I2C0_MSTR_CLK ((I2C0_MSTR_CORE_CLK_CTRL << CGL_REG) | 42)
```

I2C0 主设备（Master） 时钟（Clock）。

<a id="a4d3edc51cdbb627efc01e98ceecdce97"></a>

### `SYNA_I2C1_MSTR_CLK`

```c
#define SYNA_I2C1_MSTR_CLK ((I2C1_MSTR_CORE_CLK_CTRL << CGL_REG) | 43)
```

I2C1 主设备（Master） 时钟（Clock）。

<a id="a125f77cf7aace7a3073a7f113beabba5"></a>

### `SYNA_I2C_SLV_CLK`

```c
#define SYNA_I2C_SLV_CLK ((I2C_SLV_CORE_CLK_CTRL << CGL_REG) | 44)
```

I2C 从设备（Slave） 时钟（Clock）。

<a id="adeddb8b169cc7da67d690b33fce59451"></a>

### `SYNA_I2S_CFG_CLK`

```c
#define SYNA_I2S_CFG_CLK 46
```

I2S 时钟（Clock）。

<a id="af74b5565a0bd8ec887211acc38f98f4b"></a>

### `SYNA_I2S_RX0_PCLK`

```c
#define SYNA_I2S_RX0_PCLK 51
```

I2S RX0 时钟（Clock）。

<a id="a2bc93185bd315f97cecad9bd63b6ad9e"></a>

### `SYNA_I2S_RX1_PCLK`

```c
#define SYNA_I2S_RX1_PCLK 52
```

I2S RX1 时钟（Clock）。

<a id="a2ffb895b4e84108618f226bd00096bf6"></a>

### `SYNA_I2S_RX2_PCLK`

```c
#define SYNA_I2S_RX2_PCLK 53
```

I2S RX2 时钟（Clock）。

<a id="a59d5945dc7011425a08d195264445276"></a>

### `SYNA_I2S_RX3_PCLK`

```c
#define SYNA_I2S_RX3_PCLK 54
```

I2S RX3 时钟（Clock）。

<a id="a311d8c0fa3dec51c6b5a18c026d4ea42"></a>

### `SYNA_I2S_SWIRE_CFG_CLK`

```c
#define SYNA_I2S_SWIRE_CFG_CLK 55
```

I2S SWIRE 时钟（Clock）。

<a id="ac7587c7d34c76f200f70b5f865313114"></a>

### `SYNA_I2S_TX0_PCLK`

```c
#define SYNA_I2S_TX0_PCLK 47
```

I2S TX0 时钟（Clock）。

<a id="ab0934249511aaa879e62ed4f36bf9e6b"></a>

### `SYNA_I2S_TX1_PCLK`

```c
#define SYNA_I2S_TX1_PCLK 48
```

I2S TX1 时钟（Clock）。

<a id="a6b82baf1efde09a3ecb67e359ec05b78"></a>

### `SYNA_I2S_TX2_PCLK`

```c
#define SYNA_I2S_TX2_PCLK 49
```

I2S TX2 时钟（Clock）。

<a id="aeec3d29c3298e00a31bdac3225c79327"></a>

### `SYNA_I2S_TX3_PCLK`

```c
#define SYNA_I2S_TX3_PCLK 50
```

I2S TX3 时钟（Clock）。

<a id="ab00ceea69339a2b4a72b7d127adbaa73"></a>

### `SYNA_I3C0_CLK`

```c
#define SYNA_I3C0_CLK ((I3C0_CORE_CLK_CTRL << CGL_REG) | 38)
```

I3C0 时钟（Clock）。

<a id="a121083fe7e0229a49cd8af87f333d378"></a>

### `SYNA_I3C1_CLK`

```c
#define SYNA_I3C1_CLK ((I3C1_CORE_CLK_CTRL << CGL_REG) | 39)
```

I3C1 时钟（Clock）。

<a id="a44b3a1ef76cbccdd0db1af502be82bcf"></a>

### `SYNA_IMG_APB_CLK`

```c
#define SYNA_IMG_APB_CLK 11
```

图像处理时钟（Image Processing Clock），apb。

<a id="a949b977ada41053d8d02377022f47488"></a>

### `SYNA_IMG_CAM_CLK`

```c
#define SYNA_IMG_CAM_CLK 0
```

设备域时钟选择（Device Domain Clock Selection）。

相机时钟（Camera Clock）。

<a id="a218df200f4885077220150f11ba4bd54"></a>

### `SYNA_IMG_CFG_CLK`

```c
#define SYNA_IMG_CFG_CLK 10
```

图像处理时钟（Image Processing Clock），cfg。

<a id="af9b07d18c40fd6ce7d4d675aa3335036"></a>

### `SYNA_IMG_SYS_CLK`

```c
#define SYNA_IMG_SYS_CLK 9
```

图像处理时钟（Image Processing Clock），sys。

<a id="aa61e4c579e7e1cde51b5f4589af44691"></a>

### `SYNA_NPU_CLK`

```c
#define SYNA_NPU_CLK 3
```

NPU 时钟（Clock）。

<a id="ada90a0b6a2ca62daea79f110c7fe9ca0"></a>

### `SYNA_PVT_APB_CLK`

```c
#define SYNA_PVT_APB_CLK 13
```

工艺、电压与温度时钟（Process, Voltage, and Temperature Clock）。

<a id="a97b0ea8d2720b197e9eb8225f6bb8732"></a>

### `SYNA_SD0_CLK`

```c
#define SYNA_SD0_CLK ((SD0_CORE_CLK_CTRL << CGL_REG) | (5 << AXI_ID) | 33)
```

SD0 时钟（Clock）。

<a id="a5890b5fc369dc9861a31bdb383815705"></a>

### `SYNA_SD1_CLK`

```c
#define SYNA_SD1_CLK ((SD1_CORE_CLK_CTRL << CGL_REG) | (6 << AXI_ID) | 34)
```

SD1 时钟（Clock）。

<a id="a59656ee063e2f42b3ebef92757ec5c5a"></a>

### `SYNA_SPI_MSTR_CLK`

```c
#define SYNA_SPI_MSTR_CLK ((SPI_MSTR_SSI_CLK_CTRL << CGL_REG) | 36)
```

SPI 主设备（Master） 时钟（Clock）。

<a id="a7046f59a30f98329117d41aa0ba04693"></a>

### `SYNA_SPI_SLV_CLK`

```c
#define SYNA_SPI_SLV_CLK ((SPI_SLV_SSI_CLK_CTRL << CGL_REG) | 37)
```

SPI 从设备（Slave） 时钟（Clock）。

<a id="a76e9f0a802e7799f04ebf3a6f524cf75"></a>

### `SYNA_UART0_CLK`

```c
#define SYNA_UART0_CLK ((UART0_CORE_CLK_CTRL << CGL_REG) | 40)
```

UART0 时钟（Clock）。

<a id="a8ea942f81b9d7f443e3062c212aa26ad"></a>

### `SYNA_UART1_CLK`

```c
#define SYNA_UART1_CLK ((UART1_CORE_CLK_CTRL << CGL_REG) | 41)
```

UART1 时钟（Clock）。

<a id="ac2b015d27000cdc1554bc273a8539071"></a>

### `SYNA_USB_CLK`

```c
#define SYNA_USB_CLK ((USB2_CORE_CLK_CTRL << CGL_REG) | (8 << AXI_ID) | 35)
```

USB 时钟（Clock）。

<a id="a1fd4b7fd428ecdb6b77223071b801932"></a>

### `SYNA_XSPI_CLK`

```c
#define SYNA_XSPI_CLK ((XSPI_CORE_CLK_CTRL << CGL_REG) | (7 << AXI_ID) | 32)
```

xSPI 时钟（Clock）。

<a id="a90f5295e630e446572d87aa49d71964c"></a>

### `UART0_CORE_CLK_CTRL`

```c
#define UART0_CORE_CLK_CTRL 0x50
```

UART0 时钟门控辅助宏（Clock Gating Helper）。

<a id="a5e57580c17d65900d130a580ae850288"></a>

### `UART1_CORE_CLK_CTRL`

```c
#define UART1_CORE_CLK_CTRL 0x54
```

UART1 时钟门控辅助宏（Clock Gating Helper）。

<a id="afb192359bb0e0839a7b2d76abdc1b48a"></a>

### `USB2_CORE_CLK_CTRL`

```c
#define USB2_CORE_CLK_CTRL 0x64
```

USB 时钟门控辅助宏（Clock Gating Helper）。

<a id="a7690acc7f2717e0bdc4c133181a7aebd"></a>

### `XSPI_CORE_CLK_CTRL`

```c
#define XSPI_CORE_CLK_CTRL 0x30
```

时钟门控辅助宏（Clock Gating Helpers）。

XSPI 时钟门控辅助宏（Clock Gating Helper）。


## 12.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P849_syna_sr100_clock.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P011_zephyr__drivers__modem__simcom-sim7080.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_____w__zephyr__zephyr__subsys__testsuite__ztest__include__zephyr__ztest_test.h_文件参考.md)
