---
id: learning.zephyr-docs.api-file-reference.page-361
title: zephyr__dt-bindings__dma__rpi-pico-dma-rp2040.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-dma-rp2040_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第361章\_zephyr\_\_dt-bindings\_\_dma\_\_rpi-pico-dma-rp2040.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rpi-pico-dma-rp2040_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include "rpi-pico-dma-common.h"
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 361.1\_宏定义（Macros）

<a id="r_ae18eed6d9f3a59b17d98e1d327d67cf7"></a>

```c
#define RPI_PICO_DMA_SLOT_SPI0_TX RPI_PICO_DMA_DREQ_TO_SLOT(0x10)
```

相关声明：[RPI_PICO_DMA_SLOT_SPI0_TX](#ae18eed6d9f3a59b17d98e1d327d67cf7)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_aa955cbbf46c4c22ad7a57471aeed4344"></a>

```c
#define RPI_PICO_DMA_SLOT_SPI0_RX RPI_PICO_DMA_DREQ_TO_SLOT(0x11)
```

相关声明：[RPI_PICO_DMA_SLOT_SPI0_RX](#aa955cbbf46c4c22ad7a57471aeed4344)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a0076112cb2bb0ac30b53ba51b67cde13"></a>

```c
#define RPI_PICO_DMA_SLOT_SPI1_TX RPI_PICO_DMA_DREQ_TO_SLOT(0x12)
```

相关声明：[RPI_PICO_DMA_SLOT_SPI1_TX](#a0076112cb2bb0ac30b53ba51b67cde13)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a11b34c896fbb7993712f2a6228f0f470"></a>

```c
#define RPI_PICO_DMA_SLOT_SPI1_RX RPI_PICO_DMA_DREQ_TO_SLOT(0x13)
```

相关声明：[RPI_PICO_DMA_SLOT_SPI1_RX](#a11b34c896fbb7993712f2a6228f0f470)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a8e4849d94891581e54c20f1ad3053e61"></a>

```c
#define RPI_PICO_DMA_SLOT_UART0_TX RPI_PICO_DMA_DREQ_TO_SLOT(0x14)
```

相关声明：[RPI_PICO_DMA_SLOT_UART0_TX](#a8e4849d94891581e54c20f1ad3053e61)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a6c9dbf9ae4a775350dba0192d2d22ece"></a>

```c
#define RPI_PICO_DMA_SLOT_UART0_RX RPI_PICO_DMA_DREQ_TO_SLOT(0x15)
```

相关声明：[RPI_PICO_DMA_SLOT_UART0_RX](#a6c9dbf9ae4a775350dba0192d2d22ece)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_ae3b608078bb7b0076565d6ba01b7f2db"></a>

```c
#define RPI_PICO_DMA_SLOT_UART1_TX RPI_PICO_DMA_DREQ_TO_SLOT(0x16)
```

相关声明：[RPI_PICO_DMA_SLOT_UART1_TX](#ae3b608078bb7b0076565d6ba01b7f2db)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a867620802abfb1ea68f4de34bd9220c8"></a>

```c
#define RPI_PICO_DMA_SLOT_UART1_RX RPI_PICO_DMA_DREQ_TO_SLOT(0x17)
```

相关声明：[RPI_PICO_DMA_SLOT_UART1_RX](#a867620802abfb1ea68f4de34bd9220c8)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_aaf7f3a66c0e4bd1ba533c926e088bb72"></a>

```c
#define RPI_PICO_DMA_SLOT_PWM_WRAP0 RPI_PICO_DMA_DREQ_TO_SLOT(0x18)
```

相关声明：[RPI_PICO_DMA_SLOT_PWM_WRAP0](#aaf7f3a66c0e4bd1ba533c926e088bb72)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a4c4d3ebb5cb30a4af4289e72c74ac705"></a>

```c
#define RPI_PICO_DMA_SLOT_PWM_WRAP1 RPI_PICO_DMA_DREQ_TO_SLOT(0x19)
```

相关声明：[RPI_PICO_DMA_SLOT_PWM_WRAP1](#a4c4d3ebb5cb30a4af4289e72c74ac705)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a6807669224a777d8b8342d5a59b87370"></a>

```c
#define RPI_PICO_DMA_SLOT_PWM_WRAP2 RPI_PICO_DMA_DREQ_TO_SLOT(0x1A)
```

相关声明：[RPI_PICO_DMA_SLOT_PWM_WRAP2](#a6807669224a777d8b8342d5a59b87370)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a69039f5a94f8f30f46e488df743d8623"></a>

```c
#define RPI_PICO_DMA_SLOT_PWM_WRAP3 RPI_PICO_DMA_DREQ_TO_SLOT(0x1B)
```

相关声明：[RPI_PICO_DMA_SLOT_PWM_WRAP3](#a69039f5a94f8f30f46e488df743d8623)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a16432ea7735d3d2b46696eb42c3a5a78"></a>

```c
#define RPI_PICO_DMA_SLOT_PWM_WRAP4 RPI_PICO_DMA_DREQ_TO_SLOT(0x1C)
```

相关声明：[RPI_PICO_DMA_SLOT_PWM_WRAP4](#a16432ea7735d3d2b46696eb42c3a5a78)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a262317a40c039af688969d08b734cb30"></a>

```c
#define RPI_PICO_DMA_SLOT_PWM_WRAP5 RPI_PICO_DMA_DREQ_TO_SLOT(0x1D)
```

相关声明：[RPI_PICO_DMA_SLOT_PWM_WRAP5](#a262317a40c039af688969d08b734cb30)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_acc46df2f8f0ba68e155eb9dfb78d316b"></a>

```c
#define RPI_PICO_DMA_SLOT_PWM_WRAP6 RPI_PICO_DMA_DREQ_TO_SLOT(0x1E)
```

相关声明：[RPI_PICO_DMA_SLOT_PWM_WRAP6](#acc46df2f8f0ba68e155eb9dfb78d316b)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_acd268446715055b789d0b32527eaec18"></a>

```c
#define RPI_PICO_DMA_SLOT_PWM_WRAP7 RPI_PICO_DMA_DREQ_TO_SLOT(0x1F)
```

相关声明：[RPI_PICO_DMA_SLOT_PWM_WRAP7](#acd268446715055b789d0b32527eaec18)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_aeb3507fc3e3416b7bedfaebbfe8ba980"></a>

```c
#define RPI_PICO_DMA_SLOT_I2C0_TX RPI_PICO_DMA_DREQ_TO_SLOT(0x20)
```

相关声明：[RPI_PICO_DMA_SLOT_I2C0_TX](#aeb3507fc3e3416b7bedfaebbfe8ba980)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a22bdae09d66f57f0b2f26e6bd6b36f31"></a>

```c
#define RPI_PICO_DMA_SLOT_I2C0_RX RPI_PICO_DMA_DREQ_TO_SLOT(0x21)
```

相关声明：[RPI_PICO_DMA_SLOT_I2C0_RX](#a22bdae09d66f57f0b2f26e6bd6b36f31)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_afa10629c69c563ca959fe692f40bc5bb"></a>

```c
#define RPI_PICO_DMA_SLOT_I2C1_TX RPI_PICO_DMA_DREQ_TO_SLOT(0x22)
```

相关声明：[RPI_PICO_DMA_SLOT_I2C1_TX](#afa10629c69c563ca959fe692f40bc5bb)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a0f6717d3026d1c19c30e84bd4f91511b"></a>

```c
#define RPI_PICO_DMA_SLOT_I2C1_RX RPI_PICO_DMA_DREQ_TO_SLOT(0x23)
```

相关声明：[RPI_PICO_DMA_SLOT_I2C1_RX](#a0f6717d3026d1c19c30e84bd4f91511b)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_ab9e20d2a674fa5d1947c01a5dc2fb359"></a>

```c
#define RPI_PICO_DMA_SLOT_ADC RPI_PICO_DMA_DREQ_TO_SLOT(0x24)
```

相关声明：[RPI_PICO_DMA_SLOT_ADC](#ab9e20d2a674fa5d1947c01a5dc2fb359)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a831f08fba56848125d1e8773c05ac588"></a>

```c
#define RPI_PICO_DMA_SLOT_XIP_STREAM RPI_PICO_DMA_DREQ_TO_SLOT(0x25)
```

相关声明：[RPI_PICO_DMA_SLOT_XIP_STREAM](#a831f08fba56848125d1e8773c05ac588)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_a01f1ea52277e47bff8c3d76d6da7dab3"></a>

```c
#define RPI_PICO_DMA_SLOT_XIP_SSITX RPI_PICO_DMA_DREQ_TO_SLOT(0x26)
```

相关声明：[RPI_PICO_DMA_SLOT_XIP_SSITX](#a01f1ea52277e47bff8c3d76d6da7dab3)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

<a id="r_abdb688be5a52ddc5c3aacf2048096987"></a>

```c
#define RPI_PICO_DMA_SLOT_XIP_SSIRX RPI_PICO_DMA_DREQ_TO_SLOT(0x27)
```

相关声明：[RPI_PICO_DMA_SLOT_XIP_SSIRX](#abdb688be5a52ddc5c3aacf2048096987)、[RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)。

## 361.2\_详细说明（Detailed Documentation）

<a id="ab9e20d2a674fa5d1947c01a5dc2fb359"></a>

### `RPI_PICO_DMA_SLOT_ADC`

```c
#define RPI_PICO_DMA_SLOT_ADC RPI_PICO_DMA_DREQ_TO_SLOT(0x24)
```

<a id="a22bdae09d66f57f0b2f26e6bd6b36f31"></a>

### `RPI_PICO_DMA_SLOT_I2C0_RX`

```c
#define RPI_PICO_DMA_SLOT_I2C0_RX RPI_PICO_DMA_DREQ_TO_SLOT(0x21)
```

<a id="aeb3507fc3e3416b7bedfaebbfe8ba980"></a>

### `RPI_PICO_DMA_SLOT_I2C0_TX`

```c
#define RPI_PICO_DMA_SLOT_I2C0_TX RPI_PICO_DMA_DREQ_TO_SLOT(0x20)
```

<a id="a0f6717d3026d1c19c30e84bd4f91511b"></a>

### `RPI_PICO_DMA_SLOT_I2C1_RX`

```c
#define RPI_PICO_DMA_SLOT_I2C1_RX RPI_PICO_DMA_DREQ_TO_SLOT(0x23)
```

<a id="afa10629c69c563ca959fe692f40bc5bb"></a>

### `RPI_PICO_DMA_SLOT_I2C1_TX`

```c
#define RPI_PICO_DMA_SLOT_I2C1_TX RPI_PICO_DMA_DREQ_TO_SLOT(0x22)
```

<a id="aaf7f3a66c0e4bd1ba533c926e088bb72"></a>

### `RPI_PICO_DMA_SLOT_PWM_WRAP0`

```c
#define RPI_PICO_DMA_SLOT_PWM_WRAP0 RPI_PICO_DMA_DREQ_TO_SLOT(0x18)
```

<a id="a4c4d3ebb5cb30a4af4289e72c74ac705"></a>

### `RPI_PICO_DMA_SLOT_PWM_WRAP1`

```c
#define RPI_PICO_DMA_SLOT_PWM_WRAP1 RPI_PICO_DMA_DREQ_TO_SLOT(0x19)
```

<a id="a6807669224a777d8b8342d5a59b87370"></a>

### `RPI_PICO_DMA_SLOT_PWM_WRAP2`

```c
#define RPI_PICO_DMA_SLOT_PWM_WRAP2 RPI_PICO_DMA_DREQ_TO_SLOT(0x1A)
```

<a id="a69039f5a94f8f30f46e488df743d8623"></a>

### `RPI_PICO_DMA_SLOT_PWM_WRAP3`

```c
#define RPI_PICO_DMA_SLOT_PWM_WRAP3 RPI_PICO_DMA_DREQ_TO_SLOT(0x1B)
```

<a id="a16432ea7735d3d2b46696eb42c3a5a78"></a>

### `RPI_PICO_DMA_SLOT_PWM_WRAP4`

```c
#define RPI_PICO_DMA_SLOT_PWM_WRAP4 RPI_PICO_DMA_DREQ_TO_SLOT(0x1C)
```

<a id="a262317a40c039af688969d08b734cb30"></a>

### `RPI_PICO_DMA_SLOT_PWM_WRAP5`

```c
#define RPI_PICO_DMA_SLOT_PWM_WRAP5 RPI_PICO_DMA_DREQ_TO_SLOT(0x1D)
```

<a id="acc46df2f8f0ba68e155eb9dfb78d316b"></a>

### `RPI_PICO_DMA_SLOT_PWM_WRAP6`

```c
#define RPI_PICO_DMA_SLOT_PWM_WRAP6 RPI_PICO_DMA_DREQ_TO_SLOT(0x1E)
```

<a id="acd268446715055b789d0b32527eaec18"></a>

### `RPI_PICO_DMA_SLOT_PWM_WRAP7`

```c
#define RPI_PICO_DMA_SLOT_PWM_WRAP7 RPI_PICO_DMA_DREQ_TO_SLOT(0x1F)
```

<a id="aa955cbbf46c4c22ad7a57471aeed4344"></a>

### `RPI_PICO_DMA_SLOT_SPI0_RX`

```c
#define RPI_PICO_DMA_SLOT_SPI0_RX RPI_PICO_DMA_DREQ_TO_SLOT(0x11)
```

<a id="ae18eed6d9f3a59b17d98e1d327d67cf7"></a>

### `RPI_PICO_DMA_SLOT_SPI0_TX`

```c
#define RPI_PICO_DMA_SLOT_SPI0_TX RPI_PICO_DMA_DREQ_TO_SLOT(0x10)
```

<a id="a11b34c896fbb7993712f2a6228f0f470"></a>

### `RPI_PICO_DMA_SLOT_SPI1_RX`

```c
#define RPI_PICO_DMA_SLOT_SPI1_RX RPI_PICO_DMA_DREQ_TO_SLOT(0x13)
```

<a id="a0076112cb2bb0ac30b53ba51b67cde13"></a>

### `RPI_PICO_DMA_SLOT_SPI1_TX`

```c
#define RPI_PICO_DMA_SLOT_SPI1_TX RPI_PICO_DMA_DREQ_TO_SLOT(0x12)
```

<a id="a6c9dbf9ae4a775350dba0192d2d22ece"></a>

### `RPI_PICO_DMA_SLOT_UART0_RX`

```c
#define RPI_PICO_DMA_SLOT_UART0_RX RPI_PICO_DMA_DREQ_TO_SLOT(0x15)
```

<a id="a8e4849d94891581e54c20f1ad3053e61"></a>

### `RPI_PICO_DMA_SLOT_UART0_TX`

```c
#define RPI_PICO_DMA_SLOT_UART0_TX RPI_PICO_DMA_DREQ_TO_SLOT(0x14)
```

<a id="a867620802abfb1ea68f4de34bd9220c8"></a>

### `RPI_PICO_DMA_SLOT_UART1_RX`

```c
#define RPI_PICO_DMA_SLOT_UART1_RX RPI_PICO_DMA_DREQ_TO_SLOT(0x17)
```

<a id="ae3b608078bb7b0076565d6ba01b7f2db"></a>

### `RPI_PICO_DMA_SLOT_UART1_TX`

```c
#define RPI_PICO_DMA_SLOT_UART1_TX RPI_PICO_DMA_DREQ_TO_SLOT(0x16)
```

<a id="abdb688be5a52ddc5c3aacf2048096987"></a>

### `RPI_PICO_DMA_SLOT_XIP_SSIRX`

```c
#define RPI_PICO_DMA_SLOT_XIP_SSIRX RPI_PICO_DMA_DREQ_TO_SLOT(0x27)
```

<a id="a01f1ea52277e47bff8c3d76d6da7dab3"></a>

### `RPI_PICO_DMA_SLOT_XIP_SSITX`

```c
#define RPI_PICO_DMA_SLOT_XIP_SSITX RPI_PICO_DMA_DREQ_TO_SLOT(0x26)
```

<a id="a831f08fba56848125d1e8773c05ac588"></a>

### `RPI_PICO_DMA_SLOT_XIP_STREAM`

```c
#define RPI_PICO_DMA_SLOT_XIP_STREAM RPI_PICO_DMA_DREQ_TO_SLOT(0x25)
```


## 361.3\_原页交叉引用（Cross References）

- [rpi-pico-dma-common.h](../api_source_supplement_reference/P166_rpi-pico-dma-common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P723_rpi-pico-dma-rp2040.h_源码浏览.md)
- [RPI_PICO_DMA_DREQ_TO_SLOT](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md#a108c9650b4eb398c9994d7c1683beaa8)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P360_zephyr__dt-bindings__dma__rpi-pico-dma-common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P362_zephyr__dt-bindings__dma__rpi-pico-dma-rp2350.h_文件参考.md)
