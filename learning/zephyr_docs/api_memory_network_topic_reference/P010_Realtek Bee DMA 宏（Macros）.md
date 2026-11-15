---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-10
title: Realtek Bee DMA 宏（Macros）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_Realtek Bee DMA 宏（Macros）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于从设备树（Devicetree）提取DMA配置的宏。

<a id="details"></a>

用于从设备树（Devicetree）提取DMA配置的宏。

<a id="header-files"></a>
<a id="files"></a>

## 10.1\_文件（Files）

<a id="r_dma_5Fbee_2Eh"></a>

```c
file dma_bee.h
```

相关声明：[dma_bee.h](../api_file_system_power_reference/P006_zephyr__drivers__dma__dma_bee.h_文件参考.md)。

Realtek Bee直接内存访问（DMA）的配置宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.2\_宏定义（Macros）

<a id="r_ga7f7de861a3d6579de3ec0255eff5ef81"></a>

```c
#define BEE_DMA_CTLR(id, dir)
```

相关声明：[BEE_DMA_CTLR](#ga7f7de861a3d6579de3ec0255eff5ef81)。

获取 DMA 控制器设备节点标识符（Device Node Identifier）。

<a id="r_ga5c8f42abc8e0c017d5d59dca440ad830"></a>

```c
#define BEE_DMA_CHANNEL_CONFIG(id, dir)
```

相关声明：[BEE_DMA_CHANNEL_CONFIG](#ga5c8f42abc8e0c017d5d59dca440ad830)。

从设备树（Devicetree）获取原始配置值（Raw Configuration Value）。

<a id="r_gaad85cefe1e3acecb5e0db39a70891ec7"></a>

```c
#define BEE_DMA_CONFIG_DIRECTION(config)
```

相关声明：[BEE_DMA_CONFIG_DIRECTION](#gaad85cefe1e3acecb5e0db39a70891ec7)。

提取 DMA 传输方向（Transfer Direction）。

<a id="r_gac8040213e8e245dcf35e26983abe18e7"></a>

```c
#define BEE_DMA_CONFIG_SOURCE_ADDR_INC(config)
```

相关声明：[BEE_DMA_CONFIG_SOURCE_ADDR_INC](#gac8040213e8e245dcf35e26983abe18e7)。

提取源地址递增模式（Source Address Increment Mode）。

<a id="r_ga5f5b3ffe251f9ba7f2829dc24ca84d7c"></a>

```c
#define BEE_DMA_CONFIG_DESTINATION_ADDR_INC(config)
```

相关声明：[BEE_DMA_CONFIG_DESTINATION_ADDR_INC](#ga5f5b3ffe251f9ba7f2829dc24ca84d7c)。

提取目的地址递增模式（Destination Address Increment Mode）。

<a id="r_gaf7f813b700f9d3df193e13e915ebc229"></a>

```c
#define BEE_DMA_CONFIG_SOURCE_DATA_SIZE(config)
```

相关声明：[BEE_DMA_CONFIG_SOURCE_DATA_SIZE](#gaf7f813b700f9d3df193e13e915ebc229)。

提取源数据大小（Source Data Size），单位为字节。

<a id="r_ga3cab990c70baa4f7e0bc9bb2a8d87b5b"></a>

```c
#define BEE_DMA_CONFIG_DESTINATION_DATA_SIZE(config)
```

相关声明：[BEE_DMA_CONFIG_DESTINATION_DATA_SIZE](#ga3cab990c70baa4f7e0bc9bb2a8d87b5b)。

提取目的数据大小（Destination Data Size），单位为字节。

<a id="r_ga1a172ed943d0f0f58f583bffe7d341a6"></a>

```c
#define BEE_DMA_CONFIG_SOURCE_MSIZE(config)
```

相关声明：[BEE_DMA_CONFIG_SOURCE_MSIZE](#ga1a172ed943d0f0f58f583bffe7d341a6)。

提取源端 MSIZE（Source MSIZE）。

<a id="r_gae85ae32789febeaae914e7d49cf7c6c5"></a>

```c
#define BEE_DMA_CONFIG_DESTINATION_MSIZE(config)
```

相关声明：[BEE_DMA_CONFIG_DESTINATION_MSIZE](#gae85ae32789febeaae914e7d49cf7c6c5)。

提取目的端 MSIZE（Destination MSIZE）。

<a id="r_gaf6e9123b444721e303483b79abeff47c"></a>

```c
#define BEE_DMA_CONFIG_PRIORITY(config)
```

相关声明：[BEE_DMA_CONFIG_PRIORITY](#gaf6e9123b444721e303483b79abeff47c)。

提取通道优先级（Channel Priority）。

## 10.3\_详细说明（Detailed Documentation）

<a id="ga5c8f42abc8e0c017d5d59dca440ad830"></a>

### `BEE_DMA_CHANNEL_CONFIG`

```c
#define BEE_DMA_CHANNEL_CONFIG ( id, dir )
```

```c
#include <zephyr/drivers/dma/dma_bee.h>
```

展开值（Value）：

```c
DT_INST_DMAS_CELL_BY_NAME(id, dir, config)
```

从设备树（Devicetree）获取原始配置值（Raw Configuration Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 实例标识符（Instance Identifier）。 |
| `dir` | 方向名称（Direction Name），例如 rx、tx。 |

**返回（Returns）**：返回值（Returns）：config 单元（Cell）的整数值。

<a id="ga5f5b3ffe251f9ba7f2829dc24ca84d7c"></a>

### `BEE_DMA_CONFIG_DESTINATION_ADDR_INC`

```c
#define BEE_DMA_CONFIG_DESTINATION_ADDR_INC ( config)
```

```c
#include <zephyr/drivers/dma/dma_bee.h>
```

展开值（Value）：

```c
((config >> 4) & 0x3)
```

提取目的地址递增模式（Destination Address Increment Mode）。

位于 config 的位 4～5。

- 0：递增（Increment）。
- 1：递减（Decrement）。
- 2：不变（No Change）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `config` | 配置值（Configuration Value）。 |

**返回（Returns）**：返回值（Returns）：目标地址递增模式（Destination Address Increment Mode），0～3。

<a id="ga3cab990c70baa4f7e0bc9bb2a8d87b5b"></a>

### `BEE_DMA_CONFIG_DESTINATION_DATA_SIZE`

```c
#define BEE_DMA_CONFIG_DESTINATION_DATA_SIZE ( config)
```

```c
#include <zephyr/drivers/dma/dma_bee.h>
```

展开值（Value）：

```c
(1 << ((config >> 8) & 0x3))
```

提取目的数据大小（Destination Data Size），单位为字节。

位于 config 的位 8～9。

- 0 → 1 字节（Byte）。
- 1 → 2 字节（Bytes）。
- 2 → 4 字节（Bytes）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `config` | 配置值（Configuration Value）。 |

**返回（Returns）**：返回值（Returns）：数据大小，单位为字节，可为 1、2 或 4。

<a id="gae85ae32789febeaae914e7d49cf7c6c5"></a>

### `BEE_DMA_CONFIG_DESTINATION_MSIZE`

```c
#define BEE_DMA_CONFIG_DESTINATION_MSIZE ( config)
```

```c
#include <zephyr/drivers/dma/dma_bee.h>
```

展开值（Value）：

```c
((1 << (((config >> 13) & 0x7) + 1)) - (((config >> 13) & 0x7) == 0 ? 1 : 0))
```

提取目的端 MSIZE（Destination MSIZE）。

位于 config 的位 13～15，将 3 位索引映射为实际 msize：

- 0 → msize（突发大小）。
- 1 → msize 4（突发大小）。
- 2 → msize 8（突发大小）。
- 3 → msize 16（突发大小）。
- 4 → msize 32（突发大小）。
- 5 → msize 64（突发大小）。
- 6 → msize 128（突发大小）。
- 7 → msize 256（突发大小）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `config` | 配置值（Configuration Value）。 |

**返回（Returns）**：返回值（Returns）：突发大小（Burst Size）。

<a id="gaad85cefe1e3acecb5e0db39a70891ec7"></a>

### `BEE_DMA_CONFIG_DIRECTION`

```c
#define BEE_DMA_CONFIG_DIRECTION ( config)
```

```c
#include <zephyr/drivers/dma/dma_bee.h>
```

展开值（Value）：

```c
((config >> 0) & 0x3)
```

提取 DMA 传输方向（Transfer Direction）。

位于 config 的位 0～1。

- 0：内存到内存（Memory to Memory）。
- 1：内存到外设（Memory to Peripheral）。
- 2：外设到内存（Peripheral to Memory）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `config` | 配置值（Configuration Value）。 |

**返回（Returns）**：返回值（Returns）：方向代码（Direction Code），0～3。

<a id="gaf6e9123b444721e303483b79abeff47c"></a>

### `BEE_DMA_CONFIG_PRIORITY`

```c
#define BEE_DMA_CONFIG_PRIORITY ( config)
```

```c
#include <zephyr/drivers/dma/dma_bee.h>
```

展开值（Value）：

```c
((config >> 16) & 0x1f)
```

提取通道优先级（Channel Priority）。

位于 config 的位 16～20，范围为 0～9。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `config` | 配置值（Configuration Value）。 |

**返回（Returns）**：返回值（Returns）：优先级（Priority Level）。

<a id="gac8040213e8e245dcf35e26983abe18e7"></a>

### `BEE_DMA_CONFIG_SOURCE_ADDR_INC`

```c
#define BEE_DMA_CONFIG_SOURCE_ADDR_INC ( config)
```

```c
#include <zephyr/drivers/dma/dma_bee.h>
```

展开值（Value）：

```c
((config >> 2) & 0x3)
```

提取源地址递增模式（Source Address Increment Mode）。

位于 config 的位 2～3。

- 0：递增（Increment）。
- 1：递减（Decrement）。
- 2：不变（No Change）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `config` | 配置值（Configuration Value）。 |

**返回（Returns）**：返回值（Returns）：源地址递增模式（Source Address Increment Mode），0～3。

<a id="gaf7f813b700f9d3df193e13e915ebc229"></a>

### `BEE_DMA_CONFIG_SOURCE_DATA_SIZE`

```c
#define BEE_DMA_CONFIG_SOURCE_DATA_SIZE ( config)
```

```c
#include <zephyr/drivers/dma/dma_bee.h>
```

展开值（Value）：

```c
(1 << ((config >> 6) & 0x3))
```

提取源数据大小（Source Data Size），单位为字节。

位于 config 的位 6～7。

- 0 → 1 字节（Byte）。
- 1 → 2 字节（Bytes）。
- 2 → 4 字节（Bytes）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `config` | 配置值（Configuration Value）。 |

**返回（Returns）**：返回值（Returns）：数据大小，单位为字节，可为 1、2 或 4。

<a id="ga1a172ed943d0f0f58f583bffe7d341a6"></a>

### `BEE_DMA_CONFIG_SOURCE_MSIZE`

```c
#define BEE_DMA_CONFIG_SOURCE_MSIZE ( config)
```

```c
#include <zephyr/drivers/dma/dma_bee.h>
```

展开值（Value）：

```c
((1 << (((config >> 10) & 0x7) + 1)) - (((config >> 10) & 0x7) == 0 ? 1 : 0))
```

提取源端 MSIZE（Source MSIZE）。

位于 config 的位 10～12，将 3 位索引映射为实际 msize：

- 0 → msize（突发大小）。
- 1 → msize 4（突发大小）。
- 2 → msize 8（突发大小）。
- 3 → msize 16（突发大小）。
- 4 → msize 32（突发大小）。
- 5 → msize 64（突发大小）。
- 6 → msize 128（突发大小）。
- 7 → msize 256（突发大小）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `config` | 配置值（Configuration Value）。 |

**返回（Returns）**：返回值（Returns）：突发大小（Burst Size）。

<a id="ga7f7de861a3d6579de3ec0255eff5ef81"></a>

### `BEE_DMA_CTLR`

```c
#define BEE_DMA_CTLR ( id, dir )
```

```c
#include <zephyr/drivers/dma/dma_bee.h>
```

展开值（Value）：

```c
DT_INST_DMAS_CTLR_BY_NAME(id, dir)
```

获取 DMA 控制器设备节点标识符（Device Node Identifier）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 实例标识符（Instance Identifier）。 |
| `dir` | 方向名称（Direction Name），例如 rx、tx。 |

**返回（Returns）**：返回值（Returns）：控制器设备标识符（Controller Device Identifier）。


## 10.4\_原页交叉引用（Cross References）

- [dma_bee.h](../api_file_system_power_reference/P006_zephyr__drivers__dma__dma_bee.h_文件参考.md)
- [DT_INST_DMAS_CELL_BY_NAME](../dma_reference/P008_DMA设备树宏.md#ga2cc0124a66cf3b9f1c4c506b7f978d30)
- [DT_INST_DMAS_CTLR_BY_NAME](../dma_reference/P008_DMA设备树宏.md#gad098f0b51ee1f629c1259ca346f49303)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-dmas_html_ga2cc0124a66cf3b9f1c4c506b7f978d30"></a>
<a id="agroup__devicetree-dmas_html_gad098f0b51ee1f629c1259ca346f49303"></a>

---

[上一章](P009_音量控制配置文件（Volume Control Profile，VCP）.md) · [返回大纲](大纲.md) · [下一章](P011_以太网物理层接口（Ethernet PHY Interface）.md)
