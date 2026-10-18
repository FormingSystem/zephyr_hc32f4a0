---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-43
title: bt_cap_unicast_audio_update_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__unicast__audio__update__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_bt\_cap\_unicast\_audio\_update\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__unicast__audio__update__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

`bt_cap_initiator_unicast_audio_update()` 函数的参数（Parameters）。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

`bt_cap_initiator_unicast_audio_update()` 函数的参数（Parameters）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 43.1\_数据成员（Data Fields）

<a id="r_a768029ce89b74e0bcc06bb50f1fd8dcd"></a>

```c
enum bt_cap_set_type type
```

相关声明：[bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)、[type](#a768029ce89b74e0bcc06bb50f1fd8dcd)。

集合类型（Set type）。

<a id="r_ac8982f313161380af536d41ec48dcba1"></a>

```c
size_t count
```

相关声明：[count](#ac8982f313161380af536d41ec48dcba1)。

`stream_params` 中的参数数量。

<a id="r_a3d8f940d8401b8524764e7ecab3cfacb"></a>

```c
struct bt_cap_unicast_audio_update_stream_param * stream_params
```

相关声明：[bt_cap_unicast_audio_update_stream_param](P044_bt_cap_unicast_audio_update_stream_param_结构体.md)、[stream_params](#a3d8f940d8401b8524764e7ecab3cfacb)。

流参数数组（Stream Parameters Array）。

## 43.2\_详细说明（Detailed Documentation）

<a id="ac8982f313161380af536d41ec48dcba1"></a>

### `count`

```c
size_t bt_cap_unicast_audio_update_param::count
```

`stream_params` 中的参数数量。

<a id="a3d8f940d8401b8524764e7ecab3cfacb"></a>

### `stream_params`

```c
struct bt_cap_unicast_audio_update_stream_param* bt_cap_unicast_audio_update_param::stream_params
```

流参数数组（Stream Parameters Array）。

<a id="a768029ce89b74e0bcc06bb50f1fd8dcd"></a>

### `type`

```c
enum bt_cap_set_type bt_cap_unicast_audio_update_param::type
```

集合类型（Set type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 43.3\_原页交叉引用（Cross References）

- [bt_cap_initiator_unicast_audio_update()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga92e4e2c12720ec25c4050cde307cd639)
- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)
- [bt_cap_unicast_audio_update_stream_param](P044_bt_cap_unicast_audio_update_stream_param_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P042_bt_cap_unicast_audio_stop_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P044_bt_cap_unicast_audio_update_stream_param_结构体.md)
