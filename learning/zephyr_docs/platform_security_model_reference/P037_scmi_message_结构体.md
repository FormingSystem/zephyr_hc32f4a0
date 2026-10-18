---
id: learning.zephyr-docs.platform-security-model-reference.page-37
title: scmi_message_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__message.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_scmi\_message\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__message.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）的消息结构。

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

<a id="details"></a>

系统控制与管理接口（SCMI）的消息结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 37.1\_数据成员（Data Fields）

<a id="r_a4b329136651a527d51310af82dc24795"></a>

```c
uint32_t hdr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[hdr](#a4b329136651a527d51310af82dc24795)。

消息头（Message header），参见 `SCMI_MESSAGE_HDR_MAKE`。

<a id="r_aad4f7713d97765414e21a4cb6ed4b01f"></a>

```c
uint32_t len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[len](#aad4f7713d97765414e21a4cb6ed4b01f)。

`content` 所指数据的大小，单位为字节。

<a id="r_ae868ec173129a6f81c895279e95bb52d"></a>

```c
void * content
```

相关声明：[content](#ae868ec173129a6f81c895279e95bb52d)。

指向消息载荷（Payload）的指针；载荷为参数或返回值。

## 37.2\_详细说明（Detailed Documentation）

<a id="ae868ec173129a6f81c895279e95bb52d"></a>

### `content`

```c
void* scmi_message::content
```

指向消息载荷（Payload）的指针；载荷为参数或返回值。

<a id="a4b329136651a527d51310af82dc24795"></a>

### `hdr`

```c
uint32_t scmi_message::hdr
```

消息头（Message header），参见 `SCMI_MESSAGE_HDR_MAKE`。

<a id="aad4f7713d97765414e21a4cb6ed4b01f"></a>

### `len`

```c
uint32_t scmi_message::len
```

`content` 所指数据的大小，单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/protocol.h`

## 37.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [SCMI_MESSAGE_HDR_MAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#ga100155d2238e9f860e2cab8ad8209a8a)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P036_scmi_clock_rate_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P038_scmi_nxp_cpu_info_结构体.md)
