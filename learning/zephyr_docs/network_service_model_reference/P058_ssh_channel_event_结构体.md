---
id: learning.zephyr-docs.network-service-model-reference.page-58
title: ssh_channel_event_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structssh__channel__event.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_ssh\_channel\_event\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structssh__channel__event.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SSH通道事件信息（Channel Event Information）。

```c
#include <zephyr/net/ssh/common.h>
```

<a id="details"></a>

SSH通道事件信息（Channel Event Information）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 58.1\_数据成员（Data Fields）

<a id="r_a3d6ac4601d29b26a437866f5c58360c8"></a>

```c
enum ssh_channel_event_type type
```

相关声明：[ssh_channel_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaba3db037a1fbeca22f2c3c30063788b9)、[type](#a3d6ac4601d29b26a437866f5c58360c8)。

安全外壳（SSH）通道所发出的事件类型。

```c
union {
```

<a id="r_a0a0ece343f98999d92c2467ac1216c18"></a>

```c
struct ssh_channel_event_channel_request channel_request
```

相关声明：[ssh_channel_event_channel_request](P059_ssh_channel_event_channel_request_结构体.md)、[channel_request](#ac66cc9b82e394c6b51c4e54620351f1b)。

`SSH_CHANNEL_EVENT_REQUEST` 的数据。

<a id="r_ac196f9b84638e638f6e33adcabae16dd"></a>

```c
struct ssh_channel_event_channel_request_result channel_request_result
```

相关声明：[ssh_channel_event_channel_request_result](P060_ssh_channel_event_channel_request_result_结构体.md)、[channel_request_result](#a5177c6f41210417205ceaab1c366390b)。

`SSH_CHANNEL_EVENT_REQUEST_RESULT` 的数据。

<a id="r_af8c3bf95fd8781868128e1c8e9ae2ee1"></a>

```c
};
```

通道事件载荷数据。

## 58.2\_详细说明（Detailed Documentation）

<a id="af8c3bf95fd8781868128e1c8e9ae2ee1"></a>

### `[union]`

```c
union { ... } ssh_channel_event
```

通道事件载荷数据。

<a id="ac66cc9b82e394c6b51c4e54620351f1b"></a>

### `channel_request`

```c
struct ssh_channel_event_channel_request ssh_channel_event::channel_request
```

`SSH_CHANNEL_EVENT_REQUEST` 的数据。

<a id="a5177c6f41210417205ceaab1c366390b"></a>

### `channel_request_result`

```c
struct ssh_channel_event_channel_request_result ssh_channel_event::channel_request_result
```

`SSH_CHANNEL_EVENT_REQUEST_RESULT` 的数据。

<a id="a3d6ac4601d29b26a437866f5c58360c8"></a>

### `type`

```c
enum ssh_channel_event_type ssh_channel_event::type
```

安全外壳（SSH）通道所发出的事件类型。

本数据类型文档由以下文件生成：

- `zephyr/net/ssh/common.h`

## 58.3\_原页交叉引用（Cross References）

- [zephyr/net/ssh/common.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2net_2ssh_2common_8h_source.html)
- [ssh_channel_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__common.html#gaba3db037a1fbeca22f2c3c30063788b9)
- [ssh_channel_event_channel_request](P059_ssh_channel_event_channel_request_结构体.md)
- [ssh_channel_event_channel_request_result](P060_ssh_channel_event_channel_request_result_结构体.md)
- [ssh_channel_event](P058_ssh_channel_event_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P057_socketcan_frame_结构体.md) · [返回大纲](大纲.md) · [下一章](P059_ssh_channel_event_channel_request_结构体.md)
