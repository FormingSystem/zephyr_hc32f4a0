---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-87
title: bt_iso_server_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第87章\_bt\_iso\_server\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__server.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

等时通信服务器（ISO Server）结构。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

等时通信服务器（ISO Server）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 87.1\_数据成员（Data Fields）

<a id="r_ae67a000ae524cba53b6bda503568ba38"></a>

```c
int(* accept )(const struct bt_iso_accept_info *info, struct bt_iso_chan **chan)
```

相关声明：[accept](#ae67a000ae524cba53b6bda503568ba38)、[bt_iso_accept_info](P070_bt_iso_accept_info_结构体.md)、[bt_iso_chan](P077_bt_iso_chan_结构体.md)。

服务器接受回调（Server accept callback）。

## 87.2\_详细说明（Detailed Documentation）

<a id="ae67a000ae524cba53b6bda503568ba38"></a>

### `accept`

```c
int(* bt_iso_server::accept) (const struct bt_iso_accept_info *info, struct bt_iso_chan **chan)
```

服务器接受回调（Server accept callback）。

每当新的传入连接需要授权（Authorization）时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `info` | 等时连接接受信息结构（ISO accept information structure）。 |
| `chan` | 用于接收已分配通道（Allocated channel）的指针。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 87.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [bt_iso_accept_info](P070_bt_iso_accept_info_结构体.md)
- [bt_iso_chan](P077_bt_iso_chan_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P086_bt_iso_recv_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P088_bt_iso_sync_receiver_info_结构体.md)
