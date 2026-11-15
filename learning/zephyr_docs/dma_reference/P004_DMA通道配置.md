---
id: learning.zephyr-docs.dma-reference.page-4
title: DMA通道配置
kind: reference
status: maintained
domains: [zephyr, dma, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdma__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_DMA通道配置

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdma__config.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是直接内存访问（Direct Memory Access，DMA）应用程序接口（Application Programming Interface，API）参考。先读[DMA概述](../hardware/P011_DMA直接内存访问.md)，再按[本册大纲](大纲.md)区分通道配置（Channel Configuration）、传输块（Transfer Block）、运行状态（Runtime Status）与驱动后端（Driver Backend）。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

DMA配置结构（Configuration）。

```c
#include <zephyr/drivers/dma.h>
```

<a id="details"></a>

DMA配置结构（Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_a8e6c5cab5ec030066a3e57e0507fbf9f"></a>

```c
uint32_t dma_slot: 8
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dma_slot](#a8e6c5cab5ec030066a3e57e0507fbf9f)。

选择外设及方向，具体含义取决于硬件。

<a id="r_aaf903b1badff8b0fc4ef18a34c2773d7"></a>

```c
uint32_t channel_direction: 3
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[channel_direction](#aaf903b1badff8b0fc4ef18a34c2773d7)。

传输进行的方向。

<a id="r_a0e2da7a8f4439ceb3f2acf02e4681396"></a>

```c
uint32_t half_complete_callback_en: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[half_complete_callback_en](#a0e2da7a8f4439ceb3f2acf02e4681396)。

置1时启用半完成回调（Half Completion Callback）。

<a id="r_a39526177f03017d245651b4f51820161"></a>

```c
uint32_t complete_callback_en: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[complete_callback_en](#a39526177f03017d245651b4f51820161)。

完成回调使能（Completion Callback Enable）。

<a id="r_a416a0ef20318fe77d7e383caeee67e94"></a>

```c
uint32_t error_callback_dis: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[error_callback_dis](#a416a0ef20318fe77d7e383caeee67e94)。

错误回调禁用（Error Callback Disable）。

<a id="r_a2927e31730c6ca2f5ac8db38c255d9f7"></a>

```c
uint32_t source_handshake: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[source_handshake](#a2927e31730c6ca2f5ac8db38c255d9f7)。

源握手方式（Source Handshake），具体含义取决于硬件。

<a id="r_af570b4050200ec510df323bd31558233"></a>

```c
uint32_t dest_handshake: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dest_handshake](#af570b4050200ec510df323bd31558233)。

目标握手方式（Destination Handshake），具体含义取决于硬件。

<a id="r_a284d96c59945aaa851d235802aee979a"></a>

```c
uint32_t channel_priority: 4
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[channel_priority](#a284d96c59945aaa851d235802aee979a)。

用于仲裁（Arbitration）的通道优先级，具体含义取决于硬件。

<a id="r_a7c77afc1f546efda6ce22f50560b8840"></a>

```c
uint32_t source_chaining_en: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[source_chaining_en](#a7c77afc1f546efda6ce22f50560b8840)。

源链接使能（Source Chaining Enable），具体含义取决于硬件。

<a id="r_a8a304fdada9ec7fc87402449e1410486"></a>

```c
uint32_t dest_chaining_en: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dest_chaining_en](#a8a304fdada9ec7fc87402449e1410486)。

目标链接使能（Destination Chaining Enable），具体含义取决于硬件。

<a id="r_ace2dc918fcfea264a579b1084fcb7fe5"></a>

```c
uint32_t linked_channel: 7
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[linked_channel](#ace2dc918fcfea264a579b1084fcb7fe5)。

关联通道（Linked Channel），具体含义取决于硬件。

<a id="r_afa70dbf1ee7bb5fb6a771f634783b7a2"></a>

```c
uint32_t cyclic: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cyclic](#afa70dbf1ee7bb5fb6a771f634783b7a2)。

循环传输列表（Cyclic Transfer List），具体含义取决于硬件。

<a id="r_ac9144783b4843182451b440d97ecd273"></a>

```c
uint32_t source_data_size: 16
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[source_data_size](#ac9144783b4843182451b440d97ecd273)。

源数据宽度，单位为字节。

<a id="r_adfa9efbfbef3ed41b2f8dd5b9c441e08"></a>

```c
uint32_t dest_data_size: 16
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dest_data_size](#adfa9efbfbef3ed41b2f8dd5b9c441e08)。

目标数据宽度，单位为字节。

<a id="r_ad750b724bab1503ded7c163d8228aa80"></a>

```c
uint32_t source_burst_length: 16
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[source_burst_length](#ad750b724bab1503ded7c163d8228aa80)。

源突发传输长度，单位为字节。

<a id="r_aca47b00f817e55bf662fdd6767a59ed0"></a>

```c
uint32_t dest_burst_length: 16
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dest_burst_length](#aca47b00f817e55bf662fdd6767a59ed0)。

目标突发传输长度，单位为字节。

<a id="r_adb776a4940c71b61cab60eb05159b2d4"></a>

```c
uint32_t block_count
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[block_count](#adb776a4940c71b61cab60eb05159b2d4)。

传输列表中的块数。

<a id="r_aca6a1cb9b580a61bf91490fecf10cb16"></a>

```c
struct dma_block_config * head_block
```

相关声明：[dma_block_config](P003_DMA传输块配置.md)、[head_block](#aca6a1cb9b580a61bf91490fecf10cb16)。

指向传输列表中的第一个块。

<a id="r_a510eed1cadbf411c9e94e1d1fb43d39d"></a>

```c
void * user_data
```

相关声明：[user_data](#a510eed1cadbf411c9e94e1d1fb43d39d)。

可选的回调附加用户数据。

<a id="r_a69110abc43227bd7df217c4e25bb964b"></a>

```c
dma_callback_t dma_callback
```

相关声明：[dma_callback_t](P001_DMA公共接口.md#ga94745b4472ee1addd4f82db4e59e9fb5)、[dma_callback](#a69110abc43227bd7df217c4e25bb964b)。

可选的完成及错误事件回调。

## 4.2\_详细说明（Detailed Documentation）

<a id="adb776a4940c71b61cab60eb05159b2d4"></a>

### `block_count`

```c
uint32_t dma_config::block_count
```

传输列表中的块数。

<a id="aaf903b1badff8b0fc4ef18a34c2773d7"></a>

### `channel_direction`

```c
uint32_t dma_config::channel_direction
```

传输进行的方向。

- 0b000：内存到内存（Memory to Memory）。
- 0b001：内存到外设（Memory to Peripheral）。
- 0b010：外设到内存（Peripheral to Memory）。
- 0b011：外设到外设（Peripheral to Peripheral）。
- 0b100：主机到内存（Host to Memory）。
- 0b101：内存到主机（Memory to Host）。
- 其他值由硬件专门定义。

<a id="a284d96c59945aaa851d235802aee979a"></a>

### `channel_priority`

```c
uint32_t dma_config::channel_priority
```

用于仲裁（Arbitration）的通道优先级，具体含义取决于硬件。

<a id="a39526177f03017d245651b4f51820161"></a>

### `complete_callback_en`

```c
uint32_t dma_config::complete_callback_en
```

完成回调使能（Completion Callback Enable）。

- 0b0：仅在整个传输列表完成时调用回调。
- 0b1：每个传输块完成时调用回调。

> 译注——源码核对：置0不是完全关闭完成回调，而是仅在整个传输列表完成时调用；置1表示每块完成时调用。是否具备该能力仍由驱动和硬件决定。

<a id="afa70dbf1ee7bb5fb6a771f634783b7a2"></a>

### `cyclic`

```c
uint32_t dma_config::cyclic
```

循环传输列表（Cyclic Transfer List），具体含义取决于硬件。

<a id="aca47b00f817e55bf662fdd6767a59ed0"></a>

### `dest_burst_length`

```c
uint32_t dma_config::dest_burst_length
```

目标突发传输长度，单位为字节。

<a id="a8a304fdada9ec7fc87402449e1410486"></a>

### `dest_chaining_en`

```c
uint32_t dma_config::dest_chaining_en
```

目标链接使能（Destination Chaining Enable），具体含义取决于硬件。

<a id="adfa9efbfbef3ed41b2f8dd5b9c441e08"></a>

### `dest_data_size`

```c
uint32_t dma_config::dest_data_size
```

目标数据宽度，单位为字节。

<a id="af570b4050200ec510df323bd31558233"></a>

### `dest_handshake`

```c
uint32_t dma_config::dest_handshake
```

目标握手方式（Destination Handshake），具体含义取决于硬件。

- 0b0：硬件握手（Hardware，HW）。
- 0b1：软件握手（Software，SW）。

<a id="a69110abc43227bd7df217c4e25bb964b"></a>

### `dma_callback`

```c
dma_callback_t dma_config::dma_callback
```

可选的完成及错误事件回调。

<a id="a8e6c5cab5ec030066a3e57e0507fbf9f"></a>

### `dma_slot`

```c
uint32_t dma_config::dma_slot
```

选择外设及方向，具体含义取决于硬件。

<a id="a416a0ef20318fe77d7e383caeee67e94"></a>

### `error_callback_dis`

```c
uint32_t dma_config::error_callback_dis
```

错误回调禁用（Error Callback Disable）。

- 0b0：启用错误回调。
- 0b1：禁用错误回调。

<a id="a0e2da7a8f4439ceb3f2acf02e4681396"></a>

### `half_complete_callback_en`

```c
uint32_t dma_config::half_complete_callback_en
```

置1时启用半完成回调（Half Completion Callback）。

<a id="aca6a1cb9b580a61bf91490fecf10cb16"></a>

### `head_block`

```c
struct dma_block_config* dma_config::head_block
```

指向传输列表中的第一个块。

<a id="ace2dc918fcfea264a579b1084fcb7fe5"></a>

### `linked_channel`

```c
uint32_t dma_config::linked_channel
```

关联通道（Linked Channel），具体含义取决于硬件。

<a id="ad750b724bab1503ded7c163d8228aa80"></a>

### `source_burst_length`

```c
uint32_t dma_config::source_burst_length
```

源突发传输长度，单位为字节。

<a id="a7c77afc1f546efda6ce22f50560b8840"></a>

### `source_chaining_en`

```c
uint32_t dma_config::source_chaining_en
```

源链接使能（Source Chaining Enable），具体含义取决于硬件。

<a id="ac9144783b4843182451b440d97ecd273"></a>

### `source_data_size`

```c
uint32_t dma_config::source_data_size
```

源数据宽度，单位为字节。

<a id="a2927e31730c6ca2f5ac8db38c255d9f7"></a>

### `source_handshake`

```c
uint32_t dma_config::source_handshake
```

源握手方式（Source Handshake），具体含义取决于硬件。

- 0b0：硬件握手（Hardware，HW）。
- 0b1：软件握手（Software，SW）。

<a id="a510eed1cadbf411c9e94e1d1fb43d39d"></a>

### `user_data`

```c
void* dma_config::user_data
```

可选的回调附加用户数据。

## 4.3\_源码定位与版本边界

接口、配置结构和内联包装均可在仓库的[dma.h](../../../include/zephyr/drivers/dma.h)中相对定位。本次译注核对了[官方main头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/dma.h)，摘要见[来源记录](../SOURCES.md)；本地源码、滚动更新的main与latest网页不能自动视为同一版本。原始头文件法律署名为Copyright (c) 2016 Intel Corporation，许可证为Apache-2.0。

> 译注——三个数量：source_data_size／dest_data_size是单项数据宽度，source_burst_length／dest_burst_length是突发长度，两者均以字节计；block_count是块数，head_block指向块链表首项。配置操作只转发给驱动，不承诺立即复制并接管全部描述符；数据和配置的有效期应遵循具体驱动要求。

本批只翻译和核对官方源码，没有构建、执行DMA搬运、运行驱动测试或进行实板验证；这组参考也不声明本仓库已实现HC32 DMA驱动。

## 4.4\_原页交叉引用（Cross References）

- [zephyr/drivers/dma.h](P010_DMA驱动头文件源码.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [dma_block_config](P003_DMA传输块配置.md)
- [dma_callback_t](P001_DMA公共接口.md#ga94745b4472ee1addd4f82db4e59e9fb5)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_DMA传输块配置.md) · [返回大纲](大纲.md) · [下一章](P005_DMA运行状态.md)
