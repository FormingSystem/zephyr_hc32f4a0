---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-84
title: bt_iso_connect_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__connect__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第84章\_bt\_iso\_connect\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__connect__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

等时连接（ISO Connection）的参数结构。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

等时连接（ISO Connection）的参数结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 84.1\_数据成员（Data Fields）

<a id="r_ad004956584d2d065d8c0c52959f350d5"></a>

```c
struct bt_iso_chan * iso_chan
```

相关声明：[bt_iso_chan](P077_bt_iso_chan_结构体.md)、[iso_chan](#ad004956584d2d065d8c0c52959f350d5)。

要连接的等时通道（ISO channel）。

<a id="r_aba2f3838e03a1e31699a4623ba93d372"></a>

```c
struct bt_conn * acl
```

相关声明：[bt_conn](P002_bt_conn_结构体.md)、[acl](#aba2f3838e03a1e31699a4623ba93d372)。

异步面向连接链路连接（ACL connection）。

## 84.2\_详细说明（Detailed Documentation）

<a id="aba2f3838e03a1e31699a4623ba93d372"></a>

### `acl`

```c
struct bt_conn* bt_iso_connect_param::acl
```

异步面向连接链路连接（ACL connection）。

<a id="ad004956584d2d065d8c0c52959f350d5"></a>

### `iso_chan`

```c
struct bt_iso_chan* bt_iso_connect_param::iso_chan
```

要连接的等时通道（ISO channel）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 84.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [bt_iso_chan](P077_bt_iso_chan_结构体.md)
- [bt_conn](P002_bt_conn_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P083_bt_iso_cig_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P085_bt_iso_info_结构体.md)
