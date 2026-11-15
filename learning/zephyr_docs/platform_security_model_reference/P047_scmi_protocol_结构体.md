---
id: learning.zephyr-docs.platform-security-model-reference.page-47
title: scmi_protocol_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__protocol.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_scmi\_protocol\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__protocol.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）的协议结构。

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

<a id="details"></a>

系统控制与管理接口（SCMI）的协议结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 47.1\_数据成员（Data Fields）

<a id="r_ae2c2026eeaad8c5bf73be885fdd6315c"></a>

```c
uint32_t id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[id](#ae2c2026eeaad8c5bf73be885fdd6315c)。

协议 ID（Protocol ID）。

<a id="r_aa2a78f57d21a573c6091fba89a757a52"></a>

```c
struct scmi_channel * tx
```

相关声明：[scmi_channel](P033_scmi_channel_结构体.md)、[tx](#aa2a78f57d21a573c6091fba89a757a52)。

发送通道（TX channel）。

<a id="r_a4580aabc67a32be7dc9e914dd863a90b"></a>

```c
struct scmi_channel * rx
```

相关声明：[scmi_channel](P033_scmi_channel_结构体.md)、[rx](#a4580aabc67a32be7dc9e914dd863a90b)。

接收通道（RX channel）。

<a id="r_a9081097c7aa12c407ec1d837c541d666"></a>

```c
const struct device * transport
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[transport](#a9081097c7aa12c407ec1d837c541d666)。

传输层设备（Transport layer device）。

<a id="r_ad6c1e08eebc96ff76ae656510d04a9d5"></a>

```c
void * data
```

相关声明：[data](#ad6c1e08eebc96ff76ae656510d04a9d5)。

协议私有数据。

<a id="r_a809979e1c761c8486d62a4af6a21b4ad"></a>

```c
uint32_t version
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[version](#a809979e1c761c8486d62a4af6a21b4ad)。

协议支持的版本。

<a id="r_a1b414028a899b5bef9c4df38352c5928"></a>

```c
const struct scmi_protocol_events * events
```

相关声明：[scmi_protocol_events](P048_scmi_protocol_events_结构体.md)、[events](#a1b414028a899b5bef9c4df38352c5928)。

协议事件（Protocol events）。

## 47.2\_详细说明（Detailed Documentation）

<a id="ad6c1e08eebc96ff76ae656510d04a9d5"></a>

### `data`

```c
void* scmi_protocol::data
```

协议私有数据。

<a id="a1b414028a899b5bef9c4df38352c5928"></a>

### `events`

```c
const struct scmi_protocol_events* scmi_protocol::events
```

协议事件（Protocol events）。

<a id="ae2c2026eeaad8c5bf73be885fdd6315c"></a>

### `id`

```c
uint32_t scmi_protocol::id
```

协议 ID（Protocol ID）。

<a id="a4580aabc67a32be7dc9e914dd863a90b"></a>

### `rx`

```c
struct scmi_channel* scmi_protocol::rx
```

接收通道（RX channel）。

<a id="a9081097c7aa12c407ec1d837c541d666"></a>

### `transport`

```c
const struct device* scmi_protocol::transport
```

传输层设备（Transport layer device）。

<a id="aa2a78f57d21a573c6091fba89a757a52"></a>

### `tx`

```c
struct scmi_channel* scmi_protocol::tx
```

发送通道（TX channel）。

<a id="a809979e1c761c8486d62a4af6a21b4ad"></a>

### `version`

```c
uint32_t scmi_protocol::version
```

协议支持的版本。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/protocol.h`

## 47.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [scmi_channel](P033_scmi_channel_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [scmi_protocol_events](P048_scmi_protocol_events_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P046_scmi_power_state_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P048_scmi_protocol_events_结构体.md)
