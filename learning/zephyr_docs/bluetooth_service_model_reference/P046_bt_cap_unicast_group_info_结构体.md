---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-46
title: bt_cap_unicast_group_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__unicast__group__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_bt\_cap\_unicast\_group\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__unicast__group__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存音频流端点信息的结构体。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

保存音频流端点信息的结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 46.1\_数据成员（Data Fields）

<a id="r_afbfd6705742d15081f6cf4dca21e242b"></a>

```c
const struct bt_bap_unicast_group * unicast_group
```

相关声明：[bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)、[unicast_group](#afbfd6705742d15081f6cf4dca21e242b)。

指向底层基本音频规范单播组（Basic Audio Profile unicast group）的指针。

## 46.2\_详细说明（Detailed Documentation）

<a id="afbfd6705742d15081f6cf4dca21e242b"></a>

### `unicast_group`

```c
const struct bt_bap_unicast_group* bt_cap_unicast_group_info::unicast_group
```

指向底层基本音频规范单播组（Basic Audio Profile unicast group）的指针。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 46.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P045_bt_cap_unicast_group_结构体.md) · [返回大纲](大纲.md) · [下一章](P047_bt_cap_unicast_group_param_结构体.md)
