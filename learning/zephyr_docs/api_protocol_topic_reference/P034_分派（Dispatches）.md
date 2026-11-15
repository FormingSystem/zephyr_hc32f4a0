---
id: learning.zephyr-docs.api-protocol-topic-reference.page-34
title: 分派（Dispatches）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_分派（Dispatches）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

元素（Elements）之间交换的查询和事件。

<a id="details"></a>

元素（elements）之间交换的查询和事件。当元素通过连接端（pad）链路向对端发送的内容不是数据时，传递的是分派对象（dispatch）。它有两种用途：传给 `mpipe_pad_query()` 的查询（query），由对端就地填写答案，发起方随后从同一分派对象中读出；或者传给 `mpipe_pad_send_event()` 的事件（event），作为单向通知，由对端处理并转发。两者共用一个固定大小的结构体，因为协商（negotiation）过程不得进行内存分配。分派对象也不同于消息（Messages）：消息沿总线向上传递给应用程序，而分派对象沿连接端链路在两个元素之间传递。结构体自身不标明它是查询还是事件；类型字段说明分派对象的主题，接收它的函数决定它是在询问还是在通知。

| 类型（Type） | 用作查询（As a query） | 用作事件（As an event） |
| --- | --- | --- |
| `CAPS` | 在给定此筛选条件时，你接受什么？ | 使用此格式，请应用它。 |
| `BUFFER_POOL` | 你需要什么缓冲区？ | — |
| `EOS` | — | 数据流已结束。 |

<a id="header-files"></a>
<a id="files"></a>

## 34.1\_文件（Files）

<a id="r_mpipe_5Fdispatch_2Eh"></a>

```c
file mpipe_dispatch.h
```

相关声明：[mpipe_dispatch.h](../api_file_supplement_reference/P073_zephyr__mpipe__mpipe_dispatch.h_文件参考.md)。

元素（Elements）之间交换的查询和事件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 34.2\_数据结构（Data Structures）

<a id="r_mpipe_5Fdispatch"></a>

```c
struct mpipe_dispatch
```

相关声明：[mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)。

沿端口连接（Pad Link）传递的查询或事件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 34.3\_枚举（Enumerations）

<a id="r_gae32e15ab045bc017100a7e713c3999b1"></a>

```c
enum mpipe_dispatch_type { MPIPE_DISPATCH_UNKNOWN = 0 , MPIPE_DISPATCH_EOS , MPIPE_DISPATCH_CAPS , MPIPE_DISPATCH_BUFFER_POOL , MPIPE_DISPATCH_END = UINT8_MAX }
```

相关声明：[mpipe_dispatch_type](#gae32e15ab045bc017100a7e713c3999b1)、[MPIPE_DISPATCH_UNKNOWN](#ggae32e15ab045bc017100a7e713c3999b1a8c9d64cd72d6864da7f03786906fe08d)、[MPIPE_DISPATCH_EOS](#ggae32e15ab045bc017100a7e713c3999b1a729237cee6bba4d22ce3035bd01c82ed)、[MPIPE_DISPATCH_CAPS](#ggae32e15ab045bc017100a7e713c3999b1a63a565f281055915f13e3ec202fe177d)、[MPIPE_DISPATCH_BUFFER_POOL](#ggae32e15ab045bc017100a7e713c3999b1a9db1cfed44ee98fa15d75e3916a26fd3)、[MPIPE_DISPATCH_END](#ggae32e15ab045bc017100a7e713c3999b1a6e9d033347db915fffd909f373e4095a)。

支持的分派类型（Dispatch Types）。

## 34.4\_详细说明（Detailed Documentation）

<a id="gae32e15ab045bc017100a7e713c3999b1"></a>

### `mpipe_dispatch_type`

```c
enum mpipe_dispatch_type
```

```c
#include <zephyr/mpipe/mpipe_dispatch.h>
```

支持的分派类型（Dispatch Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_DISPATCH_UNKNOWN` | 未初始化的分派对象（uninitialized dispatch）。 |
| `MPIPE_DISPATCH_EOS` | 流结束（End of Stream，EOS），属于事件。 |
| `MPIPE_DISPATCH_CAPS` | 能力（capability），可用作查询或事件。 |
| `MPIPE_DISPATCH_BUFFER_POOL` | 缓冲池（buffer pool），属于查询。 |
| `MPIPE_DISPATCH_END` | 分派类型标识符（dispatch type identifier）的最大值。 |


## 34.5\_原页交叉引用（Cross References）

- [mpipe_dispatch.h](../api_file_supplement_reference/P073_zephyr__mpipe__mpipe_dispatch.h_文件参考.md)
- [mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)
- [mpipe_pad_query()](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga35b334800669dbe25a46c71d75afd775)
- [mpipe_pad_send_event()](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga867dff16bf63d21cab505f2b1f282ebc)
- [消息（Messages）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggae32e15ab045bc017100a7e713c3999b1a8c9d64cd72d6864da7f03786906fe08d"></a>
<a id="ggae32e15ab045bc017100a7e713c3999b1a729237cee6bba4d22ce3035bd01c82ed"></a>
<a id="ggae32e15ab045bc017100a7e713c3999b1a63a565f281055915f13e3ec202fe177d"></a>
<a id="ggae32e15ab045bc017100a7e713c3999b1a9db1cfed44ee98fa15d75e3916a26fd3"></a>
<a id="ggae32e15ab045bc017100a7e713c3999b1a6e9d033347db915fffd909f373e4095a"></a>

---

[上一章](P033_蜂窝调制解调器辅助功能（Cellular modem helpers）.md) · [返回大纲](大纲.md) · [下一章](P035_解析器（Parsers）.md)
