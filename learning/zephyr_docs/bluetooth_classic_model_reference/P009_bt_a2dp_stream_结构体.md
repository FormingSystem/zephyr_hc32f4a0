---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-9
title: bt_a2dp_stream_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__stream.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_bt\_a2dp\_stream\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__stream.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

A2DP 流（Stream）。

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

<a id="details"></a>

A2DP 流（Stream）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_aa490bb24525c50cf8c1675a01223420c"></a>

```c
struct bt_a2dp_ep * local_ep
```

相关声明：[bt_a2dp_ep](P007_bt_a2dp_ep_结构体.md)、[local_ep](#aa490bb24525c50cf8c1675a01223420c)。

本地端点（Local Endpoint）。

<a id="r_a4ea9de245b573b7d0c495aacd7534099"></a>

```c
struct bt_a2dp_ep * remote_ep
```

相关声明：[bt_a2dp_ep](P007_bt_a2dp_ep_结构体.md)、[remote_ep](#a4ea9de245b573b7d0c495aacd7534099)。

远端端点（Remote Endpoint）。

<a id="r_a3361f68c31075014c2c3cf62494ff3ec"></a>

```c
uint8_t remote_ep_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[remote_ep_id](#a3361f68c31075014c2c3cf62494ff3ec)。

远端端点的流端点 ID（Stream End Point ID）。

<a id="r_ac0cf29d0d327ecdc3f5678055df4c974"></a>

```c
bool delay_report
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[delay_report](#ac0cf29d0d327ecdc3f5678055df4c974)。

此流是否配置了延迟报告。

<a id="r_aa51509d9f0c50118177345988ddb8fa5"></a>

```c
struct bt_a2dp_stream_ops * ops
```

相关声明：[bt_a2dp_stream_ops](P010_bt_a2dp_stream_ops_结构体.md)、[ops](#aa51509d9f0c50118177345988ddb8fa5)。

音频流操作（Audio Stream Operations）。

<a id="r_ab62b3f17a198600e683c26cf3d3e87e2"></a>

```c
struct bt_a2dp * a2dp
```

相关声明：[bt_a2dp](P001_bt_a2dp_结构体.md)、[a2dp](#ab62b3f17a198600e683c26cf3d3e87e2)。

A2DP 连接。

<a id="r_aff775fe292618da4de467aa96cbf79b0"></a>

```c
struct bt_a2dp_codec_ie codec_config
```

相关声明：[bt_a2dp_codec_ie](P004_bt_a2dp_codec_ie_结构体.md)、[codec_config](#aff775fe292618da4de467aa96cbf79b0)。

流的当前配置。

## 9.2\_详细说明（Detailed Documentation）

<a id="ab62b3f17a198600e683c26cf3d3e87e2"></a>

### `a2dp`

```c
struct bt_a2dp* bt_a2dp_stream::a2dp
```

A2DP 连接。

<a id="aff775fe292618da4de467aa96cbf79b0"></a>

### `codec_config`

```c
struct bt_a2dp_codec_ie bt_a2dp_stream::codec_config
```

流的当前配置。

<a id="ac0cf29d0d327ecdc3f5678055df4c974"></a>

### `delay_report`

```c
bool bt_a2dp_stream::delay_report
```

此流是否配置了延迟报告。

<a id="aa490bb24525c50cf8c1675a01223420c"></a>

### `local_ep`

```c
struct bt_a2dp_ep* bt_a2dp_stream::local_ep
```

本地端点（Local Endpoint）。

<a id="aa51509d9f0c50118177345988ddb8fa5"></a>

### `ops`

```c
struct bt_a2dp_stream_ops* bt_a2dp_stream::ops
```

音频流操作（Audio Stream Operations）。

<a id="a4ea9de245b573b7d0c495aacd7534099"></a>

### `remote_ep`

```c
struct bt_a2dp_ep* bt_a2dp_stream::remote_ep
```

远端端点（Remote Endpoint）。

<a id="a3361f68c31075014c2c3cf62494ff3ec"></a>

### `remote_ep_id`

```c
uint8_t bt_a2dp_stream::remote_ep_id
```

远端端点的流端点 ID（Stream End Point ID）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/a2dp.h`

## 9.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/a2dp.h](https://docs.zephyrproject.org/latest/doxygen/html/a2dp_8h_source.html)
- [bt_a2dp_ep](P007_bt_a2dp_ep_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_a2dp_stream_ops](P010_bt_a2dp_stream_ops_结构体.md)
- [bt_a2dp](P001_bt_a2dp_结构体.md)
- [bt_a2dp_codec_ie](P004_bt_a2dp_codec_ie_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_bt_a2dp_ep_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_bt_a2dp_stream_ops_结构体.md)
