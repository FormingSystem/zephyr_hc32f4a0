---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-98
title: bt_mesh_sar_tx_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__sar__tx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第98章\_bt\_mesh\_sar\_tx\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__sar__tx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

分段与重组发送器配置（SAR Transmitter Configuration）的状态结构。

```c
#include <zephyr/bluetooth/mesh/sar_cfg.h>
```

<a id="details"></a>

分段与重组发送器配置（SAR Transmitter Configuration）的状态结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 98.1\_数据成员（Data Fields）

<a id="r_aa491eda390c1b9532e968ed566ec23c2"></a>

```c
uint8_t seg_int_step
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[seg_int_step](#aa491eda390c1b9532e968ed566ec23c2)。

分段与重组的分段间隔步长状态（SAR Segment Interval Step state）。

<a id="r_adaa856b561ac24c07706a04eea157183"></a>

```c
uint8_t unicast_retrans_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[unicast_retrans_count](#adaa856b561ac24c07706a04eea157183)。

分段与重组的单播重传次数状态（SAR Unicast Retransmissions Count state）。

<a id="r_a1893bbeb473ebcf99db633e7f979b376"></a>

```c
uint8_t unicast_retrans_without_prog_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[unicast_retrans_without_prog_count](#a1893bbeb473ebcf99db633e7f979b376)。

分段与重组的无进展单播重传次数状态（SAR Unicast Retransmissions Without Progress Count state）。

<a id="r_a8e0ad5b5977bd4aad20bd79977a0342d"></a>

```c
uint8_t unicast_retrans_int_step
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[unicast_retrans_int_step](#a8e0ad5b5977bd4aad20bd79977a0342d)。

<a id="r_a40a96d401f44345397bd605d6f25e04a"></a>

```c
uint8_t unicast_retrans_int_inc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[unicast_retrans_int_inc](#a40a96d401f44345397bd605d6f25e04a)。

分段与重组的单播重传间隔增量状态（SAR Unicast Retransmissions Interval Increment state）。

<a id="r_a686a6a4a7e6a7c6a532ddb8c8bad76df"></a>

```c
uint8_t multicast_retrans_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[multicast_retrans_count](#a686a6a4a7e6a7c6a532ddb8c8bad76df)。

分段与重组的多播重传次数状态（SAR Multicast Retransmissions Count state）。

<a id="r_a6fec529b66c04f0828f5d5d716fd9281"></a>

```c
uint8_t multicast_retrans_int
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[multicast_retrans_int](#a6fec529b66c04f0828f5d5d716fd9281)。

分段与重组的多播重传间隔状态（SAR Multicast Retransmissions Interval state）。

## 98.2\_详细说明（Detailed Documentation）

<a id="a686a6a4a7e6a7c6a532ddb8c8bad76df"></a>

### `multicast_retrans_count`

```c
uint8_t bt_mesh_sar_tx::multicast_retrans_count
```

分段与重组的多播重传次数状态（SAR Multicast Retransmissions Count state）。

<a id="a6fec529b66c04f0828f5d5d716fd9281"></a>

### `multicast_retrans_int`

```c
uint8_t bt_mesh_sar_tx::multicast_retrans_int
```

分段与重组的多播重传间隔状态（SAR Multicast Retransmissions Interval state）。

<a id="aa491eda390c1b9532e968ed566ec23c2"></a>

### `seg_int_step`

```c
uint8_t bt_mesh_sar_tx::seg_int_step
```

分段与重组的分段间隔步长状态（SAR Segment Interval Step state）。

<a id="adaa856b561ac24c07706a04eea157183"></a>

### `unicast_retrans_count`

```c
uint8_t bt_mesh_sar_tx::unicast_retrans_count
```

分段与重组的单播重传次数状态（SAR Unicast Retransmissions Count state）。

<a id="a40a96d401f44345397bd605d6f25e04a"></a>

### `unicast_retrans_int_inc`

```c
uint8_t bt_mesh_sar_tx::unicast_retrans_int_inc
```

分段与重组的单播重传间隔增量状态（SAR Unicast Retransmissions Interval Increment state）。

<a id="a8e0ad5b5977bd4aad20bd79977a0342d"></a>

### `unicast_retrans_int_step`

```c
uint8_t bt_mesh_sar_tx::unicast_retrans_int_step
```

<a id="a1893bbeb473ebcf99db633e7f979b376"></a>

### `unicast_retrans_without_prog_count`

```c
uint8_t bt_mesh_sar_tx::unicast_retrans_without_prog_count
```

分段与重组的无进展单播重传次数状态（SAR Unicast Retransmissions Without Progress Count state）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/sar_cfg.h`

## 98.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/sar_cfg.h](https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P097_bt_mesh_sar_rx_结构体.md) · [返回大纲](大纲.md) · [下一章](P099_bt_mesh_send_cb_结构体.md)
