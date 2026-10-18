---
id: learning.zephyr-docs.dma-reference.page-5
title: DMA运行状态
kind: reference
status: maintained
domains: [zephyr, dma, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdma__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_DMA运行状态

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdma__status.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是直接内存访问（Direct Memory Access，DMA）应用程序接口（Application Programming Interface，API）参考。先读[DMA概述](../hardware/P011_DMA直接内存访问.md)，再按[本册大纲](大纲.md)区分通道配置（Channel Configuration）、传输块（Transfer Block）、运行状态（Runtime Status）与驱动后端（Driver Backend）。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

DMA运行时状态结构（Runtime Status）。

```c
#include <zephyr/drivers/dma.h>
```

<a id="details"></a>

DMA运行时状态结构（Runtime Status）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a92ec05d9207caa828064661897f2f31c"></a>

```c
bool busy
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[busy](#a92ec05d9207caa828064661897f2f31c)。

当前DMA传输是忙碌（Busy）还是空闲（Idle）。

<a id="r_aacfe94ad8e60ea77bca2423bd9bf8409"></a>

```c
enum dma_channel_direction dir
```

相关声明：[dma_channel_direction](P001_DMA公共接口.md#gae442d8ba73be7e53b68165647b0ea402)、[dir](#aacfe94ad8e60ea77bca2423bd9bf8409)。

传输方向。

<a id="r_a3a33f92b1d100f988fca2bea0a6deb24"></a>

```c
uint32_t pending_length
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pending_length](#a3a33f92b1d100f988fca2bea0a6deb24)。

待传输长度，单位为字节，具体含义取决于硬件。

<a id="r_a2b481bf13de03e49146eb6a26563776e"></a>

```c
uint32_t free
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[free](#a2b481bf13de03e49146eb6a26563776e)。

可用缓冲区空间，具体含义取决于硬件。

<a id="r_aa7288b85f41098e59ad4f96dcea4ccde"></a>

```c
uint32_t write_position
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[write_position](#aa7288b85f41098e59ad4f96dcea4ccde)。

循环DMA缓冲区中的写入位置，具体含义取决于硬件。

<a id="r_afa401acfb26cd26b73e4a52066989847"></a>

```c
uint32_t read_position
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[read_position](#afa401acfb26cd26b73e4a52066989847)。

循环DMA缓冲区中的读取位置，具体含义取决于硬件。

<a id="r_a9f743c98e6343d55eccc27e528b79b1a"></a>

```c
uint64_t total_copied
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[total_copied](#a9f743c98e6343d55eccc27e528b79b1a)。

累计复制量（Total Copied），具体含义取决于硬件。

## 5.2\_详细说明（Detailed Documentation）

<a id="a92ec05d9207caa828064661897f2f31c"></a>

### `busy`

```c
bool dma_status::busy
```

当前DMA传输是忙碌（Busy）还是空闲（Idle）。

<a id="aacfe94ad8e60ea77bca2423bd9bf8409"></a>

### `dir`

```c
enum dma_channel_direction dma_status::dir
```

传输方向。

<a id="a2b481bf13de03e49146eb6a26563776e"></a>

### `free`

```c
uint32_t dma_status::free
```

可用缓冲区空间，具体含义取决于硬件。

<a id="a3a33f92b1d100f988fca2bea0a6deb24"></a>

### `pending_length`

```c
uint32_t dma_status::pending_length
```

待传输长度，单位为字节，具体含义取决于硬件。

<a id="afa401acfb26cd26b73e4a52066989847"></a>

### `read_position`

```c
uint32_t dma_status::read_position
```

循环DMA缓冲区中的读取位置，具体含义取决于硬件。

<a id="a9f743c98e6343d55eccc27e528b79b1a"></a>

### `total_copied`

```c
uint64_t dma_status::total_copied
```

累计复制量（Total Copied），具体含义取决于硬件。

<a id="aa7288b85f41098e59ad4f96dcea4ccde"></a>

### `write_position`

```c
uint32_t dma_status::write_position
```

循环DMA缓冲区中的写入位置，具体含义取决于硬件。

## 5.3\_源码定位与版本边界

接口、配置结构和内联包装均可在仓库的[dma.h](../../../include/zephyr/drivers/dma.h)中相对定位。本次译注核对了[官方main头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/dma.h)，摘要见[来源记录](../SOURCES.md)；本地源码、滚动更新的main与latest网页不能自动视为同一版本。原始头文件法律署名为Copyright (c) 2016 Intel Corporation，许可证为Apache-2.0。

> 译注——状态解释：pending_length、free、write_position、read_position和total_copied都标记为硬件相关。应只依据目标驱动实际填充和支持的字段判断状态，不能把所有驱动的total_copied都当成同一种累计计数器。查询前提供有效dma_status对象，并检查函数返回值。

本批只翻译和核对官方源码，没有构建、执行DMA搬运、运行驱动测试或进行实板验证；这组参考也不声明本仓库已实现HC32 DMA驱动。

## 5.4\_原页交叉引用（Cross References）

- [zephyr/drivers/dma.h](P010_DMA驱动头文件源码.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [dma_channel_direction](P001_DMA公共接口.md#gae442d8ba73be7e53b68165647b0ea402)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_DMA通道配置.md) · [返回大纲](大纲.md) · [下一章](P006_DMA通道分配上下文.md)
