---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-81
title: bt_iso_chan_qos_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan__qos.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第81章\_bt\_iso\_chan\_qos\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan__qos.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

等时信道（ISO Channel）的服务质量（QoS）结构。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

等时信道（ISO Channel）的服务质量（QoS）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 81.1\_数据成员（Data Fields）

<a id="r_ac231434d1798f431c4fbac5a759784a5"></a>

```c
struct bt_iso_chan_io_qos * rx
```

相关声明：[bt_iso_chan_io_qos](P078_bt_iso_chan_io_qos_结构体.md)、[rx](#ac231434d1798f431c4fbac5a759784a5)。

通道接收服务质量（Channel Receiving QoS）。

<a id="r_a47a99a6ccfa5f1e0c9fb859e66d2e9e3"></a>

```c
struct bt_iso_chan_io_qos * tx
```

相关声明：[bt_iso_chan_io_qos](P078_bt_iso_chan_io_qos_结构体.md)、[tx](#a47a99a6ccfa5f1e0c9fb859e66d2e9e3)。

通道发送服务质量（Channel Transmission QoS）。

<a id="r_a4c6bfa577f8cbd724ed2561850fd6255"></a>

```c
uint8_t num_subevents
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_subevents](#a4c6bfa577f8cbd724ed2561850fd6255)。

子事件数量（Number of Subevents）。

## 81.2\_详细说明（Detailed Documentation）

<a id="a4c6bfa577f8cbd724ed2561850fd6255"></a>

### `num_subevents`

```c
uint8_t bt_iso_chan_qos::num_subevents
```

子事件数量（Number of Subevents）。

每个 CIS 或 BIS 事件中的最大子事件数量。

取值范围为 `BT_ISO_NSE_MIN` 到 `BT_ISO_NSE_MAX`。

<a id="ac231434d1798f431c4fbac5a759784a5"></a>

### `rx`

```c
struct bt_iso_chan_io_qos* bt_iso_chan_qos::rx
```

通道接收服务质量（Channel Receiving QoS）。

设为 `NULL` 时禁用数据路径 `BT_HCI_DATAPATH_DIR_CTLR_TO_HOST`。

只能为连接等时通道（Connected isochronous channel）或广播等时接收方（Broadcast isochronous receiver）设置。

<a id="a47a99a6ccfa5f1e0c9fb859e66d2e9e3"></a>

### `tx`

```c
struct bt_iso_chan_io_qos* bt_iso_chan_qos::tx
```

通道发送服务质量（Channel Transmission QoS）。

设为 `NULL` 时禁用数据路径 `BT_HCI_DATAPATH_DIR_HOST_TO_CTLR`。

只能为连接等时通道（Connected isochronous channel）或广播等时发送方（Broadcast isochronous transmitter）设置。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 81.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [bt_iso_chan_io_qos](P078_bt_iso_chan_io_qos_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_ISO_NSE_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga3eba4c20b4203b0323b14178522e6159)
- [BT_ISO_NSE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gab7637d96bde7a41123b34f487eec3436)
- [BT_HCI_DATAPATH_DIR_CTLR_TO_HOST](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#af8d89c712a3d27f9b6f92a31bea2a8c3)
- [BT_HCI_DATAPATH_DIR_HOST_TO_CTLR](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a0f74c19fabbcb3088e1a819d33a05a1c)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P080_bt_iso_chan_path_结构体.md) · [返回大纲](大纲.md) · [下一章](P082_bt_iso_cig_结构体.md)
