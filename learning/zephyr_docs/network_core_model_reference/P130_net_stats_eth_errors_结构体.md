---
id: learning.zephyr-docs.network-core-model-reference.page-130
title: net_stats_eth_errors_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__eth__errors.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第130章\_net\_stats\_eth\_errors\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__stats__eth__errors.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网错误（Error）统计信息。

```c
#include <zephyr/net/net_stats.h>
```

<a id="details"></a>

以太网错误（Error）统计信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 130.1\_数据成员（Data Fields）

<a id="r_aca0e2e4807fa70279dee8ddaad2d7ef7"></a>

```c
net_stats_t rx_length_errors
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx_length_errors](#aca0e2e4807fa70279dee8ddaad2d7ef7)。

接收长度错误（RX length errors）数量。

<a id="r_a9afee89f5bb01907e7cd515e2a0ff1b5"></a>

```c
net_stats_t rx_over_errors
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx_over_errors](#a9afee89f5bb01907e7cd515e2a0ff1b5)。

接收溢出错误（RX overrun errors）数量。

<a id="r_a4dab70cf219269bb393ce14faf0ed77e"></a>

```c
net_stats_t rx_crc_errors
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx_crc_errors](#a4dab70cf219269bb393ce14faf0ed77e)。

接收循环冗余校验错误（RX CRC errors）数量。

<a id="r_a8dfcc5cd1b4decec5783d01ba7033b05"></a>

```c
net_stats_t rx_frame_errors
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx_frame_errors](#a8dfcc5cd1b4decec5783d01ba7033b05)。

接收帧错误（RX frame errors）数量。

<a id="r_a82622736d226b4d3b999f1f22ccf8529"></a>

```c
net_stats_t rx_no_buffer_count
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx_no_buffer_count](#a82622736d226b4d3b999f1f22ccf8529)。

接收时 `net_pkt` 分配错误数量（RX allocation errors）。

<a id="r_a2d2b2c4e3764ebec841f1ecbe7058d99"></a>

```c
net_stats_t rx_missed_errors
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx_missed_errors](#a2d2b2c4e3764ebec841f1ecbe7058d99)。

接收遗漏错误（RX missed errors）数量。

<a id="r_a0e83e270a35222ed3e927800be4159e7"></a>

```c
net_stats_t rx_long_length_errors
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx_long_length_errors](#a0e83e270a35222ed3e927800be4159e7)。

接收长度过长错误（RX long length errors）数量。

<a id="r_a5e3d39d8417bb180cbfcb8c901006e81"></a>

```c
net_stats_t rx_short_length_errors
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx_short_length_errors](#a5e3d39d8417bb180cbfcb8c901006e81)。

接收长度过短错误（RX short length errors）数量。

<a id="r_a7618f10af3443c49a6e256bb41e77781"></a>

```c
net_stats_t rx_align_errors
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx_align_errors](#a7618f10af3443c49a6e256bb41e77781)。

接收缓冲区对齐错误（RX buffer align errors）数量。

<a id="r_a7bcfbb13836f162ceeb5f021304b5c76"></a>

```c
net_stats_t rx_dma_failed
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx_dma_failed](#a7bcfbb13836f162ceeb5f021304b5c76)。

接收直接存储器访问失败错误（RX DMA failed errors）数量。

<a id="r_adbcae9c10c081f1cdf304bcdce740aa4"></a>

```c
net_stats_t rx_buf_alloc_failed
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[rx_buf_alloc_failed](#adbcae9c10c081f1cdf304bcdce740aa4)。

接收时 `net_buf` 分配错误数量（RX allocation errors）。

<a id="r_afec6a7e24c6f3cc74dd9f739f27b3e48"></a>

```c
net_stats_t tx_aborted_errors
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[tx_aborted_errors](#afec6a7e24c6f3cc74dd9f739f27b3e48)。

发送中止错误（TX aborted errors）数量。

<a id="r_a0043d1a1481040a6d7439bd23423ec12"></a>

```c
net_stats_t tx_carrier_errors
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[tx_carrier_errors](#a0043d1a1481040a6d7439bd23423ec12)。

发送载波错误（TX carrier errors）数量。

<a id="r_a84630da9b82557f56dc35cd59ca2f7ae"></a>

```c
net_stats_t tx_fifo_errors
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[tx_fifo_errors](#a84630da9b82557f56dc35cd59ca2f7ae)。

发送先进先出队列错误（TX FIFO errors）数量。

<a id="r_ae2a13733c1a5f0cc3e00efca0c3f429d"></a>

```c
net_stats_t tx_heartbeat_errors
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[tx_heartbeat_errors](#ae2a13733c1a5f0cc3e00efca0c3f429d)。

发送心跳错误（TX heartbeat errors）数量。

<a id="r_a17624a12d6473bdd78698076fed0d122"></a>

```c
net_stats_t tx_window_errors
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[tx_window_errors](#a17624a12d6473bdd78698076fed0d122)。

发送窗口错误（TX window errors）数量。

<a id="r_abfbf6478b7afdd5935d7c6948c9ef426"></a>

```c
net_stats_t tx_dma_failed
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[tx_dma_failed](#abfbf6478b7afdd5935d7c6948c9ef426)。

发送直接存储器访问失败错误（TX DMA failed errors）数量。

<a id="r_a07d0a435f2129556520c732571d28edf"></a>

```c
net_stats_t uncorr_ecc_errors
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[uncorr_ecc_errors](#a07d0a435f2129556520c732571d28edf)。

未纠正的纠错码错误（Uncorrected ECC errors）数量。

<a id="r_a257113639f0e0e3085febb7a147f498f"></a>

```c
net_stats_t corr_ecc_errors
```

相关声明：[net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)、[corr_ecc_errors](#a257113639f0e0e3085febb7a147f498f)。

已纠正的纠错码错误（Corrected ECC errors）数量。

## 130.2\_详细说明（Detailed Documentation）

<a id="a257113639f0e0e3085febb7a147f498f"></a>

### `corr_ecc_errors`

```c
net_stats_t net_stats_eth_errors::corr_ecc_errors
```

已纠正的纠错码错误（Corrected ECC errors）数量。

<a id="a7618f10af3443c49a6e256bb41e77781"></a>

### `rx_align_errors`

```c
net_stats_t net_stats_eth_errors::rx_align_errors
```

接收缓冲区对齐错误（RX buffer align errors）数量。

<a id="adbcae9c10c081f1cdf304bcdce740aa4"></a>

### `rx_buf_alloc_failed`

```c
net_stats_t net_stats_eth_errors::rx_buf_alloc_failed
```

接收时 `net_buf` 分配错误数量（RX allocation errors）。

<a id="a4dab70cf219269bb393ce14faf0ed77e"></a>

### `rx_crc_errors`

```c
net_stats_t net_stats_eth_errors::rx_crc_errors
```

接收循环冗余校验错误（RX CRC errors）数量。

<a id="a7bcfbb13836f162ceeb5f021304b5c76"></a>

### `rx_dma_failed`

```c
net_stats_t net_stats_eth_errors::rx_dma_failed
```

接收直接存储器访问失败错误（RX DMA failed errors）数量。

<a id="a8dfcc5cd1b4decec5783d01ba7033b05"></a>

### `rx_frame_errors`

```c
net_stats_t net_stats_eth_errors::rx_frame_errors
```

接收帧错误（RX frame errors）数量。

<a id="aca0e2e4807fa70279dee8ddaad2d7ef7"></a>

### `rx_length_errors`

```c
net_stats_t net_stats_eth_errors::rx_length_errors
```

接收长度错误（RX length errors）数量。

<a id="a0e83e270a35222ed3e927800be4159e7"></a>

### `rx_long_length_errors`

```c
net_stats_t net_stats_eth_errors::rx_long_length_errors
```

接收长度过长错误（RX long length errors）数量。

<a id="a2d2b2c4e3764ebec841f1ecbe7058d99"></a>

### `rx_missed_errors`

```c
net_stats_t net_stats_eth_errors::rx_missed_errors
```

接收遗漏错误（RX missed errors）数量。

<a id="a82622736d226b4d3b999f1f22ccf8529"></a>

### `rx_no_buffer_count`

```c
net_stats_t net_stats_eth_errors::rx_no_buffer_count
```

接收时 `net_pkt` 分配错误数量（RX allocation errors）。

<a id="a9afee89f5bb01907e7cd515e2a0ff1b5"></a>

### `rx_over_errors`

```c
net_stats_t net_stats_eth_errors::rx_over_errors
```

接收溢出错误（RX overrun errors）数量。

<a id="a5e3d39d8417bb180cbfcb8c901006e81"></a>

### `rx_short_length_errors`

```c
net_stats_t net_stats_eth_errors::rx_short_length_errors
```

接收长度过短错误（RX short length errors）数量。

<a id="afec6a7e24c6f3cc74dd9f739f27b3e48"></a>

### `tx_aborted_errors`

```c
net_stats_t net_stats_eth_errors::tx_aborted_errors
```

发送中止错误（TX aborted errors）数量。

<a id="a0043d1a1481040a6d7439bd23423ec12"></a>

### `tx_carrier_errors`

```c
net_stats_t net_stats_eth_errors::tx_carrier_errors
```

发送载波错误（TX carrier errors）数量。

<a id="abfbf6478b7afdd5935d7c6948c9ef426"></a>

### `tx_dma_failed`

```c
net_stats_t net_stats_eth_errors::tx_dma_failed
```

发送直接存储器访问失败错误（TX DMA failed errors）数量。

<a id="a84630da9b82557f56dc35cd59ca2f7ae"></a>

### `tx_fifo_errors`

```c
net_stats_t net_stats_eth_errors::tx_fifo_errors
```

发送先进先出队列错误（TX FIFO errors）数量。

<a id="ae2a13733c1a5f0cc3e00efca0c3f429d"></a>

### `tx_heartbeat_errors`

```c
net_stats_t net_stats_eth_errors::tx_heartbeat_errors
```

发送心跳错误（TX heartbeat errors）数量。

<a id="a17624a12d6473bdd78698076fed0d122"></a>

### `tx_window_errors`

```c
net_stats_t net_stats_eth_errors::tx_window_errors
```

发送窗口错误（TX window errors）数量。

<a id="a07d0a435f2129556520c732571d28edf"></a>

### `uncorr_ecc_errors`

```c
net_stats_t net_stats_eth_errors::uncorr_ecc_errors
```

未纠正的纠错码错误（Uncorrected ECC errors）数量。

本数据类型文档由以下文件生成：

- `zephyr/net/net_stats.h`

## 130.3\_原页交叉引用（Cross References）

- [zephyr/net/net_stats.h](https://docs.zephyrproject.org/latest/doxygen/html/net__stats_8h_source.html)
- [net_stats_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html#ga05ec15873e79256c287f21b6b6fcd752)
- [net_pkt](P114_net_pkt_结构体.md)
- [net_buf](P046_net_buf_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P129_net_stats_eth_csum_结构体.md) · [返回大纲](大纲.md) · [下一章](P131_net_stats_eth_flow_结构体.md)
