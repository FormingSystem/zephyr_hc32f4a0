---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-109
title: bt_le_local_features_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__local__features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第109章\_bt\_le\_local\_features\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__local__features.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本地低功耗蓝牙控制器（Bluetooth LE Controller）的特性与能力。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

本地蓝牙低功耗控制器特性及能力（Local Bluetooth LE controller features and capabilities）。此结构提供控制器支持的特性、状态及其他能力信息，包括异步面向连接链路（ACL）和等时（ISO）数据包长度、控制器解析列表大小（Resolving list size）、最大广播数据长度等。使用 `bt_enable` 函数启用蓝牙协议栈后，即可获取这些信息。各字段含义和取值的详细说明，参见蓝牙核心规范（Bluetooth Core Specification）第 6 卷 B 部分及第 4 卷 E 部分。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 109.1\_数据成员（Data Fields）

<a id="r_a516ca4b44a693f045a45eedf375c9ea6"></a>

```c
uint8_t features [BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[features](#a516ca4b44a693f045a45eedf375c9ea6)、[BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a81b4b9ce53511c62889790a79b0f6a34)。

本地低功耗控制器支持的特性（Local LE controller supported features）。

<a id="r_aa2dc6363feab37af195ee192f2b906f1"></a>

```c
uint64_t states
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[states](#aa2dc6363feab37af195ee192f2b906f1)。

本地低功耗控制器支持的状态（Local LE controller supported states）。

<a id="r_a22ce370b338f687ce6860435cc0ec9c5"></a>

```c
uint16_t acl_mtu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[acl_mtu](#a22ce370b338f687ce6860435cc0ec9c5)。

异步面向连接链路数据包长度（ACL data packet length）。

<a id="r_a19cecbe8574229844e9416842bc42b0c"></a>

```c
uint8_t acl_pkts
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[acl_pkts](#a19cecbe8574229844e9416842bc42b0c)。

异步面向连接链路数据包总数（ACL data packets）。

<a id="r_ad7b95feb82c1dece8bb8bb7969efa2ec"></a>

```c
uint16_t iso_mtu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[iso_mtu](#ad7b95feb82c1dece8bb8bb7969efa2ec)。

等时数据包长度（ISO data packet length）。

<a id="r_a8b413bf80ccd7e3af67f7e1c28a1beeb"></a>

```c
uint8_t iso_pkts
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[iso_pkts](#a8b413bf80ccd7e3af67f7e1c28a1beeb)。

等时数据包总数（ISO data packets）。

<a id="r_ac86ae6974627ddb2e34b0d028cdcfe32"></a>

```c
uint8_t rl_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rl_size](#ac86ae6974627ddb2e34b0d028cdcfe32)。

控制器解析列表最大大小（Maximum controller resolving list size）。

<a id="r_a932af365332149ec620413a8504d342c"></a>

```c
uint16_t max_adv_data_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_adv_data_len](#a932af365332149ec620413a8504d342c)。

最大广播数据长度（Maximum advertising data length）。

## 109.2\_详细说明（Detailed Documentation）

<a id="a22ce370b338f687ce6860435cc0ec9c5"></a>

### `acl_mtu`

```c
uint16_t bt_le_local_features::acl_mtu
```

异步面向连接链路数据包长度（ACL data packet length）。

表示可从主机（Host）发送到控制器（Controller）的最大异步面向连接链路 HCI 数据包（ACL HCI Data packet）。主机可能支持大于此值的 L2CAP 和 ATT 最大传输单元（MTUs）。参见蓝牙核心规范（Bluetooth Core Specification）第 6 卷 E 部分第 7.8.2 节。译注：此处卷号按原文保留。

<a id="a19cecbe8574229844e9416842bc42b0c"></a>

### `acl_pkts`

```c
uint8_t bt_le_local_features::acl_pkts
```

异步面向连接链路数据包总数（ACL data packets）。

<a id="a516ca4b44a693f045a45eedf375c9ea6"></a>

### `features`

```c
uint8_t bt_le_local_features::features[BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE]
```

本地低功耗控制器支持的特性（Local LE controller supported features）。

取值参见 `BT_LE_FEAT_BIT_*`，取值比较参见 `BT_FEAT_LE_*` 宏。另见蓝牙核心规范（Bluetooth Core Specification）第 6 卷 B 部分第 4.6 节。

<a id="ad7b95feb82c1dece8bb8bb7969efa2ec"></a>

### `iso_mtu`

```c
uint16_t bt_le_local_features::iso_mtu
```

等时数据包长度（ISO data packet length）。

表示可从主机（Host）发送到控制器（Controller）的最大等时 HCI 数据包（ISO HCI Data packet）。大于此大小的等时服务数据单元（ISO SDUs）可以分片，前提是 `bt_le_local_features::iso_pkts` 所表示的数量能够支持所需最大大小。

<a id="a8b413bf80ccd7e3af67f7e1c28a1beeb"></a>

### `iso_pkts`

```c
uint8_t bt_le_local_features::iso_pkts
```

等时数据包总数（ISO data packets）。

<a id="a932af365332149ec620413a8504d342c"></a>

### `max_adv_data_len`

```c
uint16_t bt_le_local_features::max_adv_data_len
```

最大广播数据长度（Maximum advertising data length）。

参见蓝牙核心规范（Bluetooth Core Specification）第 6 卷 E 部分第 7.8.57 节。译注：此处卷号按原文保留。

**说明（Note）**：注意（Note）：最大广播数据长度（Maximum advertising data length）还取决于广播类型。

<a id="ac86ae6974627ddb2e34b0d028cdcfe32"></a>

### `rl_size`

```c
uint8_t bt_le_local_features::rl_size
```

控制器解析列表最大大小（Maximum controller resolving list size）。

参见蓝牙核心规范（Bluetooth Core Specification）第 6 卷 E 部分第 7.8.41 节。译注：此处卷号按原文保留。

<a id="aa2dc6363feab37af195ee192f2b906f1"></a>

### `states`

```c
uint64_t bt_le_local_features::states
```

本地低功耗控制器支持的状态（Local LE controller supported states）。

取值参见 `BT_LE_STATES_*`。另见蓝牙核心规范（Bluetooth Core Specification）6.0 版第 4 卷 E 部分第 7.8.27 节。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 109.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a81b4b9ce53511c62889790a79b0f6a34)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac45d16bfe21c3c38e834c293e5ebc42b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P108_bt_le_ext_adv_start_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P110_bt_le_oob_结构体.md)
