---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-32
title: bt_conn_le_subrate_changed_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__subrate__changed.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_bt\_conn\_le\_subrate\_changed\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__subrate__changed.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LE 连接已更新的子速率（Subrating）连接参数。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

LE 连接已更新的子速率（Subrating）连接参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 32.1\_数据成员（Data Fields）

<a id="r_afc5a577dadf41819e89bc3af016ce258"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#afc5a577dadf41819e89bc3af016ce258)。

低功耗子速率变化事件（LE Subrate Changed）的主机控制器接口状态（HCI Status）。

<a id="r_a0c3e3dc41ca4dec92740c920e959060b"></a>

```c
uint16_t factor
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[factor](#a0c3e3dc41ca4dec92740c920e959060b)。

连接子速率因子（Connection subrate factor）。

<a id="r_a2420a0a3145471c6a1a618bea8d1d7c6"></a>

```c
uint16_t continuation_number
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[continuation_number](#a2420a0a3145471c6a1a618bea8d1d7c6)。

发送或接收到包含长度字段（Length field）非零的链路层协议数据单元（Link Layer PDU）的数据包后，继续保持活动状态的底层连接事件数量（Underlying connection events）。

<a id="r_aa0bab070bc43972dfb3a5259934b4931"></a>

```c
uint16_t peripheral_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[peripheral_latency](#aa0bab070bc43972dfb3a5259934b4931)。

外设延迟（Peripheral latency），以子速率连接间隔（Subrated connection intervals）为单位。

<a id="r_aab0cb08a7549401684bcab3c291dc192"></a>

```c
uint16_t supervision_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[supervision_timeout](#aab0cb08a7549401684bcab3c291dc192)。

连接监督超时（Connection Supervision timeout），为 N × 10 毫秒。

## 32.2\_详细说明（Detailed Documentation）

<a id="a2420a0a3145471c6a1a618bea8d1d7c6"></a>

### `continuation_number`

```c
uint16_t bt_conn_le_subrate_changed::continuation_number
```

发送或接收到包含长度字段（Length field）非零的链路层协议数据单元（Link Layer PDU）的数据包后，继续保持活动状态的底层连接事件数量（Underlying connection events）。

<a id="a0c3e3dc41ca4dec92740c920e959060b"></a>

### `factor`

```c
uint16_t bt_conn_le_subrate_changed::factor
```

连接子速率因子（Connection subrate factor）。

<a id="aa0bab070bc43972dfb3a5259934b4931"></a>

### `peripheral_latency`

```c
uint16_t bt_conn_le_subrate_changed::peripheral_latency
```

外设延迟（Peripheral latency），以子速率连接间隔（Subrated connection intervals）为单位。

<a id="afc5a577dadf41819e89bc3af016ce258"></a>

### `status`

```c
uint8_t bt_conn_le_subrate_changed::status
```

低功耗子速率变化事件（LE Subrate Changed）的主机控制器接口状态（HCI Status）。

若 `status` 不是 `BT_HCI_ERR_SUCCESS`，则其余参数保持不变。

<a id="aab0cb08a7549401684bcab3c291dc192"></a>

### `supervision_timeout`

```c
uint16_t bt_conn_le_subrate_changed::supervision_timeout
```

连接监督超时（Connection Supervision timeout），为 N × 10 毫秒。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 32.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P031_bt_conn_le_remote_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P033_bt_conn_le_subrate_param_结构体.md)
