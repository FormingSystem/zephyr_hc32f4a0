---
id: learning.zephyr-docs.api-usb-gnss-topic-reference.page-12
title: 连接端口（Pad）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_连接端口（Pad）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

两个元素相连接的位置。

<a id="details"></a>

两个元素（Element）的连接点。端口（Pad）是元素的输入或输出连接器（Connector），具有方向：源端口（Source Pad，`MPIPE_PAD_SRC`）发出数据，接收端口（Sink Pad，`MPIPE_PAD_SINK`）接收数据；`mpipe_pad_link` 将两者各一个连接起来。连接通过两侧的 `peer` 指针记录，这对指针构成每个缓冲区、事件和查询经过的路径。端口还按值保存一个已确定的能力结构体（Capability Structure）。协商（Negotiation）完成之前，它不施加任何限制；调用 `mpipe_pad_set_caps` 并传入 `NULL` 会恢复这种状态，这也是从 `PAUSED` 转换到 `READY` 时执行的操作。

缓冲区、事件与查询（Buffers, Events and Queries）：连接上传递三类信息，各自具有对应的钩子（Hook）：

- 缓冲区到达接收端口的 `process_fn`。处理函数拥有传入的缓冲区，即使处理失败，也必须释放它；无论成功还是失败，调用者都不再访问该缓冲区。
- 事件（Event）用于通告某件事，通过 `mpipe_pad_send_event` 发送，例如要应用的格式或流结束。默认处理程序穿过元素，将事件转发到另一侧端口的对端。
- 查询（Query）用于提出问题，通过 `mpipe_pad_query` 发送。答案写入查询发起方拥有的存储空间，因此查询不进行任何内存分配。

事件和查询均由分派对象（Dispatches）承载。决定分派是询问还是通告的是接收它的函数，而不是分派对象本身的内容。

枚举能力（Enumerating Capabilities）：支持多种格式的元素不会用一个包含列表的能力对象描述它们；由于不进行内存分配，这里没有列表类型。元素按索引分别响应 `enum_caps_fn`，每次产生一个能力对象，协商过程遍历这些索引。驱动遍历过程的三种返回结果参见 `mpipe_pad_enum_caps`。

存在方式（Presence）：端口记录其预期存在时机。`MPIPE_PAD_ALWAYS` 表示元素构建后即存在；`MPIPE_PAD_SOMETIMES` 表示随媒体流出现或消失；`MPIPE_PAD_REQUEST` 表示仅在收到请求后存在。目前仅实现 `MPIPE_PAD_ALWAYS`：该字段会被存储，但尚无逻辑据此执行操作，因此应将另外两种取值视为保留值。

<a id="header-files"></a>
<a id="files"></a>

## 12.1\_文件（Files）

<a id="r_mpipe_5Fpad_2Eh"></a>

```c
file mpipe_pad.h
```

相关声明：[mpipe_pad.h](../api_file_protocol_service_reference/P026_zephyr__mpipe__mpipe_pad.h_文件参考.md)。

端口（Pad）：两个元素连接的位置。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.2\_数据结构（Data Structures）

<a id="r_mpipe_5Fpad"></a>

```c
struct mpipe_pad
```

相关声明：[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)。

端口（Pad）结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.3\_枚举（Enumerations）

<a id="r_ga9de49691e139241133f231188671d4f2"></a>

```c
enum mpipe_pad_direction { MPIPE_PAD_UNKNOWN , MPIPE_PAD_SRC , MPIPE_PAD_SINK }
```

