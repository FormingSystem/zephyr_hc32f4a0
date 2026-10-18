---
id: learning.zephyr-docs.api-file-system-power-reference.page-6
title: zephyr__drivers__dma__dma_bee.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__bee_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_drivers\_\_dma\_\_dma\_bee.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dma__bee_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Realtek Bee直接内存访问（DMA）的配置宏。

查看此文件的源码。

<a id="details"></a>

Realtek Bee DMA 配置宏（Configuration Macros）。本头文件包含辅助宏，用于从 Realtek Bee 系列 SoC 的设备树配置单元（Devicetree Config Cell）提取 DMA 配置参数，例如方向、数据大小、突发大小等。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_ga7f7de861a3d6579de3ec0255eff5ef81"></a>

```c
#define BEE_DMA_CTLR(id, dir)
```

相关声明：[BEE_DMA_CTLR](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#ga7f7de861a3d6579de3ec0255eff5ef81)。

获取 DMA 控制器设备节点标识符（Device Node Identifier）。

<a id="r_ga5c8f42abc8e0c017d5d59dca440ad830"></a>

```c
#define BEE_DMA_CHANNEL_CONFIG(id, dir)
```

相关声明：[BEE_DMA_CHANNEL_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#ga5c8f42abc8e0c017d5d59dca440ad830)。

从设备树（Devicetree）获取原始配置值（Raw Configuration Value）。

<a id="r_gaad85cefe1e3acecb5e0db39a70891ec7"></a>

```c
#define BEE_DMA_CONFIG_DIRECTION(config)
```

相关声明：[BEE_DMA_CONFIG_DIRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#gaad85cefe1e3acecb5e0db39a70891ec7)。

提取 DMA 传输方向（Transfer Direction）。

<a id="r_gac8040213e8e245dcf35e26983abe18e7"></a>

```c
#define BEE_DMA_CONFIG_SOURCE_ADDR_INC(config)
```

相关声明：[BEE_DMA_CONFIG_SOURCE_ADDR_INC](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#gac8040213e8e245dcf35e26983abe18e7)。

提取源地址递增模式（Source Address Increment Mode）。

<a id="r_ga5f5b3ffe251f9ba7f2829dc24ca84d7c"></a>

```c
#define BEE_DMA_CONFIG_DESTINATION_ADDR_INC(config)
```

相关声明：[BEE_DMA_CONFIG_DESTINATION_ADDR_INC](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#ga5f5b3ffe251f9ba7f2829dc24ca84d7c)。

提取目的地址递增模式（Destination Address Increment Mode）。

<a id="r_gaf7f813b700f9d3df193e13e915ebc229"></a>

```c
#define BEE_DMA_CONFIG_SOURCE_DATA_SIZE(config)
```

相关声明：[BEE_DMA_CONFIG_SOURCE_DATA_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#gaf7f813b700f9d3df193e13e915ebc229)。

提取源数据大小（Source Data Size），单位为字节。

<a id="r_ga3cab990c70baa4f7e0bc9bb2a8d87b5b"></a>

```c
#define BEE_DMA_CONFIG_DESTINATION_DATA_SIZE(config)
```

相关声明：[BEE_DMA_CONFIG_DESTINATION_DATA_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#ga3cab990c70baa4f7e0bc9bb2a8d87b5b)。

提取目的数据大小（Destination Data Size），单位为字节。

<a id="r_ga1a172ed943d0f0f58f583bffe7d341a6"></a>

```c
#define BEE_DMA_CONFIG_SOURCE_MSIZE(config)
```

相关声明：[BEE_DMA_CONFIG_SOURCE_MSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#ga1a172ed943d0f0f58f583bffe7d341a6)。

提取源端 MSIZE（Source MSIZE）。

<a id="r_gae85ae32789febeaae914e7d49cf7c6c5"></a>

```c
#define BEE_DMA_CONFIG_DESTINATION_MSIZE(config)
```

相关声明：[BEE_DMA_CONFIG_DESTINATION_MSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#gae85ae32789febeaae914e7d49cf7c6c5)。

提取目的端 MSIZE（Destination MSIZE）。

<a id="r_gaf6e9123b444721e303483b79abeff47c"></a>

```c
#define BEE_DMA_CONFIG_PRIORITY(config)
```

相关声明：[BEE_DMA_CONFIG_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#gaf6e9123b444721e303483b79abeff47c)。

提取通道优先级（Channel Priority）。


## 6.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_runtime_reference/P012_dma_bee.h_源码浏览.md)
- [BEE_DMA_CTLR](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#ga7f7de861a3d6579de3ec0255eff5ef81)
- [BEE_DMA_CHANNEL_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#ga5c8f42abc8e0c017d5d59dca440ad830)
- [BEE_DMA_CONFIG_DIRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#gaad85cefe1e3acecb5e0db39a70891ec7)
- [BEE_DMA_CONFIG_SOURCE_ADDR_INC](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#gac8040213e8e245dcf35e26983abe18e7)
- [BEE_DMA_CONFIG_DESTINATION_ADDR_INC](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#ga5f5b3ffe251f9ba7f2829dc24ca84d7c)
- [BEE_DMA_CONFIG_SOURCE_DATA_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#gaf7f813b700f9d3df193e13e915ebc229)
- [BEE_DMA_CONFIG_DESTINATION_DATA_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#ga3cab990c70baa4f7e0bc9bb2a8d87b5b)
- [BEE_DMA_CONFIG_SOURCE_MSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#ga1a172ed943d0f0f58f583bffe7d341a6)
- [BEE_DMA_CONFIG_DESTINATION_MSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#gae85ae32789febeaae914e7d49cf7c6c5)
- [BEE_DMA_CONFIG_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html#gaf6e9123b444721e303483b79abeff47c)

<a id="header-details"></a>

---

[上一章](P005_zephyr__cleanup.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__net__dplpmtud.h_文件参考.md)
