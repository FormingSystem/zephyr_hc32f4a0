---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-105
title: bt_l2cap_le_endpoint_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__le__endpoint.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第105章\_bt\_l2cap\_le\_endpoint\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__le__endpoint.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

低功耗（LE）L2CAP端点结构。

```c
#include <zephyr/bluetooth/l2cap.h>
```

<a id="details"></a>

低功耗（LE）L2CAP端点结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 105.1\_数据成员（Data Fields）

<a id="r_aeee85135541b17bede098891b820c63f"></a>

```c
uint16_t cid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cid](#aeee85135541b17bede098891b820c63f)。

端点通道标识符（Channel Identifier，CID）。

<a id="r_a598f0c7f0ad4cc029013358d35ce9dc2"></a>

```c
uint16_t mtu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mtu](#a598f0c7f0ad4cc029013358d35ce9dc2)。

端点最大传输单元（Maximum Transmission Unit，MTU）。

<a id="r_aa9e4f21e48eda61a3d0b777ee13c2599"></a>

```c
uint16_t mps
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mps](#aa9e4f21e48eda61a3d0b777ee13c2599)。

端点最大协议数据单元（PDU）载荷大小。

<a id="r_ab3f475c383791731c595845c80c27edf"></a>

```c
atomic_t credits
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[credits](#ab3f475c383791731c595845c80c27edf)。

端点信用数（credits）。

## 105.2\_详细说明（Detailed Documentation）

<a id="aeee85135541b17bede098891b820c63f"></a>

### `cid`

```c
uint16_t bt_l2cap_le_endpoint::cid
```

端点通道标识符（Channel Identifier，CID）。

<a id="ab3f475c383791731c595845c80c27edf"></a>

### `credits`

```c
atomic_t bt_l2cap_le_endpoint::credits
```

端点信用数（credits）。

<a id="aa9e4f21e48eda61a3d0b777ee13c2599"></a>

### `mps`

```c
uint16_t bt_l2cap_le_endpoint::mps
```

端点最大协议数据单元（PDU）载荷大小。

<a id="a598f0c7f0ad4cc029013358d35ce9dc2"></a>

### `mtu`

```c
uint16_t bt_l2cap_le_endpoint::mtu
```

端点最大传输单元（Maximum Transmission Unit，MTU）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/l2cap.h`

## 105.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P104_bt_l2cap_le_chan_结构体.md) · [返回大纲](大纲.md) · [下一章](P106_bt_l2cap_server_结构体.md)
