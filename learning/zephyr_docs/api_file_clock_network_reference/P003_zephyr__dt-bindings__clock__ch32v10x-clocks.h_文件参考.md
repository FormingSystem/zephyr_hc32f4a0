---
id: learning.zephyr-docs.api-file-clock-network-reference.page-3
title: zephyr__dt-bindings__clock__ch32v10x-clocks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ch32v10x-clocks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_dt-bindings\_\_clock\_\_ch32v10x-clocks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ch32v10x-clocks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于设备树绑定（Devicetree Bindings）的CH32V10x外设时钟标识符。

查看此文件的源码。

<a id="details"></a>

用于设备树绑定（Devicetree Bindings）的CH32V10x外设时钟标识符。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="r_a1918cd6f6d15fe82faf96e08f1b91e71"></a>

```c
#define CH32V10X_AHB_PCENR_OFFSET 0
```

相关声明：[CH32V10X_AHB_PCENR_OFFSET](#a1918cd6f6d15fe82faf96e08f1b91e71)。

AHB 总线寄存器偏移量（Bus Register Offset）。

<a id="r_aa71f26820937bfa8ec2eed99a1c8072f"></a>

```c
#define CH32V10X_APB2_PCENR_OFFSET 1
```

相关声明：[CH32V10X_APB2_PCENR_OFFSET](#aa71f26820937bfa8ec2eed99a1c8072f)。

APB2 总线寄存器偏移量（Bus Register Offset）。

<a id="r_aa78f2f054afa6f334125df4dbf8fa283"></a>

```c
#define CH32V10X_APB1_PCENR_OFFSET 2
```

相关声明：[CH32V10X_APB1_PCENR_OFFSET](#aa78f2f054afa6f334125df4dbf8fa283)。

APB1 总线寄存器偏移量（Bus Register Offset）。

<a id="r_ae3310d8b4193e6568ec7692f7a9c7b50"></a>

```c
#define CH32V10X_CLOCK_CONFIG(bus, bit)
```

相关声明：[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

根据总线与位位置编码时钟标识符（Clock Identifier）。

<a id="r_ab0aa9199f833deaed88c71a5ace260a9"></a>

```c
#define CH32V10X_CLOCK_DMA1 CH32V10X_CLOCK_CONFIG(AHB, 0)
```

相关声明：[CH32V10X_CLOCK_DMA1](#ab0aa9199f833deaed88c71a5ace260a9)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

DMA1 时钟（Clock），位于 AHB。

<a id="r_ac5aebfc5868c3b629c5c704a2acda902"></a>

```c
#define CH32V10X_CLOCK_SRAM CH32V10X_CLOCK_CONFIG(AHB, 2)
```

相关声明：[CH32V10X_CLOCK_SRAM](#ac5aebfc5868c3b629c5c704a2acda902)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

SRAM 时钟（Clock），位于 AHB。

<a id="r_a39384f525270230ef9cdbc01e848b8cb"></a>

```c
#define CH32V10X_CLOCK_FLITF CH32V10X_CLOCK_CONFIG(AHB, 4)
```

相关声明：[CH32V10X_CLOCK_FLITF](#a39384f525270230ef9cdbc01e848b8cb)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

闪存接口（Flash Interface） 时钟（Clock），位于 AHB。

<a id="r_a742053475b8886ed9e8deb65e1a6ab80"></a>

```c
#define CH32V10X_CLOCK_CRC CH32V10X_CLOCK_CONFIG(AHB, 6)
```

相关声明：[CH32V10X_CLOCK_CRC](#a742053475b8886ed9e8deb65e1a6ab80)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

CRC 时钟（Clock），位于 AHB。

<a id="r_a6af8344fb15ef71efa42aefea4c29312"></a>

```c
#define CH32V10X_CLOCK_FSMC CH32V10X_CLOCK_CONFIG(AHB, 8)
```

相关声明：[CH32V10X_CLOCK_FSMC](#a6af8344fb15ef71efa42aefea4c29312)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

FSMC 时钟（Clock），位于 AHB。

<a id="r_a6e0ef723a316295a98dbeda185bf7953"></a>

```c
#define CH32V10X_CLOCK_USBHD CH32V10X_CLOCK_CONFIG(AHB, 12)
```

相关声明：[CH32V10X_CLOCK_USBHD](#a6e0ef723a316295a98dbeda185bf7953)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

USB HD 时钟（Clock），位于 AHB。

<a id="r_a72e89ecbb43f067a20e0caa3567ee916"></a>

```c
#define CH32V10X_CLOCK_AFIO CH32V10X_CLOCK_CONFIG(APB2, 0)
```

相关声明：[CH32V10X_CLOCK_AFIO](#a72e89ecbb43f067a20e0caa3567ee916)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

AFIO 时钟（Clock），位于 APB2。

<a id="r_a9384e8276e6b91cff3af390e44ac1716"></a>

```c
#define CH32V10X_CLOCK_IOPA CH32V10X_CLOCK_CONFIG(APB2, 2)
```

相关声明：[CH32V10X_CLOCK_IOPA](#a9384e8276e6b91cff3af390e44ac1716)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

GPIO 端口 A 时钟（Clock），位于 APB2。

<a id="r_a2f2b8390267f95591bfcbef0bde4d680"></a>

```c
#define CH32V10X_CLOCK_IOPB CH32V10X_CLOCK_CONFIG(APB2, 3)
```

相关声明：[CH32V10X_CLOCK_IOPB](#a2f2b8390267f95591bfcbef0bde4d680)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

GPIO 端口 B 时钟（Clock），位于 APB2。

<a id="r_aa33e90cb22eecaa8c162562f53a29b05"></a>

```c
#define CH32V10X_CLOCK_IOPC CH32V10X_CLOCK_CONFIG(APB2, 4)
```

相关声明：[CH32V10X_CLOCK_IOPC](#aa33e90cb22eecaa8c162562f53a29b05)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

GPIO 端口 C 时钟（Clock），位于 APB2。

<a id="r_aba1d579077a1962608e339583128157b"></a>

```c
#define CH32V10X_CLOCK_IOPD CH32V10X_CLOCK_CONFIG(APB2, 5)
```

相关声明：[CH32V10X_CLOCK_IOPD](#aba1d579077a1962608e339583128157b)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

GPIO 端口 D 时钟（Clock），位于 APB2。

<a id="r_a9491c6aa00bbfab63fecbacd490183d4"></a>

```c
#define CH32V10X_CLOCK_ADC1 CH32V10X_CLOCK_CONFIG(APB2, 9)
```

相关声明：[CH32V10X_CLOCK_ADC1](#a9491c6aa00bbfab63fecbacd490183d4)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

ADC1 时钟（Clock），位于 APB2。

<a id="r_acc3a9ae84e551804a9e5126da651fc7b"></a>

```c
#define CH32V10X_CLOCK_TIM1 CH32V10X_CLOCK_CONFIG(APB2, 11)
```

相关声明：[CH32V10X_CLOCK_TIM1](#acc3a9ae84e551804a9e5126da651fc7b)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

TIM1 时钟（Clock），位于 APB2。

<a id="r_ad3e5efc65d834525d02eddc21d482365"></a>

```c
#define CH32V10X_CLOCK_SPI1 CH32V10X_CLOCK_CONFIG(APB2, 12)
```

相关声明：[CH32V10X_CLOCK_SPI1](#ad3e5efc65d834525d02eddc21d482365)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

SPI1 时钟（Clock），位于 APB2。

<a id="r_a4948fef8c4b34821b70f1894301b3abe"></a>

```c
#define CH32V10X_CLOCK_USART1 CH32V10X_CLOCK_CONFIG(APB2, 14)
```

相关声明：[CH32V10X_CLOCK_USART1](#a4948fef8c4b34821b70f1894301b3abe)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

USART1 时钟（Clock），位于 APB2。

<a id="r_a0c175c653740fa05279d3da20839c090"></a>

```c
#define CH32V10X_CLOCK_TIM2 CH32V10X_CLOCK_CONFIG(APB1, 0)
```

相关声明：[CH32V10X_CLOCK_TIM2](#a0c175c653740fa05279d3da20839c090)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

TIM2 时钟（Clock），位于 APB1。

<a id="r_a2284cde25f82d9632979f2b7d73ac5b9"></a>

```c
#define CH32V10X_CLOCK_TIM3 CH32V10X_CLOCK_CONFIG(APB1, 1)
```

相关声明：[CH32V10X_CLOCK_TIM3](#a2284cde25f82d9632979f2b7d73ac5b9)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

TIM3 时钟（Clock），位于 APB1。

<a id="r_a7f2821a8e37567000655c63e402868da"></a>

```c
#define CH32V10X_CLOCK_TIM4 CH32V10X_CLOCK_CONFIG(APB1, 2)
```

相关声明：[CH32V10X_CLOCK_TIM4](#a7f2821a8e37567000655c63e402868da)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

TIM4 时钟（Clock），位于 APB1。

<a id="r_a36138ea14255f8d4b74a0f67c869a162"></a>

```c
#define CH32V10X_CLOCK_WWDG CH32V10X_CLOCK_CONFIG(APB1, 11)
```

相关声明：[CH32V10X_CLOCK_WWDG](#a36138ea14255f8d4b74a0f67c869a162)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

WWDG 时钟（Clock），位于 APB1。

<a id="r_a5079861b2fb9231039567e805a265962"></a>

```c
#define CH32V10X_CLOCK_SPI2 CH32V10X_CLOCK_CONFIG(APB1, 14)
```

相关声明：[CH32V10X_CLOCK_SPI2](#a5079861b2fb9231039567e805a265962)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

SPI2 时钟（Clock），位于 APB1。

<a id="r_a611e30e0ca0904ff6823b4fa7c6aec6c"></a>

```c
#define CH32V10X_CLOCK_USART2 CH32V10X_CLOCK_CONFIG(APB1, 17)
```

相关声明：[CH32V10X_CLOCK_USART2](#a611e30e0ca0904ff6823b4fa7c6aec6c)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

USART2 时钟（Clock），位于 APB1。

<a id="r_a0e2d8a88e6b8f5374334b187f859370d"></a>

```c
#define CH32V10X_CLOCK_USART3 CH32V10X_CLOCK_CONFIG(APB1, 18)
```

相关声明：[CH32V10X_CLOCK_USART3](#a0e2d8a88e6b8f5374334b187f859370d)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

USART3 时钟（Clock），位于 APB1。

<a id="r_a99a6ac3a5209132a90dd1bdc6954720c"></a>

```c
#define CH32V10X_CLOCK_I2C1 CH32V10X_CLOCK_CONFIG(APB1, 21)
```

相关声明：[CH32V10X_CLOCK_I2C1](#a99a6ac3a5209132a90dd1bdc6954720c)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

I2C1 时钟（Clock），位于 APB1。

<a id="r_a7dc5f20ed169a871396edfb0391bbd4b"></a>

```c
#define CH32V10X_CLOCK_I2C2 CH32V10X_CLOCK_CONFIG(APB1, 22)
```

相关声明：[CH32V10X_CLOCK_I2C2](#a7dc5f20ed169a871396edfb0391bbd4b)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

I2C2 时钟（Clock），位于 APB1。

<a id="r_ac8a5893f7a6444a4cb9103d57d1bc2a2"></a>

```c
#define CH32V10X_CLOCK_USBD CH32V10X_CLOCK_CONFIG(APB1, 23)
```

相关声明：[CH32V10X_CLOCK_USBD](#ac8a5893f7a6444a4cb9103d57d1bc2a2)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

USB 设备（Device） 时钟（Clock），位于 APB1。

<a id="r_a6e745800323f55f2b27937eb96100211"></a>

```c
#define CH32V10X_CLOCK_CAN1 CH32V10X_CLOCK_CONFIG(APB1, 25)
```

相关声明：[CH32V10X_CLOCK_CAN1](#a6e745800323f55f2b27937eb96100211)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

CAN1 时钟（Clock），位于 APB1。

<a id="r_a614a892a9c08953d393ebc7c662b401b"></a>

```c
#define CH32V10X_CLOCK_BKP CH32V10X_CLOCK_CONFIG(APB1, 27)
```

相关声明：[CH32V10X_CLOCK_BKP](#a614a892a9c08953d393ebc7c662b401b)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

备份域（Backup Domain） 时钟（Clock），位于 APB1。

<a id="r_a8ff5a8b2eb551bc35e7578d2cbe08757"></a>

```c
#define CH32V10X_CLOCK_PWR CH32V10X_CLOCK_CONFIG(APB1, 28)
```

相关声明：[CH32V10X_CLOCK_PWR](#a8ff5a8b2eb551bc35e7578d2cbe08757)、[CH32V10X_CLOCK_CONFIG](#ae3310d8b4193e6568ec7692f7a9c7b50)。

电源接口（Power Interface） 时钟（Clock），位于 APB1。

## 3.2\_详细说明（Detailed Documentation）

<a id="a1918cd6f6d15fe82faf96e08f1b91e71"></a>

### `CH32V10X_AHB_PCENR_OFFSET`

```c
#define CH32V10X_AHB_PCENR_OFFSET 0
```

AHB 总线寄存器偏移量（Bus Register Offset）。

<a id="aa78f2f054afa6f334125df4dbf8fa283"></a>

### `CH32V10X_APB1_PCENR_OFFSET`

```c
#define CH32V10X_APB1_PCENR_OFFSET 2
```

APB1 总线寄存器偏移量（Bus Register Offset）。

<a id="aa71f26820937bfa8ec2eed99a1c8072f"></a>

### `CH32V10X_APB2_PCENR_OFFSET`

```c
#define CH32V10X_APB2_PCENR_OFFSET 1
```

APB2 总线寄存器偏移量（Bus Register Offset）。

<a id="a9491c6aa00bbfab63fecbacd490183d4"></a>

### `CH32V10X_CLOCK_ADC1`

```c
#define CH32V10X_CLOCK_ADC1 CH32V10X_CLOCK_CONFIG(APB2, 9)
```

ADC1 时钟（Clock），位于 APB2。

<a id="a72e89ecbb43f067a20e0caa3567ee916"></a>

### `CH32V10X_CLOCK_AFIO`

```c
#define CH32V10X_CLOCK_AFIO CH32V10X_CLOCK_CONFIG(APB2, 0)
```

AFIO 时钟（Clock），位于 APB2。

<a id="a614a892a9c08953d393ebc7c662b401b"></a>

### `CH32V10X_CLOCK_BKP`

```c
#define CH32V10X_CLOCK_BKP CH32V10X_CLOCK_CONFIG(APB1, 27)
```

备份域（Backup Domain） 时钟（Clock），位于 APB1。

<a id="a6e745800323f55f2b27937eb96100211"></a>

### `CH32V10X_CLOCK_CAN1`

```c
#define CH32V10X_CLOCK_CAN1 CH32V10X_CLOCK_CONFIG(APB1, 25)
```

CAN1 时钟（Clock），位于 APB1。

<a id="ae3310d8b4193e6568ec7692f7a9c7b50"></a>

### `CH32V10X_CLOCK_CONFIG`

```c
#define CH32V10X_CLOCK_CONFIG ( bus, bit )
```

展开值（Value）：

```c
(((CH32V10X_##bus##_PCENR_OFFSET) << 5) | (bit))
```

根据总线与位位置编码时钟标识符（Clock Identifier）。

<a id="a742053475b8886ed9e8deb65e1a6ab80"></a>

### `CH32V10X_CLOCK_CRC`

```c
#define CH32V10X_CLOCK_CRC CH32V10X_CLOCK_CONFIG(AHB, 6)
```

CRC 时钟（Clock），位于 AHB。

<a id="ab0aa9199f833deaed88c71a5ace260a9"></a>

### `CH32V10X_CLOCK_DMA1`

```c
#define CH32V10X_CLOCK_DMA1 CH32V10X_CLOCK_CONFIG(AHB, 0)
```

DMA1 时钟（Clock），位于 AHB。

<a id="a39384f525270230ef9cdbc01e848b8cb"></a>

### `CH32V10X_CLOCK_FLITF`

```c
#define CH32V10X_CLOCK_FLITF CH32V10X_CLOCK_CONFIG(AHB, 4)
```

闪存接口（Flash Interface） 时钟（Clock），位于 AHB。

<a id="a6af8344fb15ef71efa42aefea4c29312"></a>

### `CH32V10X_CLOCK_FSMC`

```c
#define CH32V10X_CLOCK_FSMC CH32V10X_CLOCK_CONFIG(AHB, 8)
```

FSMC 时钟（Clock），位于 AHB。

<a id="a99a6ac3a5209132a90dd1bdc6954720c"></a>

### `CH32V10X_CLOCK_I2C1`

```c
#define CH32V10X_CLOCK_I2C1 CH32V10X_CLOCK_CONFIG(APB1, 21)
```

I2C1 时钟（Clock），位于 APB1。

<a id="a7dc5f20ed169a871396edfb0391bbd4b"></a>

### `CH32V10X_CLOCK_I2C2`

```c
#define CH32V10X_CLOCK_I2C2 CH32V10X_CLOCK_CONFIG(APB1, 22)
```

I2C2 时钟（Clock），位于 APB1。

<a id="a9384e8276e6b91cff3af390e44ac1716"></a>

### `CH32V10X_CLOCK_IOPA`

```c
#define CH32V10X_CLOCK_IOPA CH32V10X_CLOCK_CONFIG(APB2, 2)
```

GPIO 端口 A 时钟（Clock），位于 APB2。

<a id="a2f2b8390267f95591bfcbef0bde4d680"></a>

### `CH32V10X_CLOCK_IOPB`

```c
#define CH32V10X_CLOCK_IOPB CH32V10X_CLOCK_CONFIG(APB2, 3)
```

GPIO 端口 B 时钟（Clock），位于 APB2。

<a id="aa33e90cb22eecaa8c162562f53a29b05"></a>

### `CH32V10X_CLOCK_IOPC`

```c
#define CH32V10X_CLOCK_IOPC CH32V10X_CLOCK_CONFIG(APB2, 4)
```

GPIO 端口 C 时钟（Clock），位于 APB2。

<a id="aba1d579077a1962608e339583128157b"></a>

### `CH32V10X_CLOCK_IOPD`

```c
#define CH32V10X_CLOCK_IOPD CH32V10X_CLOCK_CONFIG(APB2, 5)
```

GPIO 端口 D 时钟（Clock），位于 APB2。

<a id="a8ff5a8b2eb551bc35e7578d2cbe08757"></a>

### `CH32V10X_CLOCK_PWR`

```c
#define CH32V10X_CLOCK_PWR CH32V10X_CLOCK_CONFIG(APB1, 28)
```

电源接口（Power Interface） 时钟（Clock），位于 APB1。

<a id="ad3e5efc65d834525d02eddc21d482365"></a>

### `CH32V10X_CLOCK_SPI1`

```c
#define CH32V10X_CLOCK_SPI1 CH32V10X_CLOCK_CONFIG(APB2, 12)
```

SPI1 时钟（Clock），位于 APB2。

<a id="a5079861b2fb9231039567e805a265962"></a>

### `CH32V10X_CLOCK_SPI2`

```c
#define CH32V10X_CLOCK_SPI2 CH32V10X_CLOCK_CONFIG(APB1, 14)
```

SPI2 时钟（Clock），位于 APB1。

<a id="ac5aebfc5868c3b629c5c704a2acda902"></a>

### `CH32V10X_CLOCK_SRAM`

```c
#define CH32V10X_CLOCK_SRAM CH32V10X_CLOCK_CONFIG(AHB, 2)
```

SRAM 时钟（Clock），位于 AHB。

<a id="acc3a9ae84e551804a9e5126da651fc7b"></a>

### `CH32V10X_CLOCK_TIM1`

```c
#define CH32V10X_CLOCK_TIM1 CH32V10X_CLOCK_CONFIG(APB2, 11)
```

TIM1 时钟（Clock），位于 APB2。

<a id="a0c175c653740fa05279d3da20839c090"></a>

### `CH32V10X_CLOCK_TIM2`

```c
#define CH32V10X_CLOCK_TIM2 CH32V10X_CLOCK_CONFIG(APB1, 0)
```

TIM2 时钟（Clock），位于 APB1。

<a id="a2284cde25f82d9632979f2b7d73ac5b9"></a>

### `CH32V10X_CLOCK_TIM3`

```c
#define CH32V10X_CLOCK_TIM3 CH32V10X_CLOCK_CONFIG(APB1, 1)
```

TIM3 时钟（Clock），位于 APB1。

<a id="a7f2821a8e37567000655c63e402868da"></a>

### `CH32V10X_CLOCK_TIM4`

```c
#define CH32V10X_CLOCK_TIM4 CH32V10X_CLOCK_CONFIG(APB1, 2)
```

TIM4 时钟（Clock），位于 APB1。

<a id="a4948fef8c4b34821b70f1894301b3abe"></a>

### `CH32V10X_CLOCK_USART1`

```c
#define CH32V10X_CLOCK_USART1 CH32V10X_CLOCK_CONFIG(APB2, 14)
```

USART1 时钟（Clock），位于 APB2。

<a id="a611e30e0ca0904ff6823b4fa7c6aec6c"></a>

### `CH32V10X_CLOCK_USART2`

```c
#define CH32V10X_CLOCK_USART2 CH32V10X_CLOCK_CONFIG(APB1, 17)
```

USART2 时钟（Clock），位于 APB1。

<a id="a0e2d8a88e6b8f5374334b187f859370d"></a>

### `CH32V10X_CLOCK_USART3`

```c
#define CH32V10X_CLOCK_USART3 CH32V10X_CLOCK_CONFIG(APB1, 18)
```

USART3 时钟（Clock），位于 APB1。

<a id="ac8a5893f7a6444a4cb9103d57d1bc2a2"></a>

### `CH32V10X_CLOCK_USBD`

```c
#define CH32V10X_CLOCK_USBD CH32V10X_CLOCK_CONFIG(APB1, 23)
```

USB 设备（Device） 时钟（Clock），位于 APB1。

<a id="a6e0ef723a316295a98dbeda185bf7953"></a>

### `CH32V10X_CLOCK_USBHD`

```c
#define CH32V10X_CLOCK_USBHD CH32V10X_CLOCK_CONFIG(AHB, 12)
```

USB HD 时钟（Clock），位于 AHB。

<a id="a36138ea14255f8d4b74a0f67c869a162"></a>

### `CH32V10X_CLOCK_WWDG`

```c
#define CH32V10X_CLOCK_WWDG CH32V10X_CLOCK_CONFIG(APB1, 11)
```

WWDG 时钟（Clock），位于 APB1。


## 3.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P093_ch32v10x-clocks.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P002_zephyr__bluetooth__att.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__bluetooth__cs.h_文件参考.md)
