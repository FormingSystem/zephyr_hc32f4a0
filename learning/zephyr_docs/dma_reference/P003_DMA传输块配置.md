---
id: learning.zephyr-docs.dma-reference.page-3
title: DMA传输块配置
kind: reference
status: maintained
domains: [zephyr, dma, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdma__block__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_DMA传输块配置

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdma__block__config.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是直接内存访问（Direct Memory Access，DMA）应用程序接口（Application Programming Interface，API）参考。先读[DMA概述](../hardware/P011_DMA直接内存访问.md)，再按[本册大纲](大纲.md)区分通道配置（Channel Configuration）、传输块（Transfer Block）、运行状态（Runtime Status）与驱动后端（Driver Backend）。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

DMA传输块配置结构（Block Configuration）。

```c
#include <zephyr/drivers/dma.h>
```

<a id="details"></a>

DMA传输块配置结构（Block Configuration）。除源地址、目标地址和块大小外，其中许多选项都取决于硬件及驱动。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a9fbd1deae8936a806ecc79bad3f3b9bb"></a>

```c
uint32_t source_address
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[source_address](#a9fbd1deae8936a806ecc79bad3f3b9bb)。

传输块的源起始地址。

<a id="r_a9a66e0a647c55e94423ababf44c04325"></a>

```c
uint32_t dest_address
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dest_address](#a9a66e0a647c55e94423ababf44c04325)。

传输块的目标起始地址。

<a id="r_a3180ef98f007ad9be7f6ff363dc125c3"></a>

```c
uint32_t source_gather_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[source_gather_interval](#a3180ef98f007ad9be7f6ff363dc125c3)。

聚集边界（Gather Boundary）处的地址调整量。

<a id="r_a18bafb80538bca9c12197955770b6511"></a>

```c
uint32_t dest_scatter_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dest_scatter_interval](#a18bafb80538bca9c12197955770b6511)。

分散边界（Scatter Boundary）处的地址调整量。

<a id="r_ae38027f6262c34d9f1abe4f923d904b4"></a>

```c
uint16_t dest_scatter_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dest_scatter_count](#ae38027f6262c34d9f1abe4f923d904b4)。

两个分散边界之间的连续传输次数。

<a id="r_a8ffcde07d02317b3cc1b327bd0b88395"></a>

```c
uint16_t source_gather_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[source_gather_count](#a8ffcde07d02317b3cc1b327bd0b88395)。

两个聚集边界之间的连续传输次数。

<a id="r_a3fdab19df16d5e96054aabffbf27fcc1"></a>

```c
uint32_t block_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[block_size](#a3fdab19df16d5e96054aabffbf27fcc1)。

此传输块需要传输的字节数。

<a id="r_a937168582c7473fe1b2b696cd1433605"></a>

```c
struct dma_block_config * next_block
```

相关声明：[dma_block_config](P003_DMA传输块配置.md)、[next_block](#a937168582c7473fe1b2b696cd1433605)。

指向传输列表中的下一个块。

<a id="r_abbac399f6c6e18ad2ed25359ebb799ef"></a>

```c
uint16_t source_gather_en: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[source_gather_en](#abbac399f6c6e18ad2ed25359ebb799ef)。

置1时启用源聚集（Source Gathering）。

<a id="r_a778935d5b806002b902b72304b845ea0"></a>

```c
uint16_t dest_scatter_en: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dest_scatter_en](#a778935d5b806002b902b72304b845ea0)。

置1时启用目标分散（Destination Scattering）。

<a id="r_a9110f948520186aa5718f57b4bbbd24a"></a>

```c
uint16_t source_addr_adj: 2
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[source_addr_adj](#a9110f948520186aa5718f57b4bbbd24a)。

源地址调整选项（Source Address Adjustment）。

<a id="r_ad69502226d2c60adbdb9fe5e93dc0a05"></a>

```c
uint16_t dest_addr_adj: 2
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dest_addr_adj](#ad69502226d2c60adbdb9fe5e93dc0a05)。

目标地址调整方式（Destination Address Adjustment）。

<a id="r_a4f8f5b65002f65eaacdd3dde26c47170"></a>

```c
uint16_t source_reload_en: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[source_reload_en](#a4f8f5b65002f65eaacdd3dde26c47170)。

块传输结束时重新装载源地址。

<a id="r_a7dedf429f44f3af6fcc0db125d6494c8"></a>

```c
uint16_t dest_reload_en: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dest_reload_en](#a7dedf429f44f3af6fcc0db125d6494c8)。

块传输结束时重新装载目标地址。

<a id="r_a877a30b62fd8e0e1773890a10c8a2751"></a>

```c
uint16_t fifo_mode_control: 4
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[fifo_mode_control](#a877a30b62fd8e0e1773890a10c8a2751)。

开始传输前的先进先出缓冲区（First In, First Out，FIFO）填充设置，具体含义取决于硬件。

<a id="r_aecf6805b898a70922c58d15127bafc92"></a>

```c
uint16_t flow_control_mode: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[flow_control_mode](#aecf6805b898a70922c58d15127bafc92)。

传输流控模式（Flow Control Mode）。

## 3.2\_详细说明（Detailed Documentation）

<a id="a3fdab19df16d5e96054aabffbf27fcc1"></a>

### `block_size`

```c
uint32_t dma_block_config::block_size
```

此传输块需要传输的字节数。

<a id="ad69502226d2c60adbdb9fe5e93dc0a05"></a>

### `dest_addr_adj`

```c
uint16_t dma_block_config::dest_addr_adj
```

目标地址调整方式（Destination Address Adjustment）。

- 0b00：递增（Increment）。
- 0b01：递减（Decrement）。
- 0b10：保持不变（No Change）。

<a id="a9a66e0a647c55e94423ababf44c04325"></a>

### `dest_address`

```c
uint32_t dma_block_config::dest_address
```

传输块的目标起始地址。

<a id="a7dedf429f44f3af6fcc0db125d6494c8"></a>

### `dest_reload_en`

```c
uint16_t dma_block_config::dest_reload_en
```

块传输结束时重新装载目标地址。

<a id="ae38027f6262c34d9f1abe4f923d904b4"></a>

### `dest_scatter_count`

```c
uint16_t dma_block_config::dest_scatter_count
```

两个分散边界之间的连续传输次数。

<a id="a778935d5b806002b902b72304b845ea0"></a>

### `dest_scatter_en`

```c
uint16_t dma_block_config::dest_scatter_en
```

置1时启用目标分散（Destination Scattering）。

<a id="a18bafb80538bca9c12197955770b6511"></a>

### `dest_scatter_interval`

```c
uint32_t dma_block_config::dest_scatter_interval
```

分散边界（Scatter Boundary）处的地址调整量。

<a id="a877a30b62fd8e0e1773890a10c8a2751"></a>

### `fifo_mode_control`

```c
uint16_t dma_block_config::fifo_mode_control
```

开始传输前的先进先出缓冲区（First In, First Out，FIFO）填充设置，具体含义取决于硬件。

<a id="aecf6805b898a70922c58d15127bafc92"></a>

### `flow_control_mode`

```c
uint16_t dma_block_config::flow_control_mode
```

传输流控模式（Flow Control Mode）。

- 0b0：数据可用时，源端请求服务。
- 0b1：源端请求延后，直到目标端发出请求。

<a id="a937168582c7473fe1b2b696cd1433605"></a>

### `next_block`

```c
struct dma_block_config* dma_block_config::next_block
```

指向传输列表中的下一个块。

<a id="a9110f948520186aa5718f57b4bbbd24a"></a>

### `source_addr_adj`

```c
uint16_t dma_block_config::source_addr_adj
```

源地址调整选项（Source Address Adjustment）。

- 0b00：递增（Increment）。
- 0b01：递减（Decrement）。
- 0b10：保持不变（No Change）。

<a id="a9fbd1deae8936a806ecc79bad3f3b9bb"></a>

### `source_address`

```c
uint32_t dma_block_config::source_address
```

传输块的源起始地址。

<a id="a8ffcde07d02317b3cc1b327bd0b88395"></a>

### `source_gather_count`

```c
uint16_t dma_block_config::source_gather_count
```

两个聚集边界之间的连续传输次数。

<a id="abbac399f6c6e18ad2ed25359ebb799ef"></a>

### `source_gather_en`

```c
uint16_t dma_block_config::source_gather_en
```

置1时启用源聚集（Source Gathering）。

<a id="a3180ef98f007ad9be7f6ff363dc125c3"></a>

### `source_gather_interval`

```c
uint32_t dma_block_config::source_gather_interval
```

聚集边界（Gather Boundary）处的地址调整量。

<a id="a4f8f5b65002f65eaacdd3dde26c47170"></a>

### `source_reload_en`

```c
uint16_t dma_block_config::source_reload_en
```

块传输结束时重新装载源地址。

## 3.3\_源码定位与版本边界

接口、配置结构和内联包装均可在仓库的[dma.h](../../../include/zephyr/drivers/dma.h)中相对定位。本次译注核对了[官方main头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/dma.h)，摘要见[来源记录](../SOURCES.md)；本地源码、滚动更新的main与latest网页不能自动视为同一版本。原始头文件法律署名为Copyright (c) 2016 Intel Corporation，许可证为Apache-2.0。

> 译注——地址与块大小：source_address／dest_address在CONFIG_DMA_64BIT下为uint64_t，否则为uint32_t；此页保留网页的32位声明。block_size单位是字节，不是数据项数，也不等于source_data_size或突发长度。gather／scatter及FIFO选项的支持与具体取值应查目标驱动，不能仅凭公共字段存在推断硬件支持。

本批只翻译和核对官方源码，没有构建、执行DMA搬运、运行驱动测试或进行实板验证；这组参考也不声明本仓库已实现HC32 DMA驱动。

## 3.4\_原页交叉引用（Cross References）

- [zephyr/drivers/dma.h](P010_DMA驱动头文件源码.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [dma_block_config](P003_DMA传输块配置.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_DMA驱动后端接口.md) · [返回大纲](大纲.md) · [下一章](P004_DMA通道配置.md)
