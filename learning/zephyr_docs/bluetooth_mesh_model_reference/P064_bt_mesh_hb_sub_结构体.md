---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-64
title: bt_mesh_hb_sub_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__hb__sub.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_bt\_mesh\_hb\_sub\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__hb__sub.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

心跳订阅（Heartbeat Subscription）的参数。

```c
#include <zephyr/bluetooth/mesh/heartbeat.h>
```

<a id="details"></a>

心跳订阅（Heartbeat Subscription）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 64.1\_数据成员（Data Fields）

<a id="r_af7b20a7337c31110b1ae38c7eacc071a"></a>

```c
uint32_t period
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[period](#af7b20a7337c31110b1ae38c7eacc071a)。

订阅周期（Subscription period），单位为秒。

<a id="r_ad66fd08eb09d475bef9c290fa7ae0a90"></a>

```c
uint32_t remaining
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[remaining](#ad66fd08eb09d475bef9c290fa7ae0a90)。

剩余订阅时间（Remaining subscription time），单位为秒。

<a id="r_afb9fba6c32257690539dd621e215708b"></a>

```c
uint16_t src
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[src](#afb9fba6c32257690539dd621e215708b)。

要从中接收心跳（Heartbeats）的源地址（Source address）。

<a id="r_ab10708af9ddfd7a80c370d40d2146a8b"></a>

```c
uint16_t dst
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dst](#ab10708af9ddfd7a80c370d40d2146a8b)。

用于接收心跳（Heartbeats）的目的地址（Destination address）。

<a id="r_a41dd595eb6a0c980c49f84aca11b3ac2"></a>

```c
uint16_t count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[count](#a41dd595eb6a0c980c49f84aca11b3ac2)。

截至当前已接收的心跳消息数量（Heartbeat message count）。

<a id="r_aae4eb4e77166dfb49a7341ae8fcb9e6e"></a>

```c
uint8_t min_hops
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_hops](#aae4eb4e77166dfb49a7341ae8fcb9e6e)。

接收消息中的最小跳数（Minimum hops），即从发布节点到订阅节点记录到的最短路径。

<a id="r_a38252818d3a2e136e5dfc9bda847d0b0"></a>

```c
uint8_t max_hops
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_hops](#a38252818d3a2e136e5dfc9bda847d0b0)。

接收消息中的最大跳数（Maximum hops），即从发布节点到订阅节点记录到的最长路径。

## 64.2\_详细说明（Detailed Documentation）

<a id="a41dd595eb6a0c980c49f84aca11b3ac2"></a>

### `count`

```c
uint16_t bt_mesh_hb_sub::count
```

截至当前已接收的心跳消息数量（Heartbeat message count）。

<a id="ab10708af9ddfd7a80c370d40d2146a8b"></a>

### `dst`

```c
uint16_t bt_mesh_hb_sub::dst
```

用于接收心跳（Heartbeats）的目的地址（Destination address）。

<a id="a38252818d3a2e136e5dfc9bda847d0b0"></a>

### `max_hops`

```c
uint8_t bt_mesh_hb_sub::max_hops
```

接收消息中的最大跳数（Maximum hops），即从发布节点到订阅节点记录到的最长路径。

从直接邻居（Immediate neighbor）收到的心跳，其跳数（Hop count）为 `1`。

<a id="aae4eb4e77166dfb49a7341ae8fcb9e6e"></a>

### `min_hops`

```c
uint8_t bt_mesh_hb_sub::min_hops
```

接收消息中的最小跳数（Minimum hops），即从发布节点到订阅节点记录到的最短路径。

从直接邻居（Immediate neighbor）收到的心跳，其跳数（Hop count）为 `1`。

<a id="af7b20a7337c31110b1ae38c7eacc071a"></a>

### `period`

```c
uint32_t bt_mesh_hb_sub::period
```

订阅周期（Subscription period），单位为秒。

<a id="ad66fd08eb09d475bef9c290fa7ae0a90"></a>

### `remaining`

```c
uint32_t bt_mesh_hb_sub::remaining
```

剩余订阅时间（Remaining subscription time），单位为秒。

<a id="afb9fba6c32257690539dd621e215708b"></a>

### `src`

```c
uint16_t bt_mesh_hb_sub::src
```

要从中接收心跳（Heartbeats）的源地址（Source address）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/heartbeat.h`

## 64.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/heartbeat.h](https://docs.zephyrproject.org/latest/doxygen/html/heartbeat_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P063_bt_mesh_hb_pub_结构体.md) · [返回大纲](大纲.md) · [下一章](P065_bt_mesh_health_cli_结构体.md)
