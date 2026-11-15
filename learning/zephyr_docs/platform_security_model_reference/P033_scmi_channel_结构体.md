---
id: learning.zephyr-docs.platform-security-model-reference.page-33
title: scmi_channel_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__channel.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_scmi\_channel\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__channel.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）的通道结构。

```c
#include <zephyr/drivers/firmware/scmi/transport.h>
```

<a id="details"></a>

SCMI 通道结构体（Channel structure）。SCMI 通道是协议发送和接收消息的媒介。每个 SCMI 通道均由一个 `struct scmi_channel` 表示。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.1\_数据成员（Data Fields）

<a id="r_a1b69c9d0c6b49f5496ad59270ab8f157"></a>

```c
void * data
```

相关声明：[data](#a1b69c9d0c6b49f5496ad59270ab8f157)。

通道私有数据。

<a id="r_a81065fcba9755ccf88c3ce372ded5d56"></a>

```c
scmi_channel_cb cb
```

相关声明：[scmi_channel_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__transport.html#ga4c6cccb4e76fef22ec9f3527a96a8de5)、[cb](#a81065fcba9755ccf88c3ce372ded5d56)。

回调函数（Callback function）。

<a id="r_ad049e30d6a1806232e2f0adf19e472c9"></a>

```c
bool polling_only
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[polling_only](#ad049e30d6a1806232e2f0adf19e472c9)。

指示通道是否要求仅使用轮询（Polling-only）方式运行。

## 33.2\_详细说明（Detailed Documentation）

<a id="a81065fcba9755ccf88c3ce372ded5d56"></a>

### `cb`

```c
scmi_channel_cb scmi_channel::cb
```

回调函数（Callback function）。

此回调应由 SCMI 核心设置；SCMI 传输层驱动每当收到回复时，都应调用它。

<a id="a1b69c9d0c6b49f5496ad59270ab8f157"></a>

### `data`

```c
void* scmi_channel::data
```

通道私有数据。

<a id="ad049e30d6a1806232e2f0adf19e472c9"></a>

### `polling_only`

```c
bool scmi_channel::polling_only
```

指示通道是否要求仅使用轮询（Polling-only）方式运行。

设置为 `true` 时，通道无法使用基于中断的消息传输，必须始终轮询响应。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/transport.h`

## 33.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/transport.h](https://docs.zephyrproject.org/latest/doxygen/html/transport_8h_source.html)
- [scmi_channel_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__transport.html#ga4c6cccb4e76fef22ec9f3527a96a8de5)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [scmi_channel](P033_scmi_channel_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_scmi_agent_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_scmi_clock_attributes_结构体.md)
