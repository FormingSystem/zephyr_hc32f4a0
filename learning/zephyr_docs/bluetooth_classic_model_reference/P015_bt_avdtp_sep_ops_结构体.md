---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-15
title: bt_avdtp_sep_ops_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avdtp__sep__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_bt\_avdtp\_sep\_ops\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avdtp__sep__ops.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

AVDTP 流端点操作结构体（SEP Operations Structure）。

```c
#include <zephyr/bluetooth/classic/avdtp.h>
```

<a id="details"></a>

AVDTP 流端点操作结构体（SEP Operations Structure）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_a97a6ac5f821579e2ab04ee22e738f173"></a>

```c
void(* connected )(struct bt_avdtp_sep *sep)
```

相关声明：[connected](#a97a6ac5f821579e2ab04ee22e738f173)、[bt_avdtp_sep](P013_bt_avdtp_sep_结构体.md)。

流端点（SEP）的 L2CAP 连接完成回调。

<a id="r_add289f4fed823f55e80fbf29b6e87e1c"></a>

```c
void(* disconnected )(struct bt_avdtp_sep *sep)
```

相关声明：[disconnected](#add289f4fed823f55e80fbf29b6e87e1c)、[bt_avdtp_sep](P013_bt_avdtp_sep_结构体.md)。

流端点（SEP）的 L2CAP 断开连接回调。

<a id="r_a62cffe9d43241f5314ae04fd993d4943"></a>

```c
void(* media_data_cb )(struct bt_avdtp_sep *sep, struct net_buf *buf)
```

相关声明：[media_data_cb](#a62cffe9d43241f5314ae04fd993d4943)、[bt_avdtp_sep](P013_bt_avdtp_sep_结构体.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

流端点（SEP）收到数据。

## 15.2\_详细说明（Detailed Documentation）

<a id="a97a6ac5f821579e2ab04ee22e738f173"></a>

### `connected`

```c
void(* bt_avdtp_sep_ops::connected) (struct bt_avdtp_sep *sep)
```

流端点（SEP）的 L2CAP 连接完成回调。

如果提供此回调，则每当流的 L2CAP 连接完成时调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sep` | 已连接的流端点（SEP）。 |

<a id="add289f4fed823f55e80fbf29b6e87e1c"></a>

### `disconnected`

```c
void(* bt_avdtp_sep_ops::disconnected) (struct bt_avdtp_sep *sep)
```

流端点（SEP）的 L2CAP 断开连接回调。

如果提供此回调，则每当流的 L2CAP 通道断开时调用它，包括连接被拒绝的情况。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sep` | 已断开连接的流端点（SEP）。 |

<a id="a62cffe9d43241f5314ae04fd993d4943"></a>

### `media_data_cb`

```c
void(* bt_avdtp_sep_ops::media_data_cb) (struct bt_avdtp_sep *sep, struct net_buf *buf)
```

流端点（SEP）收到数据。

如果提供此回调，则每当流的 L2CAP 通道收到数据时调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sep` | 收到数据的流端点（SEP）。 |
| `buf` | 数据缓冲区。 |

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avdtp.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avdtp.h](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h_source.html)
- [bt_avdtp_sep](P013_bt_avdtp_sep_结构体.md)
- [net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_bt_avdtp_sep_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_bt_avrcp_add_to_now_playing_cmd_结构体.md)
