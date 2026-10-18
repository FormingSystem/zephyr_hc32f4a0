---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-49
title: bt_cap_unicast_group_stream_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__unicast__group__stream__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_bt\_cap\_unicast\_group\_stream\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__unicast__group__stream__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

单播组中每条流的参数结构体。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

单播组中每条流的参数结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 49.1\_数据成员（Data Fields）

<a id="r_a16aacd43bb7b449648ab6a5a89999fba"></a>

```c
struct bt_cap_stream * stream
```

相关声明：[bt_cap_stream](P039_bt_cap_stream_结构体.md)、[stream](#a16aacd43bb7b449648ab6a5a89999fba)。

指向流对象的指针。

<a id="r_a02672d241f243a7530eeff191e9a034b"></a>

```c
const struct bt_bap_qos_cfg * qos_cfg
```

相关声明：[bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)、[qos_cfg](#a02672d241f243a7530eeff191e9a034b)。

流对象的 QoS 设置。

## 49.2\_详细说明（Detailed Documentation）

<a id="a02672d241f243a7530eeff191e9a034b"></a>

### `qos_cfg`

```c
const struct bt_bap_qos_cfg* bt_cap_unicast_group_stream_param::qos_cfg
```

流对象的 QoS 设置。

<a id="a16aacd43bb7b449648ab6a5a89999fba"></a>

### `stream`

```c
struct bt_cap_stream* bt_cap_unicast_group_stream_param::stream
```

指向流对象的指针。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 49.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_stream](P039_bt_cap_stream_结构体.md)
- [bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P048_bt_cap_unicast_group_stream_pair_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P050_bt_ccp_call_control_client_结构体.md)
