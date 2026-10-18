---
id: learning.zephyr-docs.api-file-audio-test-reference.page-2
title: zephyr__dt-bindings__dma__ameba_dma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ameba__dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_dt-bindings\_\_dma\_\_ameba\_dma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ameba__dma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Ameba片上系统（SoC）的DMA设备树绑定标志。

查看此文件的源码。

<a id="details"></a>

Ameba SoC DMA 设备树绑定标志（Devicetree Binding Flags）。本文件定义用于在 Ameba SoC 设备树中配置 DMA 通道（Channels）的位字段标志。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="define-members-0"></a>

### DMA 通道配置标志（DMA Channel Configuration Flags）

<a id="r_a50b8f499002cd0210dc27e1edfbf3f68"></a>

```c
#define AMEBA_DMA_CH_DIR_SET(val)
```

相关声明：[AMEBA_DMA_CH_DIR_SET](#a50b8f499002cd0210dc27e1edfbf3f68)。

设置 DMA 传输方向（Transfer Direction）的位 [1:0]。

<a id="r_a98724da58edd08ff694aa445df5b0802"></a>

```c
#define AMEBA_DMA_MEMORY_TO_MEMORY AMEBA_DMA_CH_DIR_SET(0)
```

相关声明：[AMEBA_DMA_MEMORY_TO_MEMORY](#a98724da58edd08ff694aa445df5b0802)、[AMEBA_DMA_CH_DIR_SET](#a50b8f499002cd0210dc27e1edfbf3f68)。

DMA 传输方向（Transfer Direction）：内存到内存（Memory to Memory）。

<a id="r_a552cdafa33c2b874c98c3b4cc16b06d8"></a>

```c
#define AMEBA_DMA_MEMORY_TO_PERIPH AMEBA_DMA_CH_DIR_SET(1)
```

相关声明：[AMEBA_DMA_MEMORY_TO_PERIPH](#a552cdafa33c2b874c98c3b4cc16b06d8)、[AMEBA_DMA_CH_DIR_SET](#a50b8f499002cd0210dc27e1edfbf3f68)。

DMA 传输方向（Transfer Direction）：内存到外设（Memory to Peripheral）。

<a id="r_a5b45a1221f9bdf49b8dcafc0acdfe57d"></a>

```c
#define AMEBA_DMA_PERIPH_TO_MEMORY AMEBA_DMA_CH_DIR_SET(2)
```

相关声明：[AMEBA_DMA_PERIPH_TO_MEMORY](#a5b45a1221f9bdf49b8dcafc0acdfe57d)、[AMEBA_DMA_CH_DIR_SET](#a50b8f499002cd0210dc27e1edfbf3f68)。

DMA 传输方向（Transfer Direction）：外设到内存（Peripheral to Memory）。

<a id="r_aa16e93c69cfcf0834ab8873b88e1f46e"></a>

```c
#define AMEBA_DMA_PERIPH_TO_PERIPH AMEBA_DMA_CH_DIR_SET(3)
```

相关声明：[AMEBA_DMA_PERIPH_TO_PERIPH](#aa16e93c69cfcf0834ab8873b88e1f46e)、[AMEBA_DMA_CH_DIR_SET](#a50b8f499002cd0210dc27e1edfbf3f68)。

DMA 传输方向（Transfer Direction）：外设到外设（Peripheral to Peripheral）。

<a id="r_a40f32907475e0e82cfc7054a4725de25"></a>

```c
#define AMEBA_DMA_SRC_ADDR_ADJ_SET(val)
```

相关声明：[AMEBA_DMA_SRC_ADDR_ADJ_SET](#a40f32907475e0e82cfc7054a4725de25)。

设置源地址调整（Source Address Adjustment）的位 [3:2]。

<a id="r_aff061a9e6c92a4ffe30366c1b263616e"></a>

```c
#define AMEBA_DMA_SRC_ADDR_ADJ_INC AMEBA_DMA_SRC_ADDR_ADJ_SET(0)
```

相关声明：[AMEBA_DMA_SRC_ADDR_ADJ_INC](#aff061a9e6c92a4ffe30366c1b263616e)、[AMEBA_DMA_SRC_ADDR_ADJ_SET](#a40f32907475e0e82cfc7054a4725de25)。

每次传输后递增源地址（Source Address）。

<a id="r_a1cc3c23dbb25ffdaed62f0cb9ae08e76"></a>

```c
#define AMEBA_DMA_SRC_ADDR_ADJ_NO_CHANGE AMEBA_DMA_SRC_ADDR_ADJ_SET(2)
```

相关声明：[AMEBA_DMA_SRC_ADDR_ADJ_NO_CHANGE](#a1cc3c23dbb25ffdaed62f0cb9ae08e76)、[AMEBA_DMA_SRC_ADDR_ADJ_SET](#a40f32907475e0e82cfc7054a4725de25)。

源地址（Source Address）不变。

<a id="r_aa3bf86f859f3e4fe11e7911949ca8b5d"></a>

```c
#define AMEBA_DMA_DST_ADDR_ADJ_SET(val)
```

相关声明：[AMEBA_DMA_DST_ADDR_ADJ_SET](#aa3bf86f859f3e4fe11e7911949ca8b5d)。

设置目标地址调整（Destination Address Adjustment）的位 [5:4]。

<a id="r_ad3c2857946b801b79f6331592d934e3c"></a>

```c
#define AMEBA_DMA_DST_ADDR_ADJ_INC AMEBA_DMA_DST_ADDR_ADJ_SET(0)
```

相关声明：[AMEBA_DMA_DST_ADDR_ADJ_INC](#ad3c2857946b801b79f6331592d934e3c)、[AMEBA_DMA_DST_ADDR_ADJ_SET](#aa3bf86f859f3e4fe11e7911949ca8b5d)。

每次传输后递增目标地址（Destination Address）。

<a id="r_a9a228951d2f89e89b8dd078769ab34d4"></a>

```c
#define AMEBA_DMA_DST_ADDR_ADJ_NO_CHANGE AMEBA_DMA_DST_ADDR_ADJ_SET(2)
```

相关声明：[AMEBA_DMA_DST_ADDR_ADJ_NO_CHANGE](#a9a228951d2f89e89b8dd078769ab34d4)、[AMEBA_DMA_DST_ADDR_ADJ_SET](#aa3bf86f859f3e4fe11e7911949ca8b5d)。

目标地址（Destination Address）不变。

<a id="r_a752f1d14d4aa2aedaf8deb7d1a25f778"></a>

```c
#define AMEBA_DMA_SRC_DATA_SIZE_SET(val)
```

相关声明：[AMEBA_DMA_SRC_DATA_SIZE_SET](#a752f1d14d4aa2aedaf8deb7d1a25f778)。

设置源数据宽度（Source Data Width）的位 [8:6]。

<a id="r_af3dfd2af5b27a19c2af861b11d8a3a53"></a>

```c
#define AMEBA_DMA_SRC_WIDTH_8BITS AMEBA_DMA_SRC_DATA_SIZE_SET(0)
```

相关声明：[AMEBA_DMA_SRC_WIDTH_8BITS](#af3dfd2af5b27a19c2af861b11d8a3a53)、[AMEBA_DMA_SRC_DATA_SIZE_SET](#a752f1d14d4aa2aedaf8deb7d1a25f778)。

源数据宽度（Source Data Width）：8 位。

<a id="r_ab0d052583900e27ee394decd127e9805"></a>

```c
#define AMEBA_DMA_SRC_WIDTH_16BITS AMEBA_DMA_SRC_DATA_SIZE_SET(1)
```

相关声明：[AMEBA_DMA_SRC_WIDTH_16BITS](#ab0d052583900e27ee394decd127e9805)、[AMEBA_DMA_SRC_DATA_SIZE_SET](#a752f1d14d4aa2aedaf8deb7d1a25f778)。

源数据宽度（Source Data Width）：16 位。

<a id="r_a0b413be2a59668072c4eb862b901c14a"></a>

```c
#define AMEBA_DMA_SRC_WIDTH_32BITS AMEBA_DMA_SRC_DATA_SIZE_SET(2)
```

相关声明：[AMEBA_DMA_SRC_WIDTH_32BITS](#a0b413be2a59668072c4eb862b901c14a)、[AMEBA_DMA_SRC_DATA_SIZE_SET](#a752f1d14d4aa2aedaf8deb7d1a25f778)。

源数据宽度（Source Data Width）：32 位。

<a id="r_ade79f5b43140c3c819088b12da0c3539"></a>

```c
#define AMEBA_DMA_DST_DATA_SIZE_SET(val)
```

相关声明：[AMEBA_DMA_DST_DATA_SIZE_SET](#ade79f5b43140c3c819088b12da0c3539)。

设置目标数据宽度（Destination Data Width）的位 [11:9]。

<a id="r_aec2d62dfef452bd68562bb1bf39d3434"></a>

```c
#define AMEBA_DMA_DST_WIDTH_8BITS AMEBA_DMA_DST_DATA_SIZE_SET(0)
```

相关声明：[AMEBA_DMA_DST_WIDTH_8BITS](#aec2d62dfef452bd68562bb1bf39d3434)、[AMEBA_DMA_DST_DATA_SIZE_SET](#ade79f5b43140c3c819088b12da0c3539)。

目标数据宽度（Destination Data Width）：8 位。

<a id="r_a9735387b13a4ea83a246791849ab1171"></a>

```c
#define AMEBA_DMA_DST_WIDTH_16BITS AMEBA_DMA_DST_DATA_SIZE_SET(1)
```

相关声明：[AMEBA_DMA_DST_WIDTH_16BITS](#a9735387b13a4ea83a246791849ab1171)、[AMEBA_DMA_DST_DATA_SIZE_SET](#ade79f5b43140c3c819088b12da0c3539)。

目标数据宽度（Destination Data Width）：16 位。

<a id="r_af3e697239ad33d7e10771087b8b7b1fe"></a>

```c
#define AMEBA_DMA_DST_WIDTH_32BITS AMEBA_DMA_DST_DATA_SIZE_SET(2)
```

相关声明：[AMEBA_DMA_DST_WIDTH_32BITS](#af3e697239ad33d7e10771087b8b7b1fe)、[AMEBA_DMA_DST_DATA_SIZE_SET](#ade79f5b43140c3c819088b12da0c3539)。

目标数据宽度（Destination Data Width）：32 位。

<a id="r_ac92928e5df38ca6753ac8387aeb6fd12"></a>

```c
#define AMEBA_DMA_SRC_BURST_SET(val)
```

相关声明：[AMEBA_DMA_SRC_BURST_SET](#ac92928e5df38ca6753ac8387aeb6fd12)。

设置源突发长度（Source Burst Length）的位 [16:12]。

<a id="r_a2e96b26c6d84841853fab5cad6d9fde9"></a>

```c
#define AMEBA_DMA_SRC_BURST_ONE AMEBA_DMA_SRC_BURST_SET(0)
```

相关声明：[AMEBA_DMA_SRC_BURST_ONE](#a2e96b26c6d84841853fab5cad6d9fde9)、[AMEBA_DMA_SRC_BURST_SET](#ac92928e5df38ca6753ac8387aeb6fd12)。

源突发长度（Source Burst Length）：1 次传输。

<a id="r_aefffac17461ca4cd4f15e881943bf1b0"></a>

```c
#define AMEBA_DMA_SRC_BURST_FOUR AMEBA_DMA_SRC_BURST_SET(1)
```

相关声明：[AMEBA_DMA_SRC_BURST_FOUR](#aefffac17461ca4cd4f15e881943bf1b0)、[AMEBA_DMA_SRC_BURST_SET](#ac92928e5df38ca6753ac8387aeb6fd12)。

源突发长度（Source Burst Length）：4 次传输。

<a id="r_aa52cd93db66ecf798d90bdb461a22d61"></a>

```c
#define AMEBA_DMA_SRC_BURST_EIGHT AMEBA_DMA_SRC_BURST_SET(2)
```

相关声明：[AMEBA_DMA_SRC_BURST_EIGHT](#aa52cd93db66ecf798d90bdb461a22d61)、[AMEBA_DMA_SRC_BURST_SET](#ac92928e5df38ca6753ac8387aeb6fd12)。

源突发长度（Source Burst Length）：8 次传输。

<a id="r_af3c1b1b1406574d830e619683b9e2996"></a>

```c
#define AMEBA_DMA_SRC_BURST_SIXTEEN AMEBA_DMA_SRC_BURST_SET(3)
```

相关声明：[AMEBA_DMA_SRC_BURST_SIXTEEN](#af3c1b1b1406574d830e619683b9e2996)、[AMEBA_DMA_SRC_BURST_SET](#ac92928e5df38ca6753ac8387aeb6fd12)。

源突发长度（Source Burst Length）：16 次传输。

<a id="r_af0af1a6883a03f549f0f5199fb95776a"></a>

```c
#define AMEBA_DMA_DST_BURST_SET(val)
```

相关声明：[AMEBA_DMA_DST_BURST_SET](#af0af1a6883a03f549f0f5199fb95776a)。

设置目标突发长度（Destination Burst Length）的位 [21:17]。

<a id="r_aa65d2c83eaf6bf39ba218893f617e154"></a>

```c
#define AMEBA_DMA_DST_BURST_ONE AMEBA_DMA_DST_BURST_SET(0)
```

相关声明：[AMEBA_DMA_DST_BURST_ONE](#aa65d2c83eaf6bf39ba218893f617e154)、[AMEBA_DMA_DST_BURST_SET](#af0af1a6883a03f549f0f5199fb95776a)。

目标突发长度（Destination Burst Length）：1 次传输。

<a id="r_ad22c552fe40f58c13355524cbabe9624"></a>

```c
#define AMEBA_DMA_DST_BURST_FOUR AMEBA_DMA_DST_BURST_SET(1)
```

相关声明：[AMEBA_DMA_DST_BURST_FOUR](#ad22c552fe40f58c13355524cbabe9624)、[AMEBA_DMA_DST_BURST_SET](#af0af1a6883a03f549f0f5199fb95776a)。

目标突发长度（Destination Burst Length）：4 次传输。

<a id="r_a168dcf4eb8259a89718b8727485cfd39"></a>

```c
#define AMEBA_DMA_DST_BURST_EIGHT AMEBA_DMA_DST_BURST_SET(2)
```

相关声明：[AMEBA_DMA_DST_BURST_EIGHT](#a168dcf4eb8259a89718b8727485cfd39)、[AMEBA_DMA_DST_BURST_SET](#af0af1a6883a03f549f0f5199fb95776a)。

目标突发长度（Destination Burst Length）：8 次传输。

<a id="r_af3b0733de5a71a55b70b822b542e0d52"></a>

```c
#define AMEBA_DMA_DST_BURST_SIXTEEN AMEBA_DMA_DST_BURST_SET(3)
```

相关声明：[AMEBA_DMA_DST_BURST_SIXTEEN](#af3b0733de5a71a55b70b822b542e0d52)、[AMEBA_DMA_DST_BURST_SET](#af0af1a6883a03f549f0f5199fb95776a)。

目标突发长度（Destination Burst Length）：16 次传输。

<a id="r_ae300c71600f0e46ec9324c199e9c3b44"></a>

```c
#define AMEBA_DMA_CH_PRIORITY_SET(val)
```

相关声明：[AMEBA_DMA_CH_PRIORITY_SET](#ae300c71600f0e46ec9324c199e9c3b44)。

设置通道优先级（Channel Priority）的位 [24:22]。

<a id="r_a6874278cb87d1d0af76e52d2b82ffa7d"></a>

```c
#define AMEBA_DMA_PERIPH_TX (AMEBA_DMA_MEMORY_TO_PERIPH | AMEBA_DMA_SRC_ADDR_ADJ_INC | AMEBA_DMA_DST_ADDR_ADJ_NO_CHANGE)
```

相关声明：[AMEBA_DMA_PERIPH_TX](#a6874278cb87d1d0af76e52d2b82ffa7d)、[AMEBA_DMA_MEMORY_TO_PERIPH](#a552cdafa33c2b874c98c3b4cc16b06d8)、[AMEBA_DMA_SRC_ADDR_ADJ_INC](#aff061a9e6c92a4ffe30366c1b263616e)、[AMEBA_DMA_DST_ADDR_ADJ_NO_CHANGE](#a9a228951d2f89e89b8dd078769ab34d4)。

典型的外设发送配置（Peripheral TX Configuration）。

<a id="r_a5eabd64ab1c4eda17c53fae852bc02cc"></a>

```c
#define AMEBA_DMA_PERIPH_RX (AMEBA_DMA_PERIPH_TO_MEMORY | AMEBA_DMA_SRC_ADDR_ADJ_NO_CHANGE | AMEBA_DMA_DST_ADDR_ADJ_INC)
```

相关声明：[AMEBA_DMA_PERIPH_RX](#a5eabd64ab1c4eda17c53fae852bc02cc)、[AMEBA_DMA_PERIPH_TO_MEMORY](#a5b45a1221f9bdf49b8dcafc0acdfe57d)、[AMEBA_DMA_SRC_ADDR_ADJ_NO_CHANGE](#a1cc3c23dbb25ffdaed62f0cb9ae08e76)、[AMEBA_DMA_DST_ADDR_ADJ_INC](#ad3c2857946b801b79f6331592d934e3c)。

典型的外设接收配置（Peripheral RX Configuration）。

## 2.2\_详细说明（Detailed Documentation）

<a id="a50b8f499002cd0210dc27e1edfbf3f68"></a>

### `AMEBA_DMA_CH_DIR_SET`

```c
#define AMEBA_DMA_CH_DIR_SET ( val)
```

展开值（Value）：

```c
((val & 0x3) << 0)
```

设置 DMA 传输方向（Transfer Direction）的位 [1:0]。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 编码到位 [1:0] 的方向值（Direction Value）。 |

<a id="ae300c71600f0e46ec9324c199e9c3b44"></a>

### `AMEBA_DMA_CH_PRIORITY_SET`

```c
#define AMEBA_DMA_CH_PRIORITY_SET ( val)
```

展开值（Value）：

```c
((val & 0x7) << 22)
```

设置通道优先级（Channel Priority）的位 [24:22]。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 通道优先级值（Channel Priority Value），范围为 0–7。 |

<a id="ad3c2857946b801b79f6331592d934e3c"></a>

### `AMEBA_DMA_DST_ADDR_ADJ_INC`

```c
#define AMEBA_DMA_DST_ADDR_ADJ_INC AMEBA_DMA_DST_ADDR_ADJ_SET(0)
```

每次传输后递增目标地址（Destination Address）。

<a id="a9a228951d2f89e89b8dd078769ab34d4"></a>

### `AMEBA_DMA_DST_ADDR_ADJ_NO_CHANGE`

```c
#define AMEBA_DMA_DST_ADDR_ADJ_NO_CHANGE AMEBA_DMA_DST_ADDR_ADJ_SET(2)
```

目标地址（Destination Address）不变。

<a id="aa3bf86f859f3e4fe11e7911949ca8b5d"></a>

### `AMEBA_DMA_DST_ADDR_ADJ_SET`

```c
#define AMEBA_DMA_DST_ADDR_ADJ_SET ( val)
```

展开值（Value）：

```c
((val & 0x3) << 4)
```

设置目标地址调整（Destination Address Adjustment）的位 [5:4]。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 编码到位 [5:4] 的地址调整值（Address Adjustment Value）。 |

<a id="a168dcf4eb8259a89718b8727485cfd39"></a>

### `AMEBA_DMA_DST_BURST_EIGHT`

```c
#define AMEBA_DMA_DST_BURST_EIGHT AMEBA_DMA_DST_BURST_SET(2)
```

目标突发长度（Destination Burst Length）：8 次传输。

<a id="ad22c552fe40f58c13355524cbabe9624"></a>

### `AMEBA_DMA_DST_BURST_FOUR`

```c
#define AMEBA_DMA_DST_BURST_FOUR AMEBA_DMA_DST_BURST_SET(1)
```

目标突发长度（Destination Burst Length）：4 次传输。

<a id="aa65d2c83eaf6bf39ba218893f617e154"></a>

### `AMEBA_DMA_DST_BURST_ONE`

```c
#define AMEBA_DMA_DST_BURST_ONE AMEBA_DMA_DST_BURST_SET(0)
```

目标突发长度（Destination Burst Length）：1 次传输。

<a id="af0af1a6883a03f549f0f5199fb95776a"></a>

### `AMEBA_DMA_DST_BURST_SET`

```c
#define AMEBA_DMA_DST_BURST_SET ( val)
```

展开值（Value）：

```c
((val & 0x1F) << 17)
```

设置目标突发长度（Destination Burst Length）的位 [21:17]。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 编码到位 [21:17] 的突发长度值（Burst Length Value）。 |

<a id="af3b0733de5a71a55b70b822b542e0d52"></a>

### `AMEBA_DMA_DST_BURST_SIXTEEN`

```c
#define AMEBA_DMA_DST_BURST_SIXTEEN AMEBA_DMA_DST_BURST_SET(3)
```

目标突发长度（Destination Burst Length）：16 次传输。

<a id="ade79f5b43140c3c819088b12da0c3539"></a>

### `AMEBA_DMA_DST_DATA_SIZE_SET`

```c
#define AMEBA_DMA_DST_DATA_SIZE_SET ( val)
```

展开值（Value）：

```c
((val & 0x7) << 9)
```

设置目标数据宽度（Destination Data Width）的位 [11:9]。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 编码到位 [11:9] 的数据宽度值（Data Width Value）。 |

<a id="a9735387b13a4ea83a246791849ab1171"></a>

### `AMEBA_DMA_DST_WIDTH_16BITS`

```c
#define AMEBA_DMA_DST_WIDTH_16BITS AMEBA_DMA_DST_DATA_SIZE_SET(1)
```

目标数据宽度（Destination Data Width）：16 位。

<a id="af3e697239ad33d7e10771087b8b7b1fe"></a>

### `AMEBA_DMA_DST_WIDTH_32BITS`

```c
#define AMEBA_DMA_DST_WIDTH_32BITS AMEBA_DMA_DST_DATA_SIZE_SET(2)
```

目标数据宽度（Destination Data Width）：32 位。

<a id="aec2d62dfef452bd68562bb1bf39d3434"></a>

### `AMEBA_DMA_DST_WIDTH_8BITS`

```c
#define AMEBA_DMA_DST_WIDTH_8BITS AMEBA_DMA_DST_DATA_SIZE_SET(0)
```

目标数据宽度（Destination Data Width）：8 位。

<a id="a98724da58edd08ff694aa445df5b0802"></a>

### `AMEBA_DMA_MEMORY_TO_MEMORY`

```c
#define AMEBA_DMA_MEMORY_TO_MEMORY AMEBA_DMA_CH_DIR_SET(0)
```

DMA 传输方向（Transfer Direction）：内存到内存（Memory to Memory）。

<a id="a552cdafa33c2b874c98c3b4cc16b06d8"></a>

### `AMEBA_DMA_MEMORY_TO_PERIPH`

```c
#define AMEBA_DMA_MEMORY_TO_PERIPH AMEBA_DMA_CH_DIR_SET(1)
```

DMA 传输方向（Transfer Direction）：内存到外设（Memory to Peripheral）。

<a id="a5eabd64ab1c4eda17c53fae852bc02cc"></a>

### `AMEBA_DMA_PERIPH_RX`

```c
#define AMEBA_DMA_PERIPH_RX (AMEBA_DMA_PERIPH_TO_MEMORY | AMEBA_DMA_SRC_ADDR_ADJ_NO_CHANGE | AMEBA_DMA_DST_ADDR_ADJ_INC)
```

典型的外设接收配置（Peripheral RX Configuration）。

外设到内存（Peripheral to Memory），源地址固定，目标地址递增。

<a id="a5b45a1221f9bdf49b8dcafc0acdfe57d"></a>

### `AMEBA_DMA_PERIPH_TO_MEMORY`

```c
#define AMEBA_DMA_PERIPH_TO_MEMORY AMEBA_DMA_CH_DIR_SET(2)
```

DMA 传输方向（Transfer Direction）：外设到内存（Peripheral to Memory）。

<a id="aa16e93c69cfcf0834ab8873b88e1f46e"></a>

### `AMEBA_DMA_PERIPH_TO_PERIPH`

```c
#define AMEBA_DMA_PERIPH_TO_PERIPH AMEBA_DMA_CH_DIR_SET(3)
```

DMA 传输方向（Transfer Direction）：外设到外设（Peripheral to Peripheral）。

<a id="a6874278cb87d1d0af76e52d2b82ffa7d"></a>

### `AMEBA_DMA_PERIPH_TX`

```c
#define AMEBA_DMA_PERIPH_TX (AMEBA_DMA_MEMORY_TO_PERIPH | AMEBA_DMA_SRC_ADDR_ADJ_INC | AMEBA_DMA_DST_ADDR_ADJ_NO_CHANGE)
```

典型的外设发送配置（Peripheral TX Configuration）。

内存到外设（Memory to Peripheral），源地址递增，目标地址固定。

<a id="aff061a9e6c92a4ffe30366c1b263616e"></a>

### `AMEBA_DMA_SRC_ADDR_ADJ_INC`

```c
#define AMEBA_DMA_SRC_ADDR_ADJ_INC AMEBA_DMA_SRC_ADDR_ADJ_SET(0)
```

每次传输后递增源地址（Source Address）。

<a id="a1cc3c23dbb25ffdaed62f0cb9ae08e76"></a>

### `AMEBA_DMA_SRC_ADDR_ADJ_NO_CHANGE`

```c
#define AMEBA_DMA_SRC_ADDR_ADJ_NO_CHANGE AMEBA_DMA_SRC_ADDR_ADJ_SET(2)
```

源地址（Source Address）不变。

<a id="a40f32907475e0e82cfc7054a4725de25"></a>

### `AMEBA_DMA_SRC_ADDR_ADJ_SET`

```c
#define AMEBA_DMA_SRC_ADDR_ADJ_SET ( val)
```

展开值（Value）：

```c
((val & 0x3) << 2)
```

设置源地址调整（Source Address Adjustment）的位 [3:2]。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 编码到位 [3:2] 的地址调整值（Address Adjustment Value）。 |

<a id="aa52cd93db66ecf798d90bdb461a22d61"></a>

### `AMEBA_DMA_SRC_BURST_EIGHT`

```c
#define AMEBA_DMA_SRC_BURST_EIGHT AMEBA_DMA_SRC_BURST_SET(2)
```

源突发长度（Source Burst Length）：8 次传输。

<a id="aefffac17461ca4cd4f15e881943bf1b0"></a>

### `AMEBA_DMA_SRC_BURST_FOUR`

```c
#define AMEBA_DMA_SRC_BURST_FOUR AMEBA_DMA_SRC_BURST_SET(1)
```

源突发长度（Source Burst Length）：4 次传输。

<a id="a2e96b26c6d84841853fab5cad6d9fde9"></a>

### `AMEBA_DMA_SRC_BURST_ONE`

```c
#define AMEBA_DMA_SRC_BURST_ONE AMEBA_DMA_SRC_BURST_SET(0)
```

源突发长度（Source Burst Length）：1 次传输。

<a id="ac92928e5df38ca6753ac8387aeb6fd12"></a>

### `AMEBA_DMA_SRC_BURST_SET`

```c
#define AMEBA_DMA_SRC_BURST_SET ( val)
```

展开值（Value）：

```c
((val & 0x1F) << 12)
```

设置源突发长度（Source Burst Length）的位 [16:12]。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 编码到位 [16:12] 的突发长度值（Burst Length Value）。 |

<a id="af3c1b1b1406574d830e619683b9e2996"></a>

### `AMEBA_DMA_SRC_BURST_SIXTEEN`

```c
#define AMEBA_DMA_SRC_BURST_SIXTEEN AMEBA_DMA_SRC_BURST_SET(3)
```

源突发长度（Source Burst Length）：16 次传输。

<a id="a752f1d14d4aa2aedaf8deb7d1a25f778"></a>

### `AMEBA_DMA_SRC_DATA_SIZE_SET`

```c
#define AMEBA_DMA_SRC_DATA_SIZE_SET ( val)
```

展开值（Value）：

```c
((val & 0x7) << 6)
```

设置源数据宽度（Source Data Width）的位 [8:6]。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 编码到位 [8:6] 的数据宽度值（Data Width Value）。 |

<a id="ab0d052583900e27ee394decd127e9805"></a>

### `AMEBA_DMA_SRC_WIDTH_16BITS`

```c
#define AMEBA_DMA_SRC_WIDTH_16BITS AMEBA_DMA_SRC_DATA_SIZE_SET(1)
```

源数据宽度（Source Data Width）：16 位。

<a id="a0b413be2a59668072c4eb862b901c14a"></a>

### `AMEBA_DMA_SRC_WIDTH_32BITS`

```c
#define AMEBA_DMA_SRC_WIDTH_32BITS AMEBA_DMA_SRC_DATA_SIZE_SET(2)
```

源数据宽度（Source Data Width）：32 位。

<a id="af3dfd2af5b27a19c2af861b11d8a3a53"></a>

### `AMEBA_DMA_SRC_WIDTH_8BITS`

```c
#define AMEBA_DMA_SRC_WIDTH_8BITS AMEBA_DMA_SRC_DATA_SIZE_SET(0)
```

源数据宽度（Source Data Width）：8 位。


## 2.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P028_ameba_dma.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P001_zephyr__bluetooth__audio__aics.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__bluetooth__classic__avdtp.h_文件参考.md)
