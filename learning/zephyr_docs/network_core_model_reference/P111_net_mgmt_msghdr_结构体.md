---
id: learning.zephyr-docs.network-core-model-reference.page-111
title: net_mgmt_msghdr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__mgmt__msghdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第111章\_net\_mgmt\_msghdr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__mgmt__msghdr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

每条网络管理消息（Network Management Message）都以前置的此头部开始。

```c
#include <zephyr/net/socket_net_mgmt.h>
```

<a id="details"></a>

每条网络管理消息（Network Management Message）都以前置的此头部开始。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 111.1\_数据成员（Data Fields）

<a id="r_a6867379b1ab13c504ee9884cc386c05e"></a>

```c
uint32_t nm_msg_version
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[nm_msg_version](#a6867379b1ab13c504ee9884cc386c05e)。

网络管理版本（Network management version）。

<a id="r_ad7f4caefa6b3d8d93a480cd8210d7a4d"></a>

```c
uint32_t nm_msg_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[nm_msg_len](#ad7f4caefa6b3d8d93a480cd8210d7a4d)。

数据长度（Data Length）。

<a id="r_a09e1bc6f985b8fcc3397aa447b1d8e94"></a>

```c
uint8_t nm_msg []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nm_msg](#a09e1bc6f985b8fcc3397aa447b1d8e94)。

后面紧跟实际的消息数据（Message data）。

## 111.2\_详细说明（Detailed Documentation）

<a id="a09e1bc6f985b8fcc3397aa447b1d8e94"></a>

### `nm_msg`

```c
uint8_t net_mgmt_msghdr::nm_msg[]
```

后面紧跟实际的消息数据（Message data）。

<a id="ad7f4caefa6b3d8d93a480cd8210d7a4d"></a>

### `nm_msg_len`

```c
uint32_t net_mgmt_msghdr::nm_msg_len
```

数据长度（Data Length）。

<a id="a6867379b1ab13c504ee9884cc386c05e"></a>

### `nm_msg_version`

```c
uint32_t net_mgmt_msghdr::nm_msg_version
```

网络管理版本（Network management version）。

本数据类型文档由以下文件生成：

- `zephyr/net/socket_net_mgmt.h`

## 111.3\_原页交叉引用（Cross References）

- [zephyr/net/socket_net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/socket__net__mgmt_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P110_net_mgmt_event_callback_结构体.md) · [返回大纲](大纲.md) · [下一章](P112_net_msghdr_结构体.md)
