---
id: learning.zephyr-docs.network-service-model-reference.page-56
title: socketcan_filter_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsocketcan__filter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_socketcan\_filter\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsocketcan__filter.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

与Linux SocketCAN兼容的CAN过滤器（Filter）。

```c
#include <zephyr/net/socketcan.h>
```

<a id="details"></a>

用于兼容 Linux SocketCAN 的 CAN 过滤器。原文给出的匹配条件为 `received_can_id & mask == can_id & can_mask`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 56.1\_数据成员（Data Fields）

<a id="r_a9217950edb190dc70783d9b87676ae47"></a>

```c
socketcan_id_t can_id
```

相关声明：[socketcan_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga35a7941726d1e22defd8c3098391ca8e)、[can_id](#a9217950edb190dc70783d9b87676ae47)。

要匹配的 CAN 标识符。

<a id="r_a841857f05f1e1a887be50d8e507a03f9"></a>

```c
socketcan_id_t can_mask
```

相关声明：[socketcan_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga35a7941726d1e22defd8c3098391ca8e)、[can_mask](#a841857f05f1e1a887be50d8e507a03f9)。

用于匹配时施加到 `can_id` 的掩码。

<a id="r_a84abbc2f8a18bfe2d53cacf582f9fa10"></a>

```c
uint8_t flags
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](#a84abbc2f8a18bfe2d53cacf582f9fa10)。

用于灵活数据速率（FD）帧过滤器的附加标志。

## 56.2\_详细说明（Detailed Documentation）

<a id="a9217950edb190dc70783d9b87676ae47"></a>

### `can_id`

```c
socketcan_id_t socketcan_filter::can_id
```

要匹配的 CAN 标识符。

<a id="a841857f05f1e1a887be50d8e507a03f9"></a>

### `can_mask`

```c
socketcan_id_t socketcan_filter::can_mask
```

用于匹配时施加到 `can_id` 的掩码。

<a id="a84abbc2f8a18bfe2d53cacf582f9fa10"></a>

### `flags`

```c
uint8_t socketcan_filter::flags
```

用于灵活数据速率（FD）帧过滤器的附加标志。

本数据类型文档由以下文件生成：

- `zephyr/net/socketcan.h`

## 56.3\_原页交叉引用（Cross References）

- [zephyr/net/socketcan.h](https://docs.zephyrproject.org/latest/doxygen/html/socketcan_8h_source.html)
- [socketcan_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga35a7941726d1e22defd8c3098391ca8e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P055_socket_dns_offload_结构体.md) · [返回大纲](大纲.md) · [下一章](P057_socketcan_frame_结构体.md)
