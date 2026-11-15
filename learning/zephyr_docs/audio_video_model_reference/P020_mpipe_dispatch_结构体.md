---
id: learning.zephyr-docs.audio-video-model-reference.page-20
title: mpipe_dispatch_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__dispatch.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_mpipe\_dispatch\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__dispatch.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

沿端口连接（Pad Link）传递的查询或事件。

```c
#include <zephyr/mpipe/mpipe_dispatch.h>
```

<a id="details"></a>

在连接点（pad）链路上传递的查询或事件。分派对象（dispatch）沿同步遍历过程传递，因此它引用生命周期覆盖整个遍历过程的存储空间，而不是将携带的所有内容都嵌入为副本。它使用指定初始化器（designated initializer）声明，没有初始化函数；每个字段的零值都是中性值：

```c
struct mpipe_dispatch query = {
        .type = MPIPE_DISPATCH_CAPS,
        .caps = &caps_storage,
};
```

原页符号提示：`MPIPE_DISPATCH_CAPS`（`@ MPIPE_DISPATCH_CAPS`）表示能力查询或事件，定义于 `mpipe_dispatch.h:55`；`mpipe_dispatch` 表示在连接点链路上传递的查询或事件，定义于 `mpipe_dispatch.h:75`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_aaa9ac3ab2e85a0df7bab82af11d4d045"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#aaa9ac3ab2e85a0df7bab82af11d4d045)。

分派类型（Dispatch type），取自 `mpipe_dispatch_type`。

<a id="r_ad0f5202097b4ea9819acd8545f749f2c"></a>

```c
struct mpipe_structure * caps
```

相关声明：[mpipe_structure](P031_mpipe_structure_结构体.md)、[caps](#ad0f5202097b4ea9819acd8545f749f2c)。

所携带的能力；分派对象未携带能力时为 `NULL`。

<a id="r_a876f87006d975f9e292e96fd020adf74"></a>

```c
struct mpipe_buffer_pool * pool
```

相关声明：[mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)、[pool](#a876f87006d975f9e292e96fd020adf74)。

提出方提供的缓冲池，不取得其所有权。

<a id="r_ae341e350aa4cef450267c9828ffa1cdd"></a>

```c
struct mpipe_buffer_pool_config pool_cfg
```

相关声明：[mpipe_buffer_pool_config](P018_mpipe_buffer_pool_config_结构体.md)、[pool_cfg](#ae341e350aa4cef450267c9828ffa1cdd)。

不附带缓冲池而单独提出的池配置，按值协商。

## 20.2\_详细说明（Detailed Documentation）

<a id="ad0f5202097b4ea9819acd8545f749f2c"></a>

### `caps`

```c
struct mpipe_structure* mpipe_dispatch::caps
```

所携带的能力；分派对象未携带能力时为 `NULL`。

创建方将此指针指向其在整个遍历期间拥有的存储空间；其他所有元素通过该指针读取，并通过向其中复制内容作答，绝不能让指针改指别处。

查询函数可以直接解引用此指针而不作检查：在调用任何查询函数之前，`mpipe_pad_query()` 就会以 `-EINVAL` 拒绝没有携带存储空间的能力查询。事件处理函数则必须检查，因为事件可以合法携带 `NULL`。

未携带能力的能力事件是一个触发信号，而非格式通告：尚不知道格式的源元素（例如文件源）仍会发送此事件，第一个知道格式的元素会填入能力，并向下游通告。

| 值（Value）。 | 用于查询时：输入/输出存储空间（in/out storage）。 | 用于事件时：通告（announcement）。 |
| --- | --- | --- |
| 一项能力（capability）。 | 响应结果必须满足的过滤条件。 | 已确定的格式。 |
| 任意能力（`ANY`）。 | 无约束：返回所有支持的能力。 | 绝不发送此值。 |
| 空指针（`NULL`）。 | 调用方错误：没有可供写入响应的存储空间。 | 没有可通告的内容。 |

<a id="a876f87006d975f9e292e96fd020adf74"></a>

### `pool`

```c
struct mpipe_buffer_pool* mpipe_dispatch::pool
```

提出方提供的缓冲池，不取得其所有权。

<a id="ae341e350aa4cef450267c9828ffa1cdd"></a>

### `pool_cfg`

```c
struct mpipe_buffer_pool_config mpipe_dispatch::pool_cfg
```

不附带缓冲池而单独提出的池配置，按值协商。

<a id="aaa9ac3ab2e85a0df7bab82af11d4d045"></a>

### `type`

```c
uint8_t mpipe_dispatch::type
```

分派类型（Dispatch type），取自 `mpipe_dispatch_type`。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_dispatch.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_dispatch.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__dispatch_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_dispatch_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#gae32e15ab045bc017100a7e713c3999b1)
- [mpipe_structure](P031_mpipe_structure_结构体.md)
- [mpipe_buffer_pool](P017_mpipe_buffer_pool_结构体.md)
- [mpipe_buffer_pool_config](P018_mpipe_buffer_pool_config_结构体.md)
- [mpipe_dispatch](P020_mpipe_dispatch_结构体.md)
- [MPIPE_DISPATCH_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#ggae32e15ab045bc017100a7e713c3999b1a63a565f281055915f13e3ec202fe177d)
- [mpipe_pad_query()](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__pad.html#ga35b334800669dbe25a46c71d75afd775)

<a id="header-details"></a>
<a id="agroup__mpipe__dispatch_html_ggae32e15ab045bc017100a7e713c3999b1a63a565f281055915f13e3ec202fe177d"></a>
<a id="astructmpipe__dispatch_html"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_mpipe_caps_filter_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_mpipe_element_结构体.md)
