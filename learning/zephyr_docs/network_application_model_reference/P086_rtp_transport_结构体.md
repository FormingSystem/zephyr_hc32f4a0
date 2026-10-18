---
id: learning.zephyr-docs.network-application-model-reference.page-86
title: rtp_transport_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrtp__transport.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第86章\_rtp\_transport\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrtp__transport.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

嵌入rtp_session的内部传输状态（Internal Transport State）。

```c
#include <zephyr/net/rtp.h>
```

<a id="details"></a>

嵌入rtp_session的内部传输状态（Internal Transport State）。保存活动传输类型，以及发送和接收数据包所需的全部传输专用句柄。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 86.1\_数据成员（Data Fields）

<a id="r_a39a4570191bec0e16660aa666701aff4"></a>

```c
enum rtp_transport_type type
```

相关声明：[rtp_transport_type](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga15d59475e540b1ddd310005700f52701)、[type](#a39a4570191bec0e16660aa666701aff4)。

此会话的活动传输后端（Transport Backend）。

```c
union {
```

<a id="r_aca8d7549ac1be94821dc62479fe63f00"></a>

```c
};
```

保存传输相关数据（Transport Related Data）的联合体。

## 86.2\_详细说明（Detailed Documentation）

<a id="aca8d7549ac1be94821dc62479fe63f00"></a>

### `[union]`

```c
union { ... } rtp_transport
```

保存传输相关数据（Transport Related Data）的联合体。

<a id="a39a4570191bec0e16660aa666701aff4"></a>

### `type`

```c
enum rtp_transport_type rtp_transport::type
```

此会话的活动传输后端（Transport Backend）。

本数据类型文档由以下文件生成：

- `zephyr/net/rtp.h`

## 86.3\_原页交叉引用（Cross References）

- [rtp_session](P084_rtp_session_结构体.md)
- [zephyr/net/rtp.h](https://docs.zephyrproject.org/latest/doxygen/html/rtp_8h_source.html)
- [rtp_transport_type](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga15d59475e540b1ddd310005700f52701)
- [rtp_transport](P086_rtp_transport_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P085_rtp_session_context_结构体.md) · [返回大纲](大纲.md) · [下一章](P087_sntp_ctx_结构体.md)
