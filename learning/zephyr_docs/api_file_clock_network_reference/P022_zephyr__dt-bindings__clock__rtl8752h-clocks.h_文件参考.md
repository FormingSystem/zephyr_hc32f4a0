---
id: learning.zephyr-docs.api-file-clock-network-reference.page-22
title: zephyr__dt-bindings__clock__rtl8752h-clocks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-clocks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_zephyr\_\_dt-bindings\_\_clock\_\_rtl8752h-clocks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-clocks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Realtek RTL8752H时钟控制器（Clock Controller）的设备树绑定。

查看此文件的源码。

<a id="details"></a>

Realtek RTL8752H时钟控制器（Clock Controller）的设备树绑定。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 22.1\_宏定义（Macros）

<a id="r_ad55bd03e176f93e3732af365ac55f585"></a>

```c
#define APB_CLK(peri)
```

相关声明：[APB_CLK](#ad55bd03e176f93e3732af365ac55f585)。

引用 APB 外设时钟（Peripheral Clock）的辅助宏。

<a id="define-members-0"></a>

### APB 外设时钟标识符（Peripheral Clock IDs）

APB 外设的时钟标识符（Clock Identifiers）。

<a id="r_a92725eabd4435f5fae5c298b6529add9"></a>

```c
#define APB_PERIPH_I2S0_CLOCK 0U
```

相关声明：[APB_PERIPH_I2S0_CLOCK](#a92725eabd4435f5fae5c298b6529add9)。

I2S0 时钟（Clock）。

<a id="r_ac6534636af673dd9ec0bb86b9ea2b8c5"></a>

```c
#define APB_PERIPH_I2S1_CLOCK 1U
```

相关声明：[APB_PERIPH_I2S1_CLOCK](#ac6534636af673dd9ec0bb86b9ea2b8c5)。

I2S1 时钟（Clock）。

<a id="r_a9ac6830c64830ad357310dc57979ce3e"></a>

```c
#define APB_PERIPH_CODEC_CLOCK 2U
```

相关声明：[APB_PERIPH_CODEC_CLOCK](#a9ac6830c64830ad357310dc57979ce3e)。

CODEC 时钟（Clock）。

<a id="r_a02da34f9b1fe9bd11f0b2f6b47ce852c"></a>

```c
#define APB_PERIPH_GPIO_CLOCK 3U
```

相关声明：[APB_PERIPH_GPIO_CLOCK](#a02da34f9b1fe9bd11f0b2f6b47ce852c)。

GPIO 时钟（Clock）。

<a id="r_a90a6f41b4204d319e3451d149be66a5a"></a>

```c
#define APB_PERIPH_GDMA_CLOCK 4U
```

相关声明：[APB_PERIPH_GDMA_CLOCK](#a90a6f41b4204d319e3451d149be66a5a)。

GDMA 时钟（Clock）。

<a id="r_ad0939b3f96dfd6838c1bce2bc9abc245"></a>

```c
#define APB_PERIPH_TIMER_CLOCK 5U
```

相关声明：[APB_PERIPH_TIMER_CLOCK](#ad0939b3f96dfd6838c1bce2bc9abc245)。

TIMER 时钟（Clock）。

<a id="r_aa63f1195dd67f8d5339fc330bdf9266f"></a>

```c
#define APB_PERIPH_ENHTIMER_CLOCK 6U
```

相关声明：[APB_PERIPH_ENHTIMER_CLOCK](#aa63f1195dd67f8d5339fc330bdf9266f)。

ENHTIME 时钟（Clock）。

<a id="r_a54a67ebfb34dd2069141245d3c0cddf1"></a>

```c
#define APB_PERIPH_UART2_CLOCK 7U
```

相关声明：[APB_PERIPH_UART2_CLOCK](#a54a67ebfb34dd2069141245d3c0cddf1)。

UART2 时钟（Clock）。

<a id="r_a65239a50059424b4fe63aab426b96c43"></a>

```c
#define APB_PERIPH_UART0_CLOCK 8U
```

相关声明：[APB_PERIPH_UART0_CLOCK](#a65239a50059424b4fe63aab426b96c43)。

UART0 时钟（Clock）。

<a id="r_a4d3f67de5d09887822fc72bf41e52ac0"></a>

```c
#define APB_PERIPH_FLASH_CLOCK 9U
```

相关声明：[APB_PERIPH_FLASH_CLOCK](#a4d3f67de5d09887822fc72bf41e52ac0)。

FLASH 时钟（Clock）。

<a id="r_acfeb7b3b3dbe0e642d4a025cf2e0459c"></a>

```c
#define APB_PERIPH_PKE_CLOCK 10U
```

相关声明：[APB_PERIPH_PKE_CLOCK](#acfeb7b3b3dbe0e642d4a025cf2e0459c)。

PKE 时钟（Clock）。

<a id="r_ac9bf5225b62b8bcad391a6737f7f5bbc"></a>

```c
#define APB_PERIPH_SHA256_CLOCK 11U
```

相关声明：[APB_PERIPH_SHA256_CLOCK](#ac9bf5225b62b8bcad391a6737f7f5bbc)。

SHA256 时钟（Clock）。

<a id="r_afb9c5ec94d9e973aed63203800aa6fe4"></a>

```c
#define APB_PERIPH_FLASH1_CLOCK 12U
```

相关声明：[APB_PERIPH_FLASH1_CLOCK](#afb9c5ec94d9e973aed63203800aa6fe4)。

FLASH1 时钟（Clock）。

<a id="r_a080c3fb4968c666294e190c29e108795"></a>

```c
#define APB_PERIPH_FLH_SEC_CLOCK 13U
```

相关声明：[APB_PERIPH_FLH_SEC_CLOCK](#a080c3fb4968c666294e190c29e108795)。

FLH_SEC 时钟（Clock）。

<a id="r_ae4114dd3818d5cee94db5998806b2db3"></a>

```c
#define APB_PERIPH_IR_CLOCK 14U
```

相关声明：[APB_PERIPH_IR_CLOCK](#ae4114dd3818d5cee94db5998806b2db3)。

IR 时钟（Clock）。

<a id="r_a54bbbfda564bd51403d3504abfc9f2d4"></a>

```c
#define APB_PERIPH_SPI1_CLOCK 15U
```

相关声明：[APB_PERIPH_SPI1_CLOCK](#a54bbbfda564bd51403d3504abfc9f2d4)。

SPI1 时钟（Clock）。

<a id="r_a9e14717faadb8f42ce6b92e8fd4d57e1"></a>

```c
#define APB_PERIPH_SPI0_CLOCK 16U
```

相关声明：[APB_PERIPH_SPI0_CLOCK](#a9e14717faadb8f42ce6b92e8fd4d57e1)。

SPI0 时钟（Clock）。

<a id="r_a41c6b4ceaa6c13e9baea45a070007c8e"></a>

```c
#define APB_PERIPH_UART1_CLOCK 17U
```

相关声明：[APB_PERIPH_UART1_CLOCK](#a41c6b4ceaa6c13e9baea45a070007c8e)。

UART1 时钟（Clock）。

<a id="r_aaff4424b876ef3c906b344943f6e67c7"></a>

```c
#define APB_PERIPH_IF8080_CLOCK 18U
```

相关声明：[APB_PERIPH_IF8080_CLOCK](#aaff4424b876ef3c906b344943f6e67c7)。

IF8080 时钟（Clock）。

<a id="r_a184c8c279a4bd9ee6cb6b47d662108b1"></a>

```c
#define APB_PERIPH_ADC_CLOCK 19U
```

相关声明：[APB_PERIPH_ADC_CLOCK](#a184c8c279a4bd9ee6cb6b47d662108b1)。

ADC 时钟（Clock）。

<a id="r_a9eb487db596aea8c099e10482844a7ae"></a>

```c
#define APB_PERIPH_SPI2W_CLOCK 20U
```

相关声明：[APB_PERIPH_SPI2W_CLOCK](#a9eb487db596aea8c099e10482844a7ae)。

SPI2W 时钟（Clock）。

<a id="r_a8dee078f2827a2153b8840323b4616d4"></a>

```c
#define APB_PERIPH_MODEM_CLOCK 21U
```

相关声明：[APB_PERIPH_MODEM_CLOCK](#a8dee078f2827a2153b8840323b4616d4)。

MODEM 时钟（Clock）。

<a id="r_a86a2243e062e831ad1f122e0cdab3917"></a>

```c
#define APB_PERIPH_BLUEWIZ_CLOCK 22U
```

相关声明：[APB_PERIPH_BLUEWIZ_CLOCK](#a86a2243e062e831ad1f122e0cdab3917)。

BLUEWIZ 时钟（Clock）。

<a id="r_a5acd92bda12d1941a9df0659024cc286"></a>

```c
#define APB_PERIPH_ZIGBEE_CLOCK 23U
```

相关声明：[APB_PERIPH_ZIGBEE_CLOCK](#a5acd92bda12d1941a9df0659024cc286)。

ZIGBEE 时钟（Clock）。

<a id="r_a08c425744f6044f9641578402a4f7751"></a>

```c
#define APB_PERIPH_KEYSCAN_CLOCK 24U
```

相关声明：[APB_PERIPH_KEYSCAN_CLOCK](#a08c425744f6044f9641578402a4f7751)。

KEYSCAN 时钟（Clock）。

<a id="r_a8a06171b58e90cb213d113ec53a82081"></a>

```c
#define APB_PERIPH_QDEC_CLOCK 25U
```

相关声明：[APB_PERIPH_QDEC_CLOCK](#a8a06171b58e90cb213d113ec53a82081)。

QDEC 时钟（Clock）。

<a id="r_a2e596e5558f5723a4e87a0cc7e2a6b0e"></a>

```c
#define APB_PERIPH_I2C1_CLOCK 26U
```

相关声明：[APB_PERIPH_I2C1_CLOCK](#a2e596e5558f5723a4e87a0cc7e2a6b0e)。

I2C1 时钟（Clock）。

<a id="r_a4ec16e183666fc580101231ee47ac0cc"></a>

```c
#define APB_PERIPH_I2C0_CLOCK 27U
```

相关声明：[APB_PERIPH_I2C0_CLOCK](#a4ec16e183666fc580101231ee47ac0cc)。

I2C0 时钟（Clock）。

## 22.2\_详细说明（Detailed Documentation）

<a id="ad55bd03e176f93e3732af365ac55f585"></a>

### `APB_CLK`

```c
#define APB_CLK ( peri)
```

展开值（Value）：

```c
APB_PERIPH_##peri##_CLOCK
```

引用 APB 外设时钟（Peripheral Clock）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `peri` | 外设名称（Peripheral Name）。此宏自动展开为 `APB_PERIPH_<peri>_CLOCK`。 |

<a id="a184c8c279a4bd9ee6cb6b47d662108b1"></a>

### `APB_PERIPH_ADC_CLOCK`

```c
#define APB_PERIPH_ADC_CLOCK 19U
```

ADC 时钟（Clock）。

<a id="a86a2243e062e831ad1f122e0cdab3917"></a>

### `APB_PERIPH_BLUEWIZ_CLOCK`

```c
#define APB_PERIPH_BLUEWIZ_CLOCK 22U
```

BLUEWIZ 时钟（Clock）。

<a id="a9ac6830c64830ad357310dc57979ce3e"></a>

### `APB_PERIPH_CODEC_CLOCK`

```c
#define APB_PERIPH_CODEC_CLOCK 2U
```

CODEC 时钟（Clock）。

<a id="aa63f1195dd67f8d5339fc330bdf9266f"></a>

### `APB_PERIPH_ENHTIMER_CLOCK`

```c
#define APB_PERIPH_ENHTIMER_CLOCK 6U
```

ENHTIME 时钟（Clock）。

<a id="afb9c5ec94d9e973aed63203800aa6fe4"></a>

### `APB_PERIPH_FLASH1_CLOCK`

```c
#define APB_PERIPH_FLASH1_CLOCK 12U
```

FLASH1 时钟（Clock）。

<a id="a4d3f67de5d09887822fc72bf41e52ac0"></a>

### `APB_PERIPH_FLASH_CLOCK`

```c
#define APB_PERIPH_FLASH_CLOCK 9U
```

FLASH 时钟（Clock）。

<a id="a080c3fb4968c666294e190c29e108795"></a>

### `APB_PERIPH_FLH_SEC_CLOCK`

```c
#define APB_PERIPH_FLH_SEC_CLOCK 13U
```

FLH_SEC 时钟（Clock）。

<a id="a90a6f41b4204d319e3451d149be66a5a"></a>

### `APB_PERIPH_GDMA_CLOCK`

```c
#define APB_PERIPH_GDMA_CLOCK 4U
```

GDMA 时钟（Clock）。

<a id="a02da34f9b1fe9bd11f0b2f6b47ce852c"></a>

### `APB_PERIPH_GPIO_CLOCK`

```c
#define APB_PERIPH_GPIO_CLOCK 3U
```

GPIO 时钟（Clock）。

<a id="a4ec16e183666fc580101231ee47ac0cc"></a>

### `APB_PERIPH_I2C0_CLOCK`

```c
#define APB_PERIPH_I2C0_CLOCK 27U
```

I2C0 时钟（Clock）。

<a id="a2e596e5558f5723a4e87a0cc7e2a6b0e"></a>

### `APB_PERIPH_I2C1_CLOCK`

```c
#define APB_PERIPH_I2C1_CLOCK 26U
```

I2C1 时钟（Clock）。

<a id="a92725eabd4435f5fae5c298b6529add9"></a>

### `APB_PERIPH_I2S0_CLOCK`

```c
#define APB_PERIPH_I2S0_CLOCK 0U
```

I2S0 时钟（Clock）。

<a id="ac6534636af673dd9ec0bb86b9ea2b8c5"></a>

### `APB_PERIPH_I2S1_CLOCK`

```c
#define APB_PERIPH_I2S1_CLOCK 1U
```

I2S1 时钟（Clock）。

<a id="aaff4424b876ef3c906b344943f6e67c7"></a>

### `APB_PERIPH_IF8080_CLOCK`

```c
#define APB_PERIPH_IF8080_CLOCK 18U
```

IF8080 时钟（Clock）。

<a id="ae4114dd3818d5cee94db5998806b2db3"></a>

### `APB_PERIPH_IR_CLOCK`

```c
#define APB_PERIPH_IR_CLOCK 14U
```

IR 时钟（Clock）。

<a id="a08c425744f6044f9641578402a4f7751"></a>

### `APB_PERIPH_KEYSCAN_CLOCK`

```c
#define APB_PERIPH_KEYSCAN_CLOCK 24U
```

KEYSCAN 时钟（Clock）。

<a id="a8dee078f2827a2153b8840323b4616d4"></a>

### `APB_PERIPH_MODEM_CLOCK`

```c
#define APB_PERIPH_MODEM_CLOCK 21U
```

MODEM 时钟（Clock）。

<a id="acfeb7b3b3dbe0e642d4a025cf2e0459c"></a>

### `APB_PERIPH_PKE_CLOCK`

```c
#define APB_PERIPH_PKE_CLOCK 10U
```

PKE 时钟（Clock）。

<a id="a8a06171b58e90cb213d113ec53a82081"></a>

### `APB_PERIPH_QDEC_CLOCK`

```c
#define APB_PERIPH_QDEC_CLOCK 25U
```

QDEC 时钟（Clock）。

<a id="ac9bf5225b62b8bcad391a6737f7f5bbc"></a>

### `APB_PERIPH_SHA256_CLOCK`

```c
#define APB_PERIPH_SHA256_CLOCK 11U
```

SHA256 时钟（Clock）。

<a id="a9e14717faadb8f42ce6b92e8fd4d57e1"></a>

### `APB_PERIPH_SPI0_CLOCK`

```c
#define APB_PERIPH_SPI0_CLOCK 16U
```

SPI0 时钟（Clock）。

<a id="a54bbbfda564bd51403d3504abfc9f2d4"></a>

### `APB_PERIPH_SPI1_CLOCK`

```c
#define APB_PERIPH_SPI1_CLOCK 15U
```

SPI1 时钟（Clock）。

<a id="a9eb487db596aea8c099e10482844a7ae"></a>

### `APB_PERIPH_SPI2W_CLOCK`

```c
#define APB_PERIPH_SPI2W_CLOCK 20U
```

SPI2W 时钟（Clock）。

<a id="ad0939b3f96dfd6838c1bce2bc9abc245"></a>

### `APB_PERIPH_TIMER_CLOCK`

```c
#define APB_PERIPH_TIMER_CLOCK 5U
```

TIMER 时钟（Clock）。

<a id="a65239a50059424b4fe63aab426b96c43"></a>

### `APB_PERIPH_UART0_CLOCK`

```c
#define APB_PERIPH_UART0_CLOCK 8U
```

UART0 时钟（Clock）。

<a id="a41c6b4ceaa6c13e9baea45a070007c8e"></a>

### `APB_PERIPH_UART1_CLOCK`

```c
#define APB_PERIPH_UART1_CLOCK 17U
```

UART1 时钟（Clock）。

<a id="a54a67ebfb34dd2069141245d3c0cddf1"></a>

### `APB_PERIPH_UART2_CLOCK`

```c
#define APB_PERIPH_UART2_CLOCK 7U
```

UART2 时钟（Clock）。

<a id="a5acd92bda12d1941a9df0659024cc286"></a>

### `APB_PERIPH_ZIGBEE_CLOCK`

```c
#define APB_PERIPH_ZIGBEE_CLOCK 23U
```

ZIGBEE 时钟（Clock）。


## 22.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P734_rtl8752h-clocks.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P021_zephyr__drivers__misc__interconn__renesas_elc__renesas_elc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__dt-bindings__clock__rtl87x2g-clocks.h_文件参考.md)
