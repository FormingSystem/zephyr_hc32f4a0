---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-22
title: bt_avrcp_cover_art_ct_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__cover__art__ct.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_bt\_avrcp\_cover\_art\_ct\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__cover__art__ct.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

AVRCP 控制端封面图（Controller Cover Art）结构体。

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

<a id="details"></a>

AVRCP 控制端封面图（Controller Cover Art）结构体。该结构体表示 AVRCP 控制端封面图实例，负责从 AVRCP 目标设备（Target）获取封面图。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 22.1\_数据成员（Data Fields）

<a id="r_a69843b53b4398f82fae0e05c087680a1"></a>

```c
struct bt_bip bip
```

相关声明：[bt_bip](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip.html)、[bip](#a69843b53b4398f82fae0e05c087680a1)。

基本图像配置文件（Basic Image Profile，BIP）实例。

<a id="r_af44481b36c5b0ff98519e01ad0c4f61f"></a>

```c
struct bt_bip_client client
```

相关声明：[bt_bip_client](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip__client.html)、[client](#af44481b36c5b0ff98519e01ad0c4f61f)。

BIP 客户端实例。

<a id="r_a128f10710dfb12aa80a6d95354b532da"></a>

```c
struct bt_avrcp_ct * ct
```

相关声明：[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[ct](#a128f10710dfb12aa80a6d95354b532da)。

关联的 AVRCP 控制端（Controller）。

<a id="r_a4634dc499f02165e48c59c2bb87b0b81"></a>

```c
struct bt_conn * conn
```

相关声明：[bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)、[conn](#a4634dc499f02165e48c59c2bb87b0b81)。

蓝牙连接（Bluetooth Connection）。

## 22.2\_详细说明（Detailed Documentation）

<a id="a69843b53b4398f82fae0e05c087680a1"></a>

### `bip`

```c
struct bt_bip bt_avrcp_cover_art_ct::bip
```

基本图像配置文件（Basic Image Profile，BIP）实例。

<a id="af44481b36c5b0ff98519e01ad0c4f61f"></a>

### `client`

```c
struct bt_bip_client bt_avrcp_cover_art_ct::client
```

BIP 客户端实例。

<a id="a4634dc499f02165e48c59c2bb87b0b81"></a>

### `conn`

```c
struct bt_conn* bt_avrcp_cover_art_ct::conn
```

蓝牙连接（Bluetooth Connection）。

<a id="a128f10710dfb12aa80a6d95354b532da"></a>

### `ct`

```c
struct bt_avrcp_ct* bt_avrcp_cover_art_ct::ct
```

关联的 AVRCP 控制端（Controller）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp_cover_art.h`

## 22.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp_cover_art.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp__cover__art_8h_source.html)
- [bt_bip](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip.html)
- [bt_bip_client](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip__client.html)
- [bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)
- [bt_conn](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P021_bt_avrcp_change_path_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P023_bt_avrcp_cover_art_ct_cb_结构体.md)
