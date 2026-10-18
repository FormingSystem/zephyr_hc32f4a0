---
id: learning.zephyr-docs.audio-video-model-reference.page-34
title: mpipe_transform_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__transform.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_mpipe\_transform\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__transform.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

变换元素（Transform Element）的结构。

```c
#include <zephyr/mpipe/mpipe_transform.h>
```

<a id="details"></a>

变换元素（Transform element）结构体，是媒体管线中所有变换元素的基础结构。变换元素处理来自接收连接点的数据，并将结果输出到源连接点。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 34.1\_数据成员（Data Fields）

<a id="r_ad10c3a231a6409f15f670784b54bd8be"></a>

```c
struct mpipe_element element
```

相关声明：[mpipe_element](P021_mpipe_element_结构体.md)、[element](#ad10c3a231a6409f15f670784b54bd8be)。

基础元素（base element）结构体。

<a id="r_a27659ad4ddd7c042b0eda9c8faa6280a"></a>

```c
struct mpipe_pad sink_pad
```

相关声明：[mpipe_pad](P025_mpipe_pad_结构体.md)、[sink_pad](#a27659ad4ddd7c042b0eda9c8faa6280a)。

用于接收输入数据的接收连接点。

<a id="r_ad171b584bb4b610365b1ea505da3dc06"></a>

```c
struct mpipe_pad src_pad
```

相关声明：[mpipe_pad](P025_mpipe_pad_结构体.md)、[src_pad](#ad171b584bb4b610365b1ea505da3dc06)。

用于发送输出数据的源连接点。

<a id="r_aad7f8583f688e223a7d0df7cafe5bed9"></a>

```c
struct mpipe_buffer_pool * in_pool
```

相关声明：[mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)、[in_pool](#aad7f8583f688e223a7d0df7cafe5bed9)。

指向用于分配输入缓冲区的输入缓冲池的指针。

<a id="r_a5cfad87f6c19e5c898aa07c32ca5b93d"></a>

```c
struct mpipe_buffer_pool * out_pool
```

相关声明：[mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)、[out_pool](#a5cfad87f6c19e5c898aa07c32ca5b93d)。

指向用于分配输出缓冲区的输出缓冲池的指针。

<a id="r_a69adb521d80da09249a53a35a218268c"></a>

```c
enum mpipe_transform_mode mode
```

相关声明：[mpipe_transform_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga53de93e6bf6ca6cc2e4a7be14ff76652)、[mode](#a69adb521d80da09249a53a35a218268c)。

决定缓冲区处理策略的工作模式（operating mode）。

<a id="r_af6dbe1b933a463e9d2c8aabba327c804"></a>

```c
int(* set_caps )(struct mpipe_transform *self, enum mpipe_pad_direction direction, const struct mpipe_structure *caps)
```

相关声明：[set_caps](#af6dbe1b933a463e9d2c8aabba327c804)、[mpipe_transform](P034_mpipe_transform_结构体.md)、[mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)、[mpipe_structure](P031_mpipe_structure_结构体.md)。

将协商得到的能力应用到此元素的一个连接点。

<a id="r_abf312cbfe076c2d231c3408ffbd81575"></a>

```c
int(* transform_caps )(struct mpipe_transform *self, enum mpipe_pad_direction direction, const struct mpipe_structure *in, uint32_t index, struct mpipe_structure *out)
```

相关声明：[transform_caps](#abf312cbfe076c2d231c3408ffbd81575)、[mpipe_transform](P034_mpipe_transform_结构体.md)、[mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)、[mpipe_structure](P031_mpipe_structure_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[mpipe_structure](P031_mpipe_structure_结构体.md)。

生成一项能力穿过此元素后的一种变换结果。

<a id="r_a8cc54f1047f93abe7e805aa861a696c4"></a>

```c
int(* propose_buffer_pool )(struct mpipe_transform *self, struct mpipe_dispatch *query)
```

相关声明：[propose_buffer_pool](#a8cc54f1047f93abe7e805aa861a696c4)、[mpipe_transform](P034_mpipe_transform_结构体.md)、[mpipe_dispatch](P020_mpipe_dispatch_结构体.md)。

向上游提出一个缓冲池。

<a id="r_aacf7a73bb88bbea37727af5ab40347b8"></a>

```c
int(* decide_buffer_pool )(struct mpipe_transform *self, struct mpipe_dispatch *query)
```

相关声明：[decide_buffer_pool](#aacf7a73bb88bbea37727af5ab40347b8)、[mpipe_transform](P034_mpipe_transform_结构体.md)、[mpipe_dispatch](P020_mpipe_dispatch_结构体.md)。

为下游确定缓冲池。

## 34.2\_详细说明（Detailed Documentation）

<a id="aacf7a73bb88bbea37727af5ab40347b8"></a>

### `decide_buffer_pool`

```c
int(* mpipe_transform::decide_buffer_pool) (struct mpipe_transform *self, struct mpipe_dispatch *query)
```

为下游确定缓冲池。

下游提出的方案可以是完整缓冲池（查询的 `pool` 指针，其配置即为方案），也可以是单独的配置（查询的 `pool_cfg`）。只能通过 `mpipe_buffer_pool_set_config` 向提出的缓冲池施加需求；缓冲池可能拒绝，因此需要保留后备方案。如果元素为自身缓冲池作决策，每次协商都先在此处重建配置基线，然后再纳入查询提出的要求，避免反复协商时需求不断累积。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `self` | 指向变换元素的指针。 |
| `query` | 缓冲池查询，参见分派（Dispatches）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="ad10c3a231a6409f15f670784b54bd8be"></a>

### `element`

```c
struct mpipe_element mpipe_transform::element
```

基础元素（base element）结构体。

<a id="aad7f8583f688e223a7d0df7cafe5bed9"></a>

### `in_pool`

```c
struct mpipe_buffer_pool* mpipe_transform::in_pool
```

指向用于分配输入缓冲区的输入缓冲池的指针。

<a id="a69adb521d80da09249a53a35a218268c"></a>

### `mode`

```c
enum mpipe_transform_mode mpipe_transform::mode
```

决定缓冲区处理策略的工作模式（operating mode）。

<a id="a5cfad87f6c19e5c898aa07c32ca5b93d"></a>

### `out_pool`

```c
struct mpipe_buffer_pool* mpipe_transform::out_pool
```

指向用于分配输出缓冲区的输出缓冲池的指针。

<a id="a8cc54f1047f93abe7e805aa861a696c4"></a>

### `propose_buffer_pool`

```c
int(* mpipe_transform::propose_buffer_pool) (struct mpipe_transform *self, struct mpipe_dispatch *query)
```

向上游提出一个缓冲池。

变换元素可以提出完整的输入缓冲池，也可以只提出配置：前者设置查询的 `pool` 指针，池自身的配置就是方案；后者写入查询的 `pool_cfg`。提出缓冲池后，由上游元素调用其操作。在提出之前，应根据缓冲池的原始要求重建配置：当前生效的配置是上一次协商的结果，如果直接提出该配置，会使对端需求在反复协商时累积。

原地变换（in-place transform）可以用同一个缓冲池处理输入和输出。当把这个池提供给上游时，应让 `mpipe_transform::in_pool` 指向它，并将 `mpipe_transform::out_pool` 保持为 `NULL`，从而只由上游负责配置和启动该池。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `self` | 指向变换元素的指针。 |
| `query` | 缓冲池查询，参见分派（Dispatches）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="af6dbe1b933a463e9d2c8aabba327c804"></a>

### `set_caps`

```c
int(* mpipe_transform::set_caps) (struct mpipe_transform *self, enum mpipe_pad_direction direction, const struct mpipe_structure *caps)
```

将协商得到的能力应用到此元素的一个连接点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `self` | 指向变换元素的指针。 |
| `direction` | 连接点方向，类型为 `mpipe_pad_direction`。 |
| `caps` | 要应用的能力，参见能力结构（Capability Structure）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="a27659ad4ddd7c042b0eda9c8faa6280a"></a>

### `sink_pad`

```c
struct mpipe_pad mpipe_transform::sink_pad
```

用于接收输入数据的接收连接点。

<a id="ad171b584bb4b610365b1ea505da3dc06"></a>

### `src_pad`

```c
struct mpipe_pad mpipe_transform::src_pad
```

用于发送输出数据的源连接点。

<a id="abf312cbfe076c2d231c3408ffbd81575"></a>

### `transform_caps`

```c
int(* mpipe_transform::transform_caps) (struct mpipe_transform *self, enum mpipe_pad_direction direction, const struct mpipe_structure *in, uint32_t index, struct mpipe_structure *out)
```

生成一项能力穿过此元素后的一种变换结果。

一个元素通常会把一项输入能力映射到多项输出能力，例如能输出 N 种像素格式的解码器，或者能转换到 N 种格式的转换器。这些候选项通过索引表示，而不是作为集合一次性返回；协商过程逐项遍历它们，因此不会实际构造整个展开结果集。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` self` | 指向变换元素的指针。 |
| ` direction` | 要将能力变换到哪一侧连接点的方向，类型为 `mpipe_pad_direction`。 |
| ` in` | 要变换的对侧连接点能力。 |
| ` index` | 要生成的变换结果索引，从 0 开始。 |
| `[out] out` | 调用方提供的用于接收变换结果的存储空间。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EAGAIN` | 此索引没有结果，但后续索引可能有。 |
| `-ENOENT` | 已越过最后一项变换结果。 |

**返回（Returns）**：返回值：`out` 保存了一项变换结果时返回 0；失败时返回其他负值 `errno`。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_transform.h`

## 34.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_transform.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform_8h_source.html)
- [mpipe_element](P021_mpipe_element_结构体.md)
- [mpipe_pad](P025_mpipe_pad_结构体.md)
- [mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)
- [mpipe_transform_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga53de93e6bf6ca6cc2e4a7be14ff76652)
- [mpipe_transform](P034_mpipe_transform_结构体.md)
- [mpipe_pad_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga9de49691e139241133f231188671d4f2)
- [mpipe_structure](P031_mpipe_structure_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mpipe_dispatch](P020_mpipe_dispatch_结构体.md)
- [mpipe_buffer_pool_set_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__buffer.html#gab718120f2a3c3f2a13107fd14d9385ec)
- [Dispatches](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html)
- [能力结构（Capability Structure）](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__structure.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P033_mpipe_thread_结构体.md) · [返回大纲](大纲.md) · [下一章](P035_mpipe_transform_client_结构体.md)
