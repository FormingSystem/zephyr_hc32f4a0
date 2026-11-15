---
id: learning.zephyr-docs.platform-security-model-reference.page-48
title: scmi_protocol_events_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__protocol__events.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_scmi\_protocol\_events\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__protocol__events.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）的协议事件结构。

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

<a id="details"></a>

系统控制与管理接口（SCMI）的协议事件结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 48.1\_数据成员（Data Fields）

<a id="r_ac04442b926499369d7c89d8aacf0da41"></a>

```c
const uint32_t * evts
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[evts](#ac04442b926499369d7c89d8aacf0da41)。

支持的通知消息 ID。

<a id="r_a33fb7a3e095fb1ad5267080130277578"></a>

```c
uint32_t num_events
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[num_events](#a33fb7a3e095fb1ad5267080130277578)。

支持的协议通知数量。

<a id="r_a5ea92cc3ee5da51882568cc464378a7b"></a>

```c
scmi_protocol_event_callback cb
```

相关声明：[scmi_protocol_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga8430a8fd8a2f84d0f5613a88b8d86650)、[cb](#a5ea92cc3ee5da51882568cc464378a7b)。

协议通知回调（Protocol notification callback）。

## 48.2\_详细说明（Detailed Documentation）

<a id="a5ea92cc3ee5da51882568cc464378a7b"></a>

### `cb`

```c
scmi_protocol_event_callback scmi_protocol_events::cb
```

协议通知回调（Protocol notification callback）。

<a id="ac04442b926499369d7c89d8aacf0da41"></a>

### `evts`

```c
const uint32_t* scmi_protocol_events::evts
```

支持的通知消息 ID。

<a id="a33fb7a3e095fb1ad5267080130277578"></a>

### `num_events`

```c
uint32_t scmi_protocol_events::num_events
```

支持的协议通知数量。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/protocol.h`

## 48.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [scmi_protocol_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga8430a8fd8a2f84d0f5613a88b8d86650)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P047_scmi_protocol_结构体.md) · [返回大纲](大纲.md) · [下一章](P049_scmi_protocol_version_结构体.md)
