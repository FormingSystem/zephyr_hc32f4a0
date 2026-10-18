---
id: learning.zephyr-docs.api-file-network-device-reference.page-39
title: zephyr__dt-bindings__dma__stm32_dma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32__dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_zephyr\_\_dt-bindings\_\_dma\_\_stm32\_dma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stm32__dma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 39.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 通道配置的自定义 DMA 标志（Custom DMA Flags）

<a id="r_a86e8ab71081233e1f9aa8300b6ea3c85"></a>

```c
#define STM32_DMA_CH_CFG_MODE(val)
```

相关声明：[STM32_DMA_CH_CFG_MODE](#a86e8ab71081233e1f9aa8300b6ea3c85)。

位 5 配置 DMA 循环模式（Cyclic Mode）。

<a id="r_a6d811813db4e97b831b4b1fb95ec594c"></a>

```c
#define STM32_DMA_MODE_NORMAL STM32_DMA_CH_CFG_MODE(0)
```

相关声明：[STM32_DMA_MODE_NORMAL](#a6d811813db4e97b831b4b1fb95ec594c)、[STM32_DMA_CH_CFG_MODE](#a86e8ab71081233e1f9aa8300b6ea3c85)。

<a id="r_a944c3985d60fa92a53b9db6c57a54e6a"></a>

```c
#define STM32_DMA_MODE_CYCLIC STM32_DMA_CH_CFG_MODE(1)
```

相关声明：[STM32_DMA_MODE_CYCLIC](#a944c3985d60fa92a53b9db6c57a54e6a)、[STM32_DMA_CH_CFG_MODE](#a86e8ab71081233e1f9aa8300b6ea3c85)。

<a id="r_a1184bb6207bf6347ede5b3cfd1b67da9"></a>

```c
#define STM32_DMA_CH_CFG_DIRECTION(val)
```

相关声明：[STM32_DMA_CH_CFG_DIRECTION](#a1184bb6207bf6347ede5b3cfd1b67da9)。

位 6–7 配置 DMA 传输方向（Transfer Direction）。

<a id="r_a3678dc5bb6f7b7a7c7fbb87c43ad3724"></a>

```c
#define STM32_DMA_MEMORY_TO_MEMORY STM32_DMA_CH_CFG_DIRECTION(0)
```

相关声明：[STM32_DMA_MEMORY_TO_MEMORY](#a3678dc5bb6f7b7a7c7fbb87c43ad3724)、[STM32_DMA_CH_CFG_DIRECTION](#a1184bb6207bf6347ede5b3cfd1b67da9)。

<a id="r_ae0c8bc868d309a4fc1a57b28b6d88811"></a>

```c
#define STM32_DMA_MEMORY_TO_PERIPH STM32_DMA_CH_CFG_DIRECTION(1)
```

相关声明：[STM32_DMA_MEMORY_TO_PERIPH](#ae0c8bc868d309a4fc1a57b28b6d88811)、[STM32_DMA_CH_CFG_DIRECTION](#a1184bb6207bf6347ede5b3cfd1b67da9)。

<a id="r_a399cbac4220647c4604c94fdb7512f8a"></a>

```c
#define STM32_DMA_PERIPH_TO_MEMORY STM32_DMA_CH_CFG_DIRECTION(2)
```

相关声明：[STM32_DMA_PERIPH_TO_MEMORY](#a399cbac4220647c4604c94fdb7512f8a)、[STM32_DMA_CH_CFG_DIRECTION](#a1184bb6207bf6347ede5b3cfd1b67da9)。

<a id="r_a35bc7af86b12a421cc0391a43307d808"></a>

```c
#define STM32_DMA_PERIPH_TO_PERIPH STM32_DMA_CH_CFG_DIRECTION(3)
```

相关声明：[STM32_DMA_PERIPH_TO_PERIPH](#a35bc7af86b12a421cc0391a43307d808)、[STM32_DMA_CH_CFG_DIRECTION](#a1184bb6207bf6347ede5b3cfd1b67da9)。

<a id="r_a69d16d7d3474f075c8a639370297eeaa"></a>

```c
#define STM32_DMA_CH_CFG_PERIPH_ADDR_INC(val)
```

相关声明：[STM32_DMA_CH_CFG_PERIPH_ADDR_INC](#a69d16d7d3474f075c8a639370297eeaa)。

位 9 配置 DMA 外设地址递增（Peripheral Address Increment）。

<a id="r_aa7cc172e318bf2558a44c87f1b1d3693"></a>

```c
#define STM32_DMA_PERIPH_NO_INC STM32_DMA_CH_CFG_PERIPH_ADDR_INC(0)
```

相关声明：[STM32_DMA_PERIPH_NO_INC](#aa7cc172e318bf2558a44c87f1b1d3693)、[STM32_DMA_CH_CFG_PERIPH_ADDR_INC](#a69d16d7d3474f075c8a639370297eeaa)。

<a id="r_ae0f9a8b757005339a550959930084ecb"></a>

```c
#define STM32_DMA_PERIPH_INC STM32_DMA_CH_CFG_PERIPH_ADDR_INC(1)
```

相关声明：[STM32_DMA_PERIPH_INC](#ae0f9a8b757005339a550959930084ecb)、[STM32_DMA_CH_CFG_PERIPH_ADDR_INC](#a69d16d7d3474f075c8a639370297eeaa)。

<a id="r_abf66072cff1f8d835beb78a8d974fa2a"></a>

```c
#define STM32_DMA_CH_CFG_MEM_ADDR_INC(val)
```

相关声明：[STM32_DMA_CH_CFG_MEM_ADDR_INC](#abf66072cff1f8d835beb78a8d974fa2a)。

位 10 配置 DMA 内存地址递增（Memory Address Increment）。

<a id="r_ae46002f328f981e5dbe7bc502c46b759"></a>

```c
#define STM32_DMA_MEM_NO_INC STM32_DMA_CH_CFG_MEM_ADDR_INC(0)
```

相关声明：[STM32_DMA_MEM_NO_INC](#ae46002f328f981e5dbe7bc502c46b759)、[STM32_DMA_CH_CFG_MEM_ADDR_INC](#abf66072cff1f8d835beb78a8d974fa2a)。

<a id="r_a46f20993a4561c34cce25cf70f56879f"></a>

```c
#define STM32_DMA_MEM_INC STM32_DMA_CH_CFG_MEM_ADDR_INC(1)
```

相关声明：[STM32_DMA_MEM_INC](#a46f20993a4561c34cce25cf70f56879f)、[STM32_DMA_CH_CFG_MEM_ADDR_INC](#abf66072cff1f8d835beb78a8d974fa2a)。

<a id="r_a0c0c0c5cde99d895079197bf75c25245"></a>

```c
#define STM32_DMA_CH_CFG_PERIPH_WIDTH(val)
```

相关声明：[STM32_DMA_CH_CFG_PERIPH_WIDTH](#a0c0c0c5cde99d895079197bf75c25245)。

位 11、12 配置 DMA 外设数据大小（Peripheral Data Size）。

<a id="r_a8ab5a7090927e92bef333fb33416c32b"></a>

```c
#define STM32_DMA_PERIPH_8BITS STM32_DMA_CH_CFG_PERIPH_WIDTH(0)
```

相关声明：[STM32_DMA_PERIPH_8BITS](#a8ab5a7090927e92bef333fb33416c32b)、[STM32_DMA_CH_CFG_PERIPH_WIDTH](#a0c0c0c5cde99d895079197bf75c25245)。

<a id="r_aad24cf95434530d2d64025512d467d5e"></a>

```c
#define STM32_DMA_PERIPH_16BITS STM32_DMA_CH_CFG_PERIPH_WIDTH(1)
```

相关声明：[STM32_DMA_PERIPH_16BITS](#aad24cf95434530d2d64025512d467d5e)、[STM32_DMA_CH_CFG_PERIPH_WIDTH](#a0c0c0c5cde99d895079197bf75c25245)。

<a id="r_af869e4e36689a3b9402425f0a7dcc970"></a>

```c
#define STM32_DMA_PERIPH_32BITS STM32_DMA_CH_CFG_PERIPH_WIDTH(2)
```

相关声明：[STM32_DMA_PERIPH_32BITS](#af869e4e36689a3b9402425f0a7dcc970)、[STM32_DMA_CH_CFG_PERIPH_WIDTH](#a0c0c0c5cde99d895079197bf75c25245)。

<a id="r_ac0bb2e159dc52537c60851c1b9bac4c3"></a>

```c
#define STM32_DMA_CH_CFG_MEM_WIDTH(val)
```

相关声明：[STM32_DMA_CH_CFG_MEM_WIDTH](#ac0bb2e159dc52537c60851c1b9bac4c3)。

位 13、14 配置 DMA 内存数据大小（Memory Data Size）。

<a id="r_a372c638a2cffdcb69f7748e12e1564d9"></a>

```c
#define STM32_DMA_MEM_8BITS STM32_DMA_CH_CFG_MEM_WIDTH(0)
```

相关声明：[STM32_DMA_MEM_8BITS](#a372c638a2cffdcb69f7748e12e1564d9)、[STM32_DMA_CH_CFG_MEM_WIDTH](#ac0bb2e159dc52537c60851c1b9bac4c3)。

<a id="r_ac9f13ef8eb95fc507d707064a5dae605"></a>

```c
#define STM32_DMA_MEM_16BITS STM32_DMA_CH_CFG_MEM_WIDTH(1)
```

相关声明：[STM32_DMA_MEM_16BITS](#ac9f13ef8eb95fc507d707064a5dae605)、[STM32_DMA_CH_CFG_MEM_WIDTH](#ac0bb2e159dc52537c60851c1b9bac4c3)。

<a id="r_ab5cc477888dac48daacf0365530dba95"></a>

```c
#define STM32_DMA_MEM_32BITS STM32_DMA_CH_CFG_MEM_WIDTH(2)
```

相关声明：[STM32_DMA_MEM_32BITS](#ab5cc477888dac48daacf0365530dba95)、[STM32_DMA_CH_CFG_MEM_WIDTH](#ac0bb2e159dc52537c60851c1b9bac4c3)。

<a id="r_a7f7fa52e8b080c1ea756cd8df666c9cf"></a>

```c
#define STM32_DMA_CH_CFG_PERIPH_INC_FIXED(val)
```

相关声明：[STM32_DMA_CH_CFG_PERIPH_INC_FIXED](#a7f7fa52e8b080c1ea756cd8df666c9cf)。

位 15 配置 DMA 外设递增偏移（Peripheral Increment Offset）。

<a id="r_a23683d3d614c2b82cb5d93b9fe9f572d"></a>

```c
#define STM32_DMA_OFFSET_LINKED_BUS STM32_DMA_CH_CFG_PERIPH_INC_FIXED(0)
```

相关声明：[STM32_DMA_OFFSET_LINKED_BUS](#a23683d3d614c2b82cb5d93b9fe9f572d)、[STM32_DMA_CH_CFG_PERIPH_INC_FIXED](#a7f7fa52e8b080c1ea756cd8df666c9cf)。

<a id="r_a5ba0d5a9e52cb2f443504624606e4a10"></a>

```c
#define STM32_DMA_OFFSET_FIXED_4 STM32_DMA_CH_CFG_PERIPH_INC_FIXED(1)
```

相关声明：[STM32_DMA_OFFSET_FIXED_4](#a5ba0d5a9e52cb2f443504624606e4a10)、[STM32_DMA_CH_CFG_PERIPH_INC_FIXED](#a7f7fa52e8b080c1ea756cd8df666c9cf)。

<a id="r_add3e03ced6f685382d43058f0cbceb9b"></a>

```c
#define STM32_DMA_CH_CFG_PRIORITY(val)
```

相关声明：[STM32_DMA_CH_CFG_PRIORITY](#add3e03ced6f685382d43058f0cbceb9b)。

位 16、17 配置 DMA 优先级（Priority）。

<a id="r_a1e3161e8a567113a9b3a6874ad9c7ec9"></a>

```c
#define STM32_DMA_PRIORITY_LOW STM32_DMA_CH_CFG_PRIORITY(0)
```

相关声明：[STM32_DMA_PRIORITY_LOW](#a1e3161e8a567113a9b3a6874ad9c7ec9)、[STM32_DMA_CH_CFG_PRIORITY](#add3e03ced6f685382d43058f0cbceb9b)。

<a id="r_a7ab285799783a4a45248f97c24cc2572"></a>

```c
#define STM32_DMA_PRIORITY_MEDIUM STM32_DMA_CH_CFG_PRIORITY(1)
```

相关声明：[STM32_DMA_PRIORITY_MEDIUM](#a7ab285799783a4a45248f97c24cc2572)、[STM32_DMA_CH_CFG_PRIORITY](#add3e03ced6f685382d43058f0cbceb9b)。

<a id="r_a2aeaf7b8cccb8512d0f18c07e66465de"></a>

```c
#define STM32_DMA_PRIORITY_HIGH STM32_DMA_CH_CFG_PRIORITY(2)
```

相关声明：[STM32_DMA_PRIORITY_HIGH](#a2aeaf7b8cccb8512d0f18c07e66465de)、[STM32_DMA_CH_CFG_PRIORITY](#add3e03ced6f685382d43058f0cbceb9b)。

<a id="r_a5ce1311f75b678c623f1276de3463aa5"></a>

```c
#define STM32_DMA_PRIORITY_VERY_HIGH STM32_DMA_CH_CFG_PRIORITY(3)
```

相关声明：[STM32_DMA_PRIORITY_VERY_HIGH](#a5ce1311f75b678c623f1276de3463aa5)、[STM32_DMA_CH_CFG_PRIORITY](#add3e03ced6f685382d43058f0cbceb9b)。

<a id="r_a30103ad3e6fe698187674f09af5bf057"></a>

```c
#define STM32_DMA_FIFO_1_4 0U
```

相关声明：[STM32_DMA_FIFO_1_4](#a30103ad3e6fe698187674f09af5bf057)。

DMA 先进先出缓冲区阈值（FIFO Threshold）功能。

<a id="r_a6595f13f24d26e28aa82b1571c03075c"></a>

```c
#define STM32_DMA_FIFO_HALF 1U
```

相关声明：[STM32_DMA_FIFO_HALF](#a6595f13f24d26e28aa82b1571c03075c)。

<a id="r_a8720db61ce6623cf6a96ac862fa89041"></a>

```c
#define STM32_DMA_FIFO_3_4 2U
```

相关声明：[STM32_DMA_FIFO_3_4](#a8720db61ce6623cf6a96ac862fa89041)。

<a id="r_a4a561bb696eeaf8f8878fc327eab5f37"></a>

```c
#define STM32_DMA_FIFO_FULL 3U
```

相关声明：[STM32_DMA_FIFO_FULL](#a4a561bb696eeaf8f8878fc327eab5f37)。

<a id="r_ab26996ccb981ef26dc0783302f4564f7"></a>

```c
#define STM32_DMA_PERIPH_TX (STM32_DMA_MEMORY_TO_PERIPH | STM32_DMA_MEM_INC)
```

相关声明：[STM32_DMA_PERIPH_TX](#ab26996ccb981ef26dc0783302f4564f7)、[STM32_DMA_MEMORY_TO_PERIPH](#ae0c8bc868d309a4fc1a57b28b6d88811)、[STM32_DMA_MEM_INC](#a46f20993a4561c34cce25cf70f56879f)。

<a id="r_ac680c9808061136e327cf6a14b09ea57"></a>

```c
#define STM32_DMA_PERIPH_RX (STM32_DMA_PERIPH_TO_MEMORY | STM32_DMA_MEM_INC)
```

相关声明：[STM32_DMA_PERIPH_RX](#ac680c9808061136e327cf6a14b09ea57)、[STM32_DMA_PERIPH_TO_MEMORY](#a399cbac4220647c4604c94fdb7512f8a)、[STM32_DMA_MEM_INC](#a46f20993a4561c34cce25cf70f56879f)。

<a id="r_a7fd16b4e2d5fd63fc4d012def6f8c186"></a>

```c
#define STM32_DMA_16BITS (STM32_DMA_PERIPH_16BITS | STM32_DMA_MEM_16BITS)
```

相关声明：[STM32_DMA_16BITS](#a7fd16b4e2d5fd63fc4d012def6f8c186)、[STM32_DMA_PERIPH_16BITS](#aad24cf95434530d2d64025512d467d5e)、[STM32_DMA_MEM_16BITS](#ac9f13ef8eb95fc507d707064a5dae605)。

<a id="r_a9b7ff44eae7aa19676f46468e52db455"></a>

```c
#define STM32_DMA_32BITS (STM32_DMA_PERIPH_32BITS | STM32_DMA_MEM_32BITS)
```

相关声明：[STM32_DMA_32BITS](#a9b7ff44eae7aa19676f46468e52db455)、[STM32_DMA_PERIPH_32BITS](#af869e4e36689a3b9402425f0a7dcc970)、[STM32_DMA_MEM_32BITS](#ab5cc477888dac48daacf0365530dba95)。

## 39.2\_详细说明（Detailed Documentation）

<a id="a7fd16b4e2d5fd63fc4d012def6f8c186"></a>

### `STM32_DMA_16BITS`

```c
#define STM32_DMA_16BITS (STM32_DMA_PERIPH_16BITS | STM32_DMA_MEM_16BITS)
```

<a id="a9b7ff44eae7aa19676f46468e52db455"></a>

### `STM32_DMA_32BITS`

```c
#define STM32_DMA_32BITS (STM32_DMA_PERIPH_32BITS | STM32_DMA_MEM_32BITS)
```

<a id="a1184bb6207bf6347ede5b3cfd1b67da9"></a>

### `STM32_DMA_CH_CFG_DIRECTION`

```c
#define STM32_DMA_CH_CFG_DIRECTION ( val)
```

展开值（Value）：

```c
((val & 0x3) << 6)
```

位 6–7 配置 DMA 传输方向（Transfer Direction）。

<a id="abf66072cff1f8d835beb78a8d974fa2a"></a>

### `STM32_DMA_CH_CFG_MEM_ADDR_INC`

```c
#define STM32_DMA_CH_CFG_MEM_ADDR_INC ( val)
```

展开值（Value）：

```c
((val & 0x1) << 10)
```

位 10 配置 DMA 内存地址递增（Memory Address Increment）。

<a id="ac0bb2e159dc52537c60851c1b9bac4c3"></a>

### `STM32_DMA_CH_CFG_MEM_WIDTH`

```c
#define STM32_DMA_CH_CFG_MEM_WIDTH ( val)
```

展开值（Value）：

```c
((val & 0x3) << 13)
```

位 13、14 配置 DMA 内存数据大小（Memory Data Size）。

<a id="a86e8ab71081233e1f9aa8300b6ea3c85"></a>

### `STM32_DMA_CH_CFG_MODE`

```c
#define STM32_DMA_CH_CFG_MODE ( val)
```

展开值（Value）：

```c
((val & 0x1) << 5)
```

位 5 配置 DMA 循环模式（Cyclic Mode）。

<a id="a69d16d7d3474f075c8a639370297eeaa"></a>

### `STM32_DMA_CH_CFG_PERIPH_ADDR_INC`

```c
#define STM32_DMA_CH_CFG_PERIPH_ADDR_INC ( val)
```

展开值（Value）：

```c
((val & 0x1) << 9)
```

位 9 配置 DMA 外设地址递增（Peripheral Address Increment）。

<a id="a7f7fa52e8b080c1ea756cd8df666c9cf"></a>

### `STM32_DMA_CH_CFG_PERIPH_INC_FIXED`

```c
#define STM32_DMA_CH_CFG_PERIPH_INC_FIXED ( val)
```

展开值（Value）：

```c
((val & 0x1) << 15)
```

位 15 配置 DMA 外设递增偏移（Peripheral Increment Offset）。

<a id="a0c0c0c5cde99d895079197bf75c25245"></a>

### `STM32_DMA_CH_CFG_PERIPH_WIDTH`

```c
#define STM32_DMA_CH_CFG_PERIPH_WIDTH ( val)
```

展开值（Value）：

```c
((val & 0x3) << 11)
```

位 11、12 配置 DMA 外设数据大小（Peripheral Data Size）。

<a id="add3e03ced6f685382d43058f0cbceb9b"></a>

### `STM32_DMA_CH_CFG_PRIORITY`

```c
#define STM32_DMA_CH_CFG_PRIORITY ( val)
```

展开值（Value）：

```c
((val & 0x3) << 16)
```

位 16、17 配置 DMA 优先级（Priority）。

<a id="a30103ad3e6fe698187674f09af5bf057"></a>

### `STM32_DMA_FIFO_1_4`

```c
#define STM32_DMA_FIFO_1_4 0U
```

DMA 先进先出缓冲区阈值（FIFO Threshold）功能。

<a id="a8720db61ce6623cf6a96ac862fa89041"></a>

### `STM32_DMA_FIFO_3_4`

```c
#define STM32_DMA_FIFO_3_4 2U
```

<a id="a4a561bb696eeaf8f8878fc327eab5f37"></a>

### `STM32_DMA_FIFO_FULL`

```c
#define STM32_DMA_FIFO_FULL 3U
```

<a id="a6595f13f24d26e28aa82b1571c03075c"></a>

### `STM32_DMA_FIFO_HALF`

```c
#define STM32_DMA_FIFO_HALF 1U
```

<a id="ac9f13ef8eb95fc507d707064a5dae605"></a>

### `STM32_DMA_MEM_16BITS`

```c
#define STM32_DMA_MEM_16BITS STM32_DMA_CH_CFG_MEM_WIDTH(1)
```

<a id="ab5cc477888dac48daacf0365530dba95"></a>

### `STM32_DMA_MEM_32BITS`

```c
#define STM32_DMA_MEM_32BITS STM32_DMA_CH_CFG_MEM_WIDTH(2)
```

<a id="a372c638a2cffdcb69f7748e12e1564d9"></a>

### `STM32_DMA_MEM_8BITS`

```c
#define STM32_DMA_MEM_8BITS STM32_DMA_CH_CFG_MEM_WIDTH(0)
```

<a id="a46f20993a4561c34cce25cf70f56879f"></a>

### `STM32_DMA_MEM_INC`

```c
#define STM32_DMA_MEM_INC STM32_DMA_CH_CFG_MEM_ADDR_INC(1)
```

<a id="ae46002f328f981e5dbe7bc502c46b759"></a>

### `STM32_DMA_MEM_NO_INC`

```c
#define STM32_DMA_MEM_NO_INC STM32_DMA_CH_CFG_MEM_ADDR_INC(0)
```

<a id="a3678dc5bb6f7b7a7c7fbb87c43ad3724"></a>

### `STM32_DMA_MEMORY_TO_MEMORY`

```c
#define STM32_DMA_MEMORY_TO_MEMORY STM32_DMA_CH_CFG_DIRECTION(0)
```

<a id="ae0c8bc868d309a4fc1a57b28b6d88811"></a>

### `STM32_DMA_MEMORY_TO_PERIPH`

```c
#define STM32_DMA_MEMORY_TO_PERIPH STM32_DMA_CH_CFG_DIRECTION(1)
```

<a id="a944c3985d60fa92a53b9db6c57a54e6a"></a>

### `STM32_DMA_MODE_CYCLIC`

```c
#define STM32_DMA_MODE_CYCLIC STM32_DMA_CH_CFG_MODE(1)
```

<a id="a6d811813db4e97b831b4b1fb95ec594c"></a>

### `STM32_DMA_MODE_NORMAL`

```c
#define STM32_DMA_MODE_NORMAL STM32_DMA_CH_CFG_MODE(0)
```

<a id="a5ba0d5a9e52cb2f443504624606e4a10"></a>

### `STM32_DMA_OFFSET_FIXED_4`

```c
#define STM32_DMA_OFFSET_FIXED_4 STM32_DMA_CH_CFG_PERIPH_INC_FIXED(1)
```

<a id="a23683d3d614c2b82cb5d93b9fe9f572d"></a>

### `STM32_DMA_OFFSET_LINKED_BUS`

```c
#define STM32_DMA_OFFSET_LINKED_BUS STM32_DMA_CH_CFG_PERIPH_INC_FIXED(0)
```

<a id="aad24cf95434530d2d64025512d467d5e"></a>

### `STM32_DMA_PERIPH_16BITS`

```c
#define STM32_DMA_PERIPH_16BITS STM32_DMA_CH_CFG_PERIPH_WIDTH(1)
```

<a id="af869e4e36689a3b9402425f0a7dcc970"></a>

### `STM32_DMA_PERIPH_32BITS`

```c
#define STM32_DMA_PERIPH_32BITS STM32_DMA_CH_CFG_PERIPH_WIDTH(2)
```

<a id="a8ab5a7090927e92bef333fb33416c32b"></a>

### `STM32_DMA_PERIPH_8BITS`

```c
#define STM32_DMA_PERIPH_8BITS STM32_DMA_CH_CFG_PERIPH_WIDTH(0)
```

<a id="ae0f9a8b757005339a550959930084ecb"></a>

### `STM32_DMA_PERIPH_INC`

```c
#define STM32_DMA_PERIPH_INC STM32_DMA_CH_CFG_PERIPH_ADDR_INC(1)
```

<a id="aa7cc172e318bf2558a44c87f1b1d3693"></a>

### `STM32_DMA_PERIPH_NO_INC`

```c
#define STM32_DMA_PERIPH_NO_INC STM32_DMA_CH_CFG_PERIPH_ADDR_INC(0)
```

<a id="ac680c9808061136e327cf6a14b09ea57"></a>

### `STM32_DMA_PERIPH_RX`

```c
#define STM32_DMA_PERIPH_RX (STM32_DMA_PERIPH_TO_MEMORY | STM32_DMA_MEM_INC)
```

<a id="a399cbac4220647c4604c94fdb7512f8a"></a>

### `STM32_DMA_PERIPH_TO_MEMORY`

```c
#define STM32_DMA_PERIPH_TO_MEMORY STM32_DMA_CH_CFG_DIRECTION(2)
```

<a id="a35bc7af86b12a421cc0391a43307d808"></a>

### `STM32_DMA_PERIPH_TO_PERIPH`

```c
#define STM32_DMA_PERIPH_TO_PERIPH STM32_DMA_CH_CFG_DIRECTION(3)
```

<a id="ab26996ccb981ef26dc0783302f4564f7"></a>

### `STM32_DMA_PERIPH_TX`

```c
#define STM32_DMA_PERIPH_TX (STM32_DMA_MEMORY_TO_PERIPH | STM32_DMA_MEM_INC)
```

<a id="a2aeaf7b8cccb8512d0f18c07e66465de"></a>

### `STM32_DMA_PRIORITY_HIGH`

```c
#define STM32_DMA_PRIORITY_HIGH STM32_DMA_CH_CFG_PRIORITY(2)
```

<a id="a1e3161e8a567113a9b3a6874ad9c7ec9"></a>

### `STM32_DMA_PRIORITY_LOW`

```c
#define STM32_DMA_PRIORITY_LOW STM32_DMA_CH_CFG_PRIORITY(0)
```

<a id="a7ab285799783a4a45248f97c24cc2572"></a>

### `STM32_DMA_PRIORITY_MEDIUM`

```c
#define STM32_DMA_PRIORITY_MEDIUM STM32_DMA_CH_CFG_PRIORITY(1)
```

<a id="a5ce1311f75b678c623f1276de3463aa5"></a>

### `STM32_DMA_PRIORITY_VERY_HIGH`

```c
#define STM32_DMA_PRIORITY_VERY_HIGH STM32_DMA_CH_CFG_PRIORITY(3)
```


## 39.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P189_stm32_dma.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P038_zephyr__dt-bindings__pinctrl__stm32-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P040_zephyr__dt-bindings__pwm__stm32_pwm.h_文件参考.md)
