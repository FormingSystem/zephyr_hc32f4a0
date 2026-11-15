---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-40
title: bt_bap_unicast_group_stream_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__stream__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_bt\_bap\_unicast\_group\_stream\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__stream__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

单播组中每条流的参数结构体。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

单播组中每条流的参数结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 40.1\_数据成员（Data Fields）

<a id="r_acfa192fed73b27fb194881f0021fcb35"></a>

```c
struct bt_bap_stream * stream
```

相关声明：[bt_bap_stream](P033_bt_bap_stream_结构体.md)、[stream](#acfa192fed73b27fb194881f0021fcb35)。

指向流对象的指针。

<a id="r_a8424dfd660759a6dd226f53413069a8a"></a>

```c
const struct bt_bap_qos_cfg * qos
```

相关声明：[bt_bap_qos_cfg](P027_bt_bap_qos_cfg_结构体.md)、[qos](#a8424dfd660759a6dd226f53413069a8a)。

流对象的 QoS 设置。

## 40.2\_详细说明（Detailed Documentation）

<a id="a8424dfd660759a6dd226f53413069a8a"></a>

### `qos`

```c
const struct bt_bap_qos_cfg* bt_bap_unicast_group_stream_param::qos
```

流对象的 QoS 设置。

<a id="acfa192fed73b27fb194881f0021fcb35"></a>

### `stream`

```c
struct bt_bap_stream* bt_bap_unicast_group_stream_param::stream
```

指向流对象的指针。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 40.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [bt_bap_stream](P033_bt_bap_stream_结构体.md)
- [bt_bap_qos_cfg](P027_bt_bap_qos_cfg_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P039_bt_bap_unicast_group_stream_pair_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P041_bt_bap_unicast_server_cb_结构体.md)