相关声明：[mpipe_pad_direction](#ga9de49691e139241133f231188671d4f2)、[MPIPE_PAD_UNKNOWN](#gga9de49691e139241133f231188671d4f2ac78e4d56c5e4ef0c2fb540b96e768485)、[MPIPE_PAD_SRC](#gga9de49691e139241133f231188671d4f2a2bec7e8ba42eb1bd310f64ac8b226eb1)、[MPIPE_PAD_SINK](#gga9de49691e139241133f231188671d4f2a968c6b4c1354249e3c2edb90c2a9c6a4)。

衬垫方向（Pad Direction）。

<a id="r_ga6103c9bbb48a5b03a3805a561c19b9f5"></a>

```c
enum mpipe_pad_mode { MPIPE_PAD_MODE_NONE , MPIPE_PAD_MODE_PUSH , MPIPE_PAD_MODE_PULL }
```

相关声明：[mpipe_pad_mode](#ga6103c9bbb48a5b03a3805a561c19b9f5)、[MPIPE_PAD_MODE_NONE](#gga6103c9bbb48a5b03a3805a561c19b9f5ab733479f2e0ee43179b7c8f4a8e6fdbe)、[MPIPE_PAD_MODE_PUSH](#gga6103c9bbb48a5b03a3805a561c19b9f5a66654014110056bdf7bf072ee47f6e24)、[MPIPE_PAD_MODE_PULL](#gga6103c9bbb48a5b03a3805a561c19b9f5a9c3c348be8f4820abc7290a6f3c2680b)。

衬垫运行模式（Pad Operating Mode）。

<a id="r_gae260b9597d59469fdd89cc9604d33646"></a>

```c
enum mpipe_pad_presence { MPIPE_PAD_ALWAYS , MPIPE_PAD_SOMETIMES , MPIPE_PAD_REQUEST }
```

相关声明：[mpipe_pad_presence](#gae260b9597d59469fdd89cc9604d33646)、[MPIPE_PAD_ALWAYS](#ggae260b9597d59469fdd89cc9604d33646a94500ceecec6513ffec8589740432eb1)、[MPIPE_PAD_SOMETIMES](#ggae260b9597d59469fdd89cc9604d33646a9c1618c29a6b702aa7f88cb45f66b8e3)、[MPIPE_PAD_REQUEST](#ggae260b9597d59469fdd89cc9604d33646ae1d7881588a59e12a13b68465f31ebdb)。

衬垫的存在性（Pad Presence）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.4\_函数（Functions）

<a id="r_ga6b05aca1580f37d8b65d8534b5ab9fa3"></a>

```c
int mpipe_pad_enum_caps (struct mpipe_pad *pad, uint32_t index, const struct mpipe_structure *filter, struct mpipe_structure *out)
```

相关声明：[mpipe_pad_enum_caps](#ga6b05aca1580f37d8b65d8534b5ab9fa3)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

生成衬垫（Pad）支持的一项能力（Capability）。

<a id="r_ga6d217c7c0cf12e1f309839ccd3b30eb7"></a>

```c
int mpipe_pad_enum_first (struct mpipe_pad *pad, const struct mpipe_structure *filter, struct mpipe_structure *out)
```

相关声明：[mpipe_pad_enum_first](#ga6d217c7c0cf12e1f309839ccd3b30eb7)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

生成衬垫支持且被过滤器（Filter）接受的第一项能力（Capability）。

<a id="r_ga28ede4a47055d4a98aac21a15973714b"></a>

```c
int mpipe_pad_answer_caps_query (struct mpipe_pad *pad, struct mpipe_dispatch *query)
```

相关声明：[mpipe_pad_answer_caps_query](#ga28ede4a47055d4a98aac21a15973714b)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)。

使用过滤器（Filter）接受的第一项能力回答能力查询（Caps Query）。

<a id="r_ga3a02138067490e72f3b36d3cfb3639bb"></a>

```c
int mpipe_pad_enum_filter (const struct mpipe_structure *candidate, const struct mpipe_structure *filter, struct mpipe_structure *out)
```

相关声明：[mpipe_pad_enum_filter](#ga3a02138067490e72f3b36d3cfb3639bb)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

通过枚举过滤器（Enumeration Filter）收窄一项已枚举能力（Enumerated Capability）。

<a id="r_ga6daef8b8fb359e5a8edada810d5136bc"></a>

```c
void mpipe_pad_init (struct mpipe_pad *pad, uint8_t id, enum mpipe_pad_direction direction, enum mpipe_pad_presence presence)
```

相关声明：[mpipe_pad_init](#ga6daef8b8fb359e5a8edada810d5136bc)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mpipe_pad_direction](#ga9de49691e139241133f231188671d4f2)、[mpipe_pad_presence](#gae260b9597d59469fdd89cc9604d33646)。

初始化衬垫（Pad）。

<a id="r_ga1249052f4192c3cc5c052c59fc120a82"></a>

```c
int mpipe_pad_set_caps (struct mpipe_pad *pad, const struct mpipe_structure *caps)
```

相关声明：[mpipe_pad_set_caps](#ga1249052f4192c3cc5c052c59fc120a82)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)。

设置衬垫能力（Pad Capability）。

<a id="r_gaf1210118ce75177f5950074acb5bfd4f"></a>

```c
void mpipe_pad_link (struct mpipe_pad *src_pad, struct mpipe_pad *sink_pad)
```

相关声明：[mpipe_pad_link](#gaf1210118ce75177f5950074acb5bfd4f)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)。

连接两个衬垫（Link Pads）。

<a id="r_ga867dff16bf63d21cab505f2b1f282ebc"></a>

```c
int mpipe_pad_send_event (struct mpipe_pad *pad, struct mpipe_dispatch *event)
```

相关声明：[mpipe_pad_send_event](#ga867dff16bf63d21cab505f2b1f282ebc)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)。

向衬垫（Pad）发送事件（Event）。

<a id="r_ga1bc13e3d72c8daed41344d727766e830"></a>

```c
int mpipe_pad_send_event_default (struct mpipe_pad *pad, struct mpipe_dispatch *event)
```

相关声明：[mpipe_pad_send_event_default](#ga1bc13e3d72c8daed41344d727766e830)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)。

衬垫（Pad）的默认事件处理程序（Default Event Handler）。

<a id="r_ga35b334800669dbe25a46c71d75afd775"></a>

```c
int mpipe_pad_query (struct mpipe_pad *pad, struct mpipe_dispatch *query)
```

相关声明：[mpipe_pad_query](#ga35b334800669dbe25a46c71d75afd775)、[mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)、[mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)。

向衬垫（Pad）发送查询（Query）。

## 12.5\_详细说明（Detailed Documentation）

<a id="ga9de49691e139241133f231188671d4f2"></a>

### `mpipe_pad_direction`

```c
enum mpipe_pad_direction
```

```c
#include <zephyr/mpipe/mpipe_pad.h>
```

衬垫方向（Pad Direction）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_PAD_UNKNOWN` | 方向未知（Unknown Direction）。 |
| `MPIPE_PAD_SRC` | 该端口为源端口（Source Pad）。 |
| `MPIPE_PAD_SINK` | 该端口为接收端口（Sink Pad）。 |

<a id="ga6103c9bbb48a5b03a3805a561c19b9f5"></a>

### `mpipe_pad_mode`

```c
enum mpipe_pad_mode
```

```c
#include <zephyr/mpipe/mpipe_pad.h>
```

衬垫运行模式（Pad Operating Mode）。

定义端口（Pad）采用推送模式（Push Mode）、拉取模式（Pull Mode），还是两者都不采用。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_PAD_MODE_NONE` | 端口（Pad）不处理数据流（Dataflow）。 |
| `MPIPE_PAD_MODE_PUSH` | 端口（Pad）以推送模式（Push Mode）处理数据流。 |
| `MPIPE_PAD_MODE_PULL` | 端口（Pad）以拉取模式（Pull Mode）处理数据流。 |

<a id="gae260b9597d59469fdd89cc9604d33646"></a>

### `mpipe_pad_presence`

```c
enum mpipe_pad_presence
```

```c
#include <zephyr/mpipe/mpipe_pad.h>
```

衬垫的存在性（Pad Presence）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_PAD_ALWAYS` | 端口始终存在（Always Present）。 |
| `MPIPE_PAD_SOMETIMES` | 端口是否存在取决于媒体流（Media Stream）。 |
| `MPIPE_PAD_REQUEST` | 端口仅在请求时可用（Available on Request）。 |

<a id="ga28ede4a47055d4a98aac21a15973714b"></a>

### `mpipe_pad_answer_caps_query()`

```c
int mpipe_pad_answer_caps_query ( struct mpipe_pad * pad, struct mpipe_dispatch * query )
```

```c
#include <zephyr/mpipe/mpipe_pad.h>
```

使用过滤器（Filter）接受的第一项能力回答能力查询（Caps Query）。

枚举端口（Pad），并将协商会确定的能力（Capability）写回 `query`。无须进行转换的元素，即源（Source）或接收端（Sink），将本函数安装为其查询处理程序（Query Handler）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pad` | 要枚举的连接点。 |
| `query` | 要回答的能力查询（Caps Query），输入时携带过滤器（Filter）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENODATA` | 端口没有任何可被过滤器（Filter）接受的能力（Capability）。 |

**返回（Returns）**：返回值（Returns）：成功返回 0，其他失败返回负 errno。

<a id="ga6b05aca1580f37d8b65d8534b5ab9fa3"></a>

### `mpipe_pad_enum_caps()`

```c
int mpipe_pad_enum_caps ( struct mpipe_pad * pad, uint32_t index, const struct mpipe_structure * filter, struct mpipe_structure * out )
```

```c
#include <zephyr/mpipe/mpipe_pad.h>
```

生成衬垫（Pad）支持的一项能力（Capability）。

调用端口的 `enum_caps_fn`，并在索引超过 `UINT16_MAX` 后停止查询，使从不报告结束的实现以失败结束，而不是无限挂起。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` pad` | 要枚举的连接点。 |
| ` index` | 从 0 开始的能力索引。 |
| ` filter` | 可选结构体，用于缩小能力范围（Narrow the Capability），可为 `NULL`。 |
| `[out] out` | 调用方提供的用于存放能力的存储空间。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EAGAIN` | 此索引无法满足 `filter`。 |
| `-ENOENT` | 已越过最后一项能力。 |
| `-EINVAL` | 端口未提供 `enum_caps_fn`。 |

<a id="ga3a02138067490e72f3b36d3cfb3639bb"></a>

### `mpipe_pad_enum_filter()`

```c
int mpipe_pad_enum_filter ( const struct mpipe_structure * candidate, const struct mpipe_structure * filter, struct mpipe_structure * out )
```

```c
#include <zephyr/mpipe/mpipe_pad.h>
```

通过枚举过滤器（Enumeration Filter）收窄一项已枚举能力（Enumerated Capability）。

每个端口（Pad）的 `enum_caps_fn` 共用的收尾操作（Epilogue）：没有过滤器时返回 `candidate`；否则缩小其范围，并在本索引无法满足过滤器时报告这一结果，让调用者继续下一个索引。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` candidate` | 指向本索引产生的能力（Capability）的指针。 |
| ` filter` | 用于收窄结果的能力条件，可以为 `NULL`。 |
| `[out] out` | 指向结果存储空间（Result Storage）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EAGAIN` | `candidate` 无法满足 `filter`。 |

<a id="ga6d217c7c0cf12e1f309839ccd3b30eb7"></a>

### `mpipe_pad_enum_first()`

```c
int mpipe_pad_enum_first ( struct mpipe_pad * pad, const struct mpipe_structure * filter, struct mpipe_structure * out )
```

```c
#include <zephyr/mpipe/mpipe_pad.h>
```

生成衬垫支持且被过滤器（Filter）接受的第一项能力（Capability）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` pad` | 要枚举的连接点。 |
| ` filter` | 用于缩小范围的能力（Capability），可为 `NULL` 或 `ANY`。 |
| `[out] out` | 调用方提供的用于存放能力的存储空间。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENODATA` | 没有任何能力（Capability）被接受。 |

**返回（Returns）**：返回值（Returns）：端口的 `enum_caps_fn` 返回的其他任意负 `errno`。

<a id="ga6daef8b8fb359e5a8edada810d5136bc"></a>

### `mpipe_pad_init()`

```c
void mpipe_pad_init ( struct mpipe_pad * pad, uint8_t id, enum mpipe_pad_direction direction, enum mpipe_pad_presence presence )
```

```c
#include <zephyr/mpipe/mpipe_pad.h>
```

初始化衬垫（Pad）。

使用指定参数初始化已有端口结构体（Pad Structure）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pad` | 指向待初始化端口（Pad）的指针。 |
| `id` | 端口实例在元素内的唯一标识符（Unique ID）。 |
| `direction` | 连接点方向，类型为 `mpipe_pad_direction`。 |
| `presence` | 端口的存在方式（Presence）。 |

<a id="gaf1210118ce75177f5950074acb5bfd4f"></a>

### `mpipe_pad_link()`

```c
void mpipe_pad_link ( struct mpipe_pad * src_pad, struct mpipe_pad * sink_pad )
```

```c
#include <zephyr/mpipe/mpipe_pad.h>
```

连接两个衬垫（Link Pads）。

将源端口（Source Pad）连接到接收端口（Sink Pad），建立数据流连接。两个端口的 `peer` 指针互相指向对方。任一端口都不得为 `NULL`，这是断言（Assertion）要求，而不是返回错误的情形。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src_pad` | 要连接的源端口（Source Pad）。 |
| `sink_pad` | 要连接的接收端口（Sink Pad）。 |

<a id="ga35b334800669dbe25a46c71d75afd775"></a>

### `mpipe_pad_query()`

```c
int mpipe_pad_query ( struct mpipe_pad * pad, struct mpipe_dispatch * query )
```

```c
#include <zephyr/mpipe/mpipe_pad.h>
```

向衬垫（Pad）发送查询（Query）。

使用端口的查询函数（Query Function），向该端口发送查询（Query）。

能力查询（Caps Query）的答案写入其携带的存储空间，因此未携带存储空间的查询会在调用端口查询函数之前被拒绝。这样查询函数便可直接解引用 `mpipe_dispatch::caps`，无须检查。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pad` | 指向查询目标端口（Pad）的指针，不得为 `NULL`。 |
| `query` | 指向要发送的分派对象（Dispatches）的指针，不得为 `NULL`。能力查询（Caps Query）必须携带用于写入答案的能力存储空间（Capability Storage）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 能力查询（Caps Query）未携带用于写入答案的能力存储空间（Capability Storage）。 |
| `-ENOTSUP` | 端口没有查询函数（Query Function）。 |
| `-ENODATA` | 能力查询（Caps Query）返回了空能力（Empty Capability）。 |

**返回（Returns）**：返回值（Returns）：端口查询函数（Query Function）返回的任意负 `errno`。

<a id="ga867dff16bf63d21cab505f2b1f282ebc"></a>

### `mpipe_pad_send_event()`

```c
int mpipe_pad_send_event ( struct mpipe_pad * pad, struct mpipe_dispatch * event )
```

```c
#include <zephyr/mpipe/mpipe_pad.h>
```

向衬垫（Pad）发送事件（Event）。

使用指定端口的事件函数（Event Function），向该端口发送事件（Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pad` | 指向事件目标端口（Pad）的指针。 |
| `event` | 指向要发送的分派对象（Dispatches）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOTSUP` | 端口没有事件函数（Event Function）。 |

**返回（Returns）**：返回值（Returns）：端口事件函数（Event Function）返回的任意负 `errno`。

<a id="ga1bc13e3d72c8daed41344d727766e830"></a>

### `mpipe_pad_send_event_default()`

```c
int mpipe_pad_send_event_default ( struct mpipe_pad * pad, struct mpipe_dispatch * event )
```

```c
#include <zephyr/mpipe/mpipe_pad.h>
```

衬垫（Pad）的默认事件处理程序（Default Event Handler）。

将 `pad` 收到的事件（Event）转发给同一元素中所有另一侧端口的对端（Peer）。若 `pad` 为接收端口（Sink Pad），则转发给每个源端口（Source Pad）的对端；若 `pad` 为源端口，则转发给每个接收端口的对端。

如果元素只有源端口（Source Pad）或只有接收端口（Sink Pad），便没有可供发送事件的另一侧端口，因此函数返回 `-ENOTSUP`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pad` | 指向收到事件的端口（Pad）的指针。 |
| `event` | 指向要发送的分派对象（Dispatches）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 事件（Event）至少到达了一个对端（Peer）。 |
| `-ENOTSUP` | 另一侧端口均没有对端（Peer），或者所有对端都拒绝了该事件。对端自身的错误会被记录，但不会向上传播。 |

<a id="ga1249052f4192c3cc5c052c59fc120a82"></a>

### `mpipe_pad_set_caps()`

```c
int mpipe_pad_set_caps ( struct mpipe_pad * pad, const struct mpipe_structure * caps )
```

```c
#include <zephyr/mpipe/mpipe_pad.h>
```

设置衬垫能力（Pad Capability）。

将 `caps` 复制到端口（Pad）。传入 `NULL` 会将端口重置为不施加任何限制，这是重新协商（Re-negotiation）的起始状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pad` | 要设置能力（Capability）的端口（Pad）。 |
| `caps` | 要复制进去的能力（Capability）；传入 `NULL` 可重置为 `ANY`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |


## 12.6\_原页交叉引用（Cross References）

- [mpipe_pad.h](../api_file_protocol_service_reference/P026_zephyr__mpipe__mpipe_pad.h_文件参考.md)
- [mpipe_pad](../audio_video_model_reference/P025_mpipe_pad_结构体.md)
- [连接端口（Pad）](P012_连接端口（Pad）.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [mpipe_structure](../audio_video_model_reference/P031_mpipe_structure_结构体.md)
- [mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [能力结构（Capability Structure）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html)
- [分派（Dispatches）](../api_protocol_topic_reference/P034_分派（Dispatches）.md)
- [mpipe_dispatch::caps](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md#ad0f5202097b4ea9819acd8545f749f2c)

<a id="header-details"></a>
<a id="mpipe_pad_traffic"></a>
<a id="mpipe_pad_enum"></a>
<a id="mpipe_pad_presence"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga9de49691e139241133f231188671d4f2ac78e4d56c5e4ef0c2fb540b96e768485"></a>
<a id="gga9de49691e139241133f231188671d4f2a2bec7e8ba42eb1bd310f64ac8b226eb1"></a>
<a id="gga9de49691e139241133f231188671d4f2a968c6b4c1354249e3c2edb90c2a9c6a4"></a>
<a id="gga6103c9bbb48a5b03a3805a561c19b9f5ab733479f2e0ee43179b7c8f4a8e6fdbe"></a>
<a id="gga6103c9bbb48a5b03a3805a561c19b9f5a66654014110056bdf7bf072ee47f6e24"></a>
<a id="gga6103c9bbb48a5b03a3805a561c19b9f5a9c3c348be8f4820abc7290a6f3c2680b"></a>
<a id="ggae260b9597d59469fdd89cc9604d33646a94500ceecec6513ffec8589740432eb1"></a>
<a id="ggae260b9597d59469fdd89cc9604d33646a9c1618c29a6b702aa7f88cb45f66b8e3"></a>
<a id="ggae260b9597d59469fdd89cc9604d33646ae1d7881588a59e12a13b68465f31ebdb"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P011_管理（Management）.md) · [返回大纲](大纲.md) · [下一章](P013_TMAG5273 API主题.md)
