---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-10
title: bt_conn_le_conn_rate_changed_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__conn__rate__changed.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_bt\_conn\_le\_conn\_rate\_changed\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__conn__rate__changed.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

已更新的连接速率（Connection Rate）参数。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

已更新的连接速率（Connection Rate）参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_aa6dfef1425c47823897b8b84de17ecf9"></a>

```c
uint32_t interval_us
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[interval_us](#aa6dfef1425c47823897b8b84de17ecf9)。

连接间隔（Connection interval）。

<a id="r_ab2b60e61438b0d814c9a8a8adcae35fc"></a>

```c
uint16_t subrate_factor
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subrate_factor](#ab2b60e61438b0d814c9a8a8adcae35fc)。

连接子速率因子（Connection subrate factor）。

<a id="r_a768af259e8d37f463278946bd660ce58"></a>

```c
uint16_t peripheral_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[peripheral_latency](#a768af259e8d37f463278946bd660ce58)。

外设延迟（Peripheral latency）。

<a id="r_a348cc25c2f19bab8c5e140b712b3034a"></a>

```c
uint16_t continuation_number
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[continuation_number](#a348cc25c2f19bab8c5e140b712b3034a)。

发送或接收到包含长度字段（Length field）非零的链路层协议数据单元（Link Layer PDU）的数据包后，继续保持活动状态的底层连接事件数量（Underlying connection events）。

<a id="r_a47d662c1e00e8c4e1a553d9a4909f6df"></a>

```c
uint16_t supervision_timeout_10ms
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[supervision_timeout_10ms](#a47d662c1e00e8c4e1a553d9a4909f6df)。

连接监督超时（Connection Supervision timeout）。

## 10.2\_详细说明（Detailed Documentation）

<a id="a348cc25c2f19bab8c5e140b712b3034a"></a>

### `continuation_number`

```c
uint16_t bt_conn_le_conn_rate_changed::continuation_number
```

发送或接收到包含长度字段（Length field）非零的链路层协议数据单元（Link Layer PDU）的数据包后，继续保持活动状态的底层连接事件数量（Underlying connection events）。

范围（Range）：`BT_HCI_LE_CONTINUATION_NUM_MIN`–`BT_HCI_LE_CONTINUATION_NUM_MAX`。

<a id="aa6dfef1425c47823897b8b84de17ecf9"></a>

### `interval_us`

```c
uint32_t bt_conn_le_conn_rate_changed::interval_us
```

连接间隔（Connection interval）。

单位（Unit）：微秒（Microseconds）。

范围（Range）：`BT_HCI_LE_SCI_INTERVAL_MIN_US`–`BT_HCI_LE_SCI_INTERVAL_MAX_US`。

<a id="a768af259e8d37f463278946bd660ce58"></a>

### `peripheral_latency`

```c
uint16_t bt_conn_le_conn_rate_changed::peripheral_latency
```

外设延迟（Peripheral latency）。

单位（Unit）：子速率连接间隔（Subrated connection intervals），参见 `bt_conn_le_conn_rate_changed::subrate_factor`。

范围（Range）：`BT_HCI_LE_PERIPHERAL_LATENCY_MIN`–`BT_HCI_LE_PERIPHERAL_LATENCY_MAX`。

<a id="ab2b60e61438b0d814c9a8a8adcae35fc"></a>

### `subrate_factor`

```c
uint16_t bt_conn_le_conn_rate_changed::subrate_factor
```

连接子速率因子（Connection subrate factor）。

范围（Range）：`BT_HCI_LE_SUBRATE_FACTOR_MIN`–`BT_HCI_LE_SUBRATE_FACTOR_MAX`。

<a id="a47d662c1e00e8c4e1a553d9a4909f6df"></a>

### `supervision_timeout_10ms`

```c
uint16_t bt_conn_le_conn_rate_changed::supervision_timeout_10ms
```

连接监督超时（Connection Supervision timeout）。

单位（Unit）：10 毫秒（Milliseconds）。

范围（Range）：`BT_HCI_LE_SUPERVISION_TIMEOUT_MIN`–`BT_HCI_LE_SUPERVISION_TIMEOUT_MAX`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 10.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BT_HCI_LE_CONTINUATION_NUM_MIN](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6ac68f277aff54739238ffdafb640f85)
- [BT_HCI_LE_CONTINUATION_NUM_MAX](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#aa2b9a667e0b80a4cf4d8cef9cb022ad4)
- [BT_HCI_LE_SCI_INTERVAL_MIN_US](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a9d55d12b5d3c37c99730950878075684)
- [BT_HCI_LE_SCI_INTERVAL_MAX_US](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#ad6ccdf8c0658b065218f10581990fef8)
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

[上一章](P009_bt_conn_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P011_bt_conn_le_conn_rate_param_结构体.md)
