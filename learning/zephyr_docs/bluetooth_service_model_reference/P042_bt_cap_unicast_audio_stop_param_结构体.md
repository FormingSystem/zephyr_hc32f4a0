---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-42
title: bt_cap_unicast_audio_stop_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__unicast__audio__stop__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_bt\_cap\_unicast\_audio\_stop\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__unicast__audio__stop__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

`bt_cap_initiator_unicast_audio_stop()` 函数的参数（Parameters）。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

`bt_cap_initiator_unicast_audio_stop()` 函数的参数（Parameters）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 42.1\_数据成员（Data Fields）

<a id="r_a773eedda9ae8969e8749d56ffa3d1afa"></a>

```c
enum bt_cap_set_type type
```

相关声明：[bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)、[type](#a773eedda9ae8969e8749d56ffa3d1afa)。

集合类型（Set type）。

<a id="r_a11b5ac19301ce8ebd2c35df45c60bfe2"></a>

```c
size_t count
```

相关声明：[count](#a11b5ac19301ce8ebd2c35df45c60bfe2)。

`streams` 中的流数量（Number of streams）。

<a id="r_a94707060a6ef15dd8d3e48eae526aa82"></a>

```c
struct bt_cap_stream ** streams
```

相关声明：[bt_cap_stream](P039_bt_cap_stream_结构体.md)、[streams](#a94707060a6ef15dd8d3e48eae526aa82)。

要停止的流数组（Array of streams）。

<a id="r_a1cbd7ee2e4ceafd2da2858dc7c941d78"></a>

```c
bool release
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[release](#a1cbd7ee2e4ceafd2da2858dc7c941d78)。

停止后是否释放这些流（Release streams）。

## 42.2\_详细说明（Detailed Documentation）

<a id="a11b5ac19301ce8ebd2c35df45c60bfe2"></a>

### `count`

```c
size_t bt_cap_unicast_audio_stop_param::count
```

`streams` 中的流数量（Number of streams）。

<a id="a1cbd7ee2e4ceafd2da2858dc7c941d78"></a>

### `release`

```c
bool bt_cap_unicast_audio_stop_param::release
```

停止后是否释放这些流（Release streams）。

<a id="a94707060a6ef15dd8d3e48eae526aa82"></a>

### `streams`

```c
struct bt_cap_stream** bt_cap_unicast_audio_stop_param::streams
```

要停止的流数组（Array of streams）。

<a id="a773eedda9ae8969e8749d56ffa3d1afa"></a>

### `type`

```c
enum bt_cap_set_type bt_cap_unicast_audio_stop_param::type
```

集合类型（Set type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 42.3\_原页交叉引用（Cross References）

- [bt_cap_initiator_unicast_audio_stop()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gafdf6f1656249ab3ae6296272dc36b66f)
- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_set_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac9d750d0a22fab7852f0a04757feab6a)
- [bt_cap_stream](P039_bt_cap_stream_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P041_bt_cap_unicast_audio_start_stream_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P043_bt_cap_unicast_audio_update_param_结构体.md)
