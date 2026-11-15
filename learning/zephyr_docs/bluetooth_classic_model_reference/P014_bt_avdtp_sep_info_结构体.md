---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-14
title: bt_avdtp_sep_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avdtp__sep__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_bt\_avdtp\_sep\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avdtp__sep__info.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

AVDTP 流端点信息。

```c
#include <zephyr/bluetooth/classic/avdtp.h>
```

<a id="details"></a>

AVDTP 流端点信息。由于它不用于解析数据，因此不必关注字节序（Endianness）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_ab644a59a54d943e3d4729a198bda59cd"></a>

```c
uint8_t inuse: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[inuse](#ab644a59a54d943e3d4729a198bda59cd)。

端点使用状态（End Point Usage Status）。

<a id="r_a03bf1e8c29eaff7ef3b48f21dff7aa49"></a>

```c
uint8_t id: 6
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#a03bf1e8c29eaff7ef3b48f21dff7aa49)。

流端点 ID，用于标识流端点。

<a id="r_a3d6c6832a40cdb31976a447459576e0f"></a>

```c
uint8_t reserved: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved](#a3d6c6832a40cdb31976a447459576e0f)。

保留（Reserved）。

<a id="r_add86d89b0e062f034aa85bf7121313ee"></a>

```c
enum bt_avdtp_sep_type tsep
```

相关声明：[bt_avdtp_sep_type](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a28b828df32df5a40e8487dc4dee78757)、[tsep](#add86d89b0e062f034aa85bf7121313ee)。

流端点类型（Stream End-point Type），表示端点为接收端（SNK）还是发送源（SRC）。

<a id="r_a8cd4323a80ad4138095d5aceb08a64b6"></a>

```c
enum bt_avdtp_media_type media_type
```

相关声明：[bt_avdtp_media_type](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a6e9f13217ede2687e206b6a8cbd9137f)、[media_type](#a8cd4323a80ad4138095d5aceb08a64b6)。

端点的媒体类型（Media Type）；目前仅支持 `BT_AVDTP_AUDIO`。

## 14.2\_详细说明（Detailed Documentation）

<a id="a03bf1e8c29eaff7ef3b48f21dff7aa49"></a>

### `id`

```c
uint8_t bt_avdtp_sep_info::id
```

流端点 ID，用于标识流端点。

<a id="ab644a59a54d943e3d4729a198bda59cd"></a>

### `inuse`

```c
uint8_t bt_avdtp_sep_info::inuse
```

端点使用状态（End Point Usage Status）。

<a id="a8cd4323a80ad4138095d5aceb08a64b6"></a>

### `media_type`

```c
enum bt_avdtp_media_type bt_avdtp_sep_info::media_type
```

端点的媒体类型（Media Type）；目前仅支持 `BT_AVDTP_AUDIO`。

<a id="a3d6c6832a40cdb31976a447459576e0f"></a>

### `reserved`

```c
uint8_t bt_avdtp_sep_info::reserved
```

保留（Reserved）。

<a id="add86d89b0e062f034aa85bf7121313ee"></a>

### `tsep`

```c
enum bt_avdtp_sep_type bt_avdtp_sep_info::tsep
```

流端点类型（Stream End-point Type），表示端点为接收端（SNK）还是发送源（SRC）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avdtp.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avdtp.h](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avdtp_sep_type](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a28b828df32df5a40e8487dc4dee78757)
- [bt_avdtp_media_type](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a6e9f13217ede2687e206b6a8cbd9137f)
- [BT_AVDTP_AUDIO](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h.html#a6e9f13217ede2687e206b6a8cbd9137faf77a41d832f11dfa01946a6dc7ceee58)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_bt_avdtp_sep_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_bt_avdtp_sep_ops_结构体.md)
