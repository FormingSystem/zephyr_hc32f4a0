---
id: learning.zephyr-docs.api-file-flash-test-reference.page-7
title: zephyr__dt-bindings__clock__lpc84x-clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lpc84x-clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_dt-bindings\_\_clock\_\_lpc84x-clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lpc84x-clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP LPC84x时钟门控定义（Clock Gate Definitions）。

查看此文件的源码。

<a id="details"></a>

NXP LPC84x 时钟门控定义（Clock Gate Definitions）。本头文件提供 LPC84x 时钟控制驱动所用的编码时钟门控标识符（Encoded Clock Gate Identifiers）。每个标识符都编码了 AHB 时钟控制寄存器偏移量（Register Offset）及位位置（Bit Position）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="r_a9ea5311cfc3b17f761f0788969e8473a"></a>

```c
#define LPC84X_SYS_AHB_CLK_CTRL0 0U
```

相关声明：[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

SYS_AHB_CLK_CTRL0 寄存器偏移量（Register Offset）。

<a id="r_a46fbc1c1a71af64f2ce04d60159a969f"></a>

```c
#define LPC84X_SYS_AHB_CLK_CTRL1 4U
```

相关声明：[LPC84X_SYS_AHB_CLK_CTRL1](#a46fbc1c1a71af64f2ce04d60159a969f)。

SYS_AHB_CLK_CTRL1 寄存器偏移量（Register Offset）。

<a id="r_ae689958107c3afd34ebf4621f55e4b0b"></a>

```c
#define LPC84X_CLK_GATE_DEFINE(reg, bit)
```

相关声明：[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)。

编码 LPC84x 时钟门控标识符（Clock Gate Identifier）。

<a id="r_ae8cb973627b8124804bf367f3288ee7e"></a>

```c
#define LPC84X_CLK_ROM LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 1U)
```

相关声明：[LPC84X_CLK_ROM](#ae8cb973627b8124804bf367f3288ee7e)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

ROM 时钟门控（Clock Gate）。

<a id="r_a775860ff41f41c3cae8223dd2c74a674"></a>

```c
#define LPC84X_CLK_RAM0_1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 2U)
```

相关声明：[LPC84X_CLK_RAM0_1](#a775860ff41f41c3cae8223dd2c74a674)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

RAM0 和 RAM1 时钟门控（Clock Gate）。

<a id="r_a87cf30fb969db276ee95db32d0926c41"></a>

```c
#define LPC84X_CLK_FLASH LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 4U)
```

相关声明：[LPC84X_CLK_FLASH](#a87cf30fb969db276ee95db32d0926c41)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

FLASH 时钟门控（Clock Gate）。

<a id="r_a45b2fb064437bf70801308d4863004ea"></a>

```c
#define LPC84X_CLK_I2C0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 5U)
```

相关声明：[LPC84X_CLK_I2C0](#a45b2fb064437bf70801308d4863004ea)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

I2C0 时钟门控（Clock Gate）。

<a id="r_ab8627717a27ada335942b82d1bded632"></a>

```c
#define LPC84X_CLK_GPIO0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 6U)
```

相关声明：[LPC84X_CLK_GPIO0](#ab8627717a27ada335942b82d1bded632)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

GPIO0 时钟门控（Clock Gate）。

<a id="r_a5a5ed25ffcaa31408aebcea6cd08a385"></a>

```c
#define LPC84X_CLK_SWM LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 7U)
```

相关声明：[LPC84X_CLK_SWM](#a5a5ed25ffcaa31408aebcea6cd08a385)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

开关矩阵（Switch Matrix，SWM） 时钟门控（Clock Gate）。

<a id="r_a878cdb89e4ccc0e6247a8f60cb81caa2"></a>

```c
#define LPC84X_CLK_SCT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 8U)
```

相关声明：[LPC84X_CLK_SCT](#a878cdb89e4ccc0e6247a8f60cb81caa2)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

状态可配置定时器（State Configurable Timer，SCT） 时钟门控（Clock Gate）。

<a id="r_a79cf8c1353921f01ab6d2b2a237b16b1"></a>

```c
#define LPC84X_CLK_WKT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 9U)
```

相关声明：[LPC84X_CLK_WKT](#a79cf8c1353921f01ab6d2b2a237b16b1)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

唤醒定时器（Wake-up Timer，WKT） 时钟门控（Clock Gate）。

<a id="r_a0b0bedfa3c2a63820bef24679733d00f"></a>

```c
#define LPC84X_CLK_MRT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 10U)
```

相关声明：[LPC84X_CLK_MRT](#a0b0bedfa3c2a63820bef24679733d00f)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

多速率定时器（Multi-Rate Timer，MRT） 时钟门控（Clock Gate）。

<a id="r_a38a63d9ee81fe0b11237fa76a24405da"></a>

```c
#define LPC84X_CLK_SPI0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 11U)
```

相关声明：[LPC84X_CLK_SPI0](#a38a63d9ee81fe0b11237fa76a24405da)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

SPI0 时钟门控（Clock Gate）。

<a id="r_af3cbd69fbad2f9826a59edd888b895b4"></a>

```c
#define LPC84X_CLK_SPI1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 12U)
```

相关声明：[LPC84X_CLK_SPI1](#af3cbd69fbad2f9826a59edd888b895b4)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

SPI1 时钟门控（Clock Gate）。

<a id="r_adac7762135367602532a81288b4162a4"></a>

```c
#define LPC84X_CLK_CRC LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 13U)
```

相关声明：[LPC84X_CLK_CRC](#adac7762135367602532a81288b4162a4)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

CRC 引擎（CRC Engine） 时钟门控（Clock Gate）。

<a id="r_a75c3500a6713eed989baea00d7ba8728"></a>

```c
#define LPC84X_CLK_UART0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 14U)
```

相关声明：[LPC84X_CLK_UART0](#a75c3500a6713eed989baea00d7ba8728)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

UART0 时钟门控（Clock Gate）。

<a id="r_a154daba51c7d0e41b7e47042335f646c"></a>

```c
#define LPC84X_CLK_UART1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 15U)
```

相关声明：[LPC84X_CLK_UART1](#a154daba51c7d0e41b7e47042335f646c)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

UART1 时钟门控（Clock Gate）。

<a id="r_a1e5461c1f12d58970ce80e3f0ff4c7d2"></a>

```c
#define LPC84X_CLK_UART2 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 16U)
```

相关声明：[LPC84X_CLK_UART2](#a1e5461c1f12d58970ce80e3f0ff4c7d2)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

UART2 时钟门控（Clock Gate）。

<a id="r_a22435d2e5b400884818b5b2c03b14746"></a>

```c
#define LPC84X_CLK_WWDT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 17U)
```

相关声明：[LPC84X_CLK_WWDT](#a22435d2e5b400884818b5b2c03b14746)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

窗口看门狗定时器（Windowed Watchdog Timer） 时钟门控（Clock Gate）。

<a id="r_a97d81d50a44a092caa0aaf2af7ebc992"></a>

```c
#define LPC84X_CLK_IOCON LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 18U)
```

相关声明：[LPC84X_CLK_IOCON](#a97d81d50a44a092caa0aaf2af7ebc992)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

IOCON 时钟门控（Clock Gate）。

<a id="r_a20b494e041d23509f1960631bc0b7e44"></a>

```c
#define LPC84X_CLK_ACMP LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 19U)
```

相关声明：[LPC84X_CLK_ACMP](#a20b494e041d23509f1960631bc0b7e44)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

模拟比较器（Analog Comparator） 时钟门控（Clock Gate）。

<a id="r_a148ae5e042a49e58ffda3bab509e29b8"></a>

```c
#define LPC84X_CLK_GPIO1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 20U)
```

相关声明：[LPC84X_CLK_GPIO1](#a148ae5e042a49e58ffda3bab509e29b8)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

GPIO1 时钟门控（Clock Gate）。

<a id="r_a440795694db3730f28062fd39bfe993a"></a>

```c
#define LPC84X_CLK_I2C1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 21U)
```

相关声明：[LPC84X_CLK_I2C1](#a440795694db3730f28062fd39bfe993a)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

I2C1 时钟门控（Clock Gate）。

<a id="r_a91ba67a3d8761f151d8f1262452d2a0a"></a>

```c
#define LPC84X_CLK_I2C2 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 22U)
```

相关声明：[LPC84X_CLK_I2C2](#a91ba67a3d8761f151d8f1262452d2a0a)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

I2C2 时钟门控（Clock Gate）。

<a id="r_a72ec1cf2f414ac7e562baffdd7e520ef"></a>

```c
#define LPC84X_CLK_I2C3 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 23U)
```

相关声明：[LPC84X_CLK_I2C3](#a72ec1cf2f414ac7e562baffdd7e520ef)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

I2C3 时钟门控（Clock Gate）。

<a id="r_a9f00c67c96947b916e87f3c3bba39084"></a>

```c
#define LPC84X_CLK_ADC LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 24U)
```

相关声明：[LPC84X_CLK_ADC](#a9f00c67c96947b916e87f3c3bba39084)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

ADC 时钟门控（Clock Gate）。

<a id="r_a493f8a0441b79ee57c58a1d81be3435d"></a>

```c
#define LPC84X_CLK_CTIMER0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 25U)
```

相关声明：[LPC84X_CLK_CTIMER0](#a493f8a0441b79ee57c58a1d81be3435d)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

CTIMER0 时钟门控（Clock Gate）。

<a id="r_aae9a524394ed8b896d5148262c0006ed"></a>

```c
#define LPC84X_CLK_MTB LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 26U)
```

相关声明：[LPC84X_CLK_MTB](#aae9a524394ed8b896d5148262c0006ed)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

MTB 时钟门控（Clock Gate）。

<a id="r_a4eee194733f1a954e14cdb259acfcff9"></a>

```c
#define LPC84X_CLK_DAC0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 27U)
```

相关声明：[LPC84X_CLK_DAC0](#a4eee194733f1a954e14cdb259acfcff9)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

DAC0 时钟门控（Clock Gate）。

<a id="r_a1b67c6322eb9c99814d8b277515adf17"></a>

```c
#define LPC84X_CLK_GPIOINT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 28U)
```

相关声明：[LPC84X_CLK_GPIOINT](#a1b67c6322eb9c99814d8b277515adf17)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

GPIO 中断（GPIO Interrupt） 时钟门控（Clock Gate）。

<a id="r_ac0c6e79c73700754e9efebff7ab68c2e"></a>

```c
#define LPC84X_CLK_DMA LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 29U)
```

相关声明：[LPC84X_CLK_DMA](#ac0c6e79c73700754e9efebff7ab68c2e)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

DMA 时钟门控（Clock Gate）。

<a id="r_ae1a7b168be530a5bdb48aff77c2e5700"></a>

```c
#define LPC84X_CLK_UART3 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 30U)
```

相关声明：[LPC84X_CLK_UART3](#ae1a7b168be530a5bdb48aff77c2e5700)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

UART3 时钟门控（Clock Gate）。

<a id="r_ae388bb1b215097b0d2b18b9e51352e2f"></a>

```c
#define LPC84X_CLK_UART4 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 31U)
```

相关声明：[LPC84X_CLK_UART4](#ae388bb1b215097b0d2b18b9e51352e2f)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL0](#a9ea5311cfc3b17f761f0788969e8473a)。

UART4 时钟门控（Clock Gate）。

<a id="r_aaf7c9a3429b7b6dc86990f17af917ae7"></a>

```c
#define LPC84X_CLK_CAPT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL1, 0U)
```

相关声明：[LPC84X_CLK_CAPT](#aaf7c9a3429b7b6dc86990f17af917ae7)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL1](#a46fbc1c1a71af64f2ce04d60159a969f)。

CAPT 时钟门控（Clock Gate）。

<a id="r_a050fdff7e14986cd083e0e7385f9767f"></a>

```c
#define LPC84X_CLK_DAC1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL1, 1U)
```

相关声明：[LPC84X_CLK_DAC1](#a050fdff7e14986cd083e0e7385f9767f)、[LPC84X_CLK_GATE_DEFINE](#ae689958107c3afd34ebf4621f55e4b0b)、[LPC84X_SYS_AHB_CLK_CTRL1](#a46fbc1c1a71af64f2ce04d60159a969f)。

DAC1 时钟门控（Clock Gate）。

## 7.2\_详细说明（Detailed Documentation）

<a id="a20b494e041d23509f1960631bc0b7e44"></a>

### `LPC84X_CLK_ACMP`

```c
#define LPC84X_CLK_ACMP LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 19U)
```

模拟比较器（Analog Comparator） 时钟门控（Clock Gate）。

<a id="a9f00c67c96947b916e87f3c3bba39084"></a>

### `LPC84X_CLK_ADC`

```c
#define LPC84X_CLK_ADC LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 24U)
```

ADC 时钟门控（Clock Gate）。

<a id="aaf7c9a3429b7b6dc86990f17af917ae7"></a>

### `LPC84X_CLK_CAPT`

```c
#define LPC84X_CLK_CAPT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL1, 0U)
```

CAPT 时钟门控（Clock Gate）。

<a id="adac7762135367602532a81288b4162a4"></a>

### `LPC84X_CLK_CRC`

```c
#define LPC84X_CLK_CRC LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 13U)
```

CRC 引擎（CRC Engine） 时钟门控（Clock Gate）。

<a id="a493f8a0441b79ee57c58a1d81be3435d"></a>

### `LPC84X_CLK_CTIMER0`

```c
#define LPC84X_CLK_CTIMER0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 25U)
```

CTIMER0 时钟门控（Clock Gate）。

<a id="a4eee194733f1a954e14cdb259acfcff9"></a>

### `LPC84X_CLK_DAC0`

```c
#define LPC84X_CLK_DAC0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 27U)
```

DAC0 时钟门控（Clock Gate）。

<a id="a050fdff7e14986cd083e0e7385f9767f"></a>

### `LPC84X_CLK_DAC1`

```c
#define LPC84X_CLK_DAC1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL1, 1U)
```

DAC1 时钟门控（Clock Gate）。

<a id="ac0c6e79c73700754e9efebff7ab68c2e"></a>

### `LPC84X_CLK_DMA`

```c
#define LPC84X_CLK_DMA LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 29U)
```

DMA 时钟门控（Clock Gate）。

<a id="a87cf30fb969db276ee95db32d0926c41"></a>

### `LPC84X_CLK_FLASH`

```c
#define LPC84X_CLK_FLASH LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 4U)
```

FLASH 时钟门控（Clock Gate）。

<a id="ae689958107c3afd34ebf4621f55e4b0b"></a>

### `LPC84X_CLK_GATE_DEFINE`

```c
#define LPC84X_CLK_GATE_DEFINE ( reg, bit )
```

展开值（Value）：

```c
((((reg) & 0xFFU) << 8U) | ((bit) & 0xFFU))
```

编码 LPC84x 时钟门控标识符（Clock Gate Identifier）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reg` | 寄存器偏移量（Register Offset），即 SYS_AHB_CLK_CTRLx。 |
| `bit` | 寄存器内的位位置（Bit Position）。 |

<a id="ab8627717a27ada335942b82d1bded632"></a>

### `LPC84X_CLK_GPIO0`

```c
#define LPC84X_CLK_GPIO0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 6U)
```

GPIO0 时钟门控（Clock Gate）。

<a id="a148ae5e042a49e58ffda3bab509e29b8"></a>

### `LPC84X_CLK_GPIO1`

```c
#define LPC84X_CLK_GPIO1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 20U)
```

GPIO1 时钟门控（Clock Gate）。

<a id="a1b67c6322eb9c99814d8b277515adf17"></a>

### `LPC84X_CLK_GPIOINT`

```c
#define LPC84X_CLK_GPIOINT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 28U)
```

GPIO 中断（GPIO Interrupt） 时钟门控（Clock Gate）。

<a id="a45b2fb064437bf70801308d4863004ea"></a>

### `LPC84X_CLK_I2C0`

```c
#define LPC84X_CLK_I2C0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 5U)
```

I2C0 时钟门控（Clock Gate）。

<a id="a440795694db3730f28062fd39bfe993a"></a>

### `LPC84X_CLK_I2C1`

```c
#define LPC84X_CLK_I2C1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 21U)
```

I2C1 时钟门控（Clock Gate）。

<a id="a91ba67a3d8761f151d8f1262452d2a0a"></a>

### `LPC84X_CLK_I2C2`

```c
#define LPC84X_CLK_I2C2 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 22U)
```

I2C2 时钟门控（Clock Gate）。

<a id="a72ec1cf2f414ac7e562baffdd7e520ef"></a>

### `LPC84X_CLK_I2C3`

```c
#define LPC84X_CLK_I2C3 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 23U)
```

I2C3 时钟门控（Clock Gate）。

<a id="a97d81d50a44a092caa0aaf2af7ebc992"></a>

### `LPC84X_CLK_IOCON`

```c
#define LPC84X_CLK_IOCON LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 18U)
```

IOCON 时钟门控（Clock Gate）。

<a id="a0b0bedfa3c2a63820bef24679733d00f"></a>

### `LPC84X_CLK_MRT`

```c
#define LPC84X_CLK_MRT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 10U)
```

多速率定时器（Multi-Rate Timer，MRT） 时钟门控（Clock Gate）。

<a id="aae9a524394ed8b896d5148262c0006ed"></a>

### `LPC84X_CLK_MTB`

```c
#define LPC84X_CLK_MTB LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 26U)
```

MTB 时钟门控（Clock Gate）。

<a id="a775860ff41f41c3cae8223dd2c74a674"></a>

### `LPC84X_CLK_RAM0_1`

```c
#define LPC84X_CLK_RAM0_1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 2U)
```

RAM0 和 RAM1 时钟门控（Clock Gate）。

<a id="ae8cb973627b8124804bf367f3288ee7e"></a>

### `LPC84X_CLK_ROM`

```c
#define LPC84X_CLK_ROM LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 1U)
```

ROM 时钟门控（Clock Gate）。

<a id="a878cdb89e4ccc0e6247a8f60cb81caa2"></a>

### `LPC84X_CLK_SCT`

```c
#define LPC84X_CLK_SCT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 8U)
```

状态可配置定时器（State Configurable Timer，SCT） 时钟门控（Clock Gate）。

<a id="a38a63d9ee81fe0b11237fa76a24405da"></a>

### `LPC84X_CLK_SPI0`

```c
#define LPC84X_CLK_SPI0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 11U)
```

SPI0 时钟门控（Clock Gate）。

<a id="af3cbd69fbad2f9826a59edd888b895b4"></a>

### `LPC84X_CLK_SPI1`

```c
#define LPC84X_CLK_SPI1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 12U)
```

SPI1 时钟门控（Clock Gate）。

<a id="a5a5ed25ffcaa31408aebcea6cd08a385"></a>

### `LPC84X_CLK_SWM`

```c
#define LPC84X_CLK_SWM LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 7U)
```

开关矩阵（Switch Matrix，SWM） 时钟门控（Clock Gate）。

<a id="a75c3500a6713eed989baea00d7ba8728"></a>

### `LPC84X_CLK_UART0`

```c
#define LPC84X_CLK_UART0 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 14U)
```

UART0 时钟门控（Clock Gate）。

<a id="a154daba51c7d0e41b7e47042335f646c"></a>

### `LPC84X_CLK_UART1`

```c
#define LPC84X_CLK_UART1 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 15U)
```

UART1 时钟门控（Clock Gate）。

<a id="a1e5461c1f12d58970ce80e3f0ff4c7d2"></a>

### `LPC84X_CLK_UART2`

```c
#define LPC84X_CLK_UART2 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 16U)
```

UART2 时钟门控（Clock Gate）。

<a id="ae1a7b168be530a5bdb48aff77c2e5700"></a>

### `LPC84X_CLK_UART3`

```c
#define LPC84X_CLK_UART3 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 30U)
```

UART3 时钟门控（Clock Gate）。

<a id="ae388bb1b215097b0d2b18b9e51352e2f"></a>

### `LPC84X_CLK_UART4`

```c
#define LPC84X_CLK_UART4 LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 31U)
```

UART4 时钟门控（Clock Gate）。

<a id="a79cf8c1353921f01ab6d2b2a237b16b1"></a>

### `LPC84X_CLK_WKT`

```c
#define LPC84X_CLK_WKT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 9U)
```

唤醒定时器（Wake-up Timer，WKT） 时钟门控（Clock Gate）。

<a id="a22435d2e5b400884818b5b2c03b14746"></a>

### `LPC84X_CLK_WWDT`

```c
#define LPC84X_CLK_WWDT LPC84X_CLK_GATE_DEFINE(LPC84X_SYS_AHB_CLK_CTRL0, 17U)
```

窗口看门狗定时器（Windowed Watchdog Timer） 时钟门控（Clock Gate）。

<a id="a9ea5311cfc3b17f761f0788969e8473a"></a>

### `LPC84X_SYS_AHB_CLK_CTRL0`

```c
#define LPC84X_SYS_AHB_CLK_CTRL0 0U
```

SYS_AHB_CLK_CTRL0 寄存器偏移量（Register Offset）。

<a id="a46fbc1c1a71af64f2ce04d60159a969f"></a>

### `LPC84X_SYS_AHB_CLK_CTRL1`

```c
#define LPC84X_SYS_AHB_CLK_CTRL1 4U
```

SYS_AHB_CLK_CTRL1 寄存器偏移量（Register Offset）。


## 7.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P456_lpc84x-clock.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P006_zephyr__drivers__interrupt_controller__intc_esp32.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__drivers__sensor__ltc4286.h_文件参考.md)
