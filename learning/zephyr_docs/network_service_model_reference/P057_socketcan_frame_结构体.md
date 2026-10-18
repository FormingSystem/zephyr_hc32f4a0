---
id: learning.zephyr-docs.network-service-model-reference.page-57
title: socketcan_frame_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsocketcan__frame.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_socketcan\_frame\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsocketcan__frame.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

与Linux SocketCAN兼容的CAN帧（Frame）。

```c
#include <zephyr/net/socketcan.h>
```

<a id="details"></a>

与Linux SocketCAN兼容的CAN帧（Frame）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 57.1\_数据成员（Data Fields）

<a id="r_a43511a491c9b8cf63b4ff592eb77a6e6"></a>

```c
socketcan_id_t can_id
```

相关声明：[socketcan_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga35a7941726d1e22defd8c3098391ca8e)、[can_id](#a43511a491c9b8cf63b4ff592eb77a6e6)。

32 位 CAN ID，加上扩展帧格式、远程传输请求及错误（EFF/RTR/ERR）标志。

<a id="r_aa21e8007363ab0183c7b9d6c59cb4731"></a>

```c
uint8_t len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](#aa21e8007363ab0183c7b9d6c59cb4731)。

帧载荷长度，单位为字节。

<a id="r_af9ddb322cdc3d886182cce65f673177d"></a>

```c
uint8_t flags
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](#af9ddb322cdc3d886182cce65f673177d)。

用于 CAN FD 的附加标志。

<a id="r_a4ab22ff419e3c7397c64a1309cbdb623"></a>

```c
uint8_t data [8U]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a4ab22ff419e3c7397c64a1309cbdb623)。

载荷数据（payload data）。

## 57.2\_详细说明（Detailed Documentation）

<a id="a43511a491c9b8cf63b4ff592eb77a6e6"></a>

### `can_id`

```c
socketcan_id_t socketcan_frame::can_id
```

32 位 CAN ID，加上扩展帧格式、远程传输请求及错误（EFF/RTR/ERR）标志。

<a id="a4ab22ff419e3c7397c64a1309cbdb623"></a>

### `data`

```c
uint8_t socketcan_frame::data[8U]
```

载荷数据（payload data）。

<a id="af9ddb322cdc3d886182cce65f673177d"></a>

### `flags`

```c
uint8_t socketcan_frame::flags
```

用于 CAN FD 的附加标志。

<a id="aa21e8007363ab0183c7b9d6c59cb4731"></a>

### `len`

```c
uint8_t socketcan_frame::len
```

帧载荷长度，单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/net/socketcan.h`

## 57.3\_原页交叉引用（Cross References）

- [zephyr/net/socketcan.h](https://docs.zephyrproject.org/latest/doxygen/html/socketcan_8h_source.html)
- [socketcan_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga35a7941726d1e22defd8c3098391ca8e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P056_socketcan_filter_结构体.md) · [返回大纲](大纲.md) · [下一章](P058_ssh_channel_event_结构体.md)
