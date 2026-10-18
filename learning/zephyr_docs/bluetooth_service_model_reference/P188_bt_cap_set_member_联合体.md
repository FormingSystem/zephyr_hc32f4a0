---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-188
title: bt_cap_set_member_联合体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionbt__cap__set__member.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第188章\_bt\_cap\_set\_member\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionbt__cap__set__member.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

表示通用音频集合（Common Audio Set）的成员，该成员属于协调集合（Coordinated Set）或临时集合（Ad-hoc Set）。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

表示通用音频集合（Common Audio Set）的成员，该成员属于协调集合（Coordinated Set）或临时集合（Ad-hoc Set）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 188.1\_数据成员（Data Fields）

<a id="r_a692a1be2fbd79c4b6a0fbce564ff2973"></a>

```c
struct bt_conn * member
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[member](#a692a1be2fbd79c4b6a0fbce564ff2973)。

当类型为 `BT_CAP_SET_TYPE_AD_HOC` 时使用的连接指针。

<a id="r_ac17db41d21a92d8d128b70962e4eb2d6"></a>

```c
struct bt_csip_set_coordinator_csis_inst * csip
```

相关声明：[bt_csip_set_coordinator_csis_inst](P056_bt_csip_set_coordinator_csis_inst_结构体.md)、[csip](#ac17db41d21a92d8d128b70962e4eb2d6)。

当类型为 `BT_CAP_SET_TYPE_CSIP` 时使用的协调集合标识规范（CSIP）协调集合结构体。

## 188.2\_详细说明（Detailed Documentation）

<a id="ac17db41d21a92d8d128b70962e4eb2d6"></a>

### `csip`

```c
struct bt_csip_set_coordinator_csis_inst* bt_cap_set_member::csip
```

当类型为 `BT_CAP_SET_TYPE_CSIP` 时使用的协调集合标识规范（CSIP）协调集合结构体。

<a id="a692a1be2fbd79c4b6a0fbce564ff2973"></a>

### `member`

```c
struct bt_conn* bt_cap_set_member::member
```

当类型为 `BT_CAP_SET_TYPE_AD_HOC` 时使用的连接指针。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 188.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_csip_set_coordinator_csis_inst](P056_bt_csip_set_coordinator_csis_inst_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P187_bt_vocs_register_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P189_bt_obex_uuid_联合体.md)
