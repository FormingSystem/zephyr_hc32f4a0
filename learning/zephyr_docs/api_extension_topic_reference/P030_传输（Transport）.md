---
id: learning.zephyr-docs.api-extension-topic-reference.page-30
title: 传输（Transport）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__transport.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_传输（Transport）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__transport.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SCMI 传输层的抽象与定义。

<a id="details"></a>

SCMI 传输层的抽象与定义。

<a id="header-groups"></a>
<a id="groups"></a>

## 30.1\_主题（Topics）

<a id="r_scmi_5Fshmem"></a>

相关声明：[共享内存（Shared Memory）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html)。

SCMI 的共享内存传输定义。

<a id="header-files"></a>
<a id="files"></a>

## 30.2\_文件（Files）

<a id="r_transport_2Eh"></a>

```c
file transport.h
```

相关声明：[transport.h](../api_file_supplement_reference/P123_zephyr__drivers__firmware__scmi__transport.h_文件参考.md)。

系统控制与管理接口（SCMI）传输层（Transport Layer）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 30.3\_数据结构（Data Structures）

<a id="r_scmi_5Fchannel"></a>

```c
struct scmi_channel
```

相关声明：[scmi_channel](../platform_security_model_reference/P033_scmi_channel_结构体.md)。

系统控制与管理接口（SCMI）的通道结构。

<a id="r_scmi_5Ftransport_5Fapi"></a>

```c
struct scmi_transport_api
```

相关声明：[scmi_transport_api](../platform_security_model_reference/P052_scmi_transport_api_结构体.md)。

系统控制与管理接口（SCMI）的传输驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 30.4\_类型定义（Typedefs）

<a id="r_ga4c6cccb4e76fef22ec9f3527a96a8de5"></a>

```c
typedef void(* scmi_channel_cb) (struct scmi_channel *chan, uint32_t hdr)
```

相关声明：[scmi_channel_cb](#ga4c6cccb4e76fef22ec9f3527a96a8de5)、[scmi_channel](../platform_security_model_reference/P033_scmi_channel_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

用于消息回复（Message Replies）的回调函数（Callback Function）。

## 30.5\_详细说明（Detailed Documentation）

<a id="ga4c6cccb4e76fef22ec9f3527a96a8de5"></a>

### `scmi_channel_cb`

```c
typedef void(* scmi_channel_cb) (struct scmi_channel *chan, uint32_t hdr)
```

```c
#include <zephyr/drivers/firmware/scmi/transport.h>
```

用于消息回复（Message Replies）的回调函数（Callback Function）。

传输层驱动（Transport Layer Driver）每次收到对先前已发送消息的回复（Reply）时，都应调用本函数。它用于通知系统控制和管理接口核心（SCMI Core）回复已到达，以便执行适当操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 指向收到回复的系统控制和管理接口通道（SCMI Channel）的指针。 |
| `hdr` | 共享内存消息头（Shared Memory Message Header）。 |


## 30.6\_原页交叉引用（Cross References）

- [共享内存（Shared Memory）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html)
- [transport.h](../api_file_supplement_reference/P123_zephyr__drivers__firmware__scmi__transport.h_文件参考.md)
- [scmi_channel](../platform_security_model_reference/P033_scmi_channel_结构体.md)
- [scmi_transport_api](../platform_security_model_reference/P052_scmi_transport_api_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P029_S9706 API主题.md) · [返回大纲](大纲.md) · [下一章](P031_MCUX 增强型正交解码器（EQDC MCUX）.md)
