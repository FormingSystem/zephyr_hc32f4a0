---
id: learning.zephyr-docs.audio-video-model-reference.page-25
title: mpipe_pad_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__pad.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_mpipe\_pad\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__pad.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

端口（Pad）结构。

```c
#include <zephyr/mpipe/mpipe_pad.h>
```

<a id="details"></a>

连接点（Pad）结构体，表示元素的连接位置。连接点用于协商能力（capabilities），以及在元素之间传输数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 25.1\_数据成员（Data Fields）

<a id="r_af842f4ab962a4768da03661f5fb3decc"></a>

```c
struct mpipe_object object
```

相关声明：[mpipe_object](P024_mpipe_object_结构体.md)、[object](#af842f4ab962a4768da03661f5fb3decc)。

基础对象（base object）。

<a id="r_a220664610a98c5e24f15d05d3f7fbaf7"></a>

```c
enum mpipe_pad_direction direction
```

相关声明：[mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)、[direction](#a220664610a98c5e24f15d05d3f7fbaf7)。

连接点的方向；创建后不能更改。

<a id="r_a19b6d32fab3c7af1e3976c00ab0f757b"></a>

```c
enum mpipe_pad_presence presence
```

相关声明：[mpipe_pad_presence](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gae260b9597d59469fdd89cc9604d33646)、[presence](#a19b6d32fab3c7af1e3976c00ab0f757b)。

连接点的存在方式（presence）。

<a id="r_add18ea9141b50fc74ead823bc34fdba6"></a>

```c
enum mpipe_pad_mode mode
```

相关声明：[mpipe_pad_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga6103c9bbb48a5b03a3805a561c19b9f5)、[mode](#add18ea9141b50fc74ead823bc34fdba6)。

工作模式（Operating mode）。

<a id="r_a03b9660c8380aef60aae41945979aa47"></a>

```c
struct mpipe_pad * peer
```

相关声明：[mpipe_pad](P025_mpipe_pad_结构体.md)、[peer](#a03b9660c8380aef60aae41945979aa47)。

指向与本连接点相连的对端连接点的指针。

<a id="r_a7868d142a953da55530271ec6619a57c"></a>

```c
struct mpipe_structure caps
```

相关声明：[mpipe_structure](P031_mpipe_structure_结构体.md)、[caps](#a7868d142a953da55530271ec6619a57c)。

连接点的能力（capability）。

<a id="r_a8eb0fadf412d4c5307d0a0a0cf295eb7"></a>

```c
atomic_t flushing
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[flushing](#a8eb0fadf412d4c5307d0a0a0cf295eb7)。

清空控制开关（Flushing gate）。

<a id="r_a2c4552341d8a39d6c4de66055ca3fa92"></a>

```c
int(* process_fn )(struct mpipe_pad *pad, struct net_buf *in_buf, struct net_buf **out_buf)
```

相关声明：[process_fn](#a2c4552341d8a39d6c4de66055ca3fa92)、[mpipe_pad](P025_mpipe_pad_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

处理一个缓冲区。

<a id="r_a13c26a0fedaaae44870bdfd7699d88f4"></a>

```c
int(* query_fn )(struct mpipe_pad *pad, struct mpipe_dispatch *query)
```

相关声明：[query_fn](#a13c26a0fedaaae44870bdfd7699d88f4)、[mpipe_pad](P025_mpipe_pad_结构体.md)、[mpipe_dispatch](P020_mpipe_dispatch_结构体.md)。

响应一个查询。

<a id="r_a500f2d13c64cd25557aa40e64ee6a550"></a>

```c
int(* event_fn )(struct mpipe_pad *pad, struct mpipe_dispatch *event)
```

相关声明：[event_fn](#a500f2d13c64cd25557aa40e64ee6a550)、[mpipe_pad](P025_mpipe_pad_结构体.md)、[mpipe_dispatch](P020_mpipe_dispatch_结构体.md)。

处理一个事件。

<a id="r_a0a6bc88b06ead152fbe6bf8f84836f00"></a>

```c
int(* enum_caps_fn )(struct mpipe_pad *pad, uint32_t index, const struct mpipe_structure *filter, struct mpipe_structure *out)
```

相关声明：[enum_caps_fn](#a0a6bc88b06ead152fbe6bf8f84836f00)、[mpipe_pad](P025_mpipe_pad_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[mpipe_structure](P031_mpipe_structure_结构体.md)、[mpipe_structure](P031_mpipe_structure_结构体.md)。

生成此连接点支持的一项能力（capability）。

## 25.2\_详细说明（Detailed Documentation）

<a id="a7868d142a953da55530271ec6619a57c"></a>

### `caps`

```c
struct mpipe_structure mpipe_pad::caps
```

连接点的能力（capability）。

协商确定前为 `ANY`；从 `PAUSED` 转为 `READY` 时重置为 `ANY`。

<a id="a220664610a98c5e24f15d05d3f7fbaf7"></a>

### `direction`

```c
enum mpipe_pad_direction mpipe_pad::direction
```

连接点的方向；创建后不能更改。

<a id="a0a6bc88b06ead152fbe6bf8f84836f00"></a>

### `enum_caps_fn`

```c
int(* mpipe_pad::enum_caps_fn) (struct mpipe_pad *pad, uint32_t index, const struct mpipe_structure *filter, struct mpipe_structure *out)
```

生成此连接点支持的一项能力（capability）。

元素通过此函数声明自己支持的能力。框架依次使用索引 0、1、2 等调用它，每次调用返回一项能力，直到它报告 `-ENOENT`，因此多个格式以索引枚举，而不是存储在列表中。构建时已知的能力从静态结构体复制出来；只有运行时才知道的能力则通过查询驱动来构造。如果提供了 `filter`，应返回经其收窄后的能力，`mpipe_pad_enum_filter` 可完成此操作；若当前索引无法满足过滤器，则报告 `-EAGAIN`，使遍历继续到下一索引。默认实现只在索引 0 返回连接点自身的能力，之后不再返回任何能力。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` pad` | 要枚举的连接点。 |
| ` index` | 从 0 开始的能力索引。 |
| ` filter` | 用于收窄结果的能力条件，可以为 `NULL`。 |
| `[out] out` | 调用方提供的用于存放能力的存储空间。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EAGAIN` | 此索引无法满足 `filter`。 |
| `-ENOENT` | 已越过最后一项能力。 |

<a id="a500f2d13c64cd25557aa40e64ee6a550"></a>

### `event_fn`

```c
int(* mpipe_pad::event_fn) (struct mpipe_pad *pad, struct mpipe_dispatch *event)
```

处理一个事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pad` | 事件到达的连接点。 |
| `event` | 要处理并转发的事件。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="a8eb0fadf412d4c5307d0a0a0cf295eb7"></a>

### `flushing`

```c
atomic_t mpipe_pad::flushing
```

清空控制开关（Flushing gate）。

置位期间，缓冲区会被丢弃而不作处理。

<a id="add18ea9141b50fc74ead823bc34fdba6"></a>

### `mode`

```c
enum mpipe_pad_mode mpipe_pad::mode
```

工作模式（Operating mode）。

<a id="af842f4ab962a4768da03661f5fb3decc"></a>

### `object`

```c
struct mpipe_object mpipe_pad::object
```

基础对象（base object）。

<a id="a03b9660c8380aef60aae41945979aa47"></a>

### `peer`

```c
struct mpipe_pad* mpipe_pad::peer
```

指向与本连接点相连的对端连接点的指针。

<a id="a19b6d32fab3c7af1e3976c00ab0f757b"></a>

### `presence`

```c
enum mpipe_pad_presence mpipe_pad::presence
```

连接点的存在方式（presence）。

<a id="a2c4552341d8a39d6c4de66055ca3fa92"></a>

### `process_fn`

```c
int(* mpipe_pad::process_fn) (struct mpipe_pad *pad, struct net_buf *in_buf, struct net_buf **out_buf)
```

处理一个缓冲区。

元素的处理函数：每当有缓冲区被推送到元素的接收连接点（sink pad）时调用。此函数拥有 `in_buf`，无论成功还是失败都负责释放它，并交回处理结果：可以是从自身缓冲池取得的新缓冲区，也可以是在原位置完成变换或直接透传的同一缓冲区；如果已消耗输入且不再输出，则返回 `NULL`，并结束此次推送。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` pad` | 缓冲区到达的接收连接点。 |
| ` in_buf` | 要处理的缓冲区。 |
| `[out] out_buf` | 生成的缓冲区；如果输入已被消耗且不再输出，则为 `NULL`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="a13c26a0fedaaae44870bdfd7699d88f4"></a>

### `query_fn`

```c
int(* mpipe_pad::query_fn) (struct mpipe_pad *pad, struct mpipe_dispatch *query)
```

响应一个查询。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pad` | 查询到达的连接点。 |
| `query` | 需要原地填写响应的查询。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_pad.h`

## 25.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_pad.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__pad_8h_source.html)
- [mpipe_object](P024_mpipe_object_结构体.md)
- [mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)
- [mpipe_pad_presence](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#gae260b9597d59469fdd89cc9604d33646)
- [mpipe_pad_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga6103c9bbb48a5b03a3805a561c19b9f5)
- [mpipe_pad](P025_mpipe_pad_结构体.md)
- [mpipe_structure](P031_mpipe_structure_结构体.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [mpipe_dispatch](P020_mpipe_dispatch_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mpipe_pad_enum_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga3a02138067490e72f3b36d3cfb3639bb)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P024_mpipe_object_结构体.md) · [返回大纲](大纲.md) · [下一章](P026_mpipe_parser_结构体.md)
