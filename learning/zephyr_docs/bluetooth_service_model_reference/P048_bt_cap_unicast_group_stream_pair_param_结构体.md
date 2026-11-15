---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-48
title: bt_cap_unicast_group_stream_pair_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__unicast__group__stream__pair__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_bt\_cap\_unicast\_group\_stream\_pair\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__unicast__group__stream__pair__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

单播组函数使用的参数结构体。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

单播组函数的参数结构（Unicast group function parameters）。用于 `bt_cap_unicast_group_create()` 和 `bt_cap_unicast_group_add_streams()` 函数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 48.1\_数据成员（Data Fields）

<a id="r_a19d49ab8c0daa7e6a4c73563952ae461"></a>

```c
struct bt_cap_unicast_group_stream_param * rx_param
```

相关声明：[bt_cap_unicast_group_stream_param](P049_bt_cap_unicast_group_stream_param_结构体.md)、[rx_param](#a19d49ab8c0daa7e6a4c73563952ae461)。

指向接收流参数的指针。

<a id="r_a6edeca159371f3a70cc5a1f662a0e45c"></a>

```c
struct bt_cap_unicast_group_stream_param * tx_param
```

相关声明：[bt_cap_unicast_group_stream_param](P049_bt_cap_unicast_group_stream_param_结构体.md)、[tx_param](#a6edeca159371f3a70cc5a1f662a0e45c)。

指向发送流参数的指针。

## 48.2\_详细说明（Detailed Documentation）

<a id="a19d49ab8c0daa7e6a4c73563952ae461"></a>

### `rx_param`

```c
struct bt_cap_unicast_group_stream_param* bt_cap_unicast_group_stream_pair_param::rx_param
```

指向接收流参数的指针。

<a id="a6edeca159371f3a70cc5a1f662a0e45c"></a>

### `tx_param`

```c
struct bt_cap_unicast_group_stream_param* bt_cap_unicast_group_stream_pair_param::tx_param
```

指向发送流参数的指针。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 48.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_unicast_group_stream_param](P049_bt_cap_unicast_group_stream_param_结构体.md)
- [bt_cap_unicast_group_create()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gab49e8c2032a824516dc8d5f2f880dd8f)
- [bt_cap_unicast_group_add_streams()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga7b5d30c07e57f4db23f72836a3b12b2b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P047_bt_cap_unicast_group_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P049_bt_cap_unicast_group_stream_param_结构体.md)
