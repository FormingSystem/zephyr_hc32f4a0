---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-11
title: bt_conn_le_conn_rate_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__conn__rate__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_bt\_conn\_le\_conn\_rate\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__conn__rate__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

低功耗（LE）连接的连接速率参数。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

低功耗（LE）连接的连接速率参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_a264baeb210c9cbd559f0cd3ed2cd78b1"></a>

```c
uint16_t interval_min_125us
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval_min_125us](#a264baeb210c9cbd559f0cd3ed2cd78b1)。

最小连接间隔（Minimum connection interval）。

<a id="r_a9afcc899991204f17c1390b9362ec54b"></a>

```c
uint16_t interval_max_125us
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval_max_125us](#a9afcc899991204f17c1390b9362ec54b)。

最大连接间隔（Maximum connection interval）。

<a id="r_aed9238960e4be8ddbeff53afab74ef6f"></a>

```c
uint16_t subrate_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subrate_min](#aed9238960e4be8ddbeff53afab74ef6f)。

最小子速率因子（Minimum subrate factor）。

<a id="r_a751042149cb8ff1ec28de10fe1e4c8bd"></a>

```c
uint16_t subrate_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subrate_max](#a751042149cb8ff1ec28de10fe1e4c8bd)。

最大子速率因子（Maximum subrate factor）。

<a id="r_afb3fa1a4202c39a9551dd41396595771"></a>

```c
uint16_t max_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_latency](#afb3fa1a4202c39a9551dd41396595771)。

最大外设延迟（Maximum Peripheral latency）。

<a id="r_adf4c1069b5aa3b8afb09ea8b59d93eca"></a>

```c
uint16_t continuation_number
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[continuation_number](#adf4c1069b5aa3b8afb09ea8b59d93eca)。

发送或接收到包含长度字段（Length field）非零的链路层协议数据单元（Link Layer PDU）的数据包后，继续保持活动状态的底层连接事件最小数量（Underlying connection events）。

<a id="r_a50a3c9eca10ed5c11773aaf07e1fbc12"></a>

```c
uint16_t supervision_timeout_10ms
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[supervision_timeout_10ms](#a50a3c9eca10ed5c11773aaf07e1fbc12)。

连接监督超时（Connection Supervision timeout）。

<a id="r_ae4734b6d8f0f4903624e47e975828482"></a>

```c
uint16_t min_ce_len_125us
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_ce_len_125us](#ae4734b6d8f0f4903624e47e975828482)。

连接事件的最短持续时间（Minimum connection event length）。

<a id="r_aa764837e74aac1feba2025cf01a87d85"></a>

```c
uint16_t max_ce_len_125us
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_ce_len_125us](#aa764837e74aac1feba2025cf01a87d85)。

连接事件的最长持续时间（Maximum connection event length）。

## 11.2\_详细说明（Detailed Documentation）

<a id="adf4c1069b5aa3b8afb09ea8b59d93eca"></a>

### `continuation_number`

```c
uint16_t bt_conn_le_conn_rate_param::continuation_number
```

发送或接收到包含长度字段（Length field）非零的链路层协议数据单元（Link Layer PDU）的数据包后，继续保持活动状态的底层连接事件最小数量（Underlying connection events）。

范围（Range）：`BT_HCI_LE_CONTINUATION_NUM_MIN`–`BT_HCI_LE_CONTINUATION_NUM_MAX`。

<a id="a9afcc899991204f17c1390b9362ec54b"></a>

### `interval_max_125us`

```c
uint16_t bt_conn_le_conn_rate_param::interval_max_125us
```

最大连接间隔（Maximum connection interval）。

单位（Unit）：125 微秒（Microseconds）。

范围（Range）：`BT_HCI_LE_SCI_INTERVAL_MIN_125US`–`BT_HCI_LE_SCI_INTERVAL_MAX_125US`。

<a id="a264baeb210c9cbd559f0cd3ed2cd78b1"></a>

### `interval_min_125us`

```c
uint16_t bt_conn_le_conn_rate_param::interval_min_125us
```

最小连接间隔（Minimum connection interval）。

单位（Unit）：125 微秒（Microseconds）。

范围（Range）：`BT_HCI_LE_SCI_INTERVAL_MIN_125US`–`BT_HCI_LE_SCI_INTERVAL_MAX_125US`。

<a id="aa764837e74aac1feba2025cf01a87d85"></a>

### `max_ce_len_125us`

```c
uint16_t bt_conn_le_conn_rate_param::max_ce_len_125us
```

连接事件的最长持续时间（Maximum connection event length）。

单位（Unit）：125 微秒（Microseconds）。

范围（Range）：`BT_HCI_LE_SCI_CE_LEN_MIN_125US`–`BT_HCI_LE_SCI_CE_LEN_MAX_125US`。

<a id="afb3fa1a4202c39a9551dd41396595771"></a>

### `max_latency`

```c
uint16_t bt_conn_le_conn_rate_param::max_latency
```

最大外设延迟（Maximum Peripheral latency）。

单位（Unit）：子速率连接间隔（Subrated connection intervals），参见 `bt_conn_le_conn_rate_changed::subrate_factor`。

范围（Range）：`BT_HCI_LE_PERIPHERAL_LATENCY_MIN`–`BT_HCI_LE_PERIPHERAL_LATENCY_MAX`。

<a id="ae4734b6d8f0f4903624e47e975828482"></a>

### `min_ce_len_125us`

```c
uint16_t bt_conn_le_conn_rate_param::min_ce_len_125us
```

连接事件的最短持续时间（Minimum connection event length）。

单位（Unit）：125 微秒（Microseconds）。

范围（Range）：`BT_HCI_LE_SCI_CE_LEN_MIN_125US`–`BT_HCI_LE_SCI_CE_LEN_MAX_125US`。

<a id="a751042149cb8ff1ec28de10fe1e4c8bd"></a>

### `subrate_max`

```c
uint16_t bt_conn_le_conn_rate_param::subrate_max
```

最大子速率因子（Maximum subrate factor）。

范围（Range）：`BT_HCI_LE_SUBRATE_FACTOR_MIN`–`BT_HCI_LE_SUBRATE_FACTOR_MAX`。

<a id="aed9238960e4be8ddbeff53afab74ef6f"></a>

### `subrate_min`

```c
uint16_t bt_conn_le_conn_rate_param::subrate_min
```

最小子速率因子（Minimum subrate factor）。

范围（Range）：`BT_HCI_LE_SUBRATE_FACTOR_MIN`–`BT_HCI_LE_SUBRATE_FACTOR_MAX`。

<a id="a50a3c9eca10ed5c11773aaf07e1fbc12"></a>

### `supervision_timeout_10ms`

```c
uint16_t bt_conn_le_conn_rate_param::supervision_timeout_10ms
```

连接监督超时（Connection Supervision timeout）。

单位（Unit）：10 毫秒（Milliseconds）。

范围（Range）：`BT_HCI_LE_SUPERVISION_TIMEOUT_MIN`–`BT_HCI_LE_SUPERVISION_TIMEOUT_MAX`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BT_HCI_LE_CONTINUATION_NUM_MIN](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6ac68f277aff54739238ffdafb640f85)
- [BT_HCI_LE_CONTINUATION_NUM_MAX](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#aa2b9a667e0b80a4cf4d8cef9cb022ad4)
- [BT_HCI_LE_SCI_INTERVAL_MIN_125US](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a292c11301eed063f4b9cfec645881a47)
- [BT_HCI_LE_SCI_INTERVAL_MAX_125US](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a14c9d4eab8b8fe650ea2950d0c3a703f)
- [BT_HCI_LE_SCI_CE_LEN_MIN_125US](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#acef97af0baeb7f491d66ec1d0b4fff36)
- [BT_HCI_LE_SCI_CE_LEN_MAX_125US](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#ab0319b6bf5387c5a4d2d38d789fab6aa)
- [bt_conn_le_conn_rate_changed::subrate_factor](P010_bt_conn_le_conn_rate_changed_结构体.md#ab2b60e61438b0d814c9a8a8adcae35fc)
- [BT_HCI_LE_PERIPHERAL_LATENCY_MIN](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a95274b56d9d973f32d2098b433ed1ff7)
- [BT_HCI_LE_PERIPHERAL_LATENCY_MAX](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a9af7ce6ecbd978df6193c4e9c2d8b002)
- [BT_HCI_LE_SUBRATE_FACTOR_MIN](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a135059b92eba0676689abc78a2f560d3)
- [BT_HCI_LE_SUBRATE_FACTOR_MAX](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a33ce951c9eddfcc5556b0168c14b9769)
- [BT_HCI_LE_SUPERVISION_TIMEOUT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a07b822f1a826f4824ec070c4b6822fe2)
- [BT_HCI_LE_SUPERVISION_TIMEOUT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a1357a2a7227e86df1c132207ba44d6db)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_bt_conn_le_conn_rate_changed_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_bt_conn_le_create_param_结构体.md)
