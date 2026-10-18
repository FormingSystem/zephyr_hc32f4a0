---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-97
title: bt_mesh_sar_rx_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__sar__rx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第97章\_bt\_mesh\_sar\_rx\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__sar__rx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

分段与重组接收器配置（SAR Receiver Configuration）的状态结构。

```c
#include <zephyr/bluetooth/mesh/sar_cfg.h>
```

<a id="details"></a>

分段与重组接收器配置（SAR Receiver Configuration）的状态结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 97.1\_数据成员（Data Fields）

<a id="r_a32a790589ddebee397d536b18518558d"></a>

```c
uint8_t seg_thresh
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[seg_thresh](#a32a790589ddebee397d536b18518558d)。

分段与重组的分段阈值状态（SAR Segments Threshold state）。

<a id="r_a5517a0f2167340cf59ef6fc72077f010"></a>

```c
uint8_t ack_delay_inc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ack_delay_inc](#a5517a0f2167340cf59ef6fc72077f010)。

分段与重组的确认延迟增量状态（SAR Acknowledgment Delay Increment state）。

<a id="r_a70615d8df27b6f8291291b73abc57c9c"></a>

```c
uint8_t discard_timeout
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[discard_timeout](#a70615d8df27b6f8291291b73abc57c9c)。

分段与重组的丢弃超时状态（SAR Discard Timeout state）。

<a id="r_ad277cc6c5d221aab7fd22581bfccd83c"></a>

```c
uint8_t rx_seg_int_step
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_seg_int_step](#ad277cc6c5d221aab7fd22581bfccd83c)。

分段与重组的接收方分段间隔步长状态（SAR Receiver Segment Interval Step state）。

<a id="r_aac228432bddf7f112ccbcb9e3d05d2ce"></a>

```c
uint8_t ack_retrans_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ack_retrans_count](#aac228432bddf7f112ccbcb9e3d05d2ce)。

分段与重组的确认重传次数状态（SAR Acknowledgment Retransmissions Count state）。

## 97.2\_详细说明（Detailed Documentation）

<a id="a5517a0f2167340cf59ef6fc72077f010"></a>

### `ack_delay_inc`

```c
uint8_t bt_mesh_sar_rx::ack_delay_inc
```

分段与重组的确认延迟增量状态（SAR Acknowledgment Delay Increment state）。

<a id="aac228432bddf7f112ccbcb9e3d05d2ce"></a>

### `ack_retrans_count`

```c
uint8_t bt_mesh_sar_rx::ack_retrans_count
```

分段与重组的确认重传次数状态（SAR Acknowledgment Retransmissions Count state）。

<a id="a70615d8df27b6f8291291b73abc57c9c"></a>

### `discard_timeout`

```c
uint8_t bt_mesh_sar_rx::discard_timeout
```

分段与重组的丢弃超时状态（SAR Discard Timeout state）。

<a id="ad277cc6c5d221aab7fd22581bfccd83c"></a>

### `rx_seg_int_step`

```c
uint8_t bt_mesh_sar_rx::rx_seg_int_step
```

分段与重组的接收方分段间隔步长状态（SAR Receiver Segment Interval Step state）。

<a id="a32a790589ddebee397d536b18518558d"></a>

### `seg_thresh`

```c
uint8_t bt_mesh_sar_rx::seg_thresh
```

分段与重组的分段阈值状态（SAR Segments Threshold state）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/sar_cfg.h`

## 97.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/sar_cfg.h](https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P096_bt_mesh_sar_cfg_cli_结构体.md) · [返回大纲](大纲.md) · [下一章](P098_bt_mesh_sar_tx_结构体.md)
