---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-77
title: bt_iso_chan_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第77章\_bt\_iso\_chan\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

等时信道（ISO Channel）结构。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

等时信道（ISO Channel）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 77.1\_数据成员（Data Fields）

<a id="r_a7fd728385a3aec11be8883bdee8aedea"></a>

```c
struct bt_conn * iso
```

相关声明：[bt_conn](P002_bt_conn_结构体.md)、[iso](#a7fd728385a3aec11be8883bdee8aedea)。

通道连接引用（Channel connection reference）。

<a id="r_a214fe133602ac8dcfaaec7f372e12da8"></a>

```c
struct bt_iso_chan_ops * ops
```

相关声明：[bt_iso_chan_ops](P079_bt_iso_chan_ops_结构体.md)、[ops](#a214fe133602ac8dcfaaec7f372e12da8)。

通道操作引用（Channel operations reference）。

<a id="r_abe94fca71506bd590d9ef4465258914d"></a>

```c
struct bt_iso_chan_qos * qos
```

相关声明：[bt_iso_chan_qos](P081_bt_iso_chan_qos_结构体.md)、[qos](#abe94fca71506bd590d9ef4465258914d)。

通道服务质量引用（Channel QoS reference）。

<a id="r_a2b0fc7180d1983ee4a415c5331bed93d"></a>

```c
enum bt_iso_state state
```

相关声明：[bt_iso_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaf2925460cc22cc4220dc376bcbee6201)、[state](#a2b0fc7180d1983ee4a415c5331bed93d)。

通道状态（Channel state）。

<a id="r_aba7bf6dcad93b121c46daa6ad473a51c"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#aba7bf6dcad93b121c46daa6ad473a51c)。

## 77.2\_详细说明（Detailed Documentation）

<a id="a7fd728385a3aec11be8883bdee8aedea"></a>

### `iso`

```c
struct bt_conn* bt_iso_chan::iso
```

通道连接引用（Channel connection reference）。

<a id="aba7bf6dcad93b121c46daa6ad473a51c"></a>

### `node`

```c
sys_snode_t bt_iso_chan::node
```

<a id="a214fe133602ac8dcfaaec7f372e12da8"></a>

### `ops`

```c
struct bt_iso_chan_ops* bt_iso_chan::ops
```

通道操作引用（Channel operations reference）。

<a id="abe94fca71506bd590d9ef4465258914d"></a>

### `qos`

```c
struct bt_iso_chan_qos* bt_iso_chan::qos
```

通道服务质量引用（Channel QoS reference）。

<a id="a2b0fc7180d1983ee4a415c5331bed93d"></a>

### `state`

```c
enum bt_iso_state bt_iso_chan::state
```

通道状态（Channel state）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 77.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [bt_conn](P002_bt_conn_结构体.md)
- [bt_iso_chan_ops](P079_bt_iso_chan_ops_结构体.md)
- [bt_iso_chan_qos](P081_bt_iso_chan_qos_结构体.md)
- [bt_iso_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaf2925460cc22cc4220dc376bcbee6201)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P076_bt_iso_broadcaster_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P078_bt_iso_chan_io_qos_结构体.md)
