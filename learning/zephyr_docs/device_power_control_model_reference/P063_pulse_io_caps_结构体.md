---
id: learning.zephyr-docs.device-power-control-model-reference.page-63
title: pulse_io_caps_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpulse__io__caps.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_pulse\_io\_caps\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpulse__io__caps.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

每个实例的能力描述符（Capability Descriptor）。

```c
#include <zephyr/drivers/pulse_io.h>
```

<a id="details"></a>

实例级能力描述符（Per-instance capability descriptor），由 `pulse_io_get_capabilities` 返回。所有字段描述硬件实例，而非某个具体通道；通道级限制（如有）由后端文档说明。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 63.1\_数据成员（Data Fields）

<a id="r_af6dee58bfc47780ccc77092777080ce8"></a>

```c
size_t tx_min_chunk_symbols
```

相关声明：[tx_min_chunk_symbols](#af6dee58bfc47780ccc77092777080ce8)。

流式传输的最小分块大小，即硬件 FIFO 深度。

<a id="r_afc8e349e152b2a271b51a2810eab2586"></a>

```c
size_t tx_max_streaming
```

相关声明：[tx_max_streaming](#afc8e349e152b2a271b51a2810eab2586)。

单次流式发送的最大大小；不受限制时为 `SIZE_MAX`。

<a id="r_acb4396add794dda4933f9c176d1766be"></a>

```c
uint32_t modes
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[modes](#acb4396add794dda4933f9c176d1766be)。

支持的 `pulse_io_mode` 位掩码。

<a id="r_aad176fbf3bf21edc3b45a89be128002d"></a>

```c
uint32_t min_tick_ns
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[min_tick_ns](#aad176fbf3bf21edc3b45a89be128002d)。

硬件可以产生的最细时间节拍，单位为纳秒。

<a id="r_a6300be8f6722fd166d33849df9c031aa"></a>

```c
uint32_t max_tick_ns
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_tick_ns](#a6300be8f6722fd166d33849df9c031aa)。

采用最大预分频值时的最粗时间节拍，单位为纳秒。

<a id="r_a4da263bc4a355448249400ad364f87b9"></a>

```c
uint32_t max_duration_ticks
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_duration_ticks](#a4da263bc4a355448249400ad364f87b9)。

每个符号的最大持续时间，以节拍计。

<a id="r_a3b0e9052d24dbc55e53b2f0d9ceda0cf"></a>

```c
uint32_t tx_loop_max
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tx_loop_max](#a3b0e9052d24dbc55e53b2f0d9ceda0cf)。

发送（TX）的最大循环次数。

<a id="r_a92a922e8a11823ad0ba733a2ee88cf0d"></a>

```c
uint32_t rx_idle_threshold_max
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rx_idle_threshold_max](#a92a922e8a11823ad0ba733a2ee88cf0d)。

帧结束空闲阈值（End-of-frame idle threshold）的最大值，以节拍计。

<a id="r_a986f4a6419df94ce618b0d05ee876276"></a>

```c
uint32_t rx_filter_max_ticks
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rx_filter_max_ticks](#a986f4a6419df94ce618b0d05ee876276)。

毛刺滤波器（Glitch filter）的最大宽度，以节拍计；无滤波器时为 `0`。

<a id="r_a219331ae467da4a2583d4d905bbac05b"></a>

```c
uint32_t tx_channel_mask
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tx_channel_mask](#a219331ae467da4a2583d4d905bbac05b)。

可用于发送的通道位掩码，位 N 对应通道 N。

<a id="r_aa91e3a0fe7e1fd95c89a2436558467eb"></a>

```c
uint32_t rx_channel_mask
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rx_channel_mask](#aa91e3a0fe7e1fd95c89a2436558467eb)。

可用于接收的通道位掩码，位 N 对应通道 N。

<a id="r_a173fa1c857ed24a2ecb5f9de8527136b"></a>

```c
uint8_t cell_duty_bits
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cell_duty_bits](#a173fa1c857ed24a2ecb5f9de8527136b)。

单元（CELL）模式中 `duty` 字段的位宽；仅支持电平的单元为 `0`。

<a id="r_a16fa91b3ccba69c11ebc826eeb29245d"></a>

```c
uint8_t num_channels
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_channels](#a16fa91b3ccba69c11ebc826eeb29245d)。

此实例上的独立通道总数。

<a id="r_ad85c4a8652bbf80da429c87bbcb680c6"></a>

```c
bool supports_tx
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[supports_tx](#ad85c4a8652bbf80da429c87bbcb680c6)。

是否支持发送。

<a id="r_a1de73e3e72e07bc99d09808402d17b61"></a>

```c
bool supports_rx
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[supports_rx](#a1de73e3e72e07bc99d09808402d17b61)。

是否支持接收。

<a id="r_aead2efb6f8fe2955d2d9b188cd9264eb"></a>

```c
bool tx_carrier
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[tx_carrier](#aead2efb6f8fe2955d2d9b188cd9264eb)。

发送时的硬件载波调制（Carrier modulation）。

<a id="r_a2ee6e5254c8f3bf474c9c49745d8c377"></a>

```c
bool tx_loop_auto_stop
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[tx_loop_auto_stop](#a2ee6e5254c8f3bf474c9c49745d8c377)。

硬件在循环结束时自动停止。

<a id="r_ab8b1aa9fea93cd697bcc760214f12760"></a>

```c
bool tx_sync_multi_channel
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[tx_sync_multi_channel](#ab8b1aa9fea93cd697bcc760214f12760)。

多个通道可以在同一时钟边沿启动。

<a id="r_adfa8d33306657b2870d3b5df8a4dce04"></a>

```c
bool rx_carrier_demod
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[rx_carrier_demod](#adfa8d33306657b2870d3b5df8a4dce04)。

接收时的硬件载波解调（Carrier demodulation）。

<a id="r_a2084a3bd36ed5c131d898edfbcdfba0a"></a>

```c
bool rx_dma_buffered
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[rx_dma_buffered](#a2084a3bd36ed5c131d898edfbcdfba0a)。

接收使用 DMA 支持的环形缓冲区（Ring buffer）；另一种方式是：

<a id="r_a5da774fe623fd1f35cbf2e54671399d6"></a>

```c
bool rx_streaming
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[rx_streaming](#a5da774fe623fd1f35cbf2e54671399d6)。

接收支持跨越单个缓冲区容量的乒乓式流传输（Ping-pong streaming）。

<a id="r_a64cf12b881eab0f538536c34d3273c14"></a>

```c
bool cell_period_per_chunk
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[cell_period_per_chunk](#a64cf12b881eab0f538536c34d3273c14)。

在 CELL 模式下，两次提交之间可以更改周期。

## 63.2\_详细说明（Detailed Documentation）

<a id="a173fa1c857ed24a2ecb5f9de8527136b"></a>

### `cell_duty_bits`

```c
uint8_t pulse_io_caps::cell_duty_bits
```

单元（CELL）模式中 `duty` 字段的位宽；仅支持电平的单元为 `0`。

<a id="a64cf12b881eab0f538536c34d3273c14"></a>

### `cell_period_per_chunk`

```c
bool pulse_io_caps::cell_period_per_chunk
```

在 CELL 模式下，两次提交之间可以更改周期。

<a id="a4da263bc4a355448249400ad364f87b9"></a>

### `max_duration_ticks`

```c
uint32_t pulse_io_caps::max_duration_ticks
```

每个符号的最大持续时间，以节拍计。

<a id="a6300be8f6722fd166d33849df9c031aa"></a>

### `max_tick_ns`

```c
uint32_t pulse_io_caps::max_tick_ns
```

采用最大预分频值时的最粗时间节拍，单位为纳秒。

<a id="aad176fbf3bf21edc3b45a89be128002d"></a>

### `min_tick_ns`

```c
uint32_t pulse_io_caps::min_tick_ns
```

硬件可以产生的最细时间节拍，单位为纳秒。

<a id="acb4396add794dda4933f9c176d1766be"></a>

### `modes`

```c
uint32_t pulse_io_caps::modes
```

支持的 `pulse_io_mode` 位掩码。

<a id="a16fa91b3ccba69c11ebc826eeb29245d"></a>

### `num_channels`

```c
uint8_t pulse_io_caps::num_channels
```

此实例上的独立通道总数。

<a id="adfa8d33306657b2870d3b5df8a4dce04"></a>

### `rx_carrier_demod`

```c
bool pulse_io_caps::rx_carrier_demod
```

接收时的硬件载波解调（Carrier demodulation）。

<a id="aa91e3a0fe7e1fd95c89a2436558467eb"></a>

### `rx_channel_mask`

```c
uint32_t pulse_io_caps::rx_channel_mask
```

可用于接收的通道位掩码，位 N 对应通道 N。

<a id="a2084a3bd36ed5c131d898edfbcdfba0a"></a>

### `rx_dma_buffered`

```c
bool pulse_io_caps::rx_dma_buffered
```

接收使用 DMA 支持的环形缓冲区（Ring buffer）；另一种方式是：

通过中断取出数据。

<a id="a986f4a6419df94ce618b0d05ee876276"></a>

### `rx_filter_max_ticks`

```c
uint32_t pulse_io_caps::rx_filter_max_ticks
```

毛刺滤波器（Glitch filter）的最大宽度，以节拍计；无滤波器时为 `0`。

<a id="a92a922e8a11823ad0ba733a2ee88cf0d"></a>

### `rx_idle_threshold_max`

```c
uint32_t pulse_io_caps::rx_idle_threshold_max
```

帧结束空闲阈值（End-of-frame idle threshold）的最大值，以节拍计。

<a id="a5da774fe623fd1f35cbf2e54671399d6"></a>

### `rx_streaming`

```c
bool pulse_io_caps::rx_streaming
```

接收支持跨越单个缓冲区容量的乒乓式流传输（Ping-pong streaming）。

<a id="a1de73e3e72e07bc99d09808402d17b61"></a>

### `supports_rx`

```c
bool pulse_io_caps::supports_rx
```

是否支持接收。

<a id="ad85c4a8652bbf80da429c87bbcb680c6"></a>

### `supports_tx`

```c
bool pulse_io_caps::supports_tx
```

是否支持发送。

<a id="aead2efb6f8fe2955d2d9b188cd9264eb"></a>

### `tx_carrier`

```c
bool pulse_io_caps::tx_carrier
```

发送时的硬件载波调制（Carrier modulation）。

<a id="a219331ae467da4a2583d4d905bbac05b"></a>

### `tx_channel_mask`

```c
uint32_t pulse_io_caps::tx_channel_mask
```

可用于发送的通道位掩码，位 N 对应通道 N。

具有专用发送和接收通道的硬件会报告互不重叠的掩码；完全对称的硬件则将两个掩码都设置为覆盖所有通道。

<a id="a2ee6e5254c8f3bf474c9c49745d8c377"></a>

### `tx_loop_auto_stop`

```c
bool pulse_io_caps::tx_loop_auto_stop
```

硬件在循环结束时自动停止。

<a id="a3b0e9052d24dbc55e53b2f0d9ceda0cf"></a>

### `tx_loop_max`

```c
uint32_t pulse_io_caps::tx_loop_max
```

发送（TX）的最大循环次数。

`0`：不支持循环；`1`：仅支持无限循环；`N`（大于 1）：支持最多 N 次有限循环，以及无限循环。

<a id="afc8e349e152b2a271b51a2810eab2586"></a>

### `tx_max_streaming`

```c
size_t pulse_io_caps::tx_max_streaming
```

单次流式发送的最大大小；不受限制时为 `SIZE_MAX`。

<a id="af6dee58bfc47780ccc77092777080ce8"></a>

### `tx_min_chunk_symbols`

```c
size_t pulse_io_caps::tx_min_chunk_symbols
```

流式传输的最小分块大小，即硬件 FIFO 深度。

<a id="ab8b1aa9fea93cd697bcc760214f12760"></a>

### `tx_sync_multi_channel`

```c
bool pulse_io_caps::tx_sync_multi_channel
```

多个通道可以在同一时钟边沿启动。

本数据类型文档由以下文件生成：

- `zephyr/drivers/pulse_io.h`

## 63.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pulse_io.h](https://docs.zephyrproject.org/latest/doxygen/html/pulse__io_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pulse_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga8a69608ee00587642aca6e0d69878b07)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [pulse_io_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga3d92ae937058d0675dd56b009aa1138f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P062_pulse_io_bit_template_结构体.md) · [返回大纲](大纲.md) · [下一章](P064_pulse_io_config_结构体.md)
